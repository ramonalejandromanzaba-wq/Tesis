# INSTRUCCIONES DE REVISIÓN — Observaciones Tesis v3

> **Archivo de instrucciones para Claude Code (Antigravity CMD).**
> Pegar completo como prompt o colocarlo en `uploads/` del repositorio de la tesis.

---

## REGLAS GLOBALES (leer antes de hacer cualquier cambio)

1. **EL TÍTULO NO SE MODIFICA.** El título de la tesis es: *"Metodología para el diagnóstico y gestión de riesgos en el tratamiento de datos personales académicos conforme a la LOPDP"*. No se cambia bajo ninguna circunstancia.
2. **Resultados siempre agregados.** Ninguna universidad se nombra individualmente en los resultados. Solo se reporta por sostenimiento (público/privado) y, opcionalmente, por región si hay ≥5 respuestas por grupo.
3. **No es un caso de estudio.** La tesis es una investigación general. No se pide acceso a datos internos ni reuniones con autoridades universitarias.
4. **Encuesta solo a estudiantes mayores de 18 años.**
5. **El producto es la metodología**, no el diagnóstico de una universidad en particular.
6. **Fecha de corte normativa única:** 16 de noviembre de 2026 (ver OM-02).
7. **Cada cambio debe preservar la coherencia interna:** si se modifica un indicador, actualizar también las tablas, hipótesis, escenarios y anexos que lo referencian.
8. **Los ejemplos de redacción y tablas del documento de observaciones son propuestas.** Contrastarlas con el texto oficial de la norma antes de incorporarlas.
9. Lee los archivos `CLAUDE.md` del repositorio antes de empezar.

---

## RESUMEN DE OBSERVACIONES

| ID | Tema | Tipo | Páginas afectadas |
|----|------|------|-------------------|
| OM-01 | Evidencia empírica nacional; metodología aplicable por cualquier universidad | Mayor | xviii, 24-25, 29, 31-33, 53, 57-63, 84, 88-109 |
| OM-02 | Fecha de corte normativa única | Mayor | xviii, 23, 29, 33, 37, 41 |
| OM-03 | Bases de legitimación: el consentimiento no es la base de todo | Mayor | 35, 57, 65, 71, 98 |
| OM-04 | Derechos faltantes: suspensión (art. 19) y decisiones automatizadas (art. 20) | Mayor | 55, 57, 65, 98 |
| OM-05 | Protección desde el diseño y por defecto; modelo de madurez Fase 0 | Mayor | 37, 90-92 |
| OM-06 | Lista de supuestos de EIPD independiente de la matriz | Mayor | 90, 92, 96 |
| OM-07 | Cumplimiento de la LOPDP en la encuesta de la tesis | Mayor | 69-72, 136-137, 150 |
| OM-08 | Encuesta aplicada por la propia universidad (Fase 0) | Mayor | 92, 111 |
| OM-09 | Oficio sin respaldo y resultados pendientes | Mayor | 22-23, 38-39, 79-87, 97, 100 |
| Om-10 | Cobertura de los 17 numerales del art. 12 | Menor | 55, 108 |
| Om-11 | Transferencias nacionales e internacionales; inventario de encargados | Menor | 55, 57, 98 |
| Om-12 | Conservación obligatoria frente a conservación sin finalidad | Menor | 55, 98-99 |
| Om-13 | Transparencia (LOTAIP) y minimización | Menor | 98 |
| Om-14 | Definición de "datos personales académicos" y titulares cubiertos | Menor | 32-35, 97 |
| Om-15 | Responsabilidad proactiva como requisito propio | Menor | 90-91 |
| Om-16 | Régimen de sanciones para universidades públicas | Menor | 28, 30, 94 |
| Om-17 | Ataques de extracción, ransomware e información sensible | Menor | 20-22, 35, 55, 65, 98-99 |
| Om-18 | Plataformas educativas (aulas virtuales) en el censo, antecedentes y escenarios | Menor | 48-50, 55, 57-58, 97-98 |

**Orden de trabajo recomendado:** OM-01 y OM-02 primero (fijan el marco), luego OM-03 a OM-09, luego Om-10 a Om-18.

---

## OBSERVACIONES MAYORES (resolver antes de la sustentación)

### OM-01. Cambiar el ámbito de Pichincha a nacional

**Problema:** los datos oficiales (SIIES, CES) se publican a nivel nacional, no por provincia. La tesis no pudo obtener datos de Pichincha y ya usa la proporción nacional.

**Acciones — Parte A (evidencia empírica):**

1. **Censo documental nacional (OE2):**
   - Población: las 64 universidades y escuelas politécnicas del CES (36 públicas, 20 particulares autofinanciadas, 8 cofinanciadas).
   - Unidad de observación: sitio web oficial de cada institución matriz.
   - Submuestra de confiabilidad: 13 instituciones (⌈0.2 × 64⌉).

2. **Encuesta nacional (OE3):**
   - Población: estudiantes de grado mayores de edad, N = 841 404 (SIIES 2023).
   - Muestra: 384 respuestas válidas (justificadas por potencia).
   - Cuotas: 64% públicas, 36% particulares (matrícula nacional; ya no provisionales).
   - Difusión: en línea a nivel nacional + QR donde sea posible.
   - Filtro P02: "¿Estudia actualmente una carrera de grado en una universidad o escuela politécnica del Ecuador?"
   - Pregunta A5: lista de las 64 instituciones + "Prefiero no responder".
   - Pregunta opcional de región (Costa, Sierra, Amazonía, Galápagos) como dato descriptivo.

3. **Sesgo:** mantener monitoreo semanal (A2, A5, A6, región). Declarar concentración en Limitaciones.

4. **Tabla 30:** comparar muestra solo con datos nacionales del SIIES.

5. **Eliminar todos los [PENDIENTE]** que dependían de datos de Pichincha. Reemplazar con datos nacionales + fecha.

6. **Reescribir secciones:** Resumen, Abstract, 1.1.3, Delimitación espacial (1.2.5), OE2, OE3, Alcance (1.5), 3.1, 3.4.1, 3.5, Limitaciones.

7. **Resultados agregados** a nivel nacional y por sostenimiento. Por región solo si ≥5 respuestas por grupo.

**Acciones — Parte B (producto aplicable):**

8. **Crear Anexo M: "Guía de aplicación de la metodología"** que una universidad pueda usar sin leer los capítulos III y IV. Contenido:
   - Objetivo y alcance
   - Roles: máxima autoridad, delegado, TI, jurídico, responsables de proceso
   - Fases P, 0, 1, 2, 3 y 4 con pasos numerados, entradas y productos
   - Escalas, agravantes, tabla de decisión, criterios de aceptación
   - Instrucciones de la plantilla Excel hoja por hoja
   - Procedimiento ante vulneraciones
   - Hoja de normativa de referencia (OM-02)

9. **Agregar paso "Perfil institucional"** al inicio de la Fase 0, con lista de verificación:

   | Pregunta | Si la respuesta es... | Consecuencia |
   |----------|----------------------|--------------|
   | ¿Es pública? | Sí | Delegado obligatorio (art. 48); sujeta a LOTAIP; régimen sancionatorio público |
   | ¿Es privada? | Sí | Sanción sobre volumen de negocio (art. 72); delegado depende de otros supuestos |
   | ¿Cuántos estudiantes? | Cerca del umbral de gran escala | Verificar Res. 0005-R; posible EIPD y delegado |
   | ¿Trata datos de salud, discapacidad o biometría? | Sí | Categorías especiales (arts. 25-26); posible EIPD |
   | ¿Recibe aspirantes menores de edad? | Sí | Reglas para menores (art. 21); agravante en impacto |
   | ¿Tiene modalidad en línea o híbrida? | Sí | Más encargados y transferencias; revisar supervisión de exámenes |
   | ¿Usa servicios en la nube fuera del país? | Sí | Transferencia internacional (arts. 55+) |
   | ¿Tiene sedes o extensiones? | Sí | Incluirlas en el alcance |

10. **Cambiar criterio de activación (p. 98):**
    - Cada universidad activa escenarios con su propia Fase 0.
    - Umbral del 50% es valor de referencia por defecto (ajustable con justificación documentada).
    - Resultados nacionales de la tesis = **referencia sectorial**, no insumo obligatorio.

11. **Reemplazar "universidad tipo" por "perfiles de referencia"** en Tabla 44:
    - Perfil A: universidad pública, >10 000 estudiantes, presencial.
    - Perfil B: universidad privada, <5 000 estudiantes, con modalidad en línea.
    - Justificar los cortes de tamaño. Panel Delphi estima escenarios para ambos perfiles.

12. **Agregar RNF08** a Tabla 37: "Aplicabilidad nacional: la metodología puede aplicarse a cualquier universidad o escuela politécnica del país, pública o privada, de cualquier tamaño y modalidad, ajustando sus obligaciones mediante el perfil institucional."

13. **Agregar indicador de validación** a Tabla 49 y pregunta a Anexo H: "La metodología puede aplicarse en universidades de distinto tipo, sostenimiento, tamaño y modalidad (1 a 4)", meta V de Aiken ≥ 0.80.

14. **Diversificar panel de expertos** (5.7.1, p. 102): jueces de públicas y privadas, distintas regiones.

**Ejemplo de Delimitación espacial:**
> "En lo espacial, el estudio abarca las universidades y escuelas politécnicas del Ecuador registradas en el CES (64 instituciones a la fecha de consulta) y a sus estudiantes de grado mayores de edad. Se adopta el ámbito nacional porque las fuentes oficiales disponibles —el listado del CES y la matrícula del SIIES— están publicadas a ese nivel, mientras que la desagregación provincial no está disponible de forma verificable. La metodología resultante es aplicable a cualquier universidad del país, que la adapta mediante su perfil institucional y su propio diagnóstico (Fase 0)."

**Verificar:** no queda ningún [PENDIENTE] de datos provinciales; una persona de cualquier universidad puede aplicar la metodología leyendo solo el Anexo M y la plantilla.

---

### OM-02. Fijar una sola fecha de corte normativa

**Problema:** la tesis usa tres fechas distintas (27/10, 7/11 y 16/11 de 2026). "Hasta la fecha de cierre" es una fecha abierta que mueve el trabajo indefinidamente.

**Acciones:**

1. **Fijar fecha de corte normativa: 16 de noviembre de 2026.** Debe aparecer igual en: Resumen, Delimitación (1.2.5), Alcance (1.5) y Tabla 4.

2. **Distinguir dos fechas:**
   - Fecha de corte normativa: qué normativa se analiza.
   - Periodo de levantamiento: 16/11/2026 al 26/02/2027.

3. **Crear tabla "Corpus normativo del estudio"** en Capítulo II. Columnas: norma, tipo (ley/reglamento/resolución), número, fecha publicación, Registro Oficial, artículos usados. Incluir como mínimo:
   - Constitución, art. 66 num. 19
   - LOPDP (R.O. 459, 26/05/2021) + reforma 2026
   - Reglamento General (Decreto 904, R.O. 435, 13/11/2023)
   - Guía de Gestión de Riesgos v1 (SPDP-SPD-2025-0003-R) y v2 (SPDP-SPD-2026-0012-R)
   - Reglamento del delegado (SPDP-SPD-2025-0028-R)
   - Guía de protección desde el diseño y por defecto (R.O. 163, 13/11/2025)
   - Norma de gran escala (SPDP-SPD-2026-0005-R)
   - Norma de notificación de vulneraciones (SPDP-SPD-2026-0040-R)
   - Ley Orgánica para el Fortalecimiento de la Ciberseguridad
   - LOES y normativa del CES

4. **Regla para normas posteriores al corte:** no se incorporan al análisis ni cambian instrumentos. Si una deroga algo que se mide, se registra en una "nota de vigencia" en Limitaciones o anexo, indicando qué indicador afecta → Trabajos futuros.

5. **Unificar fechas** de Tablas 4, 6 y cifras de contexto, o explicar diferencias con nota.

6. **Mantener hoja "Normativa de referencia" en la plantilla** con versión y fecha (RNF07).

**Ejemplo de Delimitación normativa:**
> "En lo normativo, el estudio considera la normativa publicada en el Registro Oficial hasta el 16 de noviembre de 2026 (fecha de corte normativa), detallada en la Tabla X. Las normas publicadas después de esa fecha no modifican los indicadores ni los instrumentos; si alguna altera sustancialmente una obligación medida, se registra en la nota de vigencia del Anexo Y y se considera trabajo futuro."

**Verificar:** la fecha de corte es una sola, aparece igual en todo el documento, y la tabla del corpus enumera cada norma usada.

---

### OM-03. Bases de legitimación: el consentimiento no es la base de todo

**Problema:** la tesis trata "le pidieron consentimiento" = cumplimiento. Pero la mayoría de tratamientos universitarios se basan en la obligación legal o el contrato, NO en el consentimiento. Pedir consentimiento para todo es una mala práctica. H3 está mal planteada.

**Acciones:**

1. **Reformular H3.** Propuesta: "H3: la proporción de estudiantes que pudo aceptar o rechazar por separado las finalidades no necesarias para el servicio educativo (ej. difusión de imagen, publicidad) difiere según el tipo de universidad." Usar pregunta H8 en lugar de H2.

2. **Reinterpretar IE07 e IE09:** ya no miden cumplimiento, son datos descriptivos sobre CÓMO se recoge el consentimiento. El indicador de cumplimiento pasa a ser IE08.

3. **Agregar a Tabla 3** la definición de cada base de legitimación del art. 7 y del interés legítimo del art. 9.

4. **Crear tabla "Finalidad → base de legitimación"** para la metodología y la Guía de aplicación:

   | Finalidad | Base probable | ¿Requiere consentimiento? |
   |-----------|--------------|--------------------------|
   | Admisión y matrícula | Medidas precontractuales y contrato; obligación legal | No |
   | Registro de calificaciones y expediente | Obligación legal (LOES y normativa CES) | No |
   | Reporte al SIIES y SENESCYT | Obligación legal | No |
   | Becas y ayudas socioeconómicas | Contrato o normativa de becas; datos sensibles (art. 26) | Depende: analizar |
   | Servicio médico o psicológico | Prestación del servicio; datos de salud (art. 25) | Analizar con cuidado |
   | Fotos y videos para redes o publicidad | Consentimiento | Sí, separado |
   | Publicidad de posgrados | Consentimiento o interés legítimo | Normalmente sí |
   | Bolsa de empleo para graduados | Consentimiento | Sí |
   | Videovigilancia en campus | Interés legítimo o seguridad | No, pero con aviso visible |

   **NOTA:** Esta tabla es una propuesta. Verificar contra el texto oficial de la norma.

5. **Cambiar indicador ID04** (p. 55) a: "Declara la base de legitimación correcta para cada finalidad." Calificar P (parcial) si la universidad usa consentimiento para todo.

6. **Reformular escenario R-04:** el riesgo no es "falta de consentimiento" sino "usar datos para finalidad no necesaria sin base válida, o con consentimiento que no es libre."

**Verificar:** en ninguna parte "le pidieron consentimiento" = cumplimiento; la tabla de finalidades y bases forma parte de la metodología.

---

### OM-04. Faltan dos derechos: suspensión (art. 19) y decisiones automatizadas (art. 20)

**Problema:** solo se miden acceso, rectificación, eliminación, oposición y portabilidad (arts. 13-17). Faltan suspensión (art. 19) y no ser objeto de decisiones automatizadas (art. 20). El art. 20 es clave para R-14 (supervisión de exámenes y analítica).

**Acciones:**

1. **ID07:** agregar "suspensión del tratamiento" y "no ser objeto de decisiones automatizadas."

2. **IE10 y dimensión DER:** agregar dos ítems Likert:
   - DER8: "Sé que puedo pedir que se suspenda el uso de mis datos mientras se revisa si son correctos."
   - DER9: "Sé que puedo pedir que una decisión sobre mí no se tome solo con un sistema automático."

3. **Actualizar Tabla 16** con ítems nuevos y artículo. Registrar cambio en versión del cuestionario (Tabla 15, versión 2.2).

4. **R-14:** citar expresamente art. 20 en Tabla 46 (p. 99).

5. **Revisar si quedan otros derechos sin medir.** Si se excluye alguno, justificar.

**Verificar:** cada derecho de la LOPDP aparece en ID07, en DER o con justificación de exclusión.

---

### OM-05. Protección desde el diseño y por defecto (art. 39); modelo de madurez de Fase 0

**Problema:** la Fase 0 promete diagnóstico de "madurez" sin definir niveles ni criterios. El art. 39 no se desarrolla. La SPDP ya publicó la Guía de Protección de Datos desde el Diseño y por Defecto (R.O. 163, 13/11/2025) con escala de "Caótico" a "Maduro explícito".

**Acciones:**

1. **Leer la guía completa** y citarla en Capítulo II (sección 2.6) y cronología Tabla 4.

2. **Adoptar su escala de madurez** para la Fase 0: tabla con columnas nivel, descripción, evidencias.

3. **Definir cómo asignar el nivel institucional:** ej. "el menor nivel alcanzado en los bloques críticos" o un promedio. Elegir una regla y justificarla.

4. **Agregar RF12:** "aplicar la protección de datos desde el diseño y por defecto a los tratamientos nuevos y cambios en existentes (art. 39)", con control en la matriz.

5. Si al final NO se mide la madurez, cambiar el nombre de la Fase 0.

**Verificar:** la Fase 0 entrega un nivel de madurez basado en escala citada con criterios aplicables.

---

### OM-06. Lista de supuestos de EIPD independiente de la matriz

**Problema:** la EIPD se activa solo si riesgo alto/muy alto Y categorías especiales/gran escala. Esto es circular: si la estimación es baja por error, la EIPD nunca se hace. El art. 42 exige EIPD ANTES del tratamiento.

**Acciones:**

1. **Crear "Lista de verificación de EIPD obligatoria"** que se aplique al RAT ANTES del análisis de riesgos. Un solo supuesto basta para activar EIPD:
   - Biometría (huella o reconocimiento facial)
   - Supervisión de exámenes en línea con cámara/micrófono/monitoreo
   - Datos de salud, psicológicos o discapacidad del área de bienestar
   - Perfilamiento o analítica predictiva (riesgo deserción, rendimiento)
   - Tratamiento sistemático de datos de aspirantes menores de edad
   - Tratamientos que alcancen umbral de gran escala (Res. SPDP-SPD-2026-0005-R)
   - Tratamientos nuevos o cambios sustanciales en uno existente
   - Cualquier supuesto que la SPDP haya calificado como de alto riesgo

2. **Mantener RA-4 como activador adicional:** si la matriz da alto/muy alto → EIPD también.

3. **Explicar consulta previa a la autoridad.**

4. **Incluir plantilla mínima de EIPD:** descripción del tratamiento, necesidad y proporcionalidad, riesgos para derechos, medidas, opinión del delegado.

**Verificar:** ningún tratamiento en la lista de supuestos puede quedarse sin EIPD, sin importar el nivel de riesgo de la matriz.

---

### OM-07. Cumplimiento de la LOPDP en la encuesta de la propia tesis

**Problema:** Google/Microsoft son encargados del tratamiento y guardan datos fuera del Ecuador (transferencia internacional). La encuesta no es "anónima" (seudonimizada por cruce de A2+A3+A4+A5+A6). El consentimiento (Anexo C) no cumple todos los requisitos del art. 12.

**Acciones:**

1. **Completar Anexo C con:**
   - Base legal: consentimiento del participante (arts. 7 y 8).
   - Encargado y transferencia: "Las respuestas se almacenan en [Google/Microsoft], proveedor que actúa como encargado del tratamiento y cuyos servidores pueden estar fuera del Ecuador."
   - Derechos: "Puede ejercer los derechos de la LOPDP escribiendo a [correo]. Como no se recogen datos que lo identifiquen directamente, es posible que no podamos localizar sus respuestas una vez enviadas."
   - Reclamo: "Puede presentar un reclamo ante la Superintendencia de Protección de Datos Personales."

2. **Reemplazar "anónima" por "sin datos identificativos directos (seudonimizada)"** en 3.8, Anexo C y Resumen. Si se quiere mantener "anónima", demostrar con análisis de reidentificación que ninguna combinación de A2–A6 tiene <5 casos.

3. **Configurar formulario** sin recoger correos, sin inicio de sesión, sin carga de archivos. Decirlo en 3.8.

4. **Reducir combinaciones** de variables que no se necesiten. No cruzar A5 con A3 en la base de análisis.

5. **No abrir la encuesta** hasta tener el oficio de ética en Anexo L.

**Verificar:** Anexo C tiene todos los elementos del art. 12; el documento no dice "anónima" sin justificarlo.

---

### OM-08. Encuesta aplicada por la propia universidad (Fase 0)

**Problema:** cuando la universidad aplica la encuesta a sus propios estudiantes, ella es el responsable del tratamiento. Riesgos: relación asimétrica, falta de independencia, posible reidentificación.

**Acciones:** agregar a la Guía de aplicación (Anexo M) la sección "Aplicación del cuestionario por la institución" con reglas:

1. Base legal y aviso informativo con elementos del art. 12.
2. Participación voluntaria, sin incentivos académicos ni consecuencias.
3. La aplica un área distinta de la evaluada (delegado o dirección de investigación).
4. Respuestas no se cruzan con sistema académico; no pedir correo institucional ni matrícula.
5. Resultados solo agregados, suprimiendo celdas con <5 respuestas.
6. Base con plazo de conservación; se elimina al vencer.

**Verificar:** la Guía de aplicación explica cómo hacer la encuesta institucional cumpliendo la LOPDP.

---

### OM-09. Oficio sin respaldo y resultados pendientes

**Problema:** el oficio SPDP-IRD-2026-0221-O se usa como argumento central pero no se localizó. Hay 33 marcas [PENDIENTE]. El Capítulo IV está vacío.

**Acciones:**

1. **Oficio — elegir una opción:**
   - (a) Solicitar a la SPDP como acceso a información pública (LOTAIP). Citar completo.
   - (b) Si no se obtiene, **eliminar la afirmación** y apoyarse solo en Res. SPDP-SPD-2026-0005-R.

2. **Hacer lista de los 33 pendientes** con columnas: pendiente, sección, fuente, fecha prevista, responsable. Revisarla con la tutora en cada punto de control (Tabla 19).

3. **Completar Capítulo IV** y Tablas 44 y 47 antes de entregar versión para lectores.

4. **Revisar Recomendaciones (6.2):** cada una debe salir de un resultado o hallazgo concreto.

**Verificar:** versión final sin marcas [PENDIENTE]; cada afirmación normativa tiene fuente en la bibliografía.

---

## OBSERVACIONES MENORES (mejoras recomendadas)

### Om-10. Cobertura de los 17 numerales del art. 12

**Acción:** crear tabla de cobertura con numerales 1–17 del art. 12 (texto oficial). Columnas: numeral, contenido, indicador que lo verifica (ID o IE), y si no se mide, el motivo. Agregar indicadores para los numerales verificables desde fuera.

**Verificar:** ningún numeral sin indicador o sin justificación de exclusión.

---

### Om-11. Transferencias nacionales e internacionales; inventario de encargados

**Acciones:**

1. Dividir ID06 en:
   - **ID06a:** comunicaciones a terceros nacionales (SENESCYT, IESS, bancos, aseguradoras).
   - **ID06b:** transferencias internacionales (país de destino, garantía, base).

2. Agregar a la metodología y plantilla un **inventario de encargados**: proveedor, servicio, datos que trata, país, contrato firmado (sí/no), cláusula de protección (Reglamento art. 41). Ejemplos: aula virtual, correo y nube institucional, antiplagio, supervisión exámenes, pasarela de pagos, sistema académico en la nube.

**Verificar:** plantilla tiene hoja de encargados y transferencias.

---

### Om-12. Conservación obligatoria vs. conservación sin finalidad

**Acciones:**

1. Agregar **tabla de retención por tipo de documento**: documento, norma que obliga a conservarlo, plazo, acción al vencer (eliminar, anonimizar, archivar).

2. Reformular R-10 como "conservación de datos sin una obligación legal ni una finalidad vigente."

**Verificar:** R-10 no trata como incumplimiento la conservación que exige la ley.

---

### Om-13. Transparencia (LOTAIP) y minimización

**Acción:** agregar párrafo y regla: universidades públicas publican por LOTAIP pero deben aplicar minimización (ej. listas de admitidos sin cédula completa). La regla se aplica según el perfil institucional (OM-01).

**Verificar:** R-03 cita LOTAIP y minimización; perfil institucional indica cuándo aplica.

---

### Om-14. Definir "datos personales académicos" y titulares cubiertos

**Acciones:**

1. **Definir en Tabla 3:** "datos personales que la institución de educación superior trata con ocasión de la admisión, la formación, la evaluación, el bienestar y la titulación de sus estudiantes."

2. **Separar dos alcances:**
   - Lo que **mide la tesis:** estudiantes de grado mayores de edad.
   - Lo que **cubre la metodología:** aspirantes (incluidos menores, arts. 21 y 25), estudiantes, padres/representantes, graduados; y opcionalmente docentes y personal.

3. Escribirlo en Alcance (1.5), coherente con OM-01.

**Verificar:** término definido en Tabla 3; Alcance distingue lo medido de lo cubierto.

---

### Om-15. Responsabilidad proactiva como requisito propio

**Acciones:**

1. Agregar **RF13:** "cada fase produce evidencia documentada (actas, registros, justificaciones y aprobaciones) que permite demostrar el cumplimiento ante la SPDP" (art. 10).

2. Agregar a Tabla 38 columna "Evidencia que queda" para cada fase.

**Verificar:** existe RF13; Tabla 38 indica qué evidencia deja cada fase.

---

### Om-16. Régimen de sanciones para universidades públicas

**Acción:** agregar régimen de entidades públicas (arts. 71-72 vigentes al corte). El perfil institucional (OM-01) indica cuál corresponde.

**Verificar:** Tabla 41 y perfil institucional distinguen régimen público del privado.

---

### Om-17. Ataques de extracción de datos, ransomware e información sensible

**Acciones:**

1. **Agregar al Cap. I o II** párrafo sobre ataques de extracción en universidades: caminos de ataque, consecuencias para el titular, agravante por datos sensibles.

2. **Usar cifras de Sophos solo como contexto** (encuesta de proveedor comercial). No usar para estimar probabilidad anual.

3. **Justificar R-06 y R-08 como escenarios base obligatorios** (no se pueden observar controles técnicos desde fuera).

4. **Ampliar R-09 o crear R-15:** "Extracción de datos personales y sensibles mediante ataque informático (dimensión: confidencialidad)." También escenario base obligatorio.

5. **Valorar impacto desde el titular:**
   - R-08 (disponibilidad): impacto normalmente medio.
   - R-09/R-15 (confidencialidad): impacto alto o muy alto si datos sensibles → agravante (a).

6. **Reforzar controles de R-09/R-15** en Tabla 46: minimización y supresión de expedientes vencidos, MFA, segmentación de red, mínimo privilegio, registro y monitoreo, DLP, gestión de parches.

7. **Agregar al RAT (D4)** mapa de dónde se guardan datos sensibles.

8. **Agregar a Fase 4** caso de filtración publicada (comunicación a afectados, recomendaciones, plazos).

9. **Corregir incoherencias de datos sensibles:**
   - Datos socioeconómicos (ID13): (a) sacarlos de categorías especiales y tratarlos como alto impacto, o (b) justificar con art. 4 por qué son sensibles en contexto de becas.
   - Agregar a H1 e ID13: autoidentificación étnica, condición migratoria, identidad de género (nombre social).

**Verificar:** escenario de exfiltración con impacto desde el titular; cifras de proveedores no estiman probabilidades; ID13 y H1 coherentes con Tabla 3.

---

### Om-18. Plataformas educativas (aulas virtuales) en censo, antecedentes y escenarios

**Acciones:**

1. **Agregar tres indicadores documentales** a Tabla 12 y Anexo A (complementarios, no entran en índice principal):
   - **ID17.** Plataforma identificada y quién la aloja (ej. moodle.universidad.edu.ec).
   - **ID18.** Aviso de privacidad en la pantalla de acceso del aula virtual.
   - **ID19.** Supervisión de exámenes en línea declarada.

2. **Regla:** la revisión llega solo hasta la pantalla de acceso, sin iniciar sesión.

3. **Citar estudios ecuatorianos** en 2.7.4 y 2.7.5 y agregarlos a Tablas 9 y 10:
   - Aceptación de Moodle entre docentes ecuatorianos (Behavioral Sciences, 2023)
   - Análisis AHP de LMS para IES ecuatorianas (AGRIS, 2025)
   - Seguridad de información en LMS, caso UTEQ (Conrado, 2024)
   - Protección de datos en entornos virtuales IES (UPS, 2026)
   - Datos de estudiantes en plataformas desde la inscripción (Noesis)

4. **Conectar indicadores con escenarios:**
   - ID17 → R-07, R-11, inventario de encargados (Om-11)
   - ID18 → OM-03, brecha de información (IE03–IE06)
   - ID19 → R-14, OM-04 (art. 20). Si usa biometría → EIPD obligatoria (OM-06) + agravante (a)

5. **Completar Tabla 44** con frecuencias de ID17 e ID19 del censo nacional.

6. **Agregar al RAT (D4)** fila tipo para aula virtual: finalidad, base legal, categorías de datos, encargado, país, plazo de conservación.

**Verificar:** ficha documental incluye ID17–ID19; estudios ecuatorianos citados; R-07, R-11, R-14 los usan como activadores.

---

## PASOS DE LA METODOLOGÍA DE DIAGNÓSTICO (Parte C)

12 pasos, D0–D11. Los aplica la universidad que adopte la metodología.

| Paso | Objetivo | Producto | En la tesis |
|------|----------|----------|-------------|
| D0 | Fijar normativa de referencia | Hoja "Normativa de referencia" | Se hace completo (OM-02) |
| D1 | Mandato y alcance | Acta de inicio y plan de trabajo | No se ejecuta; se describe en Guía |
| D2 | Perfil institucional (NUEVO) | Ficha de perfil y lista de obligaciones | Se diseña como plantilla; se prueba con perfiles A y B |
| D3 | Mapa de procesos y titulares | Mapa de procesos y titulares | Se elabora para perfiles de referencia |
| D4 | Registro de actividades de tratamiento (RAT) | RAT preliminar | RAT tipo para perfiles + plantilla vacía |
| D5 | Ciclo de vida de los datos | Diagramas de flujo de datos | 2-3 diagramas de ejemplo |
| D6 | Matriz de requisitos e indicadores | Lista de verificación con criterios S/P/N | Se hace completo (OE1) |
| D7 | Instrumentos | Instrumentos validados (V de Aiken) | Se aplican ficha externa y cuestionario; instrumentos 2-4 se diseñan y validan |
| D8 | Levantamiento de evidencia | Expediente de evidencias | Censo + encuesta (OE2 y OE3) |
| D9 | Calificación y nivel de madurez | Índice de cumplimiento y nivel de madurez | Índice de transparencia agregado |
| D10 | Análisis de brechas | Matriz de brechas priorizada | Brechas norma vs. publicado vs. percibido |
| D11 | Informe de diagnóstico | Informe y línea base → entrada Fase 1 | Línea base agregada nacional como referencia sectorial |

---

## PASOS DE LA METODOLOGÍA DE GESTIÓN DE RIESGOS (Parte D)

11 pasos, G1–G11. Empieza con D11 y se repite en cada revisión.

| Paso | Objetivo | Producto | En la tesis |
|------|----------|----------|-------------|
| G1 | Contexto y criterios | Documento de criterios aprobado | Se diseña y calibra con Delphi |
| G2 | Revisión previa de EIPD | Lista de tratamientos con EIPD obligatoria | Se aplica a RAT de perfiles A y B |
| G3 | Identificación de escenarios | Catálogo de escenarios activados | Catálogo con criterios de activación ajustables |
| G4 | Análisis (probabilidad e impacto) | Matriz de riesgo inherente | Panel Delphi calibrado estima para perfiles A y B |
| G5 | Evaluación | Riesgos priorizados | Se aplica con la plantilla (Tabla 47) |
| G6 | Evaluación de impacto (EIPD) | Informe de EIPD | Plantilla de EIPD; opcional: ejemplo ilustrativo |
| G7 | Tratamiento del riesgo | Plan de tratamiento | Controles de referencia (Tabla 46) |
| G8 | Riesgo residual y aceptación | Matriz residual + actas | Delphi estima residual; aceptación como regla |
| G9 | Respuesta a vulneraciones | Procedimiento + registro de incidentes | Procedimiento documentado y validado por jueces |
| G10 | Monitoreo y mejora | Tablero de indicadores + bitácora | Indicadores definidos; aplicación = trabajo futuro |
| G11 | Comunicación y archivo de evidencia | Expediente de cumplimiento | Trazabilidad de la matriz (RNF01) |

---

## LISTA DE VERIFICACIÓN FINAL

Marcar cada casilla solo cuando la observación cumpla su "Cómo verificar":

- [x] OM-01: censo y encuesta nacionales; sin pendientes provinciales; Anexo M existe y se puede usar sin Cap. III-IV
- [x] OM-02: una sola fecha de corte normativa + tabla de corpus normativo
- [x] OM-03: H3 reformulada + tabla finalidades→bases de legitimación
- [x] OM-04: ID07 y DER incluyen arts. 19 y 20
- [x] OM-05: Fase 0 con escala de madurez citada y regla de asignación *(25-11-2026: escala tomada de análisis jurídicos de la guía porque el PDF oficial de la SPDP devolvió 404; confirmar con el PDF — PENDIENTES n.º 14)*
- [x] OM-06: lista de supuestos EIPD obligatoria (independiente de la matriz)
- [x] OM-07: Anexo C completo; ya no dice "anónima" sin justificarlo
- [x] OM-08: Guía de aplicación con reglas para encuesta institucional
- [ ] OM-09: sin marcas [PENDIENTE]; oficio citado o afirmación eliminada *(25-11-2026: oficio eliminado, opción b; [PENDIENTE] de 33 a 9, solo ética y segundo observador, listados en PENDIENTES.md; recomendaciones derivadas de hallazgos. **Abierto:** el Cap. IV y las tablas de perfiles y de riesgo esperan los datos de la recolección, 07-12-2026 a 22-01-2027)*
- [x] Om-10: tabla de cobertura de los 17 numerales del art. 12
- [x] Om-11: hoja de encargados y transferencias en la plantilla
- [x] Om-12: tabla de retención de documentos
- [x] Om-13: R-03 con LOTAIP y minimización
- [x] Om-14: "datos personales académicos" definido; alcance separa medido vs. cubierto
- [x] Om-15: RF13 existe; Tabla 38 con columna "Evidencia que queda"
- [x] Om-16: perfil institucional distingue régimen sancionatorio público/privado
- [x] Om-17: escenario de extracción valorado desde el titular; R-06/R-08/R-15 justificados; ID13/H1 coherentes con Tabla 3
- [x] Om-18: ficha documental con ID17-ID19; estudios ecuatorianos citados; R-07/R-11/R-14 los usan
