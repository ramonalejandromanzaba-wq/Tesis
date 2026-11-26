"""Crea privado/clave_universidades.xlsx: clave de codificación del censo documental (U01, U02, ...).

La clave NO se versiona (privado/ está en .gitignore) y NO se publica en el documento: en la tesis solo aparecen
resultados agregados. Las URL de evidencia se registran en la copia de trabajo privado/analisis_documental.xlsx.
Ambos archivos quedan disponibles para el tribunal si la solicita (Cap. 3, componente documental).
Fuente de la lista: páginas del CES por sostenimiento (consulta del 16-11-2026): las 64 universidades y escuelas
politécnicas del país (censo nacional, OM-01); unidad de observación: el sitio web oficial de la matriz.
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
# (institución tal como figura en el formulario, sostenimiento 1/2/3, provincia de la matriz según el CES)
FILAS = [(n, s, prov) for n, (s, prov) in C.UNIV_DATOS.items()]
REGION = {p: r for r, ps in C.REGION_PROVINCIA.items() for p in ps}


if __name__ == "__main__":
    destino = RAIZ / C.CLAVE_UNIVERSIDADES
    if destino.exists() and "--forzar" not in sys.argv:
        sys.exit(f"{destino} ya existe; no se sobrescribe (use --forzar).")
    destino.parent.mkdir(exist_ok=True)
    perm = np.random.default_rng(20261125).permutation(len(FILAS))
    clave = pd.DataFrame([{
        "Código": f"U{perm[i] + 1:02d}", "Opción en el formulario (A5)": n, "Sostenimiento": C.SOST_NOMBRE[s],
        "Sostenimiento (código)": s, "Tipo de unidad": "Matriz", "Provincia": c, "Región": REGION[c], "Fuente": CES[s],
        "Fecha de consulta de la fuente": "16-11-2026", "Sitio web oficial": "", "Observaciones": ""}
        for i, (n, s, c) in enumerate(FILAS)]).sort_values("Código")
    with pd.ExcelWriter(destino) as w:
        clave.to_excel(w, sheet_name="Clave", index=False)
    print(f"Escrito {destino}: {len(clave)} instituciones "
          f"({(clave['Sostenimiento (código)'] == 1).sum()} públicas, {(clave['Sostenimiento (código)'] == 3).sum()} "
          f"autofinanciadas, {(clave['Sostenimiento (código)'] == 2).sum()} cofinanciadas)")
