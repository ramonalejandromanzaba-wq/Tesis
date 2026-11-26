"""Limpieza y recodificación de las respuestas exportadas del formulario (cuestionario v2.2).

Uso: python analisis/limpieza.py datos/respuestas.xlsx salida/
- Identifica cada columna por el código entre corchetes al inicio del título de la pregunta ("[H5a] …").
- Conserva solo columnas con código conocido: elimina correos, nombres, marcas temporales, ID de la plataforma
  y cualquier otra columna identificativa.
- Excluye a quienes no consintieron, son menores de 18 años o no estudian una carrera de grado en el Ecuador (P00–P02) y a quienes
  declaran cursar un posgrado (A3), porque la población es la matrícula de grado.
- Convierte las etiquetas de respuesta en códigos numéricos (config.py), desdobla H1 en columnas binarias,
  recodifica los ítems inversos (x' = 6 − x) y calcula las puntuaciones de dimensión.
- A5 (universidad) se convierte en el código del censo (U01, …) con la clave privada; el nombre no sale de aquí.
- Sostenimiento (TIPO y SOST): el oficial de la universidad declarada en A5 si está en la clave; si no, el
  autodeclarado en A1; "No lo sé" sin universidad identificada queda sin valor (excluido de H1 y H3).
"""
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

import config as C
from comun import BASE, carpeta, leer_tabla

PATRON_CODIGO = re.compile(r"^\s*\[?\s*(P0\d|A\d|H\d{1,2}[ab]?|INF\d[ab]?|CON\d|DER\d|CNF\d)\s*\]?", re.IGNORECASE)


def _codigo(col):
    m = PATRON_CODIGO.match(str(col))
    if not m:
        return None
    c = m.group(1)
    # prefijo en mayúsculas y sufijo a/b en minúsculas: "inf2A" → "INF2a"
    return c[:-1].upper() + c[-1].lower() if c[-1].lower() in "ab" else c.upper()


def _a_numero(valor, mapa):
    """Etiqueta → código según el mapa; acepta también el código numérico ya escrito."""
    if valor is None or (isinstance(valor, float) and np.isnan(valor)) or str(valor).strip() == "":
        return np.nan
    s = str(valor).strip()
    if mapa and s in mapa:
        return mapa[s]
    try:
        return float(s.replace(",", "."))
    except ValueError:
        # coincidencia sin distinguir mayúsculas ni comillas tipográficas
        norm = lambda t: t.lower().replace("“", "\"").replace("”", "\"").replace("…", "...").strip()
        for k, v in (mapa or {}).items():
            if norm(k) == norm(s):
                return v
        raise ValueError(f"Respuesta no reconocida: {s!r}")


def _acepta(valor):
    s = str(valor).strip().lower()
    return s.startswith("sí") or s.startswith("si") or s == "1"


def cargar_clave(ruta=None):
    """Clave privada: número de opción de A5 → (código del censo, sostenimiento 1/2/3). Vacía si no existe."""
    ruta = Path(ruta) if ruta else BASE.parent / C.CLAVE_UNIVERSIDADES
    if not ruta.exists():
        return {}
    k = pd.read_excel(ruta, sheet_name="Clave", dtype=object)
    pos = {u: i + 1 for i, u in enumerate(C.UNIVERSIDADES)}
    return {pos[r["Opción en el formulario (A5)"]]: (r["Código"], int(r["Sostenimiento (código)"]))
            for _, r in k.iterrows() if r["Opción en el formulario (A5)"] in pos}


def limpiar(df: pd.DataFrame, clave=None):
    clave = cargar_clave() if clave is None else clave
    informe = {"recibidas": len(df)}
    codigos = {c: _codigo(c) for c in df.columns}
    descartadas = [c for c, k in codigos.items() if k is None]
    informe["columnas_descartadas"] = descartadas
    df = df[[c for c, k in codigos.items() if k is not None]].rename(columns=codigos)

    # Filtros de acceso
    falta = [f for f in C.FILTROS if f not in df.columns]
    if falta:
        raise ValueError(f"Faltan las preguntas filtro {falta}")
    ok = np.ones(len(df), dtype=bool)
    for f in C.FILTROS:
        cumple = df[f].map(_acepta).to_numpy()
        informe[f"excluidas_{f}"] = int((ok & ~cumple).sum())
        ok &= cumple
    df = df[ok].reset_index(drop=True)

    out = pd.DataFrame(index=df.index)
    for k, mapa in C.DEMOGRAFICOS.items():
        if k in df:
            out[k] = df[k].map(lambda v: _a_numero(v, mapa))
    # Posgrado: fuera de la población (matrícula de grado)
    posgrado = (out["A3"] == C.A3_POSGRADO) if "A3" in out else pd.Series(False, index=out.index)
    informe["excluidas_posgrado"] = int(posgrado.sum())
    keep = ~posgrado.to_numpy()
    df, out = df[keep].reset_index(drop=True), out[keep].reset_index(drop=True)
    informe["validas"] = len(out)

    # Universidad (A5) → código del censo y sostenimiento oficial; el número de opción se descarta
    a5 = out["A5"] if "A5" in out else pd.Series(np.nan, index=out.index)
    out["UNIV"] = a5.map(lambda v: clave[int(v)][0] if not pd.isna(v) and int(v) in clave else
                         ("OTRA" if v == 88 else (np.nan if pd.isna(v) or v == 99 else "SIN_CLAVE")))
    sost_oficial = a5.map(lambda v: clave[int(v)][1] if not pd.isna(v) and int(v) in clave else np.nan)
    sost_decl = out["A1"].where(out["A1"].isin([1, 2, 3])) if "A1" in out else pd.Series(np.nan, index=out.index)
    out[C.SOST] = sost_oficial.fillna(sost_decl)
    out["SOST_FUENTE"] = np.where(sost_oficial.notna(), "oficial (A5)", np.where(sost_decl.notna(), "declarado (A1)", "sin dato"))
    out[C.TIPO] = out[C.SOST].map({1: 1, 2: 2, 3: 2})  # 1 = pública; 2 = privada
    informe["sost_inferido_de_A5"] = int((sost_oficial.notna() & (out.get("A1") == 9)).sum()) if "A1" in out else 0
    informe["sin_sostenimiento"] = int(out[C.TIPO].isna().sum())
    informe["A1_no_sabe"] = int((out["A1"] == 9).sum()) if "A1" in out else 0
    if "A1" in out:  # concordancia entre lo declarado y lo oficial (descriptivo)
        ambos = sost_oficial.notna() & sost_decl.notna()
        informe["A1_concuerda_con_oficial_pct"] = (float(100 * (sost_oficial[ambos] == sost_decl[ambos]).mean())
                                                   if ambos.any() else np.nan)
    out = out.drop(columns=[c for c in ("A5",) if c in out])  # el número de opción no se conserva

    # H1: opción múltiple (Google Forms separa con ", "; Microsoft Forms con ";") → se busca cada etiqueta completa
    if "H1" in df:
        texto = df["H1"].fillna("").astype(str)
        for cod, etiqueta in C.H1_OPCIONES.items():
            out[cod] = texto.map(lambda t: int(etiqueta in t))
        out.loc[texto.str.strip() == "", list(C.H1_OPCIONES)] = np.nan
    for k, mapa in C.HECHOS.items():
        if k in df:
            out[k] = df[k].map(lambda v: _a_numero(v, mapa))

    for it in C.ITEMS_LIKERT:
        if it in df:
            x = df[it].map(lambda v: _a_numero(v, C.LIKERT_ETIQUETAS))
            if not x.dropna().between(1, 5).all():
                raise ValueError(f"{it} tiene valores fuera de 1–5")
            out[it] = 6 - x if it in C.INVERSOS else x  # recodificación de ítems inversos
    informe["inversos_recodificados"] = [i for i in C.INVERSOS if i in out]

    # Puntuación de dimensión = media de sus ítems (ya recodificados), si responde al menos el 80 % de ellos
    for d, info in C.DIMENSIONES.items():
        cols = [i for i in info["items"] if i in out]
        if cols:
            m = out[cols].mean(axis=1)
            m[out[cols].notna().sum(axis=1) < np.ceil(0.8 * len(cols))] = np.nan
            out[d] = m
    return out, informe


if __name__ == "__main__":
    entrada, salida = sys.argv[1], sys.argv[2]
    datos, inf = limpiar(leer_tabla(entrada))
    datos.to_csv(carpeta(salida) / "datos_limpios.csv", index=False)
    print(inf)
