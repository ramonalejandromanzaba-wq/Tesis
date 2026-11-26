# Cuestionario: Datos personales de estudiantes universitarios del Ecuador

> **Versión 2.2 (25-11-2026)**, previa al juicio de expertos y a la prueba piloto. Atiende las observaciones de revisión v3 (`uploads/observaciones_tesis_v3.md`: OM-01 ámbito nacional, OM-03 hipótesis H3, OM-04 derechos de los arts. 19 y 20, OM-07 encuesta seudonimizada, Om-17 datos sensibles en H1). Corresponde exactamente al Anexo B del documento y a la tabla de operacionalización del Cap. 3. El libro de códigos está en `analisis/config.py` (incluye el texto de cada ítem): si cambia el cuestionario, se cambia ahí y aquí.
> **Regla de formato para el análisis:** cada pregunta del formulario empieza con su **código entre corchetes**, por ejemplo `[H5a] ¿Le informaron…?`. Las opciones se copian **exactamente** como aparecen aquí, porque `analisis/limpieza.py` las reconoce por su texto. Los códigos numéricos entre paréntesis no se muestran al participante.

## Registro de versiones

| Versión | Fecha | Cambios | Estado |
|---|---|---|---|
| 1.0 | 20-10-2026 | Cuestionario de seis dimensiones, sobre todo de opción única | Sustituida |
| 2.0 | 07-11-2026 | Enfoque cuantitativo: 46 preguntas (acceso 3, generales 4, hechos 16, Likert 23 en INF, CON, DER y CNF; 5 inversos) | Sustituida |
| 2.1 | 16-11-2026 | Filtro de Pichincha (P02); universidad (A5), modalidad (A6) y canal de difusión (A7); posgrado en A3; ítems de doble contenido separados (H5 → H5a/H5b; INF2 → INF2a/INF2b; INF5 → INF5a/INF5b); redacción de un solo contenido en CON3, CNF4 y CNF5; "No estoy seguro(a)" en H16. 52 preguntas (acceso 3, generales 7, hechos 17, Likert 25) | Sustituida |
| **2.2** | **25-11-2026** | Ámbito nacional: P02 (carrera de grado en el Ecuador), A5 con las 64 instituciones del CES y A8 región (opcional); DER8 (suspensión, art. 19) y DER9 (decisiones automatizadas, art. 20); H1 con condición migratoria e identidad de género o nombre social; P00 sin "anónima"; H3 de las hipótesis con H8. **55 preguntas** (acceso 3, generales 8, hechos 17, Likert 27) | **Vigente; se somete al juicio de expertos** |
| 2.3 | — | Ajustes del juicio de expertos (V de Aiken) | Por elaborar |
| Final | [PENDIENTE] | Ajustes de la prueba piloto (~30 estudiantes) | Por elaborar (~04-12-2026) |

## Configuración obligatoria del formulario (sin datos identificativos directos y difusión)

- **Un solo formulario en línea** para toda la recolección. La difusión es mixta: en línea (enlace en redes, mensajería y correo) y presencial (**código QR**) donde sea posible, en universidades de distintas provincias y regiones. El canal se registra con la pregunta opcional A7; si se prefiere, se pueden usar además enlaces prellenados distintos por canal.
- **Google Forms:** Configuración → Respuestas → *Recopilar direcciones de correo electrónico* = **No recopilar**; *Limitar a 1 respuesta* = **desactivado** (exige iniciar sesión); sin preguntas de carga de archivos.
- **Microsoft Forms:** *Quién puede responder* = **Cualquier persona puede responder**; *Registrar nombre* = desactivado.
- **Lógica de secciones:** si P00, P01 o P02 = "No", ir directamente a la sección final.
- **Likert:** cada ítem como pregunta independiente de tipo **Escala lineal 1–5** (o de opción única con las cinco etiquetas), no como cuadrícula.
- **Sin inicio de sesión, sin recopilar correos y sin carga de archivos** (OM-07). El proveedor del formulario (Google o Microsoft) es encargado del tratamiento y sus servidores pueden estar fuera del Ecuador: se informa en el consentimiento.
- Solo P00–P02 son obligatorias.
- Al cerrar: exportar a `.xlsx` → guardar como `analisis/datos/respuestas.xlsx` (excluido de git) → **eliminar las respuestas del servicio**.

Tiempo estimado: 13–15 minutos (55 preguntas).

---

## Sección 0. Consentimiento y filtros

*(Mostrar antes el texto de `encuesta/consentimiento_informado.md`.)*

- **[P00] ¿Acepta participar voluntariamente en esta encuesta, que no recoge datos que le identifiquen directamente?** Sí, acepto · No acepto → fin
- **[P01] ¿Tiene 18 años o más?** Sí · No → fin
- **[P02] ¿Estudia actualmente una carrera de grado en una universidad o escuela politécnica del Ecuador?** Sí · No → fin
  *(Ámbito nacional, OM-01. Reemplaza el filtro de Pichincha de la v2.1.)*

## Sección A. Datos generales (no identificativos)

> La universidad (A5) no permite identificar a nadie y se usa solo internamente, para ponderar el análisis. **Nunca se publica un resultado por universidad.**

- **[A1] Su universidad es:** Pública (1) · Particular cofinanciada (2) · Particular autofinanciada (3) · No lo sé (9)
- **[A2] Área de su carrera:** Educación · Artes y humanidades · Ciencias sociales, periodismo e información · Administración y derecho · Ciencias naturales, matemáticas y estadística · Tecnologías de la información y la comunicación · Ingeniería, industria y construcción · Agricultura, silvicultura, pesca y veterinaria · Salud y bienestar · Servicios
- **[A3] Semestre o nivel en el que se encuentra:** Nivelación o curso de admisión · 1.º a 3.er semestre · 4.º a 6.º semestre · 7.º semestre o superior · Posgrado (especialización, maestría o doctorado) (9)
  *El posgrado se excluye del análisis, porque la población es la matrícula de grado.*
- **[A4] Rango de edad:** 18 a 20 · 21 a 24 · 25 a 29 · 30 o más
- **[A5] ¿En qué universidad o escuela politécnica estudia?** Escuela Politécnica Nacional · Escuela Superior Politécnica Agropecuaria de Manabí Manuel Félix López (ESPAM MFL) · Escuela Superior Politécnica de Chimborazo · Escuela Superior Politécnica del Litoral (ESPOL) · Facultad Latinoamericana de Ciencias Sociales (FLACSO) · Instituto de Altos Estudios Nacionales (IAEN) · Pontificia Universidad Católica del Ecuador (PUCE) · Universidad Agraria del Ecuador · Universidad Andina Simón Bolívar · Universidad Bolivariana del Ecuador · Universidad Casa Grande · Universidad Católica de Cuenca · Universidad Católica de Santiago de Guayaquil (UCSG) · Universidad Central del Ecuador · Universidad de Cuenca · Universidad de Especialidades Espíritu Santo (UEES) · Universidad de Especialidades Turísticas · Universidad de Guayaquil · Universidad de Investigación de Tecnología Experimental Yachay · Universidad de las Américas (UDLA) · Universidad de las Artes · Universidad de las Fuerzas Armadas ESPE · Universidad de los Hemisferios · Universidad de Otavalo · Universidad de Seguridad Ciudadana y Ciencias Policiales (USECIPOL) · Universidad del Azuay · Universidad del Pacífico - Escuela de Negocios · Universidad del Río (UDR) · Universidad Estatal Amazónica · Universidad Estatal de Bolívar · Universidad Estatal de Milagro · Universidad Estatal del Sur de Manabí · Universidad Estatal Península de Santa Elena (UPSE) · Universidad Iberoamericana del Ecuador · Universidad Intercultural de las Nacionalidades y Pueblos Indígenas Amawtay Wasi · Universidad Internacional del Ecuador (UIDE) · Universidad Laica Eloy Alfaro de Manabí · Universidad Laica Vicente Rocafuerte de Guayaquil · Universidad Metropolitana · Universidad Nacional de Chimborazo · Universidad Nacional de Educación · Universidad Nacional de Loja · Universidad Particular Internacional SEK · Universidad Politécnica Estatal del Carchi · Universidad Politécnica Salesiana (UPS) · Universidad Pública de Santo Domingo de los Tsáchilas · Universidad Regional Amazónica Ikiam · Universidad Regional Autónoma de los Andes (UNIANDES) · Universidad San Francisco de Quito (USFQ) · Universidad San Gregorio de Portoviejo · Universidad Técnica de Ambato · Universidad Técnica de Babahoyo · Universidad Técnica de Cotopaxi · Universidad Técnica de Machala · Universidad Técnica de Manabí · Universidad Técnica del Norte · Universidad Técnica Estatal de Quevedo · Universidad Técnica Luis Vargas Torres de Esmeraldas · Universidad Técnica Particular de Loja (UTPL) · Universidad Tecnológica ECOTEC · Universidad Tecnológica Empresarial de Guayaquil · Universidad Tecnológica Indoamérica · Universidad Tecnológica Israel · Universidad UTE · Prefiero no responder (99)
  *Lista: las 64 instituciones de las listas del CES por sostenimiento (consulta del 16-11-2026), en orden alfabético y sin agrupar por sostenimiento. El código de opción es su posición en la lista (1 a 64). En la base de análisis, A5 se reemplaza por el código del censo y no se cruza con A3 (OM-07).*
- **[A6] Modalidad de su carrera:** Presencial · Semipresencial o híbrida · En línea
- **[A7] ¿Cómo se enteró de esta encuesta? (opcional)** Enlace en redes sociales o grupos de mensajería · Correo electrónico · Código QR en el campus · Invitación de un docente · Invitación de un compañero o amigo · Otro
- **[A8] Región del Ecuador en la que estudia (opcional):** Costa · Sierra · Amazonía · Galápagos
  *Dato descriptivo; los resultados por región solo se informan si cada grupo tiene al menos 5 respuestas.*

*Sostenimiento para el análisis:* si A5 identifica una universidad del censo, se usa su sostenimiento oficial; si no, el declarado en A1. Pública = 1; privada = 2 o 3. Quien responde "No lo sé" en A1 y no identifica su universidad en A5 se excluye de H1 y H3, y se informa cuántos son.

## Sección H. Preguntas de hechos

Opciones por defecto (H2, H4–H8, H12–H15): **Sí (1) · No (2) · No recuerdo (3)**.

- **[H1] Desde su postulación hasta hoy (admisión, matrícula, becas, bienestar, aula virtual u otros trámites), ¿qué datos le pidió su universidad?** *(Casillas: marque todas las que correspondan.)*
  Identificación (cédula, nombres, fecha de nacimiento) · Contacto (dirección, teléfono, correo personal) · Fotografía · Datos socioeconómicos del hogar · Datos de familiares o representantes · Datos de salud · Datos de discapacidad · Autoidentificación étnica · Condición migratoria · Identidad de género o nombre social · Datos biométricos (huella, reconocimiento facial) · Ubicación o geolocalización · Actividad en plataformas virtuales · No recuerdo
- **[H2]** ¿Su universidad le pidió su consentimiento (autorización) para tratar sus datos personales?
- **[H3]** *(Solo si H2 = Sí)* ¿De qué forma lo dio? De forma expresa (marcando una casilla o firmando) · De forma implícita ("al continuar, acepta…") · De forma verbal · No recuerdo
- **[H4]** Al entregar sus datos, ¿le informaron **para qué** se usarían?
- **[H5a]** ¿Le informaron **quién es el responsable** de sus datos?
- **[H5b]** ¿Le informaron **cómo contactar** al responsable de sus datos?
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
- **[H16]** ¿Sabe por qué canal (correo, formulario u oficina) puede ejercer sus derechos sobre sus datos en su universidad? Sí (1) · No (2) · No estoy seguro(a) (3)
  *"No estoy seguro(a)" se codifica 3 y cuenta como no afirmativo, igual que "No recuerdo"; su porcentaje se informa por separado.*

## Sección L. Escalas Likert

Escala para todos los ítems: **1 = Totalmente en desacuerdo · 2 = En desacuerdo · 3 = Ni de acuerdo ni en desacuerdo · 4 = De acuerdo · 5 = Totalmente de acuerdo**.
Los ítems marcados con **(R)** son **inversos**: un acuerdo alto indica una situación desfavorable. En el análisis se recodifican como x' = 6 − x antes de calcular la puntuación de la dimensión y la confiabilidad. En el formulario **no se marca** cuáles son inversos.

### Dimensión INF — Información recibida (7 ítems)
- **[INF1]** Mi universidad me explicó con claridad para qué usa mis datos personales.
- **[INF2a]** Sé quién es el responsable de mis datos en mi universidad.
- **[INF2b]** Sé cómo contactar al responsable de mis datos en mi universidad.
- **[INF3]** Mi universidad me informó cuánto tiempo conservará mis datos.
- **[INF4] (R)** No sé con quién comparte mi universidad mis datos personales.
- **[INF5a]** La política de privacidad de mi universidad es fácil de encontrar.
- **[INF5b]** La política de privacidad de mi universidad es fácil de entender.

### Dimensión CON — Consentimiento (5 ítems)
- **[CON1]** Mi universidad me pidió autorización antes de recoger mis datos personales.
- **[CON2]** Pude aceptar o rechazar por separado los usos de mis datos que no eran necesarios para estudiar.
- **[CON3] (R)** Sentí que estaba obligado(a) a entregar todos los datos que me pedían para poder estudiar.
- **[CON4]** Entendí lo que estaba aceptando cuando di mi autorización.
- **[CON5]** Sé que puedo retirar mi autorización cuando quiera.

### Dimensión DER — Conocimiento de derechos (9 ítems)
- **[DER1]** Sé que puedo pedir a mi universidad acceso a todos los datos que tiene de mí.
- **[DER2]** Sé que puedo pedir que corrijan o actualicen mis datos.
- **[DER3]** Sé que puedo pedir que eliminen mis datos cuando ya no sean necesarios.
- **[DER4]** Sé que puedo oponerme a ciertos usos de mis datos.
- **[DER5]** Sé que puedo pedir mis datos en un formato que me permita llevarlos a otra institución.
- **[DER6] (R)** No sabría ante quién reclamar si mi universidad usa mal mis datos.
- **[DER7]** Conozco la Ley Orgánica de Protección de Datos Personales.
- **[DER8]** Sé que puedo pedir que se suspenda el uso de mis datos mientras se revisa si son correctos. *(art. 19, suspensión del tratamiento)*
- **[DER9]** Sé que puedo pedir que una decisión sobre mí no se tome solo con un sistema automático. *(art. 20, decisiones automatizadas)*

### Dimensión CNF — Confianza y percepción de seguridad (6 ítems)
- **[CNF1]** Confío en que mi universidad protege adecuadamente mis datos personales.
- **[CNF2]** Creo que el personal de mi universidad accede solo a los datos que necesita para su función.
- **[CNF3] (R)** Me preocupa que mis datos personales se filtren desde los sistemas de mi universidad.
- **[CNF4]** Si mis datos se vieran afectados por un incidente de seguridad, mi universidad me lo comunicaría.
- **[CNF5]** Me sentiría seguro(a) entregando a mi universidad datos sensibles, como los de salud.
- **[CNF6] (R)** Mi universidad trata mis datos como si le pertenecieran a ella y no a mí.

---

### Sección final

Gracias por su participación. Sus respuestas no contienen datos que le identifiquen directamente y se usarán solo de forma agregada en un Trabajo de Integración Curricular; ningún resultado se publicará por universidad. Si tiene preguntas: ramonalejandromanzaba@gmail.com

*(En el piloto se añade una pregunta abierta: "¿Alguna pregunta le resultó confusa? ¿Cuál y por qué?". Se advierte no escribir datos que identifiquen a personas.)*

---

## Revisión de ítems de doble contenido (v2.0 → v2.1)

| v2.0 | Problema | v2.1 |
|---|---|---|
| H5 "quién es el responsable y cómo contactarlo" | Dos hechos | H5a (quién) y H5b (cómo contactarlo) |
| INF2 "Sé quién es el responsable … y cómo contactarlo" | Dos contenidos (decisión de la tutora: separar) | INF2a y INF2b |
| INF5 "fácil de encontrar y de entender" | Dos contenidos | INF5a (encontrar) e INF5b (entender) |
| CON3 "perdería la matrícula o un servicio" | Dos consecuencias | "Sentí que estaba obligado(a) a entregar todos los datos que me pedían para poder estudiar." |
| CNF4 "expuestos o robados" | Dos eventos | "Si mis datos se vieran afectados por un incidente de seguridad…" |
| CNF5 "datos de salud o discapacidad" | Dos categorías | "datos sensibles, como los de salud" |
| DER2 "corrijan o actualicen" | Se mantiene: la LOPDP los reúne en un solo derecho (rectificación y actualización, art. 14) | Sin cambio |
| CON2 "aceptar o rechazar por separado" | Se mantiene: es una sola acción (elegir) | Sin cambio |

## Recodificación de ítems inversos

| Ítem | Dimensión | Respuesta original → valor analizado |
|---|---|---|
| INF4, CON3, DER6, CNF3, CNF6 | INF, CON, DER, CNF | 1→5 · 2→4 · 3→3 · 4→2 · 5→1 (x' = 6 − x) |

Puntuación de cada dimensión = media de sus ítems ya recodificados. Se calcula solo si la persona respondió al menos el 80 % de los ítems de esa dimensión.

## Regla de "respuesta afirmativa" para los indicadores de hechos

| Indicador | Pregunta | Afirmativo | Fuera del denominador |
|---|---|---|---|
| IE01 | H1_01…H1_13 (y al menos una categoría especial o dato sensible: salud, discapacidad, etnia, condición migratoria, identidad de género o biometría) | casilla marcada | "No recuerdo" |
| IE02 | H9 | Sí | No me pidieron esos datos |
| IE03 / IE04a / IE04b / IE05 / IE06 | H4 / H5a / H5b / H6 / H7 | Sí | — |
| IE07 (descriptivo) | H2 (y H3 = expresa, entre quienes respondieron Sí) | Sí | — |
| IE08 (indicador de cumplimiento; H3 de las hipótesis) | H8 | Sí | — |
| IE11 | H16 (y H11 = Sí, con o sin respuesta) | Sí | — |
| IE12 | H15 | Sí | — |
| IE14 | H14, H13, H12 | Sí | — |
| IE15 | H10 | Sí | No uso esas plataformas |

"No recuerdo" (y "No estoy seguro(a)" en H16) cuenta como no afirmativo, igual que en el KR-20 (H4, H5a, H5b, H6 y H7): el titular que no recuerda haber sido informado no puede ejercer lo que no conoce. Cada porcentaje se informa **con y sin** "No recuerdo" en el denominador, y el porcentaje de "No recuerdo" por separado. Para la brecha del responsable (ID02), el afirmativo exige Sí en H5a y en H5b.


## Bases de legitimación (OM-03)

La mayoría de los tratamientos universitarios no se basan en el consentimiento, sino en la ejecución de medidas precontractuales o del contrato y en obligaciones legales (LOPDP, art. 7, nums. 2 y 5). Por eso **H2 (se pidió el consentimiento) e IE07 e IE09 son descriptivos**: muestran cómo se recoge el consentimiento, no si se cumple la ley. El indicador de cumplimiento es **IE08 (H8)**: si el estudiante pudo aceptar o rechazar por separado las finalidades no necesarias para el servicio educativo (difusión de imagen, publicidad), que son las que sí dependen del consentimiento.
