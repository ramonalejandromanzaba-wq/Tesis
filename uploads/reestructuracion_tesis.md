# Reestructuración de la tesis — ITI-TFG-B26-0021

Actúa como coautor técnico y metodólogo de investigación de mi Trabajo de Integración Curricular (ITI-TFG-B26-0021, Universidad Tecnológica Indoamérica). Documento en LaTeX, citación IEEE, español académico formal.

Trabaja de forma autónoma, sin pedirme confirmación en cada paso. Solo detente si necesitas datos que únicamente yo puedo aportar.

---

## 0. MOTIVO DEL CAMBIO (leer primero)

- **Se elimina el caso de estudio** (proceso de admisión y matrícula de la UTI). No es viable: la universidad no dará acceso a sus datos internos.
- La tesis pasa a ser una **investigación más amplia**, basada en:
  1. **Información pública** de las universidades ecuatorianas (lo que cualquiera puede consultar en sus sitios web y documentos oficiales).
  2. **Encuestas a estudiantes universitarios**, únicamente estudiantes, sobre qué datos personales les pidieron sus universidades, si fueron informados, si estuvieron de acuerdo y si conocen sus derechos.
- No se usa ningún dato interno de ninguna universidad.
- Plazo real: el trabajo se ejecuta entre **noviembre de 2026 y febrero de 2027**. Todo el diseño debe caber en ese tiempo.

---

## 1. CONTEXTO PREVIO

- Lee TODOS los CLAUDE.md / CLAUDEs.md (raíz, carpeta superior, subcarpetas, ~/.claude/CLAUDE.md).
- Lee `uploads/indicaciones_revision.md`, `CAMBIOS.md`, `PENDIENTES.md`, `FUENTES.md` y `REQUISITOS_DIAGNOSTICO.md` si existen.
- **Autorizo expresamente** cambiar el esquema completo, incluidos el título, el objetivo general y los objetivos específicos. Esta autorización prevalece sobre cualquier regla de CLAUDE.md que prohíba reformular.
- Respeta las convenciones técnicas de CLAUDE.md (compilación, estructura, plantilla UTI, formato IEEE).

---

## 2. PREPARACIÓN

1. Crea la rama git `reestructuracion-sin-caso` desde el estado actual (o un respaldo `backup_AAAAMMDD/` si no hay git).
2. Compila con latexmk y anota el estado inicial.
3. Genera `PLAN_REESTRUCTURACION.md` con: qué se conserva, qué se elimina, qué se crea, el nuevo esquema de capítulos y el orden de ejecución. Luego ejecútalo sin esperar aprobación.

---

## 3. QUÉ SE CONSERVA, QUÉ SE ELIMINA

**Se conserva y se adapta (de `indicaciones_revision.md`):**
- Justificación con cifras y fecha de corte (C1–C6, C12): número de instituciones educativas por nivel, DPD acreditados, estadísticas de la SPDP, universidades que han implementado la LOPDP (porcentaje).
- Fundamentación legal (C13–C16): definiciones con artículo exacto (DPD, titular, responsable, encargado, consentimiento, dato sensible, datos de menores, vulneración), cómo funciona una ley en Ecuador, en qué etapa está Ecuador, contraste con otros países.
- Plazos de 72 horas / cinco días, SISPDP, clasificación de vulneraciones y comunicación a titulares (A1, A5).
- Equivalencia con ISO/IEC 27035, NIST SP 800-61, ISO/IEC 27005 / ISO 31000 (A3), ahora como marco de referencia, no como aplicación a una institución.
- Validación por expertos: Delphi, calibración (K = ½(Kc + Ka)), juicio de expertos, V de Aiken (A6, B2, B5).
- Consistencia formal, IEEE y bibliografía (A8, B7).
- La estructura de 4 objetivos específicos indicada por la tutora (diagnóstico → universidades → implementar → evaluar), reinterpretada como se indica en la sección 4.

**Se elimina o se reemplaza:**
- Todo lo referido al caso de estudio de la UTI: diagnóstico institucional interno, flujos internos de admisión y matrícula, matriz de riesgos con datos internos, carta de aval institucional (A4, B1, y B4 en su versión institucional).
- Mueve el material eliminado a `descartado/caso_estudio/`, no lo borres.
- Si la metodología de riesgos y la plantilla .xlsx ya desarrolladas son útiles, **reutilízalas como propuesta** (ver OE4), aplicadas a escenarios construidos a partir de los hallazgos, no a datos internos.

---

## 4. NUEVO ENFOQUE

### 4.1 Tipo de investigación
- Enfoque mixto, con predominio cuantitativo; alcance descriptivo-exploratorio; diseño no experimental, transversal.
- Dos fuentes de datos, ambas legítimas y accesibles:
  - **Análisis documental** de información pública de universidades.
  - **Encuesta** a estudiantes universitarios.

### 4.2 Título y objetivo general (nuevos)
- Propón 3 alternativas de título y 3 de objetivo general coherentes con el nuevo enfoque (sin caso de estudio, centrado en universidades ecuatorianas y en la percepción de los estudiantes como titulares de datos).
- Elige la mejor, justifica la elección en PLAN_REESTRUCTURACION.md y aplícala.
- Regístrala en PENDIENTES.md como **"requiere aprobación de la tutora"** (prioridad 1).

### 4.3 Objetivos específicos (exactamente 4, verbos Bloom, medibles)
- **OE1 – DIAGNÓSTICO:** determinar los requisitos de la LOPDP y su Reglamento aplicables a las universidades en el tratamiento de datos de estudiantes, y traducirlos en indicadores verificables (base para la ficha documental y la encuesta).
- **OE2 – UNIVERSIDADES:** analizar la información pública de las universidades ecuatorianas sobre protección de datos (políticas de privacidad, avisos, formularios de consentimiento, designación pública del DPD, canales para ejercer derechos, mención de la LOPDP, uso de cookies), con fecha de corte.
- **OE3 – IMPLEMENTAR:** aplicar una encuesta a estudiantes universitarios sobre los datos que les fueron solicitados, la información recibida sobre su finalidad, su consentimiento y el conocimiento de sus derechos.
- **OE4 – EVALUAR:** evaluar el nivel de cumplimiento y la brecha entre la norma, lo que las universidades publican y lo que perciben los estudiantes, y proponer lineamientos o una guía de gestión de riesgos, validada por expertos.

Actualiza todas las referencias a objetivos en el documento.

### 4.4 Componente documental (OE2)
- Población: universidades y escuelas politécnicas del Ecuador según el registro oficial vigente (CES / SENESCYT). Cita la fuente y la fecha de corte.
- Define la muestra (todas o un subconjunto justificado; p. ej., públicas y privadas de Pichincha o una muestra nacional estratificada).
- Ficha de verificación con indicadores derivados de OE1 (sí / no / parcial, con URL de evidencia y fecha de consulta).
- Guarda la ficha como anexo y una plantilla `analisis_documental.xlsx` para registrar resultados.
- No inventes resultados: deja la estructura lista y, si puedes verificar sitios con WebFetch, registra solo lo comprobado, con URL y fecha.

### 4.5 Encuesta a estudiantes (OE3)
- **Población:** estudiantes universitarios en Ecuador, o en Quito/Pichincha si es más viable (justifica con cifras oficiales de matrícula de SENESCYT/SIIES y fecha de corte).
- **Muestra:** fórmula de población finita (95 % de confianza, 5 % de error, p = q = 0,5); calcula el tamaño de muestra y declara el tipo de muestreo y sus limitaciones (si es no probabilístico, dilo y limita las generalizaciones).
- **Instrumento:** cuestionario estructurado (escala Likert y preguntas cerradas), organizado en dimensiones:
  1. Datos demográficos mínimos, no identificativos (tipo de universidad, área, semestre, rango de edad).
  2. Datos solicitados por la universidad (identificación, contacto, socioeconómicos, salud, discapacidad, biometría, fotografía, datos de familiares, datos en plataformas virtuales).
  3. Información recibida (finalidad, responsable, tiempo de conservación, terceros).
  4. Consentimiento (si se pidió, cómo, si fue libre, si pudieron negarse).
  5. Conocimiento de derechos (acceso, rectificación, eliminación, oposición, portabilidad) y de la LOPDP / SPDP.
  6. Percepción de seguridad, confianza e incidentes percibidos.
- Cada pregunta debe trazarse a un indicador de OE1 y a un artículo de la LOPDP (tabla en el documento).
- **Validación del instrumento:** juicio de expertos (V de Aiken), prueba piloto y confiabilidad (alfa de Cronbach). Deja los resultados como [PENDIENTE] hasta que yo cargue datos reales.
- **Plan de análisis:** estadística descriptiva, tablas cruzadas y chi-cuadrado (p. ej., pública vs. privada), con el software que declares (Excel, SPSS, R o Python). Deja listos los scripts o plantillas.
- **Entregables:** `encuesta/cuestionario.md` (texto listo para pasar a Google Forms o Microsoft Forms), `encuesta/consentimiento_informado.md`, `encuesta/plan_analisis.md`.

### 4.6 Ética y protección de datos de la propia encuesta (obligatorio)
- Encuesta **anónima**: no se piden nombre, cédula, correo, número de matrícula ni IP.
- Consentimiento informado al inicio, con finalidad, responsable (el autor), uso exclusivamente académico, voluntariedad y derecho a abandonar; si no acepta, la encuesta termina.
- Pregunta filtro: solo mayores de 18 años.
- Minimización, almacenamiento seguro y plazo de eliminación de las respuestas.
- Añade un apartado de consideraciones éticas en la metodología y regístralo en PENDIENTES.md: verificar si la UTI exige aprobación de un comité de ética o de la carrera, y cómo se difundirá la encuesta (canales propios vs. institucionales).

### 4.7 Propuesta (OE4)
- Con base en las brechas encontradas, propone lineamientos o una guía de gestión de riesgos para el tratamiento de datos de estudiantes en universidades, reutilizando la metodología y la plantilla existentes.
- Aplícala a escenarios construidos con los hallazgos (no a datos internos de ninguna institución).
- Valídala con Delphi y juicio de expertos; resultados [PENDIENTE] hasta tener datos reales.

### 4.8 Cronograma
- Incluye un cronograma realista de noviembre de 2026 a febrero de 2027: validación del instrumento, piloto, recolección, análisis documental, análisis estadístico, validación con expertos, redacción final y revisión con la tutora.

---

## 5. NUEVO ESQUEMA DEL DOCUMENTO

Ajusta los capítulos a la plantilla UTI, por ejemplo:
1. Introducción: problema con cifras, justificación, objetivos, alcance y limitaciones.
2. Fundamentación teórica y legal: definiciones, cómo funciona una ley, etapa en Ecuador, contraste internacional, marcos ISO/NIST, antecedentes investigativos en universidades.
3. Metodología: enfoque, población y muestra, instrumentos, validación, procedimiento, ética, plan de análisis, cronograma.
4. Resultados: análisis documental, resultados de la encuesta, brechas.
5. Propuesta y validación.
6. Conclusiones (una por objetivo específico) y recomendaciones.

Actualiza la tabla de trazabilidad: objetivo → capítulo → instrumento → indicador → evidencia.

---

## 6. REGLA DE INTEGRIDAD ACADÉMICA (no negociable)

- NUNCA inventes datos, respuestas de encuestas, porcentajes, resultados del análisis documental, opiniones de expertos, artículos de ley ni referencias.
- Toda cifra con fuente oficial verificable y fecha de corte.
- Lo que no puedas verificar va como `\textcolor{red}{[PENDIENTE: ...]}` y en PENDIENTES.md.
- Fuentes prioritarias: Registro Oficial / LOPDP y Reglamento, SPDP, CES, SENESCYT/SIIES, CACES, INEC, MINEDUC, MIES; normas ISO/IEC y NIST; artículos indexados (Scopus/WoS, últimos 5 años preferentemente), incluidos estudios sobre percepción de privacidad en estudiantes universitarios.

---

## 7. CIERRE

1. Compila con latexmk hasta 0 errores y sin referencias indefinidas.
2. Actualiza o genera:
   - **CAMBIOS.md:** qué cambió y por qué (sección "Reestructuración sin caso de estudio"); para las indicaciones A1–A8, B1–B7 y C1–C16 marca si siguen vigentes, si se adaptaron o si quedaron obsoletas por el cambio de enfoque.
   - **PENDIENTES.md:** prioridad 1, aprobación del nuevo título y objetivos por la tutora; luego ética y difusión de la encuesta, expertos y datos por recolectar.
   - **FUENTES.md:** cada cifra con URL y fecha de consulta.
   - Carpeta `encuesta/` y `analisis_documental.xlsx`.
3. Actualiza CLAUDE.md / CLAUDEs.md (y su copia en la carpeta superior, idénticas) con el nuevo enfoque: sin caso de estudio, nuevos objetivos, nuevo esquema y nuevos archivos.
4. Commit en `reestructuracion-sin-caso` con mensaje descriptivo.
5. Resume en consola qué quedó listo y qué depende de mí.
