"""Estadística inferencial: normalidad, hipótesis H1–H3 y análisis exploratorios, con tamaños del efecto.

Uso: python analisis/inferencial.py salida/datos_limpios.csv salida/
Hipótesis (Cap. 3, sección de hipótesis), α = 0,05:
  H1  La información recibida (dimensión INF) difiere entre estudiantes de universidades públicas y privadas.
      → U de Mann-Whitney; tamaño del efecto r = |Z| / √N.
  H2  El conocimiento de derechos (DER) se relaciona con la confianza en la protección de datos (CNF).
      → correlación de Spearman (ρ).
  H3  La proporción de estudiantes a quienes se pidió consentimiento (H2 = Sí) difiere según el tipo de universidad.
      → chi-cuadrado de Pearson (prueba exacta de Fisher si alguna frecuencia esperada es < 5); V de Cramér.
Los contrastes exploratorios se corrigen por comparaciones múltiples con el método de Holm.
"""
import sys

import numpy as np
import pandas as pd
from scipy import stats

import comun  # noqa: F401  (configura la salida en UTF-8)
import config as C
from comun import carpeta


def normalidad(df, n_mc=2000):
    """Kolmogorov-Smirnov con parámetros estimados (corrección de Lilliefors por Monte Carlo, scipy.goodness_of_fit)."""
    filas = []
    for d, info in C.DIMENSIONES.items():
        x = df[d].dropna().to_numpy()
        if len(x) < 8:
            continue
        r = stats.goodness_of_fit(stats.norm, x, statistic="ks", n_mc_samples=n_mc, rng=np.random.default_rng(2026))
        filas.append({"dimension": info["nombre"], "codigo": d, "n": len(x), "D": r.statistic, "p": r.pvalue,
                      "normal_a_0_05": r.pvalue >= C.ALPHA})
    return pd.DataFrame(filas)


def mann_whitney(df, var):
    a = df.loc[df[C.TIPO] == 1, var].dropna().to_numpy()
    b = df.loc[df[C.TIPO] == 2, var].dropna().to_numpy()
    if len(a) < 2 or len(b) < 2:
        return None
    u = stats.mannwhitneyu(a, b, alternative="two-sided", method="asymptotic")
    n1, n2 = len(a), len(b)
    N = n1 + n2
    # Z con corrección por empates (normal aproximada) y r = |Z| / √N (Fritz et al., 2012)
    _, t = np.unique(np.concatenate([a, b]), return_counts=True)
    sigma = np.sqrt(n1 * n2 / 12 * ((N + 1) - (t ** 3 - t).sum() / (N * (N - 1))))
    z = (u.statistic - n1 * n2 / 2) / sigma if sigma > 0 else 0.0
    return {"variable": var, "n_publica": n1, "n_privada": n2, "mediana_publica": np.median(a), "mediana_privada": np.median(b),
            "U": u.statistic, "Z": z, "p": u.pvalue, "r": abs(z) / np.sqrt(N)}


def chi_cuadrado(df, var, positivos):
    d = df[[C.TIPO, var]].dropna()
    if d.empty:
        return None
    tabla = pd.crosstab(d[C.TIPO], d[var].isin(positivos)).reindex(index=[1, 2], columns=[True, False], fill_value=0)
    obs = tabla.to_numpy()
    if (obs.sum(axis=1) == 0).any() or (obs.sum(axis=0) == 0).any():
        return None
    chi2, p, gl, esperado = stats.chi2_contingency(obs, correction=False)
    prueba = "Chi-cuadrado"
    if (esperado < 5).any():
        p = stats.fisher_exact(obs).pvalue
        prueba = "Exacta de Fisher"
    n = obs.sum()
    return {"variable": var, "prueba": prueba, "publica_si": obs[0, 0], "publica_no": obs[0, 1], "privada_si": obs[1, 0],
            "privada_no": obs[1, 1], "pct_si_publica": 100 * obs[0, 0] / obs[0].sum(), "pct_si_privada": 100 * obs[1, 0] / obs[1].sum(),
            "chi2": chi2, "gl": gl, "p": p, "V_Cramer": np.sqrt(chi2 / (n * (min(obs.shape) - 1))),
            "esperado_min": esperado.min()}


def spearman(df, x, y):
    d = df[[x, y]].dropna()
    if len(d) < 3:
        return None
    r = stats.spearmanr(d[x], d[y])
    return {"x": x, "y": y, "n": len(d), "rho": r.statistic, "p": r.pvalue}


def holm(p):
    p = np.asarray(p, dtype=float)
    orden = np.argsort(p)
    ajust = np.empty_like(p)
    m = len(p)
    acumulado = 0.0
    for k, i in enumerate(orden):
        acumulado = max(acumulado, min(1.0, (m - k) * p[i]))
        ajust[i] = acumulado
    return ajust


def hipotesis(df):
    filas = []
    h1 = mann_whitney(df, "INF")
    filas.append({"hipotesis": "H1", "prueba": "U de Mann-Whitney", "estadistico": h1 and h1["U"], "p": h1 and h1["p"],
                  "efecto": h1 and h1["r"], "medida_efecto": "r", "n": h1 and h1["n_publica"] + h1["n_privada"]})
    h2 = spearman(df, "DER", "CNF")
    filas.append({"hipotesis": "H2", "prueba": "Correlación de Spearman", "estadistico": h2 and h2["rho"], "p": h2 and h2["p"],
                  "efecto": h2 and h2["rho"], "medida_efecto": "rho", "n": h2 and h2["n"]})
    h3 = chi_cuadrado(df, "H2", [1])
    filas.append({"hipotesis": "H3", "prueba": h3 and h3["prueba"], "estadistico": h3 and h3["chi2"], "p": h3 and h3["p"],
                  "efecto": h3 and h3["V_Cramer"], "medida_efecto": "V de Cramér", "n": h3 and (h3["publica_si"] + h3["publica_no"] + h3["privada_si"] + h3["privada_no"])})
    t = pd.DataFrame(filas)
    t["decision"] = np.where(t["p"].isna(), "Sin datos", np.where(t["p"] < C.ALPHA, "Se rechaza H0", "No se rechaza H0"))
    return t, {"H1": h1, "H2": h2, "H3": h3}


def exploratorios(df):
    mw = pd.DataFrame([r for r in (mann_whitney(df, d) for d in C.DIMENSIONES) if r])
    if not mw.empty:
        mw["p_holm"] = holm(mw["p"])
    chi = pd.DataFrame([r for r in (chi_cuadrado(df, q, si) for _, (q, si, excl) in C.AFIRMATIVO.items()
                                    if q in df and q != "H3") if r])
    if not chi.empty:
        chi = chi.drop_duplicates("variable")
        chi["p_holm"] = holm(chi["p"])
    dims = list(C.DIMENSIONES)
    sp = pd.DataFrame([spearman(df, a, b) for i, a in enumerate(dims) for b in dims[i + 1:]])
    if not sp.empty:
        sp["p_holm"] = holm(sp["p"])
    return {"mann_whitney": mw, "chi_cuadrado": chi, "spearman": sp}


def ejecutar(limpios, salida):
    df = pd.read_csv(limpios)
    out = carpeta(salida)
    res = {"normalidad": normalidad(df)}
    res["hipotesis"], _ = hipotesis(df)
    res.update({f"expl_{k}": v for k, v in exploratorios(df).items()})
    for k, t in res.items():
        t.to_csv(out / f"inf_{k}.csv", index=False)
    return res


def autoprueba():
    ok = True
    def chk(nombre, obtenido, esperado, tol=1e-3):
        nonlocal ok
        bien = abs(obtenido - esperado) <= tol
        ok &= bien
        print(f"{'OK ' if bien else 'ERR'} {nombre}: obtenido {obtenido:.4f}, esperado {esperado:.4f}")
    # 2×2 [[10,20],[20,10]] → χ² = 6,667; V = 0,333
    df = pd.DataFrame({C.TIPO: [1] * 30 + [2] * 30, "H2": [1] * 10 + [2] * 20 + [1] * 20 + [2] * 10})
    r = chi_cuadrado(df, "H2", [1])
    chk("chi-cuadrado de [[10,20],[20,10]]", r["chi2"], 6.6667)
    chk("V de Cramér", r["V_Cramer"], 0.3333)
    # Mann-Whitney sin empates: a = 1..5, b = 6..10 → U = 0; Z = (0 − 12,5)/√(25·11/12) = −2,611; r = 0,826
    df = pd.DataFrame({C.TIPO: [1] * 5 + [2] * 5, "INF": list(range(1, 11))})
    r = mann_whitney(df, "INF")
    chk("U de Mann-Whitney", r["U"], 0)
    chk("r = |Z|/√N", r["r"], 2.6112 / np.sqrt(10))
    chk("Spearman monótono perfecto", spearman(pd.DataFrame({"a": [1, 2, 3, 4], "b": [1, 4, 9, 16]}), "a", "b")["rho"], 1.0)
    chk("Holm [0,01; 0,04; 0,03] → p mínimo ajustado", holm([0.01, 0.04, 0.03])[0], 0.03)
    print("AUTOPRUEBA INFERENCIAL SUPERADA" if ok else "AUTOPRUEBA INFERENCIAL CON ERRORES")
    return ok


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "prueba":
        sys.exit(0 if autoprueba() else 1)
    for k, t in ejecutar(sys.argv[1], sys.argv[2]).items():
        print(f"\n== {k} ==\n{t.to_string(index=False)}")
