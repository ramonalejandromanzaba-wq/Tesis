"""Estadística descriptiva: composición de la muestra, frecuencias de hechos y resumen de escalas Likert.

Uso: python analisis/descriptivos.py salida/datos_limpios.csv salida/
Reglas de reporte (Cap. 3, reporte agregado):
- Nunca se produce un resultado por universidad: solo total y, como máximo, por sostenimiento, área, semestre,
  edad y modalidad. De la universidad solo se informa cuántas instituciones distintas aportaron respuestas.
- Supresión de celdas pequeñas: ninguna categoría con menos de 5 respuestas se reporta sola (se agrupa).
- Las preguntas de hechos se informan con y sin "No recuerdo" (y "No estoy seguro(a)" en H16) en el denominador.
Las escalas Likert se resumen con mediana y rango intercuartílico (datos ordinales); la media y la desviación
estándar se informan solo como complemento.
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

import config as C
from comun import carpeta, suprimir

GRUPOS = {"Total": None, "Pública": 1, "Privada": 2}
COMPOSICION = {"A2": "Área de la carrera", "A3": "Semestre", "A4": "Edad", C.SOST: "Sostenimiento",
               "A6": "Modalidad", "A7": "Canal de difusión"}


def _sub(df, g):
    return df if g is None else df[df[C.TIPO] == g]


def _nombres(var):
    if var == C.SOST:
        return C.SOST_NOMBRE
    return {v: e for e, v in C.DEMOGRAFICOS[var].items()}


def composicion(df, poblacion=None):
    """Composición de la muestra por variable, con supresión de celdas < 5 y, si se dispone, el % de la matrícula
    de Pichincha (SIIES) para la misma categoría. `poblacion`: DataFrame variable | categoria | pct_poblacion."""
    filas = [{"variable": "Respuestas válidas", "categoria": "", "n": len(df), "pct": 100.0}]
    univ = df["UNIV"].dropna() if "UNIV" in df else pd.Series(dtype=object)
    del_censo = univ[univ.astype(str).str.match(r"^U\d+$")]
    filas.append({"variable": "Universidades del censo con al menos una respuesta", "categoria": "",
                  "n": int(del_censo.nunique()), "pct": np.nan})
    filas.append({"variable": "Respuestas con universidad del censo identificada", "categoria": "",
                  "n": int(len(del_censo)), "pct": 100 * len(del_censo) / len(df) if len(df) else np.nan})
    for var, titulo in COMPOSICION.items():
        if var not in df:
            continue
        nom = _nombres(var)
        cuenta = df[var].value_counts(dropna=True).sort_index()
        t = pd.DataFrame({"categoria": [nom.get(c, c) for c in cuenta.index], "n": cuenta.to_numpy()})
        t = suprimir(t, "n", total=len(df))
        t.insert(0, "variable", titulo)
        if poblacion is not None:
            p = poblacion[poblacion["variable"] == titulo].set_index("categoria")["pct_poblacion"]
            t["pct_poblacion"] = t["categoria"].map(p)
        filas += t.to_dict("records")
    sin = int(df[C.TIPO].isna().sum()) if C.TIPO in df else 0
    filas.append({"variable": "Sin sostenimiento (excluidas de H1 y H3)", "categoria": "", "n": sin,
                  "pct": 100 * sin / len(df) if len(df) else np.nan})
    return pd.DataFrame(filas)


def datos_solicitados(df):
    validos = df[df["H1_99"] != 1]
    filas = []
    for cod, etiqueta in C.H1_OPCIONES.items():
        if cod == "H1_99":
            continue
        f = {"codigo": cod, "categoria": etiqueta, "especial": cod in C.H1_ESPECIALES}
        for g, v in GRUPOS.items():
            s = _sub(validos, v)[cod].dropna()
            f[f"n_{g}"] = len(s)
            f[f"pct_{g}"] = 100 * s.mean() if len(s) >= C.MIN_CELDA else np.nan
        filas.append(f)
    # proporción a quienes se pidió al menos una categoría especial
    esp = validos[C.H1_ESPECIALES].max(axis=1)
    f = {"codigo": "IE01", "categoria": "Al menos una categoría especial (salud, discapacidad o biométricos)", "especial": True}
    for g, v in GRUPOS.items():
        s = esp[validos.index.isin(_sub(validos, v).index)].dropna()
        f[f"n_{g}"], f[f"pct_{g}"] = len(s), (100 * s.mean() if len(s) >= C.MIN_CELDA else np.nan)
    filas.append(f)
    return pd.DataFrame(filas)


def indicadores_hechos(df):
    """% afirmativo con "No recuerdo" en el denominador (contado como no afirmativo, igual que en el KR-20),
    % afirmativo sin "No recuerdo" y % de "No recuerdo"."""
    filas = []
    for nombre, (q, si, excl) in C.AFIRMATIVO.items():
        if q not in df:
            continue
        base = df if q != "H3" else df[df["H2"] == 1]  # la forma del consentimiento solo para quienes lo dieron
        nr = [C.NO_RECUERDO] if q not in ("H3", "H11") else ([4] if q == "H3" else [])
        f = {"indicador": nombre, "pregunta": q}
        for g, v in GRUPOS.items():
            s = _sub(base, v)[q].dropna()
            s = s[~s.isin(excl)]
            sin_nr = s[~s.isin(nr)]
            f[f"n_{g}"] = len(s)
            f[f"pct_{g}"] = 100 * s.isin(si).mean() if len(s) >= C.MIN_CELDA else np.nan
            f[f"pct_sin_NR_{g}"] = 100 * sin_nr.isin(si).mean() if len(sin_nr) >= C.MIN_CELDA else np.nan
            f[f"pct_NR_{g}"] = 100 * s.isin(nr).mean() if (nr and len(s) >= C.MIN_CELDA) else np.nan
        filas.append(f)
    return pd.DataFrame(filas)


def resumen_likert(df):
    filas = []
    for d, info in C.DIMENSIONES.items():
        for col in info["items"] + [d]:
            if col not in df:
                continue
            s = df[col].dropna()
            if s.empty:
                continue
            filas.append({"dimension": info["nombre"], "variable": col, "es_dimension": col == d,
                          "inverso_recodificado": col in C.INVERSOS, "n": len(s), "mediana": s.median(),
                          "q1": s.quantile(0.25), "q3": s.quantile(0.75), "ric": s.quantile(0.75) - s.quantile(0.25),
                          "media": s.mean(), "de": s.std(), "pct_de_acuerdo": 100 * (s >= 4).mean()})
    return pd.DataFrame(filas)


def ejecutar(limpios, salida, poblacion=None):
    df = pd.read_csv(limpios)
    out = carpeta(salida)
    pob = None
    if poblacion and Path(poblacion).exists():
        pob = pd.read_csv(poblacion)
    res = {"composicion": composicion(df, pob), "datos_solicitados": datos_solicitados(df),
           "indicadores_hechos": indicadores_hechos(df), "likert": resumen_likert(df)}
    for k, t in res.items():
        t.to_csv(out / f"desc_{k}.csv", index=False)
    return res


if __name__ == "__main__":
    for k, t in ejecutar(sys.argv[1], sys.argv[2]).items():
        print(f"\n== {k} ==\n{t.head(30).to_string(index=False)}")
