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


def suprimir(t: pd.DataFrame, col_n="n", total=None, minimo=5) -> pd.DataFrame:
    """Supresión de celdas pequeñas (reporte agregado): las categorías con menos de `minimo` respuestas se agrupan
    en una sola fila "Otras categorías (n < 5 cada una)". Si el grupo resultante también tiene menos de `minimo`,
    se informa como "< 5" sin porcentaje. Devuelve columnas categoria | n | pct."""
    t = t.copy()
    total = total if total else t[col_n].sum()
    peq = t[col_n] < minimo
    filas = t[~peq][["categoria", col_n]].to_dict("records")
    if peq.any():
        n_peq = int(t.loc[peq, col_n].sum())
        filas.append({"categoria": f"Otras categorías agrupadas ({int(peq.sum())}; n < {minimo} cada una)",
                      col_n: n_peq if n_peq >= minimo else f"< {minimo}"})
    r = pd.DataFrame(filas).rename(columns={col_n: "n"})
    r["pct"] = r["n"].map(lambda v: 100 * v / total if isinstance(v, (int, float)) and total else float("nan"))
    return r


def pval(p) -> str:
    if p is None or pd.isna(p):
        return "---"
    return r"$<$\,0,001" if p < 0.001 else num(p, 3)
