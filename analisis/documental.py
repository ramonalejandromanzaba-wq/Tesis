"""Lectura del registro documental (plantilla analisis_documental.xlsx, hoja Registro) e índice ITD.

La copia llena está en privado/analisis_documental.xlsx (fuera del repositorio). Cada universidad se identifica
solo por su código (U01, …). Este módulo no produce ninguna salida por universidad: lo usan brechas.py,
kappa_documental.py y sensibilidad_itd.py, que solo exportan agregados.
"""
from pathlib import Path

import numpy as np
import pandas as pd

from comun import BASE

RUTA_PRIVADA = BASE.parent / "privado" / "analisis_documental.xlsx"
# 15 indicadores principales (ID06 desdoblado en ID06a, comunicaciones nacionales, e ID06b, transferencias
# internacionales; Om-11) y 8 complementarios (ID15 a ID22), que no entran en el ITD.
PRINCIPALES = ["ID01", "ID02", "ID03", "ID04", "ID05", "ID06a", "ID06b"] + [f"ID{i:02d}" for i in range(7, 15)]
COMPLEMENTARIOS = [f"ID{i:02d}" for i in range(15, 23)]
TODOS = PRINCIPALES + COMPLEMENTARIOS
SOST_TIPO = {"Pública": 1, "Particular cofinanciada": 2, "Particular autofinanciada": 2}


def leer_registro(ruta=None, hoja="Registro") -> pd.DataFrame:
    """Devuelve codigo | sostenimiento | tipo (1 pública, 2 privada) | ID01…ID22 (S/P/N)."""
    ruta = Path(ruta) if ruta else RUTA_PRIVADA
    t = pd.read_excel(ruta, sheet_name=hoja, header=3, dtype=object)
    cod = next(c for c in t.columns if str(c).startswith("Código"))
    out = pd.DataFrame({"codigo": t[cod], "sostenimiento": t.get("Sostenimiento")})
    for i in TODOS:
        col = f"{i} calif."
        out[i] = t[col].map(lambda v: str(v).strip().upper() if isinstance(v, str) and v.strip() else np.nan) if col in t else np.nan
    out = out[out["codigo"].notna()].reset_index(drop=True)
    out["tipo"] = out["sostenimiento"].map(SOST_TIPO)
    return out


def puntaje(cal, p=0.5):
    """S = 1; P = p (0,5 por diseño; 0 y 1 en el análisis de sensibilidad); N = 0."""
    return cal.map({"S": 1.0, "P": p, "N": 0.0})


def puntaje_indicador(reg: pd.DataFrame, idd: str, p=0.5) -> pd.Series:
    """Puntaje de un indicador; "ID06" (par de la brecha con H7) es el promedio de ID06a e ID06b."""
    if idd == "ID06":
        return pd.concat([puntaje(reg["ID06a"], p), puntaje(reg["ID06b"], p)], axis=1).mean(axis=1, skipna=False)
    return puntaje(reg[idd], p)


def itd(reg: pd.DataFrame, p=0.5) -> pd.Series:
    """ITD_u = 100/15 · Σ s_{u,i} sobre los 15 principales; solo si los 15 están calificados."""
    m = pd.DataFrame({i: puntaje(reg[i], p) for i in PRINCIPALES})
    v = 100 / len(PRINCIPALES) * m.sum(axis=1)
    v[m.notna().sum(axis=1) < len(PRINCIPALES)] = np.nan
    return v
