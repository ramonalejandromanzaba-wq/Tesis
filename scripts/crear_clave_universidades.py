"""Crea privado/clave_universidades.xlsx: clave de codificación del censo documental (U01, U02, ...).

La clave NO se versiona (privado/ está en .gitignore) y NO se publica en el documento: en la tesis solo aparecen
resultados agregados. Las URL de evidencia se registran en la copia de trabajo privado/analisis_documental.xlsx.
Ambos archivos quedan disponibles para el tribunal si la solicita (Cap. 3, componente documental).
Fuente de la lista: páginas del CES por sostenimiento (consulta del 16-11-2026), instituciones con PROVINCIA = PICHINCHA.
Los códigos se asignan por permutación aleatoria (semilla fija) para que el orden no revele el sostenimiento.
Uso: python scripts/crear_clave_universidades.py   (no sobrescribe si el archivo ya existe; --forzar para rehacerlo)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "analisis"))
import config as C  # noqa: E402

CES = {1: "https://www.ces.gob.ec/?page_id=328", 3: "https://www.ces.gob.ec/?page_id=1540",
       2: "https://www.ces.gob.ec/?page_id=5398"}
# (institución tal como figura en el formulario, sostenimiento 1/2/3, cantón según el CES)
FILAS = [
    (C.UNIVERSIDADES[0], 1, "Distrito Metropolitano de Quito"), (C.UNIVERSIDADES[1], 1, "Distrito Metropolitano de Quito"),
    (C.UNIVERSIDADES[2], 1, "Distrito Metropolitano de Quito"), (C.UNIVERSIDADES[3], 1, "Distrito Metropolitano de Quito"),
    (C.UNIVERSIDADES[4], 1, "Distrito Metropolitano de Quito"), (C.UNIVERSIDADES[5], 1, "Distrito Metropolitano de Quito"),
    (C.UNIVERSIDADES[6], 1, "Rumiñahui"), (C.UNIVERSIDADES[7], 1, "Distrito Metropolitano de Quito"),
    (C.UNIVERSIDADES[8], 3, "Distrito Metropolitano de Quito"), (C.UNIVERSIDADES[9], 3, "Distrito Metropolitano de Quito"),
    (C.UNIVERSIDADES[10], 3, "Distrito Metropolitano de Quito"), (C.UNIVERSIDADES[11], 3, "Distrito Metropolitano de Quito"),
    (C.UNIVERSIDADES[12], 3, "Distrito Metropolitano de Quito"), (C.UNIVERSIDADES[13], 3, "Distrito Metropolitano de Quito"),
    (C.UNIVERSIDADES[14], 3, "Distrito Metropolitano de Quito"), (C.UNIVERSIDADES[15], 3, "Distrito Metropolitano de Quito"),
    (C.UNIVERSIDADES[16], 2, "Distrito Metropolitano de Quito"), (C.UNIVERSIDADES[17], 2, "Distrito Metropolitano de Quito"),
]

if __name__ == "__main__":
    destino = RAIZ / C.CLAVE_UNIVERSIDADES
    if destino.exists() and "--forzar" not in sys.argv:
        sys.exit(f"{destino} ya existe; no se sobrescribe (use --forzar).")
    destino.parent.mkdir(exist_ok=True)
    perm = np.random.default_rng(20261116).permutation(len(FILAS))
    clave = pd.DataFrame([{
        "Código": f"U{perm[i] + 1:02d}", "Opción en el formulario (A5)": n, "Sostenimiento": C.SOST_NOMBRE[s],
        "Sostenimiento (código)": s, "Tipo de unidad": "Matriz", "Cantón": c, "Fuente": CES[s],
        "Fecha de consulta de la fuente": "16-11-2026", "Sitio web oficial": "", "Observaciones": ""}
        for i, (n, s, c) in enumerate(FILAS)]).sort_values("Código")
    pendiente = pd.DataFrame({"PENDIENTE": [
        "Sedes y extensiones en Pichincha de universidades con matriz en otra provincia: confirmar con el CES o la "
        "SENESCYT (listado vigente) y añadirlas con código U19, U20, … y Tipo de unidad = Sede o Extensión.",
        "El único listado oficial localizado es el reporte del CES de enero de 2017 (desactualizado).",
        "Al añadir instituciones: actualizar config.UNIVERSIDADES (A5), el Anexo B, la ficha documental y el 20 % de reverificación.",
    ]})
    with pd.ExcelWriter(destino) as w:
        clave.to_excel(w, sheet_name="Clave", index=False)
        pendiente.to_excel(w, sheet_name="PENDIENTE", index=False)
    print(f"Escrito {destino}: {len(clave)} instituciones "
          f"({(clave['Sostenimiento (código)'] == 1).sum()} públicas, {(clave['Sostenimiento (código)'] == 3).sum()} "
          f"autofinanciadas, {(clave['Sostenimiento (código)'] == 2).sum()} cofinanciadas)")
