"""Genera datos SIMULADOS solo para probar los scripts (datos/ejemplo_simulado.xlsx y datos/expertos_simulado.xlsx).

Los archivos imitan la exportación de Google Forms (títulos "[CÓDIGO] …" y respuestas como etiquetas de texto)
e incluyen columnas identificativas y casos que no superan los filtros, para comprobar que la limpieza los elimina.
NUNCA deben usarse como resultados ni citarse en el documento. Semilla fija: 2026.
"""
from pathlib import Path

import numpy as np
import pandas as pd

import config as C

BASE = Path(__file__).resolve().parent / "datos"
LEEME = pd.DataFrame({"AVISO": [
    "DATOS SIMULADOS — generados por analisis/simular_datos.py con semilla 2026.",
    "Sirven solo para probar los scripts. No son respuestas reales ni pueden usarse en la tesis.",
]})


def respuestas(n=420, seed=2026):
    rng = np.random.default_rng(seed)
    inv = lambda mapa: {v: k for k, v in mapa.items()}
    filas = []
    for i in range(n):
        tipo = rng.choice([1, 2, 3, 9], p=[0.60, 0.10, 0.25, 0.05])
        privada = tipo in (2, 3)
        latente = rng.normal(0.35 if privada else 0.0, 1.0)  # rasgo común: induce correlación entre dimensiones
        f = {"Marca temporal": f"2026-12-{7 + i % 20:02d} 10:{i % 60:02d}:00", "Dirección de correo electrónico": "",
             "[P00] ¿Acepta participar?": "Sí, acepto" if i % 70 else "No acepto",
             "[P01] ¿Tiene 18 años o más?": "Sí" if i % 53 else "No",
             "[P02] ¿Está matriculado actualmente?": "Sí"}
        f["[A1] Tipo de universidad"] = inv(C.DEMOGRAFICOS["A1"])[tipo]
        for k in ("A2", "A3", "A4"):
            f[f"[{k}]"] = rng.choice(list(C.DEMOGRAFICOS[k]))
        elegidas = [e for c, e in C.H1_OPCIONES.items() if c != "H1_99" and rng.random() < (0.9 if c in ("H1_01", "H1_02") else 0.3)]
        f["[H1] ¿Qué datos le pidió su universidad?"] = ", ".join(elegidas) if elegidas else C.H1_OPCIONES["H1_99"]
        prob_si = 1 / (1 + np.exp(-(latente - 0.2)))
        for k, mapa in C.HECHOS.items():
            cods = list(mapa.values())
            if set(cods) >= {1, 2, 3} and k != "H11":
                v = 1 if rng.random() < prob_si else rng.choice([2, 3], p=[0.6, 0.4])
                if 8 in cods and rng.random() < 0.2:
                    v = 8
            else:
                v = rng.choice(cods)
            f[f"[{k}]"] = inv(mapa)[v]
        for d, info in C.DIMENSIONES.items():
            for it in info["items"]:
                z = latente + rng.normal(0, 0.9)
                x = int(np.clip(np.round(3 + 1.1 * z), 1, 5))
                if it in C.INVERSOS:
                    x = 6 - x
                f[f"[{it}]"] = x if rng.random() < 0.5 else inv(C.LIKERT_ETIQUETAS)[x]  # números o etiquetas, como en Forms
        filas.append(f)
    return pd.DataFrame(filas)


def expertos(seed=2026):
    rng = np.random.default_rng(seed + 1)
    items = ["H1", "H2", "H4", "H5", "H6", "H7"] + C.ITEMS_LIKERT
    filas = []
    for it in items:
        for cr in C.CRITERIOS:
            base = 5 if rng.random() < 0.8 else 3
            filas.append({"item": it, "criterio": cr, **{f"J{j}": int(np.clip(base - rng.integers(0, 2), 1, 5)) for j in range(1, 6)}})
    return pd.DataFrame(filas)


if __name__ == "__main__":
    BASE.mkdir(exist_ok=True)
    with pd.ExcelWriter(BASE / "ejemplo_simulado.xlsx") as w:
        LEEME.to_excel(w, sheet_name="LEEME", index=False)
        respuestas().to_excel(w, sheet_name="Respuestas SIMULADAS", index=False)
    with pd.ExcelWriter(BASE / "expertos_simulado.xlsx") as w:
        LEEME.to_excel(w, sheet_name="LEEME", index=False)
        expertos().to_excel(w, sheet_name="Expertos SIMULADOS", index=False)
    print("Escritos: datos/ejemplo_simulado.xlsx y datos/expertos_simulado.xlsx (SIMULADOS)")
