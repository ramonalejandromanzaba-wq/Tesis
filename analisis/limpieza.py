"""Limpieza y recodificación de las respuestas exportadas del formulario.

Uso: python analisis/limpieza.py datos/respuestas.xlsx salida/
- Identifica cada columna por el código entre corchetes al inicio del título de la pregunta ("[H4] …").
- Conserva solo columnas con código conocido: elimina correos, nombres, marcas temporales, ID de la plataforma
  y cualquier otra columna identificativa.
- Excluye a quienes no consintieron, son menores de 18 años o no son estudiantes (P00–P02).
- Convierte las etiquetas de respuesta en códigos numéricos (config.py), desdobla H1 en columnas binarias,
  recodifica los ítems inversos (x' = 6 − x) y calcula las puntuaciones de dimensión.
"""
import re
import sys

import numpy as np
import pandas as pd

import config as C
from comun import carpeta, leer_tabla

PATRON_CODIGO = re.compile(r"^\s*\[?\s*(P0\d|A\d|H\d{1,2}|INF\d|CON\d|DER\d|CNF\d)\s*\]?", re.IGNORECASE)


def _codigo(col):
    m = PATRON_CODIGO.match(str(col))
    return m.group(1).upper() if m else None


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


def limpiar(df: pd.DataFrame):
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
    informe["validas"] = len(df)

    out = pd.DataFrame(index=df.index)
    for k, mapa in C.DEMOGRAFICOS.items():
        if k in df:
            out[k] = df[k].map(lambda v: _a_numero(v, mapa))
    out[C.TIPO] = out["A1"].map({1: 1, 2: 2, 3: 2}) if "A1" in out else np.nan  # 1 = pública; 2 = privada

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
