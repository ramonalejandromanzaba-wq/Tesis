"""Utilidades compartidas: lectura de archivos, rutas de salida y formato numérico en español."""
import sys
from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parent
# La consola de Windows usa cp1252: se fuerza UTF-8 para imprimir tildes y símbolos
for _flujo in (sys.stdout, sys.stderr):
    if hasattr(_flujo, "reconfigure"):
        _flujo.reconfigure(encoding="utf-8", errors="replace")


def leer_tabla(ruta) -> pd.DataFrame:
    """Lee la primera hoja de un .xlsx (o un .csv) exportado del formulario, sin alterar tipos."""
    ruta = Path(ruta)
    if ruta.suffix.lower() == ".csv":
        return pd.read_csv(ruta, dtype=object, sep=None, engine="python")
    hojas = pd.read_excel(ruta, sheet_name=None, dtype=object)
    # Se omite la hoja informativa LEEME de los archivos simulados
    nombre = next(n for n in hojas if n.upper() != "LEEME")
    return hojas[nombre]


def carpeta(salida, sub=None) -> Path:
    p = Path(salida) / sub if sub else Path(salida)
    p.mkdir(parents=True, exist_ok=True)
    return p


def num(x, dec=2) -> str:
    """Número con coma decimal (convención del documento); '---' si falta."""
    if x is None or (isinstance(x, float) and pd.isna(x)):
        return "---"
    if isinstance(x, (int,)) and not isinstance(x, bool):
        return f"{x}"
    return f"{x:.{dec}f}".replace(".", ",")


def pval(p) -> str:
    if p is None or pd.isna(p):
        return "---"
    return r"$<$\,0,001" if p < 0.001 else num(p, 3)
