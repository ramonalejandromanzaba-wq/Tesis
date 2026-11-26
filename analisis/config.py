"""Libro de códigos del cuestionario (encuesta/cuestionario.md, versión 2.2 del 25-11-2026).

Única fuente de verdad para limpieza, validación, descriptivos, inferencial, brechas, gráficos y exportación.
Si se modifica el cuestionario tras el juicio de expertos o el piloto, se actualiza solo este archivo
(y el Anexo B, la tabla de operacionalización y encuesta/cuestionario.md).

Cambios de la v2.0 a la v2.1 (retroalimentación de la tutora, 11-11-2026):
- P02 pasa a ser el filtro de Pichincha (reemplaza "matriculado en el Ecuador").
- A3 incluye "Posgrado" (se excluye del análisis: la población es de grado).
- Nuevas: A5 universidad (solo para ponderar la brecha; nunca se publica por universidad),
  A6 modalidad y A7 canal de difusión (opcional).
- Ítems de doble contenido separados: H5 → H5a/H5b; INF2 → INF2a/INF2b; INF5 → INF5a/INF5b.
- Redacción de un solo contenido: CON3, CNF4 y CNF5.
- H16 añade "No estoy seguro(a)" (código 3; cuenta como no afirmativo, igual que "No recuerdo").

Cambios de la v2.1 a la v2.2 (observaciones de revisión v3, 25-11-2026):
- Ámbito nacional (OM-01): P02 = estudia una carrera de grado en una universidad o escuela politécnica del Ecuador;
  A5 = las 64 instituciones del CES + "Prefiero no responder"; nueva A8 región (opcional, descriptiva).
- Derechos de los arts. 19 y 20 de la LOPDP (OM-04): nuevos DER8 (suspensión) y DER9 (decisiones automatizadas).
- H1 añade "Condición migratoria" e "Identidad de género o nombre social" (Om-17); las categorías especiales y
  sensibles de H1 siguen la definición de datos sensibles del art. 4 y las categorías del art. 25.
- P00 deja de decir "anónima" (OM-07): la base no tiene datos identificativos directos (seudonimizada).
- H3 (hipótesis) usa H8 en lugar de H2 (OM-03).
Total: 55 preguntas (acceso, 3; generales, 8; hechos, 17; Likert, 27).
"""

ALPHA = 0.05  # nivel de significancia de las hipótesis
VERSION_CUESTIONARIO = "2.2"
MIN_CELDA = 5  # supresión de celdas pequeñas: ninguna categoría con menos de 5 respuestas se reporta sola

# ------------------------------------------------------------------ filtros (si alguno ≠ "Sí", el caso se excluye)
FILTROS = ["P00", "P01", "P02"]  # consentimiento, mayoría de edad, estudia una carrera de grado en el Ecuador

# ------------------------------------------------------------------ universidades y escuelas politécnicas (pregunta A5)
# Las 64 instituciones de las listas del CES por sostenimiento (páginas 328, 1540 y 5398; consulta del 16-11-2026,
# confirmada el 25-11-2026): 36 públicas, 20 particulares autofinanciadas y 8 particulares cofinanciadas. Es información
# pública. En el formulario se muestran en orden alfabético (UNIVERSIDADES); el número de opción es la posición + 1.
# El código de censo (U01, U02, …) NO está aquí: se lee de privado/clave_universidades.xlsx (fuera del repositorio).
# Valor: (sostenimiento 1 = pública, 2 = particular cofinanciada, 3 = particular autofinanciada; provincia de la matriz)
UNIV_DATOS = {
    "Escuela Politécnica Nacional": (1, "Pichincha"),
    "Escuela Superior Politécnica de Chimborazo": (1, "Chimborazo"),
    "Escuela Superior Politécnica Agropecuaria de Manabí Manuel Félix López (ESPAM MFL)": (1, "Manabí"),
    "Universidad Central del Ecuador": (1, "Pichincha"),
    "Universidad de Guayaquil": (1, "Guayas"),
    "Universidad de Cuenca": (1, "Azuay"),
    "Universidad Nacional de Loja": (1, "Loja"),
    "Universidad Técnica de Manabí": (1, "Manabí"),
    "Universidad Técnica de Ambato": (1, "Tungurahua"),
    "Universidad Técnica de Machala": (1, "El Oro"),
    "Universidad Técnica Luis Vargas Torres de Esmeraldas": (1, "Esmeraldas"),
    "Universidad Técnica de Babahoyo": (1, "Los Ríos"),
    "Universidad Técnica Estatal de Quevedo": (1, "Los Ríos"),
    "Universidad Técnica del Norte": (1, "Imbabura"),
    "Universidad Laica Eloy Alfaro de Manabí": (1, "Manabí"),
    "Universidad Estatal de Bolívar": (1, "Bolívar"),
    "Universidad Agraria del Ecuador": (1, "Guayas"),
    "Universidad Nacional de Chimborazo": (1, "Chimborazo"),
    "Universidad Técnica de Cotopaxi": (1, "Cotopaxi"),
    "Escuela Superior Politécnica del Litoral (ESPOL)": (1, "Guayas"),
    "Universidad Andina Simón Bolívar": (1, "Pichincha"),
    "Universidad Estatal Península de Santa Elena (UPSE)": (1, "Santa Elena"),
    "Universidad Estatal de Milagro": (1, "Guayas"),
    "Universidad Estatal del Sur de Manabí": (1, "Manabí"),
    "Facultad Latinoamericana de Ciencias Sociales (FLACSO)": (1, "Pichincha"),
    "Instituto de Altos Estudios Nacionales (IAEN)": (1, "Pichincha"),
    "Universidad Estatal Amazónica": (1, "Pastaza"),
    "Universidad Intercultural de las Nacionalidades y Pueblos Indígenas Amawtay Wasi": (1, "Pichincha"),
    "Universidad Politécnica Estatal del Carchi": (1, "Carchi"),
    "Universidad de las Fuerzas Armadas ESPE": (1, "Pichincha"),
    "Universidad Regional Amazónica Ikiam": (1, "Napo"),
    "Universidad de Investigación de Tecnología Experimental Yachay": (1, "Imbabura"),
    "Universidad de las Artes": (1, "Guayas"),
    "Universidad Nacional de Educación": (1, "Cañar"),
    "Universidad de Seguridad Ciudadana y Ciencias Policiales (USECIPOL)": (1, "Pichincha"),
    "Universidad Pública de Santo Domingo de los Tsáchilas": (1, "Santo Domingo de los Tsáchilas"),
    "Universidad Particular Internacional SEK": (3, "Pichincha"),
    "Universidad de Especialidades Espíritu Santo (UEES)": (3, "Guayas"),
    "Universidad San Francisco de Quito (USFQ)": (3, "Pichincha"),
    "Universidad de las Américas (UDLA)": (3, "Pichincha"),
    "Universidad Internacional del Ecuador (UIDE)": (3, "Pichincha"),
    "Universidad Regional Autónoma de los Andes (UNIANDES)": (3, "Tungurahua"),
    "Universidad del Pacífico - Escuela de Negocios": (3, "Guayas"),
    "Universidad Tecnológica Indoamérica": (3, "Tungurahua"),
    "Universidad Casa Grande": (3, "Guayas"),
    "Universidad Tecnológica Empresarial de Guayaquil": (3, "Guayas"),
    "Universidad Tecnológica Israel": (3, "Pichincha"),
    "Universidad de Especialidades Turísticas": (3, "Pichincha"),
    "Universidad Metropolitana": (3, "Guayas"),
    "Universidad de Otavalo": (3, "Imbabura"),
    "Universidad San Gregorio de Portoviejo": (3, "Manabí"),
    "Universidad de los Hemisferios": (3, "Pichincha"),
    "Universidad Iberoamericana del Ecuador": (3, "Pichincha"),
    "Universidad Tecnológica ECOTEC": (3, "Guayas"),
    "Universidad del Río (UDR)": (3, "Guayas"),
    "Universidad Bolivariana del Ecuador": (3, "Guayas"),
    "Pontificia Universidad Católica del Ecuador (PUCE)": (2, "Pichincha"),
    "Universidad Católica de Santiago de Guayaquil (UCSG)": (2, "Guayas"),
    "Universidad Católica de Cuenca": (2, "Azuay"),
    "Universidad Laica Vicente Rocafuerte de Guayaquil": (2, "Guayas"),
    "Universidad Técnica Particular de Loja (UTPL)": (2, "Loja"),
    "Universidad UTE": (2, "Pichincha"),
    "Universidad del Azuay": (2, "Azuay"),
    "Universidad Politécnica Salesiana (UPS)": (2, "Azuay"),
}
assert len(UNIV_DATOS) == 64
assert [s for s, _ in UNIV_DATOS.values()].count(1) == 36 and [s for s, _ in UNIV_DATOS.values()].count(2) == 8
UNIVERSIDADES = sorted(UNIV_DATOS, key=lambda n: n.lower().replace("á", "a").replace("é", "e").replace("í", "i")
                       .replace("ó", "o").replace("ú", "u"))
# Región natural de la provincia de la matriz (para el reporte por región del censo, solo con ≥ 5 por grupo)
REGION_PROVINCIA = {
    "Costa": ["Esmeraldas", "Manabí", "Los Ríos", "Guayas", "Santa Elena", "El Oro", "Santo Domingo de los Tsáchilas"],
    "Sierra": ["Carchi", "Imbabura", "Pichincha", "Cotopaxi", "Tungurahua", "Bolívar", "Chimborazo", "Cañar", "Azuay", "Loja"],
    "Amazonía": ["Sucumbíos", "Napo", "Orellana", "Pastaza", "Morona Santiago", "Zamora Chinchipe"],
    "Galápagos": ["Galápagos"],
}
UNIV_NO_RESPONDE = "Prefiero no responder"
CLAVE_UNIVERSIDADES = "privado/clave_universidades.xlsx"  # ruta relativa a la raíz del repositorio

# ------------------------------------------------------------------ datos demográficos (no identificativos)
DEMOGRAFICOS = {
    "A1": {"Pública": 1, "Particular cofinanciada": 2, "Particular autofinanciada": 3, "No lo sé": 9},
    "A2": {"Educación": 1, "Artes y humanidades": 2, "Ciencias sociales, periodismo e información": 3,
           "Administración y derecho": 4, "Ciencias naturales, matemáticas y estadística": 5,
           "Tecnologías de la información y la comunicación": 6, "Ingeniería, industria y construcción": 7,
           "Agricultura, silvicultura, pesca y veterinaria": 8, "Salud y bienestar": 9, "Servicios": 10},
    "A3": {"Nivelación o curso de admisión": 0, "1.º a 3.er semestre": 1, "4.º a 6.º semestre": 2,
           "7.º semestre o superior": 3, "Posgrado (especialización, maestría o doctorado)": 9},
    "A4": {"18 a 20": 1, "21 a 24": 2, "25 a 29": 3, "30 o más": 4},
    "A5": {**{u: i + 1 for i, u in enumerate(UNIVERSIDADES)}, UNIV_NO_RESPONDE: 99},
    "A6": {"Presencial": 1, "Semipresencial o híbrida": 2, "En línea": 3},
    "A7": {"Enlace en redes sociales o grupos de mensajería": 1, "Correo electrónico": 2,
           "Código QR en el campus": 3, "Invitación de un docente": 4, "Invitación de un compañero o amigo": 5,
           "Otro": 6},
    "A8": {"Costa": 1, "Sierra": 2, "Amazonía": 3, "Galápagos": 4},
}
A3_POSGRADO = 9  # se excluye del análisis (la población es la matrícula de grado)
A6_NOMBRE = {1: "Presencial", 2: "Semipresencial o híbrida", 3: "En línea"}
# Sostenimiento para las hipótesis (variable TIPO): 1 = pública; 2 = privada (cofinanciada o autofinanciada).
# Regla: si A5 identifica una universidad del censo, se usa su sostenimiento oficial (clave privada);
# si no, se usa A1 (autodeclarado); "No lo sé" sin universidad identificada = NaN (excluido de H1 y H3).
TIPO = "TIPO"
SOST = "SOST"  # 1 = pública, 2 = particular cofinanciada, 3 = particular autofinanciada (para el reporte)
SOST_NOMBRE = {1: "Pública", 2: "Particular cofinanciada", 3: "Particular autofinanciada"}

# ------------------------------------------------------------------ preguntas de hechos
SNR = {"Sí": 1, "No": 2, "No recuerdo": 3}
NO_RECUERDO = 3  # "No recuerdo" (y "No estoy seguro(a)" en H16) = no afirmativo; se reporta con y sin él
HECHOS = {
    "H2": SNR, "H4": SNR, "H5a": SNR, "H5b": SNR, "H6": SNR, "H7": SNR, "H8": SNR,
    "H12": SNR, "H13": SNR, "H14": SNR, "H15": SNR,
    "H3": {"De forma expresa (marcando una casilla o firmando)": 1, "De forma implícita (\"al continuar, acepta…\")": 2,
           "De forma verbal": 3, "No recuerdo": 4},
    "H9": {"Sí": 1, "No": 2, "No recuerdo": 3, "No me pidieron esos datos": 8},
    "H10": {"Sí": 1, "No": 2, "No recuerdo": 3, "No uso esas plataformas": 8},
    "H11": {"Sí, y me respondieron en un plazo razonable": 1, "Sí, pero no me respondieron o tardaron mucho": 2, "No": 3},
    "H16": {"Sí": 1, "No": 2, "No estoy seguro(a)": 3},
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
    "H1_12": "Condición migratoria",
    "H1_13": "Identidad de género o nombre social",
    "H1_09": "Datos biométricos (huella, reconocimiento facial)",
    "H1_10": "Ubicación o geolocalización",
    "H1_11": "Actividad en plataformas virtuales",
    "H1_99": "No recuerdo",
}
# Categorías especiales o datos sensibles (LOPDP art. 4, datos sensibles, y art. 25). Los datos socioeconómicos (H1_04)
# no son categoría especial: se valoran como de alto impacto en la metodología (Om-17, opción a).
H1_ESPECIALES = ["H1_06", "H1_07", "H1_08", "H1_12", "H1_13", "H1_09"]

# Regla de "respuesta afirmativa" por indicador de hechos: (pregunta, códigos afirmativos, códigos excluidos del denominador)
AFIRMATIVO = {
    "IE02 Explicación de datos sensibles": ("H9", [1], [8]),
    "IE03 Informado de la finalidad": ("H4", [1], []),
    "IE04a Informado de quién es el responsable": ("H5a", [1], []),
    "IE04b Informado de cómo contactar al responsable": ("H5b", [1], []),
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
KR20_INFO = ["H4", "H5a", "H5b", "H6", "H7"]

# ------------------------------------------------------------------ escalas Likert (1 = Totalmente en desacuerdo … 5 = Totalmente de acuerdo)
LIKERT_ETIQUETAS = {"Totalmente en desacuerdo": 1, "En desacuerdo": 2, "Ni de acuerdo ni en desacuerdo": 3,
                    "De acuerdo": 4, "Totalmente de acuerdo": 5}
DIMENSIONES = {
    "INF": {"nombre": "Información recibida", "items": ["INF1", "INF2a", "INF2b", "INF3", "INF4", "INF5a", "INF5b"],
            "inversos": ["INF4"]},
    "CON": {"nombre": "Consentimiento", "items": ["CON1", "CON2", "CON3", "CON4", "CON5"], "inversos": ["CON3"]},
    "DER": {"nombre": "Conocimiento de derechos",
            "items": ["DER1", "DER2", "DER3", "DER4", "DER5", "DER6", "DER7", "DER8", "DER9"],
            "inversos": ["DER6"]},
    "CNF": {"nombre": "Confianza y percepción de seguridad", "items": ["CNF1", "CNF2", "CNF3", "CNF4", "CNF5", "CNF6"],
            "inversos": ["CNF3", "CNF6"]},
}
INVERSOS = [i for d in DIMENSIONES.values() for i in d["inversos"]]
ITEMS_LIKERT = [i for d in DIMENSIONES.values() for i in d["items"]]

# Texto de cada ítem (para el paquete de jueces y el anexo); se mantiene igual que encuesta/cuestionario.md
TEXTO = {
    "P00": "¿Acepta participar voluntariamente en esta encuesta, que no recoge datos que le identifiquen directamente?",
    "P01": "¿Tiene 18 años o más?",
    "P02": "¿Estudia actualmente una carrera de grado en una universidad o escuela politécnica del Ecuador?",
    "A1": "Su universidad es:",
    "A2": "Área de su carrera:",
    "A3": "Semestre o nivel en el que se encuentra:",
    "A4": "Rango de edad:",
    "A5": "¿En qué universidad o escuela politécnica estudia?",
    "A6": "Modalidad de su carrera:",
    "A7": "¿Cómo se enteró de esta encuesta? (opcional)",
    "A8": "Región del Ecuador en la que estudia (opcional):",
    "H1": "Desde su postulación hasta hoy (admisión, matrícula, becas, bienestar, aula virtual u otros trámites), ¿qué datos le pidió su universidad? (marque todas las que correspondan)",
    "H2": "¿Su universidad le pidió su consentimiento (autorización) para tratar sus datos personales?",
    "H3": "(Solo si H2 = Sí) ¿De qué forma lo dio?",
    "H4": "Al entregar sus datos, ¿le informaron para qué se usarían?",
    "H5a": "¿Le informaron quién es el responsable de sus datos?",
    "H5b": "¿Le informaron cómo contactar al responsable de sus datos?",
    "H6": "¿Le informaron durante cuánto tiempo se conservarán sus datos?",
    "H7": "¿Le informaron si sus datos se compartirían con terceros (otras instituciones, proveedores, plataformas en la nube)?",
    "H8": "¿Pudo aceptar o rechazar por separado los usos no necesarios para su matrícula (por ejemplo, publicidad o difusión de su imagen)?",
    "H9": "Cuando le pidieron datos de salud, discapacidad, socioeconómicos o biométricos, ¿le explicaron para qué se usarían?",
    "H10": "¿Le informaron si alguna plataforma de su universidad (aula virtual, supervisión de exámenes en línea, analítica) analiza automáticamente su comportamiento o elabora perfiles?",
    "H11": "¿Ha solicitado alguna vez a su universidad acceder, corregir o eliminar sus datos?",
    "H12": "¿Su universidad le ha comunicado alguna vez que sus datos se vieron afectados por un incidente de seguridad?",
    "H13": "¿Ha visto publicados por su universidad listados con su número de cédula junto a su nombre, calificaciones o resultados?",
    "H14": "En el último semestre, ¿recibió en su cuenta institucional correos que pedían contraseñas, pagos o datos personales?",
    "H15": "¿Su universidad le ha dado información o capacitación sobre protección de datos personales?",
    "H16": "¿Sabe por qué canal (correo, formulario u oficina) puede ejercer sus derechos sobre sus datos en su universidad?",
    "INF1": "Mi universidad me explicó con claridad para qué usa mis datos personales.",
    "INF2a": "Sé quién es el responsable de mis datos en mi universidad.",
    "INF2b": "Sé cómo contactar al responsable de mis datos en mi universidad.",
    "INF3": "Mi universidad me informó cuánto tiempo conservará mis datos.",
    "INF4": "No sé con quién comparte mi universidad mis datos personales.",
    "INF5a": "La política de privacidad de mi universidad es fácil de encontrar.",
    "INF5b": "La política de privacidad de mi universidad es fácil de entender.",
    "CON1": "Mi universidad me pidió autorización antes de recoger mis datos personales.",
    "CON2": "Pude aceptar o rechazar por separado los usos de mis datos que no eran necesarios para estudiar.",
    "CON3": "Sentí que estaba obligado(a) a entregar todos los datos que me pedían para poder estudiar.",
    "CON4": "Entendí lo que estaba aceptando cuando di mi autorización.",
    "CON5": "Sé que puedo retirar mi autorización cuando quiera.",
    "DER1": "Sé que puedo pedir a mi universidad acceso a todos los datos que tiene de mí.",
    "DER2": "Sé que puedo pedir que corrijan o actualicen mis datos.",
    "DER3": "Sé que puedo pedir que eliminen mis datos cuando ya no sean necesarios.",
    "DER4": "Sé que puedo oponerme a ciertos usos de mis datos.",
    "DER5": "Sé que puedo pedir mis datos en un formato que me permita llevarlos a otra institución.",
    "DER6": "No sabría ante quién reclamar si mi universidad usa mal mis datos.",
    "DER7": "Conozco la Ley Orgánica de Protección de Datos Personales.",
    "DER8": "Sé que puedo pedir que se suspenda el uso de mis datos mientras se revisa si son correctos.",
    "DER9": "Sé que puedo pedir que una decisión sobre mí no se tome solo con un sistema automático.",
    "CNF1": "Confío en que mi universidad protege adecuadamente mis datos personales.",
    "CNF2": "Creo que el personal de mi universidad accede solo a los datos que necesita para su función.",
    "CNF3": "Me preocupa que mis datos personales se filtren desde los sistemas de mi universidad.",
    "CNF4": "Si mis datos se vieran afectados por un incidente de seguridad, mi universidad me lo comunicaría.",
    "CNF5": "Me sentiría seguro(a) entregando a mi universidad datos sensibles, como los de salud.",
    "CNF6": "Mi universidad trata mis datos como si le pertenecieran a ella y no a mí.",
}
ITEMS_CUESTIONARIO = (["P00", "P01", "P02"] + [f"A{i}" for i in range(1, 9)]
                      + ["H1", "H2", "H3", "H4", "H5a", "H5b"] + [f"H{i}" for i in range(6, 17)] + ITEMS_LIKERT)
assert len(ITEMS_CUESTIONARIO) == 55, len(ITEMS_CUESTIONARIO)

# Columnas que nunca deben salir de limpieza (identificativas o metadatos de la plataforma)
PATRONES_IDENTIFICATIVOS = ["correo", "email", "e-mail", "nombre", "name", "ip", "id", "hora", "time", "fecha",
                            "marca temporal", "timestamp", "cédula", "cedula", "teléfono", "telefono", "matrícula"]

# ------------------------------------------------------------------ juicio de expertos (jueces/formato_juicio_expertos.xlsx)
CRITERIOS = ["pertinencia", "claridad", "coherencia"]
AIKEN_MIN = 0.80  # se conserva el ítem si V ≥ 0,80 en los tres criterios
AIKEN_ESCALA = (1, 4)  # escala de los jueces: 1 = no cumple … 4 = cumple plenamente (l = 1; c = 4)

# ------------------------------------------------------------------ interpretación del tamaño del efecto (Cohen, 1988)
# |ρ| y r: < 0,10 trivial; 0,10–0,29 débil; 0,30–0,49 moderada; ≥ 0,50 fuerte. V de Cramér con gl* = 1: los mismos cortes.
UMBRALES_EFECTO = [(0.10, "trivial"), (0.30, "débil"), (0.50, "moderada"), (float("inf"), "fuerte")]


def magnitud(efecto):
    """Etiqueta del tamaño del efecto según Cohen (1988), sobre el valor absoluto."""
    import math
    if efecto is None or (isinstance(efecto, float) and math.isnan(efecto)):
        return "---"
    for corte, etiqueta in UMBRALES_EFECTO:
        if abs(efecto) < corte:
            return etiqueta
    return "fuerte"
