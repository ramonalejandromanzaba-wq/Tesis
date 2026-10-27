    # Indicaciones de revisión — ITI-TFG-B26-0021

Actúa como coautor técnico y revisor metodológico de mi Trabajo de Integración Curricular (ITI-TFG-B26-0021, Universidad Tecnológica Indoamérica, período B26):
"Metodología para el diagnóstico y gestión de riesgos en el tratamiento de datos personales académicos conforme a la LOPDP".
Caso de estudio: proceso de admisión y matrícula de la UTI, sede Quito. Documento en LaTeX, citación IEEE. Todo el contenido en español académico formal.

Trabaja de forma autónoma, sin pedirme confirmación en cada paso. Solo detente si necesitas datos que únicamente yo puedo aportar (ver REGLA DE INTEGRIDAD).

---

## AUTORIZACIÓN EXPRESA DEL AUTOR

- **Autorizo reducir los objetivos específicos de 5 a 4**, por indicación de la tutora (María Cristina Jiménez Hernández, MSc.) en la revisión del 27/10/2026 (ver C7–C11).
- Esta autorización prevalece sobre la regla de CLAUDE.md / CLAUDEs.md que prohíbe reformular sin autorización, **solo para los objetivos específicos y todo lo que dependa de ellos** (Cap. 1, tabla de trazabilidad, Cap. 2–4, conclusiones, resumen/abstract, matriz de consistencia).
- Redacta tú los 4 objetivos específicos según 4.2, déjalos en PLAN_REVISION.md y aplícalos sin esperar mi aprobación.
- Reasigna en la tabla de trazabilidad los capítulos del antiguo OE5 a la nueva estructura de 4 objetivos.
- El **objetivo general NO se toca**.

---

## CONTEXTO PREVIO (leer antes de cualquier acción)

- Lee TODOS los archivos CLAUDE.md / CLAUDEs.md del proyecto: el de la raíz, el de la carpeta superior, los de subcarpetas y el global de usuario (~/.claude/CLAUDE.md) si existe.
- Respeta sus convenciones (estructura de carpetas, comandos de compilación, estilo de redacción, formato IEEE, reglas del .bib, nombres de archivos, plantilla UTI).
- Si una instrucción de CLAUDE.md contradice este documento, prevalece este documento, excepto en convenciones técnicas de compilación y estructura del repositorio, donde prevalece CLAUDE.md.
- Resume en PLAN_REVISION.md qué contexto relevante obtuviste de cada CLAUDE.md.

---

## 0. PREPARACIÓN (obligatorio antes de editar)

1. Explora el repositorio: archivo principal .tex, capítulos, .bib, preámbulo, figuras, tablas y el .xlsx.
2. Crea una rama git `revision-tribunal` (o, si no hay git, una copia de respaldo `backup_AAAAMMDD/`).
3. Compila con latexmk para confirmar que el estado inicial compila. Anota errores previos.
4. Genera `PLAN_REVISION.md` con: contexto obtenido de los CLAUDE.md, los 4 objetivos específicos redactados, mapa del documento, ubicación exacta de cada cambio y orden de ejecución. Luego ejecuta el plan sin esperar aprobación.

---

## 1. RESTRICCIÓN ABSOLUTA

- NO modifiques el OBJETIVO GENERAL: ni una palabra, ni puntuación. Localízalo y déjalo intacto.
- Todo lo demás sí puede y debe mejorarse.
- NINGUNA de las indicaciones de la sección 2 puede omitirse. Todas son obligatorias.

---

## 2. INDICACIONES OBLIGATORIAS (texto original, no omitir ninguna)

### 2.A Tabla de prioridades

- **[A1 – Alta]** Verificar en las fuentes oficiales los plazos de 72 horas y cinco días, cuándo comienzan a correr y quiénes son sujetos obligados; citar artículos concretos.
- **[A2 – Alta]** Respaldar el planteamiento del problema con datos o estudios.
- **[A3 – Alta]** Incluir la fase de preparación en la metodología y mostrar la equivalencia con ISO/IEC 27035 y NIST.
- **[A4 – Alta]** Definir la institución del caso de estudio y confirmar su participación.
- **[A5 – Media]** Incorporar SISPDP, la clasificación de vulneraciones y la comunicación a titulares.
- **[A6 – Media]** Reforzar la validación: dos escenarios, metas por indicador y juicio de expertos.
- **[A7 – Media]** Ajustar los verbos de los objetivos y acortar el objetivo general.
  → EXCEPCIÓN: el objetivo general NO se modifica. Solo se ajustan los verbos de los objetivos específicos.
- **[A8 – Baja]** Corregir guiones, numeración, formato de referencias y ampliar bibliografía.

### 2.B Observaciones del tribunal

- **[B1]** Completar la aplicación de la metodología: presentar los resultados del diagnóstico institucional, la identificación de escenarios de riesgo y la matriz correspondiente, diferenciando los riesgos inherentes de los residuales.
- **[B2]** Completar la validación: incorporar los resultados de la aplicación del método Delphi, la calibración de los expertos y el juicio de expertos. Las conclusiones sobre la validez de la propuesta deben sustentarse en evidencia documentada.
- **[B3]** Justificar las estimaciones: explicar los criterios empleados para asignar probabilidad e impacto, las fuentes de información utilizadas y las reglas aplicadas para determinar los niveles de riesgo y su aceptación.
- **[B4]** Demostrar la trazabilidad: relacionar los escenarios identificados con los requisitos normativos, los controles propuestos, los responsables, los plazos y los mecanismos de seguimiento.
- **[B5]** Diferenciar las pruebas técnicas de la validación metodológica: el funcionamiento correcto de las fórmulas y de la plantilla constituye una evidencia importante, pero debe complementarse con resultados de su aplicación y evaluación por expertos.
- **[B6]** Fortalecer las conclusiones: responder explícitamente a cada objetivo específico, utilizando resultados verificables y evitando generalizaciones que excedan el alcance del caso de estudio.
- **[B7]** Revisar la consistencia formal: completar los apartados preliminares y los elementos pendientes del documento, verificar la correspondencia entre objetivos, metodología, resultados y conclusiones, y comprobar la vigencia y pertinencia de las referencias normativas.

### 2.C Indicaciones de la tutora (27/10/2026)

- **[C1]** En la justificación faltan valores numéricos.
- **[C2]** Por ejemplo: cuántas escuelas y guarderías hay en el Ecuador.
- **[C3]** Todas, según la ley, tienen la obligación de protección de datos.
- **[C4]** Cuántos delegados de protección de datos acreditados hay.
- **[C5]** Ver si hay estadísticas.
- **[C6]** Informe de universidades que hayan implementado (porcentaje).
- **[C7]** Objetivo específico 1: saber bien qué se necesita para hacer el diagnóstico (determinarlo con precisión).
- **[C8]** Objetivo específico 2: universidades.
- **[C9]** Objetivo específico 3: implementar.
- **[C10]** Solo 4 objetivos específicos.
- **[C11]** Objetivo específico 4: evaluar.
- **[C12]** Definir fechas: todo dato "hasta la fecha", con fecha de corte explícita.
- **[C13]** Definir términos legales en la fundamentación (qué es el delegado de protección de datos, etc.).
- **[C14]** Contraste con otros países.
- **[C15]** Cómo funciona una ley.
- **[C16]** En el Ecuador, en qué etapa estamos.

---

## 3. REGLA DE INTEGRIDAD ACADÉMICA (no negociable)

- NUNCA inventes datos, estadísticas, artículos de ley, plazos, resultados del diagnóstico, respuestas de expertos, puntajes Delphi ni referencias.
- Toda cifra debe tener fuente oficial verificable (usa WebSearch/WebFetch) y FECHA DE CORTE explícita ("según [fuente], con corte a [mes año]...").
- Si un dato no se encuentra en fuente oficial, inserta en el .tex: `\textcolor{red}{[PENDIENTE: descripción del dato y fuente sugerida]}` y regístralo en PENDIENTES.md.
- Los resultados empíricos (diagnóstico real, matriz con valores reales, rondas Delphi, juicio de expertos) solo pueden escribirse si existen en el repositorio. Si no existen, construye la estructura completa (tablas, instrumentos, fórmulas, criterios) con marcadores [PENDIENTE] para que yo cargue los datos reales.
- Prioriza fuentes: Registro Oficial / texto oficial de la LOPDP y su Reglamento, Superintendencia de Protección de Datos Personales (SPDP), MINEDUC (AMIE / datos abiertos), MIES, SENESCYT, CES, CACES, INEC; normas ISO/IEC y NIST; artículos indexados (Scopus/WoS, preferible últimos 5 años).

---

## 4. CAMBIOS POR SECCIÓN

### 4.1 Planteamiento del problema y justificación [A2, C1–C6, C12]

Respaldar con valores numéricos y fecha de corte:
- Número de instituciones educativas en Ecuador por nivel: guarderías/centros de desarrollo infantil, escuelas y colegios (fiscales, fiscomisionales, municipales, particulares), institutos superiores y universidades/escuelas politécnicas.
- Argumentar con base legal que todas, según la LOPDP, tienen obligación de proteger datos personales (citar artículos de ámbito de aplicación y sujetos obligados).
- Número de Delegados de Protección de Datos acreditados/registrados ante la SPDP.
- Estadísticas disponibles: incidentes o vulneraciones reportadas, sanciones, registros ante la SPDP.
- Informes sobre universidades que han implementado la LOPDP, con porcentaje si existe.
- Estudios nacionales/regionales sobre madurez en protección de datos en el sector educativo.
- Cierra con la brecha que la tesis atiende, sustentada en esas cifras.

### 4.2 Objetivos específicos — exactamente 4 [A7, C7–C11]

Mantén el objetivo general intacto. Redacta 4 objetivos específicos, con verbo en infinitivo según taxonomía de Bloom, medibles y alineados al objetivo general, respetando este orden y contenido:

- **OE1 – DIAGNÓSTICO:** determinar con precisión qué se necesita para realizar el diagnóstico (requisitos LOPDP aplicables, información, instrumentos, fuentes, actores, inventario de tratamientos y flujos de datos del proceso de admisión y matrícula, controles existentes) y realizarlo. Genera además REQUISITOS_DIAGNOSTICO.md con la lista concreta de lo que se necesita para ejecutar el diagnóstico y qué debo conseguir yo.
- **OE2 – UNIVERSIDADES:** centrado en las universidades (situación de implementación de la protección de datos en universidades, incluido el porcentaje que ha implementado si existe dato, y referentes nacionales e internacionales como insumo para la metodología).
- **OE3 – IMPLEMENTAR:** implementar la metodología en el caso de estudio (identificación de escenarios, matriz de riesgos inherente/residual, plan de tratamiento).
- **OE4 – EVALUAR:** evaluar la metodología (Delphi, calibración de expertos, juicio de expertos, indicadores con metas).

Actualiza en todo el documento las referencias a los objetivos anteriores (Cap. 1, tabla de trazabilidad, metodología, resultados, conclusiones, matriz de consistencia, resumen/abstract, .xlsx si los menciona).

### 4.3 Fundamentación teórica y legal [C12–C16]

- Definir términos legales con cita al artículo exacto de la LOPDP: Delegado de Protección de Datos (qué es, funciones, cuándo es obligatorio, requisitos), titular, dato personal, dato sensible, datos de niñas, niños y adolescentes, tratamiento, responsable, encargado, vulneración de seguridad, Autoridad de Protección de Datos.
- Cómo funciona una ley en Ecuador: jerarquía normativa (Constitución art. 425), ley orgánica, reglamento, normativa secundaria/resoluciones de la SPDP, entrada en vigencia y régimen transitorio.
- En qué etapa está Ecuador hasta la fecha: cronología verificada (publicación de la LOPDP, vigencia del régimen sancionatorio, Reglamento General, creación y designación de la SPDP, normativa secundaria emitida, estado del SISPDP). Fecha de corte explícita.
- Contraste con otros países en tabla comparativa: RGPD (UE/España), Colombia, Perú, Chile, Brasil (LGPD) y Ecuador. Criterios: año, autoridad, DPD obligatorio, plazo de notificación de vulneraciones, sanciones, régimen para datos de menores/educación.

### 4.4 Plazos y gestión de vulneraciones [A1, A5]

- Verificar en fuente oficial los plazos de 72 horas y cinco días: a quién se notifica, cuándo comienzan a correr, quiénes son sujetos obligados. Citar artículos concretos de la LOPDP y su Reglamento. Si la verificación contradice el documento, corrige y anótalo en CAMBIOS.md.
- Incorporar el SISPDP, la clasificación de vulneraciones y la comunicación a los titulares (cuándo, contenido mínimo, excepciones).

### 4.5 Metodología [A3, A4, B3]

- Incluir fase de preparación explícita.
- Tabla de equivalencia de fases entre la metodología propuesta, ISO/IEC 27035 (partes vigentes) y NIST SP 800-61 (verificar revisión vigente). Complementar con ISO/IEC 27005 / ISO 31000.
- Institución del caso de estudio ya definida (UTI, sede Quito, proceso de admisión y matrícula). La autorización formal de la UTI va como anexo; mientras no esté en el repo → [PENDIENTE], primera prioridad en PENDIENTES.md.
- Justificar las estimaciones: criterios para probabilidad e impacto (escalas con descriptores), fuentes de información, fórmula del nivel de riesgo, reglas de clasificación y criterios de aceptación.

### 4.6 Resultados – implementación [B1, B4]

- Resultados del diagnóstico institucional.
- Identificación de escenarios de riesgo.
- Matriz de riesgos diferenciando riesgo inherente y residual.
- Trazabilidad: escenario → requisito normativo (artículo) → control propuesto → responsable → plazo → mecanismo de seguimiento.

### 4.7 Evaluación / validación [A6, B2, B5]

- Separar en secciones distintas: (a) pruebas técnicas de la plantilla y fórmulas, (b) validación metodológica.
- Dos escenarios de validación.
- Metas por indicador (tabla: indicador, fórmula, meta, resultado, cumple/no cumple).
- Método Delphi: perfil y selección de expertos, calibración (coeficiente de competencia K = ½(Kc + Ka)), rondas, criterio de consenso (Kendall, IQR o % de acuerdo), resultados por ronda.
- Juicio de expertos: instrumento, criterios (pertinencia, claridad, suficiencia, coherencia), resultados (p. ej. V de Aiken).
- Sin datos reales en el repo: instrumentos como anexos y resultados [PENDIENTE]. La validez solo se afirma con evidencia documentada.

### 4.8 Conclusiones y recomendaciones [B6]

- Una conclusión por cada objetivo específico (OE1–OE4), con resultado verificable.
- Sin generalizaciones fuera del caso de estudio; declarar limitaciones.
- Recomendaciones derivadas de los resultados y trabajo futuro.

### 4.9 Consistencia formal [A8, B7]

- Completar apartados preliminares y elementos pendientes (resumen/abstract, índices, listas de tablas y figuras, siglas).
- Matriz de consistencia: problema – objetivos – metodología – resultados – conclusiones.
- Corregir guiones (– vs - vs —), numeración de tablas/figuras/ecuaciones, referencias cruzadas \label/\ref.
- Formato IEEE en todo el .bib; verificar vigencia de normas (ediciones actuales ISO/IEC y NIST).
- Ampliar bibliografía con fuentes de calidad; ninguna referencia sin verificar que existe.

---

## 5. CIERRE

1. Compila con latexmk hasta 0 errores y sin referencias indefinidas.
2. Entrega:
   - **CAMBIOS.md:** checklist con TODAS las indicaciones A1–A8, B1–B7 y C1–C16. Para cada una: estado (✔ atendida / ⚠ parcial / ✘ pendiente), qué se hizo, ubicación (archivo y sección) y fuente. No puede quedar ninguna sin fila.
   - **PENDIENTES.md:** todo dato que debo aportar yo, ordenado por prioridad (primero la autorización formal de la UTI).
   - **FUENTES.md:** cada cifra/artículo con URL oficial y fecha de consulta.
   - **REQUISITOS_DIAGNOSTICO.md:** lo que se necesita para ejecutar el diagnóstico (OE1).
3. Actualiza CLAUDE.md / CLAUDEs.md (y su copia en la carpeta superior, manteniéndolas idénticas) con los cambios estructurales: 4 objetivos específicos nuevos, nueva trazabilidad, secciones y anexos añadidos, archivos de control.
4. Commit en la rama `revision-tribunal` con mensaje descriptivo.
5. Resume en consola qué quedó completo y qué depende de mí.
