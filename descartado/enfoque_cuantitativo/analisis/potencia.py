"""Potencia estadística y efecto mínimo detectable de H1–H3 (R1.2 y plan B de R3).

Uso:
    python analisis/potencia.py                 # diseño: n = 384 (246 públicas / 138 privadas)
    python analisis/potencia.py 300             # cualquier n total, con la misma proporción 64/36
    python analisis/potencia.py 300 190 110     # n total y tamaños reales de los grupos de H1
Parámetros comunes: α = 0,05 bilateral; potencia 1 − β = 0,80. Los mismos valores se ingresan en G*Power 3.1
(analisis/GPOWER_INSTRUCCIONES.md) para la verificación cruzada.

- H2 (Spearman): se aproxima con la correlación de Pearson (transformación z de Fisher), como en el modelo
  "Correlation: Bivariate normal model" de G*Power; la eficiencia relativa de Spearman frente a Pearson con
  datos normales es ≈ 0,91, por lo que también se informa el valor corregido.
- H3 (chi-cuadrado 2×2, gl = 1): efecto w de Cohen con la distribución chi-cuadrado no central.
- H1 (U de Mann-Whitney): prueba t para muestras independientes con el método de la eficiencia relativa
  asintótica (ARE) de G*Power: ARE = 3/π ≈ 0,955 con distribución madre normal; mínimo 0,864 (peor caso).
Además informa la potencia alcanzada para efectos de referencia (ρ = 0,15; w = 0,15; d = 0,33), de modo que
con el n alcanzado en enero de 2027 se reporte la potencia efectiva (plan B).
"""
import sys

import numpy as np
import pandas as pd
from scipy import stats
from scipy.optimize import brentq
from statsmodels.stats.power import GofChisquarePower, TTestIndPower

import comun  # noqa: F401  (configura la salida en UTF-8)

ALFA, POT = 0.05, 0.80
ARE_NORMAL, ARE_MIN = 3 / np.pi, 0.864
EFICIENCIA_SPEARMAN = 0.912  # (3/π)²·… ≈ 0,91 frente a Pearson con datos normales


def potencia_r(r, n, alfa=ALFA):
    """Potencia de la prueba bilateral de ρ = 0 con la aproximación z de Fisher."""
    z = np.arctanh(r) * np.sqrt(n - 3)
    c = stats.norm.ppf(1 - alfa / 2)
    return float(stats.norm.sf(c - z) + stats.norm.cdf(-c - z))


def r_minimo(n, alfa=ALFA, pot=POT):
    return brentq(lambda r: potencia_r(r, n, alfa) - pot, 1e-4, 0.99)


def w_minimo(n, alfa=ALFA, pot=POT):
    return float(np.ravel(GofChisquarePower().solve_power(effect_size=None, nobs=n, alpha=alfa, power=pot, n_bins=2))[0])


def potencia_w(w, n, alfa=ALFA):
    return float(GofChisquarePower().power(effect_size=w, nobs=n, alpha=alfa, n_bins=2))


def d_minimo(n1, n2, are=ARE_NORMAL, alfa=ALFA, pot=POT):
    """Efecto d mínimo de Mann-Whitney por ARE: se resuelve la prueba t con n_i·ARE."""
    return float(np.ravel(TTestIndPower().solve_power(effect_size=None, nobs1=n1 * are, ratio=n2 / n1, alpha=alfa, power=pot))[0])


def potencia_d(d, n1, n2, are=ARE_NORMAL, alfa=ALFA):
    return float(TTestIndPower().power(effect_size=d, nobs1=n1 * are, ratio=n2 / n1, alpha=alfa))


def tabla(n=384, n1=None, n2=None):
    n1 = n1 if n1 else round(n * 246 / 384)
    n2 = n2 if n2 else n - n1
    r = r_minimo(n)
    filas = [
        {"hipotesis": "H2", "prueba": "Correlación de Spearman (aprox. Pearson, z de Fisher)", "n": n,
         "efecto_minimo_detectable": r, "medida": "ρ", "efecto_minimo_corregido_spearman": r_minimo(round(n * EFICIENCIA_SPEARMAN)),
         "efecto_referencia": 0.15, "potencia_con_referencia": potencia_r(0.15, n)},
        {"hipotesis": "H3", "prueba": "Chi-cuadrado 2×2 (gl = 1)", "n": n, "efecto_minimo_detectable": w_minimo(n),
         "medida": "w", "efecto_minimo_corregido_spearman": np.nan, "efecto_referencia": 0.15,
         "potencia_con_referencia": potencia_w(0.15, n)},
        {"hipotesis": "H1", "prueba": f"U de Mann-Whitney ({n1}/{n2}), ARE = 3/π (madre normal)", "n": n,
         "efecto_minimo_detectable": d_minimo(n1, n2), "medida": "d", "efecto_minimo_corregido_spearman": np.nan,
         "efecto_referencia": 0.33, "potencia_con_referencia": potencia_d(0.33, n1, n2)},
        {"hipotesis": "H1", "prueba": f"U de Mann-Whitney ({n1}/{n2}), ARE mínima = 0,864 (peor caso)", "n": n,
         "efecto_minimo_detectable": d_minimo(n1, n2, ARE_MIN), "medida": "d", "efecto_minimo_corregido_spearman": np.nan,
         "efecto_referencia": 0.33, "potencia_con_referencia": potencia_d(0.33, n1, n2, ARE_MIN)},
    ]
    return pd.DataFrame(filas)


def muestra_finita(N, z=1.96, p=0.5, e=0.05):
    """Referencia: fórmula para población finita (Cochran). Se informa, pero no fija el tamaño de muestra."""
    return N * z ** 2 * p * (1 - p) / (e ** 2 * (N - 1) + z ** 2 * p * (1 - p))


def autoprueba():
    ok = True
    def chk(nombre, obtenido, esperado, tol):
        nonlocal ok
        bien = abs(obtenido - esperado) <= tol
        ok &= bien
        print(f"{'OK ' if bien else 'ERR'} {nombre}: obtenido {obtenido:.4f}, esperado {esperado:.4f}")
    # w mínimo con gl = 1: λ = 7,849 para potencia 0,80 → w = √(λ/n)
    lam = brentq(lambda l: stats.ncx2.sf(stats.chi2.ppf(0.95, 1), 1, l) - 0.80, 0.1, 50)
    chk("λ no central (gl = 1, potencia 0,80)", lam, 7.849, 0.005)
    chk("w mínimo con n = 384", w_minimo(384), np.sqrt(lam / 384), 1e-3)
    chk("d de la prueba t con 64 por grupo (Cohen: d ≈ 0,50)", TTestIndPower().solve_power(None, nobs1=64, ratio=1, alpha=0.05, power=0.8), 0.50, 0.01)
    chk("potencia de r = 0,30 con n = 84 (Cohen: ≈ 0,80)", potencia_r(0.30, 84), 0.80, 0.02)
    print("AUTOPRUEBA DE POTENCIA SUPERADA" if ok else "AUTOPRUEBA DE POTENCIA CON ERRORES")
    return ok


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "prueba":
        sys.exit(0 if autoprueba() else 1)
    args = [int(a) for a in sys.argv[1:]]
    t = tabla(*args) if args else tabla()
    pd.set_option("display.width", 200)
    print(t.round(3).to_string(index=False))
