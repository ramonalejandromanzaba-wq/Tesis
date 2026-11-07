"""Libro de códigos del cuestionario (encuesta/cuestionario.md, v2.0).

Única fuente de verdad para limpieza, validación, descriptivos, inferencial, gráficos y exportación.
Si se modifica el cuestionario tras el juicio de expertos o el piloto, se actualiza solo este archivo.
"""

ALPHA = 0.05  # nivel de significancia de las hipótesis

# ------------------------------------------------------------------ filtros (si alguno ≠ "Sí", el caso se excluye)
FILTROS = ["P00", "P01", "P02"]

# ------------------------------------------------------------------ datos demográficos (no identificativos)
DEMOGRAFICOS = {
    "A1": {"Pública": 1, "Particular cofinanciada": 2, "Particular autofinanciada": 3, "No lo sé": 9},
    "A2": {"Educación": 1, "Artes y humanidades": 2, "Ciencias sociales, periodismo e información": 3,
           "Administración y derecho": 4, "Ciencias naturales, matemáticas y estadística": 5,
           "Tecnologías de la información y la comunicación": 6, "Ingeniería, industria y construcción": 7,
           "Agricultura, silvicultura, pesca y veterinaria": 8, "Salud y bienestar": 9, "Servicios": 10},
    "A3": {"Nivelación o curso de admisión": 0, "1.º a 3.er semestre": 1, "4.º a 6.º semestre": 2,
           "7.º semestre o superior": 3},
    "A4": {"18 a 20": 1, "21 a 24": 2, "25 a 29": 3, "30 o más": 4},
}
# Tipo de universidad recodificado para las hipótesis: 1 = pública, 2 = privada (particular), NaN = no sabe
TIPO = "TIPO"

# ------------------------------------------------------------------ preguntas de hechos
SNR = {"Sí": 1, "No": 2, "No recuerdo": 3}
HECHOS = {
    "H2": SNR, "H4": SNR, "H5": SNR, "H6": SNR, "H7": SNR, "H8": SNR, "H12": SNR, "H13": SNR, "H14": SNR, "H15": SNR,
    "H3": {"De forma expresa (marcando una casilla o firmando)": 1, "De forma implícita (\"al continuar, acepta…\")": 2,
           "De forma verbal": 3, "No recuerdo": 4},
    "H9": {"Sí": 1, "No": 2, "No recuerdo": 3, "No me pidieron esos datos": 8},
    "H10": {"Sí": 1, "No": 2, "No recuerdo": 3, "No uso esas plataformas": 8},
    "H11": {"Sí, y me respondieron en un plazo razonable": 1, "Sí, pero no me respondieron o tardaron mucho": 2, "No": 3},
    "H16": {"Sí": 1, "No": 2},
}
# H1: opción múltiple → una columna binaria por categoría
H1_OPCIONES = {
    "H1_01": "Identificación (cédula, nombres, fecha de nacimiento)",
    "H1_02": "Contacto (dirección, teléfono, correo personal)",
    "H1_03": "Fotografía",
    "H1_04": "Datos socioeconómicos del hogar",
    "H1_05": "Datos de familiares o representantes",
    "H1_06": "Datos de salud",
    "H1_07": "Datos de discapacidad",
    "H1_08": "Autoidentificación étnica",
    "H1_09": "Datos biométricos (huella, reconocimiento facial)",
    "H1_10": "Ubicación o geolocalización",
    "H1_11": "Actividad en plataformas virtuales",
    "H1_99": "No recuerdo",
}
H1_ESPECIALES = ["H1_06", "H1_07", "H1_09"]  # categorías especiales / sensibles (LOPDP arts. 25 y 26)

# Regla de "respuesta afirmativa" por indicador de hechos: (pregunta, códigos afirmativos, códigos excluidos del denominador)
AFIRMATIVO = {
    "IE02 Explicación de datos sensibles": ("H9", [1], [8]),
    "IE03 Informado de la finalidad": ("H4", [1], []),
    "IE04 Informado del responsable": ("H5", [1], []),
    "IE05 Informado de la conservación": ("H6", [1], []),
    "IE06 Informado de terceros": ("H7", [1], []),
    "IE07 Se pidió consentimiento": ("H2", [1], []),
    "IE07b Consentimiento expreso (si se pidió)": ("H3", [1], []),
    "IE08 Consentimiento separado por finalidad": ("H8", [1], []),
    "IE11 Conoce el canal de derechos": ("H16", [1], []),
    "IE11b Ejerció algún derecho": ("H11", [1, 2], []),
    "IE12b Recibió información o capacitación": ("H15", [1], []),
    "IE14a Correos sospechosos en el semestre": ("H14", [1], []),
    "IE14b Vio listados con su cédula": ("H13", [1], []),
    "IE14c Recibió comunicación de vulneración": ("H12", [1], []),
    "IE15 Informado de perfiles automatizados": ("H10", [1], [8]),
}
# Escala dicotómica para KR-20: información recibida según hechos (Sí = 1; No o No recuerdo = 0)
KR20_INFO = ["H4", "H5", "H6", "H7"]

# ------------------------------------------------------------------ escalas Likert (1 = Totalmente en desacuerdo … 5 = Totalmente de acuerdo)
LIKERT_ETIQUETAS = {"Totalmente en desacuerdo": 1, "En desacuerdo": 2, "Ni de acuerdo ni en desacuerdo": 3,
                    "De acuerdo": 4, "Totalmente de acuerdo": 5}
DIMENSIONES = {
    "INF": {"nombre": "Información recibida", "items": ["INF1", "INF2", "INF3", "INF4", "INF5"], "inversos": ["INF4"]},
    "CON": {"nombre": "Consentimiento", "items": ["CON1", "CON2", "CON3", "CON4", "CON5"], "inversos": ["CON3"]},
    "DER": {"nombre": "Conocimiento de derechos", "items": ["DER1", "DER2", "DER3", "DER4", "DER5", "DER6", "DER7"], "inversos": ["DER6"]},
    "CNF": {"nombre": "Confianza y percepción de seguridad", "items": ["CNF1", "CNF2", "CNF3", "CNF4", "CNF5", "CNF6"], "inversos": ["CNF3", "CNF6"]},
}
INVERSOS = [i for d in DIMENSIONES.values() for i in d["inversos"]]
ITEMS_LIKERT = [i for d in DIMENSIONES.values() for i in d["items"]]

# Columnas que nunca deben salir de limpieza (identificativas o metadatos de la plataforma)
PATRONES_IDENTIFICATIVOS = ["correo", "email", "e-mail", "nombre", "name", "ip", "id", "hora", "time", "fecha",
                            "marca temporal", "timestamp", "cédula", "cedula", "teléfono", "telefono", "matrícula"]

# ------------------------------------------------------------------ juicio de expertos
CRITERIOS = ["pertinencia", "claridad", "coherencia"]
AIKEN_MIN = 0.80  # se conserva el ítem si V ≥ 0,80 en los tres criterios
AIKEN_ESCALA = (1, 5)  # l, l + (c − 1)
