"""Validez de constructo: análisis factorial exploratorio (AFE) de las escalas Likert (R1.4).

Uso: python analisis/validez_constructo.py salida/datos_limpios.csv salida/
Con la muestra final (ítems inversos ya recodificados):
1. Adecuación: KMO global y por ítem (Kaiser, 1974; aceptable ≥ 0,60) y esfericidad de Bartlett (1950; p < 0,05).
2. Unidimensionalidad de cada escala (INF, CON, DER, CNF): número de factores sugerido por el análisis paralelo
   de Horn (1965; 500 réplicas, percentil 95) y por la regla de autovalores > 1; AFE de un factor con
   extracción por ejes principales (la misma que usa el omega de McDonald en validacion.py) y sin rotación.
   Criterio de retención: carga ≥ 0,40; se informa la varianza explicada.
3. Estructura conjunta: AFE de los 25 ítems con 4 factores, extracción por ejes principales y rotación oblimin
   (oblicua, porque se espera que las dimensiones se correlacionen), para comprobar que cada ítem carga en su
   dimensión.
Se usa la matriz de correlaciones de Pearson; con cinco categorías de respuesta y n ≥ 300 la diferencia con la
policórica es pequeña, y la limitación se declara.
"""
import sys

import numpy as np
import pandas as pd
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo
from factor_analyzer.rotator import Rotator

import comun  # noqa: F401  (configura la salida en UTF-8)
import config as C
from comun import carpeta

CARGA_MIN = 0.40


def ejes_principales(R, k, iter_max=500, tol=1e-6):
    """Extracción por ejes principales iterada sobre la matriz de correlaciones R (k factores).
    Se implementa aquí (igual que en validacion.omega_total) porque FactorAnalyzer.fit es incompatible con
    scikit-learn >= 1.8. Devuelve las cargas (p × k) y la proporción de varianza explicada por factor."""
    h2 = np.clip(1 - 1 / np.diag(np.linalg.inv(R)), 0.005, 0.995)
    for _ in range(iter_max):
        Rr = R.copy()
        np.fill_diagonal(Rr, h2)
        val, vec = np.linalg.eigh(Rr)
        orden = np.argsort(val)[::-1][:k]
        L = vec[:, orden] * np.sqrt(np.clip(val[orden], 0, None))
        nuevo = np.clip((L ** 2).sum(axis=1), 0.005, 0.995)
        if np.max(np.abs(nuevo - h2)) < tol:
            break
        h2 = nuevo
    L = L * np.where(L.sum(axis=0) < 0, -1, 1)
    return L, (L ** 2).sum(axis=0) / R.shape[0]


def analisis_paralelo(x: pd.DataFrame, reps=500, seed=2026):
    rng = np.random.default_rng(seed)
    obs = np.sort(np.linalg.eigvalsh(np.corrcoef(x.to_numpy(), rowvar=False)))[::-1]
    sim = np.empty((reps, x.shape[1]))
    for r in range(reps):
        z = rng.standard_normal(x.shape)
        sim[r] = np.sort(np.linalg.eigvalsh(np.corrcoef(z, rowvar=False)))[::-1]
    p95 = np.percentile(sim, 95, axis=0)
    n = 0
    for o, s in zip(obs, p95):
        if o > s:
            n += 1
        else:
            break
    return n, obs


def por_escala(df):
    resumen, cargas = [], []
    for d, info in C.DIMENSIONES.items():
        cols = [i for i in info["items"] if i in df]
        x = df[cols].dropna()
        if len(x) < 3 * len(cols) or len(cols) < 3:
            continue
        kmo_items, kmo = calculate_kmo(x)
        chi2, p = calculate_bartlett_sphericity(x)
        n_par, autoval = analisis_paralelo(x)
        L1, prop = ejes_principales(np.corrcoef(x.to_numpy(), rowvar=False), 1)
        lam, var = L1[:, 0], prop[0]
        resumen.append({"dimension": d, "nombre": info["nombre"], "n": len(x), "items": len(cols), "KMO": kmo,
                        "bartlett_chi2": chi2, "bartlett_p": p, "factores_analisis_paralelo": n_par,
                        "autovalores_mayores_1": int((autoval > 1).sum()), "varianza_explicada_1f": var,
                        "items_carga_menor_0_40": int((np.abs(lam) < CARGA_MIN).sum()),
                        "unidimensional": n_par <= 1 and (np.abs(lam) >= CARGA_MIN).all()})
        for it, l, k in zip(cols, lam, kmo_items):
            cargas.append({"dimension": d, "item": it, "carga": l, "comunalidad": l ** 2, "KMO_item": k,
                           "se_retiene": abs(l) >= CARGA_MIN})
    return pd.DataFrame(resumen), pd.DataFrame(cargas)


def conjunto(df):
    cols = [i for i in C.ITEMS_LIKERT if i in df]
    x = df[cols].dropna()
    if len(x) < 2 * len(cols):
        return pd.DataFrame(), {}
    _, kmo = calculate_kmo(x)
    chi2, p = calculate_bartlett_sphericity(x)
    k = len(C.DIMENSIONES)
    L0, prop = ejes_principales(np.corrcoef(x.to_numpy(), rowvar=False), k)
    Lr = Rotator(method="oblimin").fit_transform(L0)
    L = pd.DataFrame(Lr, index=cols, columns=[f"F{i + 1}" for i in range(k)])
    L["dimension_teorica"] = [next(d for d, info in C.DIMENSIONES.items() if i in info["items"]) for i in cols]
    L["factor_carga_max"] = L[[c for c in L.columns if c.startswith("F")]].abs().idxmax(axis=1)
    L["carga_max"] = L[[c for c in L.columns if c.startswith("F")]].abs().max(axis=1)
    return L.reset_index(names="item"), {"n": len(x), "KMO": kmo, "bartlett_chi2": chi2, "bartlett_p": p,
                                         "varianza_acumulada_sin_rotar": float(prop.sum())}


def ejecutar(limpios, salida):
    df = pd.read_csv(limpios)
    out = carpeta(salida)
    res, cargas = por_escala(df)
    L, glob = conjunto(df)
    res.to_csv(out / "afe_por_escala.csv", index=False)
    cargas.to_csv(out / "afe_cargas.csv", index=False)
    L.to_csv(out / "afe_conjunto_oblimin.csv", index=False)
    pd.DataFrame([glob]).to_csv(out / "afe_conjunto_resumen.csv", index=False)
    return res, cargas, L, glob


if __name__ == "__main__":
    res, cargas, L, glob = ejecutar(sys.argv[1], sys.argv[2])
    print(res.round(3).to_string(index=False))
    print(cargas.round(3).to_string(index=False))
    print(glob)
