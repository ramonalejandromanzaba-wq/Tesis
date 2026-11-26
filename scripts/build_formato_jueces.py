"""Genera jueces/formato_juicio_expertos.xlsx: formato de juicio de expertos del cuestionario v2.2 y de la ficha documental.

- Hoja "Cuestionario": los 55 ítems del cuestionario (texto tomado de analisis/config.py, igual que el Anexo B),
  con pertinencia, claridad y coherencia en escala 1–4 (validación de datos) y observaciones.
- Hoja "Ficha documental": los 16 indicadores ID01–ID16 con los mismos criterios.
- Hoja "Competencia (K)": autoevaluación para el coeficiente K = ½(Kc + Ka) (Cabero Almenara y Barroso Osuna, 2013),
  con fórmulas reales.
Un archivo por juez: el juez lo devuelve como E0n.xlsx; analisis/validacion.py lee la carpeta de respuestas.
Uso: python scripts/build_formato_jueces.py [ruta_salida.xlsx]
"""
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "analisis"))
import config as C  # noqa: E402

SALIDA = Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ / "jueces" / "formato_juicio_expertos.xlsx"
AZUL = PatternFill("solid", fgColor="1F3864")
AMARILLO = PatternFill("solid", fgColor="FFF2CC")
GRIS = PatternFill("solid", fgColor="EDEDED")
BLOQUE_FILL = PatternFill("solid", fgColor="D9E1F2")
FINO = Side(style="thin", color="BFBFBF")
BORDE = Border(left=FINO, right=FINO, top=FINO, bottom=FINO)
ENVOLVER = Alignment(wrap_text=True, vertical="top")

OPCIONES = {
    "P00": "Sí, acepto / No acepto (fin)", "P01": "Sí / No (fin)", "P02": "Sí / No (fin)",
    "A1": "Pública / Particular cofinanciada / Particular autofinanciada / No lo sé",
    "A2": "Diez campos amplios de conocimiento (CINE)", "A3": "Nivelación / 1.º–3.º / 4.º–6.º / 7.º o superior / Posgrado",
    "A4": "18–20 / 21–24 / 25–29 / 30 o más",
    "A5": f"Lista de las {len(C.UNIVERSIDADES)} universidades y escuelas politécnicas del CES / Prefiero no responder",
    "A6": "Presencial / Semipresencial o híbrida / En línea",
    "A7": "Redes o mensajería / Correo / Código QR en el campus / Docente / Compañero o amigo / Otro",
    "A8": "Costa / Sierra / Amazonía / Galápagos (opcional)",
    "H1": "Casillas: identificación; contacto; fotografía; socioeconómicos; familiares; salud; discapacidad; etnia; condición migratoria; identidad de género o nombre social; biométricos; ubicación; actividad en plataformas; no recuerdo",
    "H3": "Expresa / Implícita / Verbal / No recuerdo",
    "H9": "Sí / No / No recuerdo / No me pidieron esos datos",
    "H10": "Sí / No / No recuerdo / No uso esas plataformas",
    "H11": "Sí, con respuesta en plazo / Sí, sin respuesta o con demora / No",
    "H16": "Sí / No / No estoy seguro(a)",
}
BLOQUES = [("Acceso (filtros)", ["P00", "P01", "P02"]),
           ("A. Datos generales no identificativos", [f"A{i}" for i in range(1, 9)]),
           ("H. Preguntas de hechos", ["H1", "H2", "H3", "H4", "H5a", "H5b"] + [f"H{i}" for i in range(6, 17)])]
BLOQUES += [(f"L. Likert — {d}: {info['nombre']}", info["items"]) for d, info in C.DIMENSIONES.items()]
FICHA = [
    ("ID01", "Existe una política o aviso de privacidad publicado y accesible desde el sitio principal"),
    ("ID02", "Identifica al responsable del tratamiento con dirección, teléfono y correo electrónico"),
    ("ID03", "Declara los fines del tratamiento de los datos de los estudiantes"),
    ("ID04", "Declara la base de legitimación correcta para cada finalidad (parcial si usa el consentimiento para todo)"),
    ("ID05", "Declara el tiempo de conservación de los datos"),
    ("ID06a", "Informa las comunicaciones a terceros nacionales (destinatarios, finalidad y base)"),
    ("ID06b", "Informa las transferencias internacionales (país de destino, garantía y base)"),
    ("ID07", "Enumera los derechos del titular (acceso, rectificación y actualización, eliminación, oposición, portabilidad, suspensión y no ser objeto de decisiones automatizadas) y la forma de ejercerlos"),
    ("ID08", "Ofrece un canal específico y operativo para ejercer derechos (correo, formulario o ventanilla)"),
    ("ID09", "Indica dónde y cómo reclamar ante el responsable y ante la Autoridad de Protección de Datos Personales"),
    ("ID10", "Informa la posibilidad de revocar el consentimiento"),
    ("ID11", "Publica la designación del delegado de protección de datos con sus datos de contacto"),
    ("ID12", "Hace referencia expresa a la LOPDP y a su Reglamento como marco del tratamiento"),
    ("ID13", "Declara las categorías especiales y los datos sensibles que trata (salud, discapacidad, biométricos, etnia, condición migratoria, identidad de género) y su base, y por separado los datos socioeconómicos"),
    ("ID14", "Los formularios en línea de admisión, inscripción o contacto incluyen una cláusula informativa previa y un consentimiento separado para las finalidades no necesarias"),
    ("ID15", "Informa sobre el uso de cookies u otras tecnologías de seguimiento y permite aceptarlas o rechazarlas (complementario)"),
    ("ID16", "Indica la fecha de vigencia o de última actualización de la política (complementario)"),
    ("ID17", "Identifica la plataforma educativa (aula virtual) y quién la aloja (complementario)"),
    ("ID18", "Muestra un aviso de privacidad en la pantalla de acceso del aula virtual, sin iniciar sesión (complementario)"),
    ("ID19", "Declara el uso de supervisión de exámenes en línea y si usa biometría (complementario)"),
    ("ID20", "Describe los tipos de tratamiento, la base de datos, el origen de los datos no obtenidos del titular y las finalidades ulteriores (complementario)"),
    ("ID21", "Informa las consecuencias de entregar o negarse a entregar los datos y el efecto de datos erróneos (complementario)"),
    ("ID22", "Informa la existencia de valoraciones o decisiones automatizadas, incluida la elaboración de perfiles (complementario)"),
]
CABECERA = ["Código", "Bloque", "Texto del ítem", "Opciones de respuesta", "Pertinencia (1–4)", "Claridad (1–4)",
            "Coherencia (1–4)", "Observaciones y redacción sugerida"]


def cabecera(ws, fila, valores):
    for j, v in enumerate(valores, 1):
        c = ws.cell(fila, j, v)
        c.fill, c.border = AZUL, BORDE
        c.font = Font(bold=True, color="FFFFFF")
        c.alignment = Alignment(wrap_text=True, horizontal="center", vertical="center")


def hoja_items(ws, titulo, filas):
    ws["A1"] = titulo
    ws["A1"].font = Font(bold=True, size=13, color="1F3864")
    ws["A2"] = ("Escala: 1 = no cumple el criterio; 2 = bajo nivel (requiere cambios importantes); "
                "3 = nivel moderado (requiere ajustes menores); 4 = cumple plenamente. Escriba solo 1, 2, 3 o 4.")
    ws["A2"].font = Font(italic=True, size=9)
    cabecera(ws, 4, CABECERA)
    dv = DataValidation(type="whole", operator="between", formula1="1", formula2="4", allow_blank=True,
                        showErrorMessage=True, errorTitle="Valor no válido", error="Escriba un número entero de 1 a 4.")
    ws.add_data_validation(dv)
    r = 5
    for bloque, codigo, texto, opciones in filas:
        valores = [codigo, bloque, texto, opciones]
        for j, v in enumerate(valores, 1):
            c = ws.cell(r, j, v)
            c.border, c.alignment, c.fill = BORDE, ENVOLVER, GRIS
        for j in range(5, 9):
            c = ws.cell(r, j)
            c.border, c.alignment, c.fill = BORDE, ENVOLVER, AMARILLO
        dv.add(f"E{r}:G{r}")
        r += 1
    for col, w in zip("ABCDEFGH", (8, 22, 60, 34, 12, 12, 12, 45)):
        ws.column_dimensions[col].width = w
    ws.freeze_panes = "E5"
    return r - 1


def main():
    wb = Workbook()
    ins = wb.active
    ins.title = "Instrucciones"
    textos = [
        ("Juicio de expertos — cuestionario v2.2 y ficha documental", True),
        ("Trabajo de Integración Curricular: Metodología para el diagnóstico y gestión de riesgos en el tratamiento de datos "
         "personales académicos conforme a la LOPDP. Autor: Ramón Alejandro Manzaba Castro. "
         "Tutora: María Cristina Jiménez Hernández, MSc. Universidad Tecnológica Indoamérica.", False),
        ("1. Escriba su código de juez (lo asigna el investigador: E01, E02, …) y su perfil en la hoja «Datos del juez».", False),
        ("2. En las hojas «Cuestionario» y «Ficha documental», califique cada ítem de 1 a 4 en tres criterios:", False),
        ("   • Pertinencia: el ítem mide el indicador o la dimensión a la que está asignado.", False),
        ("   • Claridad: el ítem se comprende sin ambigüedad y mide una sola cosa.", False),
        ("   • Coherencia: el ítem corresponde a la obligación del artículo de la LOPDP que operacionaliza.", False),
        ("   Escala: 1 = no cumple; 2 = bajo nivel; 3 = nivel moderado; 4 = cumple plenamente.", False),
        ("3. Si califica 1 o 2 en algún criterio, escriba en «Observaciones» la razón y, si puede, una redacción alternativa.", False),
        ("4. Complete la hoja «Competencia (K)» (dos minutos).", False),
        ("5. Guarde el archivo con su código (por ejemplo, E01.xlsx) y devuélvalo al investigador en el plazo indicado.", False),
        ("Los ítems con (R) son inversos: el acuerdo indica una situación desfavorable; la marca no se muestra a los estudiantes.", False),
        ("Sus calificaciones se usan solo con fines académicos, con su código y nunca con su nombre (ver jueces/instrucciones_jueces.md).", False),
    ]
    for i, (t, negrita) in enumerate(textos, 1):
        c = ins.cell(i, 1, t)
        c.font = Font(bold=negrita, size=13 if negrita else 10, color="1F3864" if negrita else "000000")
        c.alignment = Alignment(wrap_text=True)
    ins.column_dimensions["A"].width = 130

    dj = wb.create_sheet("Datos del juez")
    for i, (k, v) in enumerate([("Código del juez", ""), ("Perfil principal", ""), ("Años de experiencia en el área", ""),
                                ("Máximo título académico", ""), ("Fecha de la evaluación", "")], 2):
        dj.cell(i, 1, k).font = Font(bold=True)
        c = dj.cell(i, 2, v)
        c.fill, c.border = AMARILLO, BORDE
    dv = DataValidation(type="list", formula1='"Protección de datos personales (jurídico),Seguridad de la información,'
                                              'Metodología de la investigación,Otro"', allow_blank=True)
    dj.add_data_validation(dv)
    dv.add("B3")
    dj.column_dimensions["A"].width = 32
    dj.column_dimensions["B"].width = 50

    filas = []
    for bloque, items in BLOQUES:
        for it in items:
            texto = C.TEXTO[it] + (" (R)" if it in C.INVERSOS else "")
            filas.append((bloque, it, texto, OPCIONES.get(it, "Likert 1–5" if it in C.ITEMS_LIKERT else "Sí / No / No recuerdo")))
    n_cuest = hoja_items(wb.create_sheet("Cuestionario"), "Cuestionario a estudiantes, versión 2.2 (Anexo B)", filas) - 4
    n_ficha = hoja_items(wb.create_sheet("Ficha documental"), "Ficha de verificación documental (Anexo A)",
                         [("Ficha documental", i, t, "S / P / N") for i, t in FICHA]) - 4

    k = wb.create_sheet("Competencia (K)")
    k["A1"] = "Autoevaluación del coeficiente de competencia experta K = ½ (Kc + Ka)"
    k["A1"].font = Font(bold=True, size=13, color="1F3864")
    k["A3"] = ("Parte 1 (Kc). Su nivel de conocimiento sobre protección de datos personales y gestión de riesgos en "
               "universidades, de 0 (ninguno) a 10 (pleno):")
    k["A3"].alignment = ENVOLVER
    k["B3"].fill, k["B3"].border = AMARILLO, BORDE
    dvk = DataValidation(type="whole", operator="between", formula1="0", formula2="10", allow_blank=True)
    k.add_data_validation(dvk)
    dvk.add("B3")
    k["C3"] = "Kc ="
    k["D3"] = '=IF(B3="","",B3/10)'
    cabecera(k, 5, ["Fuente de argumentación (Parte 2, Ka)", "Grado de influencia", "Alto", "Medio", "Bajo", "Peso"])
    fuentes = [("Análisis teóricos realizados por usted", 0.3, 0.2, 0.1), ("Experiencia práctica obtenida", 0.5, 0.4, 0.2),
               ("Trabajos de autores nacionales", 0.05, 0.05, 0.05), ("Trabajos de autores extranjeros", 0.05, 0.05, 0.05),
               ("Conocimiento del estado del tema en el extranjero", 0.05, 0.05, 0.05), ("Su intuición", 0.05, 0.05, 0.05)]
    dvg = DataValidation(type="list", formula1='"Alto,Medio,Bajo"', allow_blank=True)
    k.add_data_validation(dvg)
    for i, (f, a, m, b) in enumerate(fuentes, 6):
        k.cell(i, 1, f).border = BORDE
        g = k.cell(i, 2)
        g.fill, g.border = AMARILLO, BORDE
        dvg.add(f"B{i}")
        for j, v in enumerate((a, m, b), 3):
            k.cell(i, j, v).border = BORDE
        k.cell(i, 6, f'=IF(B{i}="Alto",C{i},IF(B{i}="Medio",D{i},IF(B{i}="Bajo",E{i},"")))').fill = GRIS
    k["E13"] = "Ka ="
    k["F13"] = '=IF(COUNT(F6:F11)<6,"",SUM(F6:F11))'
    k["E14"] = "K ="
    k["F14"] = '=IF(OR(D3="",F13=""),"",ROUND((D3+F13)/2,3))'
    k["E15"] = "Competencia:"
    k["F15"] = '=IF(F14="","",IF(F14>0.8,"Alta",IF(F14>=0.5,"Media","Baja")))'
    for ref in ("F13", "F14", "F15", "D3"):
        k[ref].fill, k[ref].font = GRIS, Font(bold=True)
    for col, w in zip("ABCDEF", (55, 18, 8, 8, 8, 10)):
        k.column_dimensions[col].width = w

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    wb.save(SALIDA)
    print(f"Escrito {SALIDA}: {n_cuest} ítems del cuestionario y {n_ficha} de la ficha")


if __name__ == "__main__":
    main()
