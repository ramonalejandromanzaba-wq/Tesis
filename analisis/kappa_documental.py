"""Confiabilidad del registro documental con el kappa de Cohen ponderado (R1.5).

Uso: python analisis/kappa_documental.py privado/analisis_documental.xlsx privado/analisis_documental_observador2.xlsx salida/
- Intraobservador: primera calificación (hoja Registro) frente a la reverificación del mismo observador, al menos dos
  semanas después (hoja Reverificación), sobre ⌈0,2·U⌉ universidades elegidas al azar.
- Interobservador: primera calificación frente a la de un segundo observador independiente que califica a ciegas
  las mismas universidades en su propio archivo (plantilla generada con --observador2).
Categorías ordinales N < P < S (0, 1, 2) con pesos lineales (Cohen, 1968): un desacuerdo S–N pesa el doble que S–P.
Interpretación de Landis y Koch (1977). Solo se exportan valores agregados (sobre todas las universidades y los
14 indicadores principales), nunca por universidad.
"""
import sys

import numpy as np
import pandas as pd

import documental as D
from comun import carpeta

ORD = {"N": 0, "P": 1, "S": 2}


def kappa_ponderado(a, b, k=3, pesos="lineal"):
    """κ_w = 1 − Σ w_ij o_ij / Σ w_ij e_ij, con w_ij = |i − j| (lineal) o (i − j)² (cuadrático)."""
    a, b = np.asarray(a, dtype=int), np.asarray(b, dtype=int)
    if len(a) == 0:
        return np.nan
    o = np.zeros((k, k))
    for i, j in zip(a, b):
        o[i, j] += 1
    o /= o.sum()
    e = np.outer(o.sum(axis=1), o.sum(axis=0))
    idx = np.arange(k)
    w = np.abs(idx[:, None] - idx[None, :]).astype(float)
    if pesos == "cuadratico":
        w = w ** 2
    den = (w * e).sum()
    return float(1 - (w * o).sum() / den) if den > 0 else np.nan


def landis_koch(k):
    if pd.isna(k):
        return "---"
    for corte, et in [(0, "pobre"), (0.20, "leve"), (0.40, "aceptable"), (0.60, "moderado"), (0.80, "sustancial")]:
        if k <= corte:
            return et
    return "casi perfecto"


def pares(r1: pd.DataFrame, r2: pd.DataFrame):
    m = r1.merge(r2, on="codigo", suffixes=("_1", "_2"))
    a, b = [], []
    for i in D.PRINCIPALES:
        x = m[[f"{i}_1", f"{i}_2"]].dropna()
        x = x[x[f"{i}_1"].isin(ORD) & x[f"{i}_2"].isin(ORD)]
        a += list(x[f"{i}_1"].map(ORD))
        b += list(x[f"{i}_2"].map(ORD))
    return a, b, int(m["codigo"].nunique())


def leer_reverificacion(ruta) -> pd.DataFrame:
    """Hoja Reverificación: N.º en Registro | Código | Fecha | IDxx 2.ª … → codigo | ID01…ID14."""
    t = pd.read_excel(ruta, sheet_name="Reverificación", header=3, dtype=object)
    reg = D.leer_registro(ruta)
    t = t[t["N.º en Registro"].notna()]
    out = pd.DataFrame({"codigo": [reg["codigo"].iloc[int(n) - 1] for n in t["N.º en Registro"]]})
    for i in D.PRINCIPALES:
        out[i] = t[f"{i} 2.ª"].map(lambda v: str(v).strip().upper() if isinstance(v, str) else np.nan).to_numpy()
    return out


def calcular(ruta1, ruta_obs2=None):
    r1 = D.leer_registro(ruta1)
    filas = []
    fuentes = [("Intraobservador (reverificación)", leer_reverificacion(ruta1))]
    if ruta_obs2:
        fuentes.append(("Interobservador (segundo observador, calificación ciega)", D.leer_registro(ruta_obs2)))
    for nombre, r2 in fuentes:
        a, b, n_u = pares(r1, r2)
        k = kappa_ponderado(a, b) if a else np.nan
        filas.append({"tipo": nombre, "universidades": n_u, "calificaciones_comparadas": len(a),
                      "acuerdo_bruto_pct": 100 * np.mean(np.array(a) == np.array(b)) if a else np.nan,
                      "kappa_ponderado_lineal": k, "interpretacion": landis_koch(k)})
    return pd.DataFrame(filas)


def autoprueba():
    ok = True
    try:
        from sklearn.metrics import cohen_kappa_score
    except ImportError:
        cohen_kappa_score = None
    a = [2, 2, 1, 0, 2, 1, 0, 0, 2, 1]
    b = [2, 1, 1, 0, 2, 2, 0, 1, 2, 1]
    k = kappa_ponderado(a, b)
    if cohen_kappa_score:
        ref = cohen_kappa_score(a, b, weights="linear")
        bien = abs(k - ref) < 1e-9
        print(f"{'OK ' if bien else 'ERR'} kappa ponderado lineal = {k:.4f}; scikit-learn = {ref:.4f}")
        ok &= bien
    bien = abs(kappa_ponderado([0, 1, 2] * 5, [0, 1, 2] * 5) - 1) < 1e-12
    print(f"{'OK ' if bien else 'ERR'} acuerdo perfecto → κ = 1")
    return ok & bien


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "prueba":
        sys.exit(0 if autoprueba() else 1)
    ruta1 = sys.argv[1]
    obs2 = sys.argv[2] if len(sys.argv) > 3 else None
    t = calcular(ruta1, obs2)
    t.to_csv(carpeta(sys.argv[-1]) / "kappa_documental.csv", index=False)
    print(t.round(3).to_string(index=False))
