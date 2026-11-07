"""Estadística descriptiva: composición de la muestra, frecuencias de hechos y resumen de escalas Likert.

Uso: python analisis/descriptivos.py salida/datos_limpios.csv salida/
Las escalas Likert se resumen con mediana y rango intercuartílico (datos ordinales); la media y la desviación
estándar se informan solo como complemento.
"""
import sys

import numpy as np
import pandas as pd

import config as C
from comun import carpeta

GRUPOS = {"Total": None, "Pública": 1, "Privada": 2}


def _sub(df, g):
    return df if g is None else df[df[C.TIPO] == g]


def composicion(df):
    filas = [{"variable": "Respuestas válidas", "categoria": "", "n": len(df), "pct": 100.0}]
    for k, mapa in C.DEMOGRAFICOS.items():
        inv = {v: e for e, v in mapa.items()}
        for cod, n in df[k].value_counts(dropna=True).sort_index().items():
            filas.append({"variable": k, "categoria": inv.get(cod, cod), "n": int(n), "pct": 100 * n / len(df)})
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
            f[f"pct_{g}"] = 100 * s.mean() if len(s) else np.nan
        filas.append(f)
    # proporción a quienes se pidió al menos una categoría especial
    esp = validos[C.H1_ESPECIALES].max(axis=1)
    f = {"codigo": "IE01", "categoria": "Al menos una categoría especial (salud, discapacidad o biométricos)", "especial": True}
    for g, v in GRUPOS.items():
        s = esp[validos.index.isin(_sub(validos, v).index)].dropna()
        f[f"n_{g}"], f[f"pct_{g}"] = len(s), (100 * s.mean() if len(s) else np.nan)
    filas.append(f)
    return pd.DataFrame(filas)


def indicadores_hechos(df):
    filas = []
    for nombre, (q, si, excl) in C.AFIRMATIVO.items():
        base = df if q != "H3" else df[df["H2"] == 1]  # la forma del consentimiento solo para quienes lo dieron
        f = {"indicador": nombre, "pregunta": q}
        for g, v in GRUPOS.items():
            s = _sub(base, v)[q].dropna()
            s = s[~s.isin(excl)]
            f[f"n_{g}"], f[f"pct_{g}"] = len(s), (100 * s.isin(si).mean() if len(s) else np.nan)
        filas.append(f)
    return pd.DataFrame(filas)


def resumen_likert(df):
    filas = []
    for d, info in C.DIMENSIONES.items():
        for col in info["items"] + [d]:
            s = df[col].dropna()
            if s.empty:
                continue
            filas.append({"dimension": info["nombre"], "variable": col, "es_dimension": col == d,
                          "inverso_recodificado": col in C.INVERSOS, "n": len(s), "mediana": s.median(),
                          "q1": s.quantile(0.25), "q3": s.quantile(0.75), "ric": s.quantile(0.75) - s.quantile(0.25),
                          "media": s.mean(), "de": s.std(), "pct_de_acuerdo": 100 * (s >= 4).mean()})
    return pd.DataFrame(filas)


def ejecutar(limpios, salida):
    df = pd.read_csv(limpios)
    out = carpeta(salida)
    res = {"composicion": composicion(df), "datos_solicitados": datos_solicitados(df),
           "indicadores_hechos": indicadores_hechos(df), "likert": resumen_likert(df)}
    for k, t in res.items():
        t.to_csv(out / f"desc_{k}.csv", index=False)
    return res


if __name__ == "__main__":
    for k, t in ejecutar(sys.argv[1], sys.argv[2]).items():
        print(f"\n== {k} ==\n{t.head(20).to_string(index=False)}")
