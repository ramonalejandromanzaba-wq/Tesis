"""Análisis de sensibilidad del índice de transparencia documental (R1.6).

Uso: python analisis/sensibilidad_itd.py [privado/analisis_documental.xlsx] salida/
Recalcula el ITD con tres pesos para el nivel parcial: P = 0 (criterio estricto), P = 0,5 (decisión de diseño)
y P = 1 (criterio laxo), y compara pública y privada en cada escenario (mediana, media y diferencia; U de
Mann-Whitney exploratoria). La conclusión por sostenimiento es robusta si el signo de la diferencia no cambia.
Solo agregados: nunca se exporta el ITD de una universidad.
"""
import sys

import numpy as np
import pandas as pd
from scipy import stats

import documental as D
from comun import carpeta

PESOS = {"P = 0 (estricto)": 0.0, "P = 0,5 (diseño)": 0.5, "P = 1 (laxo)": 1.0}


def calcular(reg: pd.DataFrame) -> pd.DataFrame:
    filas = []
    for nombre, p in PESOS.items():
        v = D.itd(reg, p)
        pub, pri = v[reg["tipo"] == 1].dropna(), v[reg["tipo"] == 2].dropna()
        f = {"escenario": nombre, "P": p, "n_total": int(v.notna().sum()), "mediana_total": v.median(),
             "media_total": v.mean(), "n_publica": len(pub), "mediana_publica": pub.median(), "media_publica": pub.mean(),
             "n_privada": len(pri), "mediana_privada": pri.median(), "media_privada": pri.mean()}
        f["diferencia_medianas_pub_menos_priv"] = f["mediana_publica"] - f["mediana_privada"]
        if len(pub) >= 2 and len(pri) >= 2:
            f["p_mann_whitney"] = stats.mannwhitneyu(pub, pri, alternative="two-sided").pvalue
        else:
            f["p_mann_whitney"] = np.nan
        filas.append(f)
    t = pd.DataFrame(filas)
    signos = np.sign(t["diferencia_medianas_pub_menos_priv"].dropna())
    t["conclusion_robusta"] = bool(len(signos) == len(PESOS) and signos.nunique() == 1)
    return t


if __name__ == "__main__":
    reg = D.leer_registro(sys.argv[1] if len(sys.argv) > 2 else None)
    t = calcular(reg)
    t.to_csv(carpeta(sys.argv[-1]) / "sensibilidad_itd.csv", index=False)
    print(t.round(2).to_string(index=False))
