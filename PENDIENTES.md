# PENDIENTES — Lo que debe aportar o decidir el autor (por prioridad)

Corte: **2026-11-16** (retroalimentación v2: alcance Pichincha, reporte agregado, cuestionario v2.1). En el PDF, lo no verificable aparece como **`[PENDIENTE: …]` en rojo** (macro `\pend` de `main.tex`) y las celdas de resultados aún no medidos, como "---" con una nota. Al resolver un punto: reemplazar la marca, actualizar `CAMBIOS.md` y, si es una cifra, `FUENTES.md`. **La recolección empieza el 7-12-2026 solo si los puntos 1 y 2 están resueltos.**

| # | Qué | Dónde se usa | Cómo / fecha |
|---|---|---|---|
| **1** | **Enviar la solicitud de verificación ética esta semana.** Completar en `etica/solicitud_verificacion_etica.md` los nombres y cargos de la Coordinación de la carrera y de la Dirección de Investigación, la fecha y (si la carrera lo exige) la cédula; confirmar si la tutora firma. Adjuntar `jueces/cuestionario_v2.1.pdf` y `encuesta/consentimiento_informado.md`. **La recolección no inicia sin la respuesta documentada** (aval, exención o aprobación de un CEISH, con número de oficio y fecha) | Cap. 3 §Consideraciones éticas; Anexo "Aval o verificación ética"; consentimiento (Anexo C y `encuesta/consentimiento_informado.md`) | Envío: semana del 16-11-2026. Respuesta: antes del 04-12-2026 (PC2) |
| **2** | **Convocar a los jueces** (3 a 5; invitar a 6: protección de datos, seguridad, metodología). Enviar `jueces/correo_invitacion.md` (completar nombre del juez y fecha límite) con `cuestionario_v2.1.pdf`, `formato_juicio_expertos.xlsx` e `instrucciones_jueces.md`; asignar códigos E01… Guardar los formatos devueltos en `analisis/datos/jueces/E0n.xlsx` y correr `python analisis/run_all.py` | Cap. 4, Tabla de validez de contenido; versión 2.2 (Tabla de versiones); IV10 | Envío: 16–20-11-2026; plazo de 5 días; PC1 el 27-11-2026 |
| **3** | **Capturas de G*Power 3.1** de H1, H2 y H3 (análisis de sensibilidad) con los parámetros de `analisis/GPOWER_INSTRUCCIONES.md`; guardarlas en `Capítulos/fig/gpower_H1.png`, `gpower_H2.png`, `gpower_H3.png` | Cap. 3, Tabla de potencia (fuente) | Antes del PC1 |
| **4** | **Segundo observador independiente** para la confiabilidad del registro documental (nombre o código, fecha de la capacitación de 30 min y de su calificación ciega de 4 universidades). Generar su archivo con `node scripts/build_analisis_documental.js privado/analisis_documental_observador2.xlsx --observador2` | Cap. 3 §Confiabilidad del registro; Cap. 4, Tabla de kappa | 11 a 15-01-2027 |
| **5** | **Oficio N.º SPDP-IRD-2026-0221-O**: conseguir el texto (fecha, destinatario, contenido sobre gran escala) y su referencia para `referencias.bib`. Hoy solo se cita lo que indicó la tutora | Cap. 1 (contexto meso); Cap. 2 §2.3 y Tabla comparativa | Cuanto antes |
| 6 | **Aprobación de la tutora** del cambio de alcance (nacional → **Pichincha**; el título no cambia: se restauró el de `v2-antes-retro` el 16-11-2026), del objetivo general sin "y docentes", de los OE2 y OE3 y del cuestionario v2.1 | Cap. 1; `main.tex`; Resumen; Abstract; Anexo de consistencia | 20-11-2026 |
| 7 | **Sedes y extensiones en Pichincha** de universidades con matriz en otra provincia: confirmar con el CES o la SENESCYT (listado vigente, fecha de corte). Añadirlas a `privado/clave_universidades.xlsx` (U19…), a la pregunta A5 (`analisis/config.py`, Anexo B, `encuesta/cuestionario.md`) y recalcular ⌈0,2·U⌉ | Cap. 1 (Tabla de cifras); Cap. 3 §Población; Cap. 4; Anexo B | Antes del PC1 (cierre de la versión 2.2) |
| 8 | **Matrícula de grado de Pichincha (N)**, total y por sostenimiento, y número de universidades con matrícula de grado, de la base oficial del SIIES ("Base estadística de matrícula de UEP 2015–2023"; el archivo está en cloud-pro.senescyt.gob.ec, que no respondió el 07-11 ni el 16-11-2026). Con ella: aplicar la fórmula de referencia, ajustar la cuota pública/privada y explicar la diferencia con el censo | Cap. 1 (Tabla de cifras); Cap. 3 §Población, §Tamaño, §Muestreo | Antes del 07-12-2026 |
| 9 | Composición de la matrícula de Pichincha por área, nivel, edad, sostenimiento y modalidad (si el SIIES la publica), como `analisis/datos/siies_pichincha.csv` (`variable,categoria,pct_poblacion`) | Cap. 4, Tabla de composición | Antes del cierre de la encuesta |
| 10 | Crear el formulario anónimo (configuración de `encuesta/cuestionario.md`, P02 de Pichincha, A5–A7) y el **código QR**; planificar la difusión en varias universidades de Pichincha y con docentes de otras instituciones | Cap. 3 §Muestreo y difusión | 23 a 27-11-2026 |
| 11 | Prueba piloto (~30 estudiantes): tiempo, ajustes, alfa, omega, KR-20 → versión final del cuestionario e inserción en el Anexo B | Cap. 4, Tablas de ajustes y de confiabilidad; Anexo B (versión final) | 30-11 a 04-12-2026 (PC2) |
| 12 | Censo documental de las 18 universidades (+ sedes): 50 % al 11-12-2026 (PC3) y cierre al 08-01-2027, en `privado/analisis_documental.xlsx` | Cap. 4, Tablas documentales, ITD y sensibilidad | 23-11-2026 a 08-01-2027 |
| 13 | Encuesta: 384 válidas (423 brutas); revisión semanal de la composición; plan B el 08-01-2027; cierre el 22-01-2027 (PC4) | Cap. 4 | 07-12-2026 a 22-01-2027 |
| 14 | Análisis con datos reales (`python analisis/run_all.py`), verificación cruzada en jamovi o JASP, AFE, brechas ponderadas y redacción dato → prueba → interpretación | Caps. 4 y 6; Resumen; Abstract | 25-01 a 05-02-2027 |
| 15 | Perfil de la universidad tipo con valores agregados del censo y del SIIES (mediana de matrícula, modalidad, proporciones IE01, ID13, H10) | Cap. 5, Tabla de la universidad tipo | Al cerrar el censo y la encuesta |
| 16 | Panel Delphi (≥ 5; invitar a 7–8) y juicio de expertos V2 (≥ 5, **al menos 2 fuera del Delphi**): códigos, perfiles, K, Brier, rondas, V01–V12 | Cap. 5, Tablas del panel, Delphi y juicio; IV06–IV09 | 04-01 a 19-02-2027 |
| 17 | Fechas de la versión 2.2 y de la versión final en la Tabla de registro de versiones | Cap. 3 | 26-11 y 04-12-2026 |

## Datos oficiales por confirmar (vigentes de la lista anterior)

| # | Dato | Fuente sugerida |
|---|---|---|
| 18 | Número oficial de DPD registrados ante la SPDP en 2026 y por sector | Solicitud de acceso a la información pública a la SPDP |
| 19 | Vulneraciones notificadas a la SPDP por el sector educativo | Solicitud a la SPDP (LOPDP art. 76 num. 14) |
| 20 | Criterios y niveles de clasificación de la Res. SPDP-SPD-2026-0040-R en el texto oficial (RO 1S 376) | Registro Oficial |
| 21 | Perú: supuestos del oficial de datos, tope de multas y edad de consentimiento (D.S. 016-2024-JUS) | El Peruano |
| 22 | Fecha exacta de la Res. SPDP-SPD-2025-0028-R | spdp.gob.ec |

## Preliminares

| # | Qué | Dónde |
|---|---|---|
| 23 | Revisar la dedicatoria y el agradecimiento | `Preliminares/05`, `06` |
| 24 | Fechas de firma (día y mes) | `Preliminares/01`–`04` |
| 25 | Volver a importar `planificacion/Planificacion_Jira.csv` en Jira (versión del 16-11-2026; el Gantt ya se regeneró) | `planificacion/` |
