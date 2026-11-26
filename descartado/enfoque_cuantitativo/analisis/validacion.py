"""Validez de contenido (V de Aiken) y confiabilidad (alfa de Cronbach, omega de McDonald, KR-20).

Uso: python analisis/validacion.py datos/jueces/ salida/datos_limpios.csv salida/
datos/jueces/: carpeta con los archivos devueltos por los jueces (E01.xlsx, E02.xlsx, …), cada uno una copia
de jueces/formato_juicio_expertos.xlsx (hojas "Cuestionario", "Ficha documental", "Competencia (K)" y
"Datos del juez"), con calificaciones de 1 a 4. También acepta el formato largo anterior
(un .xlsx con columnas item | criterio | J1 | J2 | …).
"""
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pingouin as pg

import comun  # noqa: F401  (configura la salida en UTF-8)
import config as C
from comun import carpeta, leer_tabla


# ------------------------------------------------------------------ V de Aiken
def aiken_v(calificaciones, l=C.AIKEN_ESCALA[0], c=C.AIKEN_ESCALA[1] - C.AIKEN_ESCALA[0] + 1):
    x = np.asarray([v for v in calificaciones if not pd.isna(v)], dtype=float)
    return float(((x - l).sum()) / (len(x) * (c - 1))) if len(x) else np.nan


def tabla_aiken(df: pd.DataFrame) -> pd.DataFrame:
    jueces = [c for c in df.columns if re.fullmatch(r"J(E)?\d+", str(c).strip(), re.IGNORECASE)]
    filas = []
    for _, r in df.iterrows():
        x = pd.to_numeric(r[jueces], errors="coerce")
        filas.append({"instrumento": r.get("instrumento", "Cuestionario"), "item": r["item"], "criterio": str(r["criterio"]).strip().lower(), "jueces": int(x.notna().sum()),
                      "mediana": float(x.median()), "V": aiken_v(x)})
    t = pd.DataFrame(filas)
    # Decisión por ítem: se conserva si V ≥ AIKEN_MIN en los tres criterios
    piv = t.pivot_table(index=["instrumento", "item"], columns="criterio", values="V", sort=False)
    piv["V_min"] = piv[[c for c in C.CRITERIOS if c in piv]].min(axis=1)
    piv["decision"] = np.where(piv["V_min"] >= C.AIKEN_MIN, "Se conserva", "Corregir o eliminar")
    return t, piv.reset_index()


# ------------------------------------------------------------------ lectura del formato de los jueces
HOJAS_ITEMS = ("Cuestionario", "Ficha documental")
COLS = {"pertinencia": "Pertinencia (1–4)", "claridad": "Claridad (1–4)", "coherencia": "Coherencia (1–4)"}
PESOS_KA = [(0.3, 0.2, 0.1), (0.5, 0.4, 0.2)] + [(0.05, 0.05, 0.05)] * 4


def leer_juez(ruta):
    """Un archivo devuelto por un juez → (código, DataFrame largo item|criterio|valor|instrumento, dict de K)."""
    ruta = Path(ruta)
    datos = pd.read_excel(ruta, sheet_name=None, header=None, dtype=object)
    codigo = str(datos["Datos del juez"].iloc[1, 1]).strip() if "Datos del juez" in datos else ""
    codigo = codigo if codigo and codigo.lower() != "nan" else ruta.stem
    filas = []
    for hoja in HOJAS_ITEMS:
        if hoja not in datos:
            continue
        t = pd.read_excel(ruta, sheet_name=hoja, header=3, dtype=object)
        for _, r in t.iterrows():
            for crit, col in COLS.items():
                v = pd.to_numeric(r.get(col), errors="coerce")
                if not pd.isna(v) and not (C.AIKEN_ESCALA[0] <= v <= C.AIKEN_ESCALA[1]):
                    raise ValueError(f"{ruta.name}, {hoja}, {r['Código']}: {crit} = {v} fuera de 1–4")
                filas.append({"instrumento": hoja, "item": r["Código"], "criterio": crit, "valor": v})
    k = {"juez": codigo}
    if "Competencia (K)" in datos:
        h = datos["Competencia (K)"]
        kc = pd.to_numeric(h.iloc[2, 1], errors="coerce")
        grados = [str(h.iloc[5 + i, 1]).strip() for i in range(6)]
        idx = {"Alto": 0, "Medio": 1, "Bajo": 2}
        ka = sum(PESOS_KA[i][idx[g]] for i, g in enumerate(grados)) if all(g in idx for g in grados) else np.nan
        k.update({"Kc": kc / 10 if not pd.isna(kc) else np.nan, "Ka": ka})
        k["K"] = 0.5 * (k["Kc"] + k["Ka"]) if not (pd.isna(k["Kc"]) or pd.isna(ka)) else np.nan
        k["competencia"] = ("---" if pd.isna(k["K"]) else "Alta" if k["K"] > 0.8 else "Media" if k["K"] >= 0.5 else "Baja")
    return codigo, pd.DataFrame(filas), k


def leer_jueces(origen):
    """Carpeta de archivos de jueces (o .xlsx en formato largo) → (tabla ancha item|criterio|J…, tabla de K)."""
    origen = Path(origen)
    if origen.is_file():
        return leer_tabla(origen), pd.DataFrame()
    archivos = sorted(p for p in origen.glob("*.xlsx") if not p.name.startswith("~$"))
    if not archivos:
        raise FileNotFoundError(f"No hay archivos de jueces en {origen}")
    largas, ks = [], []
    for a in archivos:
        cod, larga, k = leer_juez(a)
        larga["juez"] = cod
        largas.append(larga)
        ks.append(k)
    larga = pd.concat(largas)
    ancha = larga.pivot_table(index=["instrumento", "item", "criterio"], columns="juez", values="valor",
                              aggfunc="first", sort=False).reset_index()
    ancha.columns = [f"J{c}" if str(c).startswith("E") else c for c in ancha.columns]
    return ancha, pd.DataFrame(ks)


# ------------------------------------------------------------------ confiabilidad
def omega_total(datos: pd.DataFrame, iter_max=200, tol=1e-6) -> float:
    """Omega total de McDonald con un modelo de un factor estimado por factorización de ejes principales
    sobre la matriz de correlaciones: ω = (Σλ)² / ((Σλ)² + Σψ), con ψ = 1 − λ²."""
    R = datos.corr().to_numpy()
    h2 = 1 - 1 / np.diag(np.linalg.inv(R))  # comunalidades iniciales (correlación múltiple al cuadrado)
    for _ in range(iter_max):
        Rr = R.copy()
        np.fill_diagonal(Rr, h2)
        val, vec = np.linalg.eigh(Rr)
        lam = vec[:, -1] * np.sqrt(max(val[-1], 0))
        nuevo = np.clip(lam ** 2, 0, 0.999)
        if np.max(np.abs(nuevo - h2)) < tol:
            break
        h2 = nuevo
    lam = np.abs(lam)
    return float(lam.sum() ** 2 / (lam.sum() ** 2 + (1 - lam ** 2).sum()))


def kr20(binarios: pd.DataFrame) -> float:
    """KR-20 de Kuder y Richardson para ítems dicotómicos (0/1): k/(k−1)·(1 − Σpq/σ²_T)."""
    x = binarios.dropna().to_numpy(dtype=float)
    k = x.shape[1]
    p = x.mean(axis=0)
    var_total = x.sum(axis=1).var(ddof=0)
    return float(k / (k - 1) * (1 - (p * (1 - p)).sum() / var_total))


def confiabilidad(limpios: pd.DataFrame) -> pd.DataFrame:
    filas = []
    for d, info in C.DIMENSIONES.items():
        cols = [i for i in info["items"] if i in limpios]
        x = limpios[cols].dropna()
        if len(x) < 3:
            continue
        a, ic = pg.cronbach_alpha(data=x)
        alfa_sin = {i: pg.cronbach_alpha(data=x.drop(columns=i))[0] for i in cols}
        r_it = {i: x[i].corr(x.drop(columns=i).sum(axis=1)) for i in cols}
        filas.append({"escala": info["nombre"], "codigo": d, "tipo": "Likert", "items": len(cols), "n": len(x),
                      "alfa": a, "alfa_ic95_inf": ic[0], "alfa_ic95_sup": ic[1], "omega": omega_total(x), "kr20": np.nan,
                      "r_item_total_min": min(r_it.values()), "item_r_min": min(r_it, key=r_it.get),
                      "alfa_si_se_elimina_max": max(alfa_sin.values()), "item_alfa_max": max(alfa_sin, key=alfa_sin.get)})
    b = limpios[C.KR20_INFO].dropna()
    if len(b) >= 3:
        b = (b == 1).astype(int)  # Sí = 1; No o No recuerdo = 0
        filas.append({"escala": "Información recibida (hechos, sí/no)", "codigo": "INFO_H", "tipo": "Dicotómica",
                      "items": len(C.KR20_INFO), "n": len(b), "alfa": np.nan, "omega": np.nan, "kr20": kr20(b)})
    return pd.DataFrame(filas)


def autoprueba():
    """Valores de referencia calculados a mano o con fórmulas cerradas."""
    ok = True
    def chk(nombre, obtenido, esperado, tol=1e-3):
        nonlocal ok
        bien = abs(obtenido - esperado) <= tol
        ok &= bien
        print(f"{'OK ' if bien else 'ERR'} {nombre}: obtenido {obtenido:.4f}, esperado {esperado:.4f}")
    chk("V de Aiken, escala 1–4, [4,4,4,4,4]", aiken_v([4, 4, 4, 4, 4]), 1.0)
    # S = 3+3+3+2+2 = 13; V = 13 / (5·3) = 0,8667
    chk("V de Aiken, escala 1–4, [4,4,4,3,3]", aiken_v([4, 4, 4, 3, 3]), 13 / 15)
    chk("V de Aiken, escala 1–4, 3 jueces [4,4,3] (umbral S ≥ 8 de 9)", aiken_v([4, 4, 3]), 8 / 9)
    chk("V de Aiken, escala 1–5 (instrumento V2), [4,4,5,5,3]", aiken_v([4, 4, 5, 5, 3], l=1, c=5), 0.8)
    m = pd.DataFrame([[1, 2, 1], [2, 3, 2], [3, 3, 3], [4, 5, 3], [5, 5, 5]], columns=list("abc"))
    chk("alfa de matriz de referencia (pingouin)", pg.cronbach_alpha(data=m)[0], 0.9672)
    # Con cargas iguales (tau-equivalencia), omega coincide con alfa estandarizado; matriz de correlaciones r = 0,5
    rng = np.random.default_rng(1)
    f = rng.normal(size=20000)
    sim = pd.DataFrame({f"i{j}": f + rng.normal(size=20000) for j in range(4)})  # r teórica = 0,5
    alfa_std = 4 * 0.5 / (1 + 3 * 0.5)
    chk("omega con cargas iguales ≈ alfa estandarizado (0,800)", omega_total(sim), alfa_std, 0.01)
    bin_ = pd.DataFrame([[1, 1, 1], [1, 1, 0], [1, 0, 0], [0, 0, 0]], columns=list("abc"))
    # p = (0,75; 0,5; 0,25) → Σpq = 0,625; totales (3,2,1,0) → σ² = 1,25; KR-20 = 1,5·(1 − 0,5) = 0,75
    chk("KR-20 de matriz de referencia", kr20(bin_), 0.75)
    print("AUTOPRUEBA DE VALIDACIÓN SUPERADA" if ok else "AUTOPRUEBA DE VALIDACIÓN CON ERRORES")
    return ok


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "prueba":
        sys.exit(0 if autoprueba() else 1)
    expertos, limpios, salida = sys.argv[1], sys.argv[2], sys.argv[3]
    ancha, ks = leer_jueces(expertos)
    larga, decision = tabla_aiken(ancha)
    out = carpeta(salida)
    if not ks.empty:
        ks.to_csv(out / "jueces_competencia.csv", index=False)
    larga.to_csv(out / "aiken_por_criterio.csv", index=False)
    decision.to_csv(out / "aiken_decision.csv", index=False)
    confiabilidad(pd.read_csv(limpios)).to_csv(out / "confiabilidad.csv", index=False)
    print(decision.to_string(index=False))
