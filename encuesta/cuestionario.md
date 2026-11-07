# Cuestionario: Datos personales de estudiantes universitarios en Ecuador

> **Versión 2.0 (07-11-2026)**, enfoque cuantitativo (`uploads/metodologia_cuantitativa.md`). Es la versión previa al juicio de expertos y a la prueba piloto. Corresponde al Anexo "Cuestionario a estudiantes" y a la tabla de operacionalización del Cap. 3.
> **Regla de formato para el análisis:** cada pregunta del formulario empieza con su **código entre corchetes**, por ejemplo `[H4] ¿Le informaron…?`. Las opciones se copian **exactamente** como aparecen aquí, porque `analisis/limpieza.py` las reconoce por su texto (libro de códigos en `analisis/config.py`). Los códigos numéricos entre paréntesis no se muestran al participante.

## Configuración obligatoria del formulario (anonimato)

- **Google Forms:** Configuración → Respuestas → *Recopilar direcciones de correo electrónico* = **No recopilar**; *Limitar a 1 respuesta* = **desactivado** (exige iniciar sesión); sin preguntas de carga de archivos.
- **Microsoft Forms:** *Quién puede responder* = **Cualquier persona puede responder**; *Registrar nombre* = desactivado.
- **Lógica de secciones:** si P00, P01 o P02 = "No", ir directamente a la sección final.
- **Likert:** cada ítem como pregunta independiente de tipo **Escala lineal 1–5** (o de opción única con las cinco etiquetas), no como cuadrícula.
- Solo P00–P02 son obligatorias.
- Al cerrar: exportar a `.xlsx` → guardar como `analisis/datos/respuestas.xlsx` (excluido de git) → **eliminar las respuestas del servicio**.

Tiempo estimado: 10–12 minutos (46 preguntas).

---

## Sección 0. Consentimiento y filtros

*(Mostrar antes el texto de `encuesta/consentimiento_informado.md`.)*

- **[P00] ¿Acepta participar voluntariamente en esta encuesta anónima?** Sí, acepto · No acepto → fin
- **[P01] ¿Tiene 18 años o más?** Sí · No → fin
- **[P02] ¿Está matriculado actualmente en una universidad o escuela politécnica del Ecuador?** Sí · No → fin

## Sección A. Datos generales (no identificativos)

> No se pregunta el nombre de su universidad ni ningún dato que permita identificarle.

- **[A1] Su universidad es:** Pública (1) · Particular cofinanciada (2) · Particular autofinanciada (3) · No lo sé (9)
  *Para las hipótesis: pública = 1; privada = 2 o 3; "No lo sé" se excluye de los contrastes.*
- **[A2] Área de su carrera:** Educación · Artes y humanidades · Ciencias sociales, periodismo e información · Administración y derecho · Ciencias naturales, matemáticas y estadística · Tecnologías de la información y la comunicación · Ingeniería, industria y construcción · Agricultura, silvicultura, pesca y veterinaria · Salud y bienestar · Servicios
- **[A3] Semestre en el que se encuentra:** Nivelación o curso de admisión · 1.º a 3.er semestre · 4.º a 6.º semestre · 7.º semestre o superior
- **[A4] Rango de edad:** 18 a 20 · 21 a 24 · 25 a 29 · 30 o más

## Sección H. Preguntas de hechos

Opciones por defecto (H2, H4–H8, H12–H15): **Sí (1) · No (2) · No recuerdo (3)**.

- **[H1] Desde su postulación hasta hoy (admisión, matrícula, becas, bienestar, aula virtual u otros trámites), ¿qué datos le pidió su universidad?** *(Casillas: marque todas las que correspondan.)*
  Identificación (cédula, nombres, fecha de nacimiento) · Contacto (dirección, teléfono, correo personal) · Fotografía · Datos socioeconómicos del hogar · Datos de familiares o representantes · Datos de salud · Datos de discapacidad · Autoidentificación étnica · Datos biométricos (huella, reconocimiento facial) · Ubicación o geolocalización · Actividad en plataformas virtuales · No recuerdo
- **[H2]** ¿Su universidad le pidió su consentimiento (autorización) para tratar sus datos personales?
- **[H3]** *(Solo si H2 = Sí)* ¿De qué forma lo dio? De forma expresa (marcando una casilla o firmando) · De forma implícita ("al continuar, acepta…") · De forma verbal · No recuerdo
- **[H4]** Al entregar sus datos, ¿le informaron **para qué** se usarían?
- **[H5]** ¿Le informaron **quién es el responsable** de sus datos y **cómo contactarlo**?
- **[H6]** ¿Le informaron **durante cuánto tiempo** se conservarán sus datos?
- **[H7]** ¿Le informaron si sus datos se **compartirían con terceros** (otras instituciones, proveedores, plataformas en la nube)?
- **[H8]** ¿Pudo aceptar o rechazar **por separado** los usos no necesarios para su matrícula (por ejemplo, publicidad o difusión de su imagen)?
- **[H9]** Cuando le pidieron datos de salud, discapacidad, socioeconómicos o biométricos, ¿le explicaron para qué se usarían? Sí · No · No recuerdo · No me pidieron esos datos (8)
- **[H10]** ¿Le informaron si alguna plataforma de su universidad (aula virtual, supervisión de exámenes en línea, analítica) analiza automáticamente su comportamiento o elabora perfiles? Sí · No · No recuerdo · No uso esas plataformas (8)
- **[H11]** ¿Ha solicitado alguna vez a su universidad acceder, corregir o eliminar sus datos? Sí, y me respondieron en un plazo razonable · Sí, pero no me respondieron o tardaron mucho · No
- **[H12]** ¿Su universidad le ha comunicado alguna vez que sus datos se vieron afectados por un incidente de seguridad?
- **[H13]** ¿Ha visto publicados por su universidad listados con su número de cédula junto a su nombre, calificaciones o resultados?
- **[H14]** En el último semestre, ¿recibió en su cuenta institucional correos que pedían contraseñas, pagos o datos personales?
- **[H15]** ¿Su universidad le ha dado información o capacitación sobre protección de datos personales?
- **[H16]** ¿Sabe por qué canal (correo, formulario u oficina) puede ejercer sus derechos sobre sus datos en su universidad? Sí · No

## Sección L. Escalas Likert

Escala para todos los ítems: **1 = Totalmente en desacuerdo · 2 = En desacuerdo · 3 = Ni de acuerdo ni en desacuerdo · 4 = De acuerdo · 5 = Totalmente de acuerdo**.
Los ítems marcados con **(R)** son **inversos**: un acuerdo alto indica una situación desfavorable. En el análisis se recodifican como x' = 6 − x antes de calcular la puntuación de la dimensión y la confiabilidad. En el formulario **no se marca** cuáles son inversos.

### Dimensión INF — Información recibida
- **[INF1]** Mi universidad me explicó con claridad para qué usa mis datos personales.
- **[INF2]** Sé quién es el responsable de mis datos en mi universidad y cómo contactarlo.
- **[INF3]** Mi universidad me informó cuánto tiempo conservará mis datos.
- **[INF4] (R)** No sé con quién comparte mi universidad mis datos personales.
- **[INF5]** La política de privacidad de mi universidad es fácil de encontrar y de entender.

### Dimensión CON — Consentimiento
- **[CON1]** Mi universidad me pidió autorización antes de recoger mis datos personales.
- **[CON2]** Pude aceptar o rechazar por separado los usos de mis datos que no eran necesarios para estudiar.
- **[CON3] (R)** Sentí que, si no entregaba todos los datos que me pedían, perdería la matrícula o un servicio.
- **[CON4]** Entendí lo que estaba aceptando cuando di mi autorización.
- **[CON5]** Sé que puedo retirar mi autorización cuando quiera.

### Dimensión DER — Conocimiento de derechos
- **[DER1]** Sé que puedo pedir a mi universidad acceso a todos los datos que tiene de mí.
- **[DER2]** Sé que puedo pedir que corrijan o actualicen mis datos.
- **[DER3]** Sé que puedo pedir que eliminen mis datos cuando ya no sean necesarios.
- **[DER4]** Sé que puedo oponerme a ciertos usos de mis datos.
- **[DER5]** Sé que puedo pedir mis datos en un formato que me permita llevarlos a otra institución.
- **[DER6] (R)** No sabría ante quién reclamar si mi universidad usa mal mis datos.
- **[DER7]** Conozco la Ley Orgánica de Protección de Datos Personales.

### Dimensión CNF — Confianza y percepción de seguridad
- **[CNF1]** Confío en que mi universidad protege adecuadamente mis datos personales.
- **[CNF2]** Creo que el personal de mi universidad accede solo a los datos que necesita para su función.
- **[CNF3] (R)** Me preocupa que mis datos personales se filtren desde los sistemas de mi universidad.
- **[CNF4]** Si mis datos fueran expuestos o robados, mi universidad me lo comunicaría.
- **[CNF5]** Me sentiría seguro(a) entregando datos de salud o discapacidad a mi universidad.
- **[CNF6] (R)** Mi universidad trata mis datos como si le pertenecieran a ella y no a mí.

---

### Sección final

Gracias por su participación. Sus respuestas son anónimas y se usarán solo de forma agregada en un trabajo de titulación. Si tiene preguntas: ramonalejandromanzaba@gmail.com

*(En el piloto se añade una pregunta abierta: "¿Alguna pregunta le resultó confusa? ¿Cuál y por qué?". Se advierte no escribir datos que identifiquen a personas.)*

---

## Recodificación de ítems inversos

| Ítem | Dimensión | Respuesta original → valor analizado |
|---|---|---|
| INF4, CON3, DER6, CNF3, CNF6 | INF, CON, DER, CNF | 1→5 · 2→4 · 3→3 · 4→2 · 5→1 (x' = 6 − x) |

Puntuación de cada dimensión = media de sus ítems ya recodificados. Se calcula solo si la persona respondió al menos el 80 % de los ítems de esa dimensión.

## Regla de "respuesta afirmativa" para los indicadores de hechos

| Indicador | Pregunta | Afirmativo | Fuera del denominador |
|---|---|---|---|
| IE01 | H1_01…H1_11 (y al menos una de salud, discapacidad o biometría) | casilla marcada | "No recuerdo" |
| IE02 | H9 | Sí | No me pidieron esos datos |
| IE03 / IE04 / IE05 / IE06 | H4 / H5 / H6 / H7 | Sí | — |
| IE07 | H2 (y H3 = expresa, entre quienes respondieron Sí) | Sí | — |
| IE08 | H8 | Sí | — |
| IE11 | H16 (y H11 = Sí, con o sin respuesta) | Sí | — |
| IE12 | H15 | Sí | — |
| IE14 | H14, H13, H12 | Sí | — |
| IE15 | H10 | Sí | No uso esas plataformas |

"No recuerdo" cuenta como no afirmativo: el titular que no recuerda haber sido informado no puede ejercer lo que no conoce. En el informe se presenta, además, su porcentaje por separado.
