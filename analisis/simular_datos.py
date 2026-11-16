"""Genera datos SIMULADOS solo para probar los scripts (cuestionario v2.1).

Archivos (todos en analisis/datos/, con "simulado" en el nombre):
- ejemplo_simulado.xlsx: respuestas que imitan la exportación de Google Forms (títulos "[CÓDIGO] …" y etiquetas de
  texto), con columnas identificativas y casos que no superan los filtros o son de posgrado, para comprobar que la
  limpieza los elimina. La muestra se concentra a propósito en pocas universidades, para probar la brecha ponderada.
- jueces_simulado/E01.xlsx … E04.xlsx: copias llenas de jueces/formato_juicio_expertos.xlsx (escala 1–4).
- documental_simulado.xlsx y documental_observador2_simulado.xlsx: registros documentales con códigos U01…U18.
NUNCA deben usarse como resultados ni citarse en el documento. Semilla fija: 2026.
"""
import shutil
from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl import load_workbook

import config as C

BASE = Path(__file__).resolve().parent / "datos"
RAIZ = Path(__file__).resolve().parents[1]
LEEME = pd.DataFrame({"AVISO": [
    "DATOS SIMULADOS — generados por analisis/simular_datos.py con semilla 2026.",
    "Sirven solo para probar los scripts. No son respuestas reales ni pueden usarse en la tesis.",
]})
# Sostenimiento simulado por opción de A5 (mismo orden que config.UNIVERSIDADES: 8 públicas, 8 autofinanciadas, 2 cofinanciadas)
SOST_SIM = [1] * 8 + [3] * 8 + [2] * 2
CLAVE_SIM = {i + 1: (f"U{i + 1:02d}", s) for i, s in enumerate(SOST_SIM)}


def respuestas(n=440, seed=2026):
    rng = np.random.default_rng(seed)
    inv = lambda mapa: {v: k for k, v in mapa.items()}
    # concentración: la mitad de la muestra en 3 universidades (sesgo de la red de contactos)
    peso = np.ones(len(C.UNIVERSIDADES))
    peso[[1, 6, 16]] = 12
    peso = peso / peso.sum()
    filas = []
    for i in range(n):
        u = int(rng.choice(len(C.UNIVERSIDADES), p=peso)) + 1
        sost = SOST_SIM[u - 1]
        privada = sost in (2, 3)
        latente = rng.normal(0.35 if privada else 0.0, 1.0)  # rasgo común: induce correlación entre dimensiones
        f = {"Marca temporal": f"2026-12-{7 + i % 20:02d} 10:{i % 60:02d}:00", "Dirección de correo electrónico": "",
             "[P00] ¿Acepta participar?": "Sí, acepto" if i % 70 else "No acepto",
             "[P01] ¿Tiene 18 años o más?": "Sí" if i % 53 else "No",
             "[P02] ¿Estudia en Pichincha?": "Sí" if i % 61 else "No"}
        a1 = sost if rng.random() > 0.08 else 9  # 8 % no sabe el tipo
        f["[A1] Su universidad es"] = inv(C.DEMOGRAFICOS["A1"])[a1]
        f["[A2]"] = rng.choice(list(C.DEMOGRAFICOS["A2"]), p=[0.05] * 5 + [0.30] + [0.15] + [0.05] * 2 + [0.20])
        f["[A3]"] = (inv(C.DEMOGRAFICOS["A3"])[C.A3_POSGRADO] if i % 47 == 0
                     else rng.choice([k for k, v in C.DEMOGRAFICOS["A3"].items() if v != C.A3_POSGRADO]))
        f["[A4]"] = rng.choice(list(C.DEMOGRAFICOS["A4"]))
        r = rng.random()
        f["[A5] ¿En qué universidad estudia?"] = (C.UNIVERSIDADES[u - 1] if r > 0.10 else
                                                  (C.UNIV_OTRA if r > 0.04 else C.UNIV_NO_RESPONDE))
        f["[A6]"] = rng.choice(list(C.DEMOGRAFICOS["A6"]), p=[0.8, 0.15, 0.05])
        f["[A7]"] = rng.choice(list(C.DEMOGRAFICOS["A7"]) + [""])
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


def jueces(n=4, seed=2027):
    """Copias llenas del formato de jueces (escala 1–4)."""
    rng = np.random.default_rng(seed)
    formato = RAIZ / "jueces" / "formato_juicio_expertos.xlsx"
    destino = BASE / "jueces_simulado"
    if destino.exists():
        shutil.rmtree(destino)
    destino.mkdir(parents=True)
    for j in range(1, n + 1):
        wb = load_workbook(formato)
        wb["Datos del juez"]["B2"] = f"E{j:02d}"
        wb["Datos del juez"]["B3"] = ["Protección de datos personales (jurídico)", "Seguridad de la información",
                                      "Metodología de la investigación", "Seguridad de la información"][(j - 1) % 4]
        for hoja in ("Cuestionario", "Ficha documental"):
            ws = wb[hoja]
            for r in range(5, ws.max_row + 1):
                if ws.cell(r, 1).value is None:
                    continue
                base = 4 if rng.random() < 0.85 else 2
                for c in (5, 6, 7):
                    ws.cell(r, c).value = int(np.clip(base - rng.integers(0, 2), 1, 4))
        k = wb["Competencia (K)"]
        k["B3"] = int(rng.integers(6, 10))
        for r in range(6, 12):
            k.cell(r, 2).value = rng.choice(["Alto", "Medio", "Bajo"], p=[0.5, 0.4, 0.1])
        wb.save(destino / f"E{j:02d}.xlsx")
    return destino


def documental(seed=2028):
    """Registro documental simulado (18 universidades) y archivo del segundo observador (4 universidades)."""
    rng = np.random.default_rng(seed)
    plantilla = RAIZ / "analisis_documental" / "analisis_documental.xlsx"
    cal = ["S", "P", "N"]
    wb = load_workbook(plantilla)
    ws = wb["Registro"]
    hdr = {ws.cell(4, c).value: c for c in range(1, ws.max_column + 1)}
    nombres = {1: "Pública", 2: "Particular cofinanciada", 3: "Particular autofinanciada"}
    calif = {}
    for i, s in enumerate(SOST_SIM):
        r = 5 + i
        ws.cell(r, 2).value = f"U{i + 1:02d}"
        ws.cell(r, 3).value = nombres[s]
        ws.cell(r, 4).value = "Matriz"
        for k in range(1, 17):
            v = cal[int(rng.choice(3, p=[0.45, 0.25, 0.30] if s != 1 else [0.30, 0.25, 0.45]))]
            ws.cell(r, hdr[f"ID{k:02d} calif."]).value = v
            calif[(i, k)] = v
    rv = wb["Reverificación"]
    hv = {rv.cell(4, c).value: c for c in range(1, rv.max_column + 1)}
    muestra = [0, 5, 10, 15]
    for j, i in enumerate(muestra):
        rv.cell(5 + j, 1).value = i + 1
        for k in range(1, 15):
            v = calif[(i, k)] if rng.random() > 0.1 else cal[int(rng.integers(3))]
            rv.cell(5 + j, hv[f"ID{k:02d} 2.ª"]).value = v
    wb.save(BASE / "documental_simulado.xlsx")
    wb2 = load_workbook(plantilla)
    ws2 = wb2["Registro"]
    for j, i in enumerate(muestra):
        r = 5 + j
        ws2.cell(r, 2).value = f"U{i + 1:02d}"
        ws2.cell(r, 3).value = nombres[SOST_SIM[i]]
        for k in range(1, 17):
            v = calif[(i, k)] if rng.random() > 0.15 else cal[int(rng.integers(3))]
            ws2.cell(r, hdr[f"ID{k:02d} calif."]).value = v
    wb2.save(BASE / "documental_observador2_simulado.xlsx")
    return BASE / "documental_simulado.xlsx", BASE / "documental_observador2_simulado.xlsx"


def escribir_todo():
    BASE.mkdir(exist_ok=True)
    with pd.ExcelWriter(BASE / "ejemplo_simulado.xlsx") as w:
        LEEME.to_excel(w, sheet_name="LEEME", index=False)
        respuestas().to_excel(w, sheet_name="Respuestas SIMULADAS", index=False)
    return BASE / "ejemplo_simulado.xlsx", jueces(), *documental()


if __name__ == "__main__":
    print("Escritos (SIMULADOS):", *escribir_todo(), sep="\n  ")
