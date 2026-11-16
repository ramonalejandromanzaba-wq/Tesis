# Retroalimentación de la tutora — versión 2 (11/11/2026)

Lee primero los CLAUDE.md / CLAUDEs.md, `uploads/reestructuracion_tesis.md` y `uploads/metodologia_cuantitativa.md`; siguen vigentes. Este archivo atiende la retroalimentación de la tutora sobre la versión 2 con enfoque cuantitativo. Trabaja de forma autónoma en la rama actual (`reestructuracion-sin-caso`) y crea antes un tag `v2-antes-retro`.

Hoy es 16/11/2026. **La recolección empieza el 7/12/2026.** Prioriza lo que bloquea esa fecha: cuestionario completo y corregido (sección 2), paquete para los jueces (sección 5) y verificación ética (sección 6).

## ALCANCE GEOGRÁFICO: PROVINCIA DE PICHINCHA (decisión nueva del autor, prevalece)

- La versión 2 tenía alcance **nacional** (censo de 64 universidades y población de 62 universidades del SIIES 2023). **Se cambia a la provincia de Pichincha**: universidades y escuelas politécnicas con matriz, sede o extensión en Pichincha (Quito y cantones como Rumiñahui, lo que incluye a la ESPE).
- Motivo: Pichincha coincide con la desagregación oficial del SIIES, así que el censo documental y la población (N) se definen con la misma unidad y la misma fuente, sin aproximaciones.
- Verifica con fuentes oficiales (CES, SENESCYT/SIIES, CACES) cuáles son esas instituciones y cuántas, con fecha de corte. No inventes el número.
- **Censo documental:** solo las universidades de Pichincha. Recalcula el 20 % para la reverificación y el kappa, y la lista de la pregunta de universidad.
- **Población (N):** matrícula de pregrado en Pichincha según SIIES, con fecha de corte. El número de universidades del censo y el de la población deben coincidir; si no, explica la diferencia.
- **Muestra:** se mantiene la meta de 384, justificada por potencia estadística (R1.2), que no depende de N.
- **Filtro en el cuestionario:** "¿Estudias actualmente en una universidad o escuela politécnica ubicada en Quito o sus alrededores (provincia de Pichincha)?" Si responde No, la encuesta termina. Esto reemplaza la pregunta de región.
- **Aplicación mixta con un solo instrumento:** la encuesta se responde siempre en el mismo formulario en línea; la difusión es en línea (enlace) y presencial (código QR en los campus). Registrar el canal de difusión con una pregunta opcional o con enlaces distintos por canal, y declararlo en la metodología.
- La **metodología** (producto) sigue siendo aplicable a cualquier universidad; se construye y valida con evidencia de Pichincha. Declara como limitación que los resultados empíricos describen a Pichincha y no al país.
- Actualiza en todo el documento: título (si conviene, añadir "en universidades de Pichincha"; registra antes/después en CAMBIOS.md), objetivos específicos OE2 y OE3, justificación, población, ética, resumen, cronograma y scripts.
- PENDIENTES.md: la tutora debe aprobar el cambio de alcance de nacional a Pichincha.

## ENFOQUE GENERAL (prevalece sobre cualquier otra indicación)

- La tesis es **general sobre las universidades de Pichincha**. No se centra en la Universidad Tecnológica Indoamérica (UTI) ni en ninguna otra institución en particular.
- El **producto principal es la metodología** para el diagnóstico y la gestión de riesgos en el tratamiento de datos personales académicos conforme a la LOPDP, aplicable a cualquier universidad. El censo documental, la encuesta y el Delphi son los insumos para construirla y validarla.
- La UTI solo aparece como **institución del autor**: portada, declaraciones, tutoría y verificación ética (la solicitud ética se presenta ante la UTI porque es la universidad donde se desarrolla la investigación, no porque sea el objeto de estudio).
- Revisa todo el documento y elimina o generaliza cualquier texto que todavía presente a la UTI como caso, ejemplo principal o referencia de los resultados. Ningún análisis, tabla ni escenario debe estar construido sobre la UTI.
- La difusión de la encuesta debe buscar estudiantes de **distintas universidades** (públicas y privadas de Pichincha), no solo de la UTI.

## REPORTE AGREGADO (prevalece)

- **Ningún resultado del documento se presenta por universidad.** No se nombra a ninguna institución en los resultados, las tablas, las figuras, las conclusiones ni los anexos de resultados. No se escribe "la universidad X tuvo N respuestas" ni "la universidad X cumple el Y %".
- Todo se reporta **agregado**: total de universidades de Pichincha y, como máximo, por sostenimiento (pública / privada / cofinanciada), por área de carrera, por semestre y por modalidad. Ejemplo de redacción: "En las universidades de Pichincha, el X % de los estudiantes indicó…", "las universidades públicas presentan un índice de transparencia mediano de…".
- **Censo documental:** las universidades se codifican (U01, U02, …). En el documento solo aparecen los resultados agregados (p. ej., "el X % de las universidades publica una política de privacidad"). La tabla de códigos y las URL de evidencia se guardan en `privado/clave_universidades.xlsx`, fuera del PDF, disponible para el tribunal si la solicita. Declararlo en la metodología.
- **Encuesta:** la pregunta de universidad sirve solo para ponderar la brecha (R1.1) y para describir cuántas universidades distintas participaron (p. ej., "respondieron estudiantes de N universidades"), sin nombrarlas.
- **Supresión de celdas pequeñas:** ninguna categoría con menos de 5 respuestas se reporta sola; se agrupa con otras, para que no se pueda identificar a nadie.
- Revisa todo el documento y elimina cualquier mención de universidades concretas en resultados, ejemplos o discusión. Esta regla no afecta a la portada ni a los datos del autor.

### Cómo redactar los resultados
Para cada hallazgo usa el orden **dato → prueba → interpretación**:
1. **Dato:** porcentaje o mediana, con n.
2. **Prueba:** estadístico, valor p y tamaño del efecto (p. ej., "ρ = 0,32; p < 0,001").
3. **Interpretación:** qué significa para la protección de datos en las universidades de Pichincha y qué artículo de la LOPDP se relaciona.
Interpretación de efectos: Spearman |ρ| < 0,10 trivial, 0,10–0,29 débil, 0,30–0,49 moderada, ≥ 0,50 fuerte; V de Cramér y r de Mann-Whitney con los umbrales de Cohen. Cita la fuente de los umbrales.
Que los scripts de `analisis/` generen las tablas y frases agregadas directamente, sin ningún desglose por universidad.

Reglas generales:
- No inventes datos, resultados, coeficientes, respuestas, contenido de oficios ni referencias. Lo que no exista va como `\textcolor{red}{[PENDIENTE: ...]}` y en PENDIENTES.md.
- Todo cambio en el número o en el código de los ítems debe propagarse a: Anexo B, tabla de operacionalización, dimensiones, cálculo de alfa/omega/KR-20, scripts de `analisis/`, consentimiento y conteos en el texto ("46 preguntas", etc.).
- Toda indicación de este archivo se registra en CAMBIOS.md con su código (R1.1, R1.2, …, R4).

---

## R1. Observaciones de fondo al diseño cuantitativo

### R1.1 Brecha de percepción (PRIORITARIA)
Problema: la Ecuación 8 calcula B_P = C_D − C_E, pero C_D es un porcentaje de universidades (todas las universidades del censo pesan igual) y C_E es un porcentaje de estudiantes; la encuesta no pregunta a qué universidad pertenece el estudiante y, con bola de nieve, la muestra puede concentrarse en pocas instituciones.
Hacer:
1. Agregar al cuestionario una pregunta: "¿En qué universidad o escuela politécnica estudias?", con la lista de las universidades del censo documental de Pichincha, más "Otra" y "Prefiero no responder". Declarar en la ética que el nombre de la universidad no identifica a la persona y que **se usa solo internamente para ponderar la brecha; nunca se publica un resultado por universidad** (ver Reporte agregado).
2. Redefinir la brecha para comparar lo mismo con lo mismo:
   - **Brecha ponderada:** C_D ponderado por la composición real de la muestra (cada universidad pesa según cuántos encuestados aporta), frente a C_E.
   - Reportar también la brecha por sostenimiento (pública/privada).
3. Reescribir la Ecuación 8 y su explicación; conservar la versión no ponderada solo como referencia descriptiva y explicar por qué no es la principal.
4. Declarar la limitación: si la muestra se concentra en pocas universidades, la brecha describe esas instituciones y no al sistema.
5. Actualizar los scripts de `analisis/` para los tres cálculos.

### R1.2 Tamaño de muestra por potencia estadística
- Mantener 384 como meta, pero cambiar la justificación principal: la fórmula de población finita queda como referencia y el argumento principal pasa a ser la **potencia estadística** (α = 0,05 bilateral, potencia 0,80).
- Reportar el efecto mínimo detectable con n = 384, por hipótesis: H2, Spearman ρ ≥ 0,15; H3, chi-cuadrado w ≥ 0,15; H1, Mann-Whitney d ≈ 0,33 con distribución 246/138. Verifica estos valores con un cálculo propio en Python (statsmodels/pingouin) y deja el script en `analisis/potencia.py`.
- Indicar que el cálculo se hizo con G*Power (versión 3.1) y dejar como `[PENDIENTE]` las capturas de G*Power, que haré yo. Genera `analisis/GPOWER_INSTRUCCIONES.md` con los parámetros exactos que debo ingresar para cada prueba.

### R1.3 Sesgo y composición de la muestra
- Agregar una sección de resultados para la composición de la muestra por área de carrera (A2), semestre (A3), edad (A4), sostenimiento y modalidad, comparada con la matrícula de Pichincha (SIIES) cuando haya dato. Anticipar y declarar la posible sobrerrepresentación de carreras de TI y de la universidad del autor (por la red de contactos de la difusión), y describir las acciones para mitigarla: difusión en varias universidades de Pichincha, apoyo de docentes de otras instituciones y seguimiento semanal de la composición de la muestra durante la recolección.
- Resolver la inconsistencia: agregar al cuestionario la pregunta filtro de **Pichincha** (ver Alcance geográfico) y la de **modalidad** (presencial, semipresencial/híbrida, en línea), y corregir en la ética y en la sección 3.13 la mención de "región", que ya no aplica.
- Declarar qué pasa con quienes responden "No lo sé" en A1 (tipo de universidad): se excluyen de H1 y H3 y se reportan cuántos son. Si con la nueva pregunta de universidad se puede inferir el sostenimiento, recodificarlo y explicarlo.

### R1.4 Validez de constructo
- Añadir un **análisis factorial exploratorio** con la muestra final: KMO, prueba de esfericidad de Bartlett, método de extracción, rotación y cargas por dimensión (criterio de retención de ítems declarado, p. ej., carga ≥ 0,40). Como mínimo, verificar la unidimensionalidad de cada escala.
- Relacionarlo con el omega de McDonald (modelo de un factor).
- Script en `analisis/validez_constructo.py` (factor_analyzer); resultados `[PENDIENTE]`.

### R1.5 Confiabilidad del registro documental
- Sustituir el porcentaje de acuerdo por el **kappa de Cohen ponderado** para las categorías S/P/N, sobre el 20 % reverificado (recalcular el número con el censo de Pichincha).
- Incluir un **segundo observador independiente** para esas universidades (confiabilidad entre observadores) y mantener la intraobservador como complemento. Define el protocolo: ficha, instrucciones, capacitación breve, calificación ciega. El segundo observador queda `[PENDIENTE]` en PENDIENTES.md (lo consigo yo).
- Script en `analisis/kappa_documental.py`.

### R1.6 Sensibilidad del índice de transparencia
- Mantener P = 0,5 como decisión de diseño y agregar un **análisis de sensibilidad** recalculando con P = 0 y P = 1, para mostrar si las conclusiones por sostenimiento cambian. Tabla y script.

### R1.7 Alcance e hipótesis
- Cambiar el alcance a **descriptivo, comparativo y correlacional** en todo el documento (resumen, introducción, metodología).
- En H4–H7, "No recuerdo" se codifica como 0 para el KR-20: declararlo también en el análisis descriptivo y reportar los porcentajes **con y sin** "No recuerdo".
- La prueba de normalidad se mantiene solo como información descriptiva; aclarar que no cambia la decisión, porque siempre se usan pruebas no paramétricas.

### R1.8 Delphi sobre la "universidad tipo"
- Definir explícitamente el **perfil de la universidad tipo**: tamaño (número de estudiantes), sostenimiento, modalidad, categorías de datos tratadas (incluidas las sensibles), plataformas (SGA, LMS, correo, nube, biometría, etc.) y procesos (admisión, matrícula, bienestar, titulación). Construirlo a partir de los datos del censo documental y de SIIES, como tabla que se entrega a cada experto.
- Declarar el posible sesgo de que el mismo panel estime los riesgos (V1) y juzgue la metodología (V2), e incluir en V2 **al menos dos jueces que no hayan participado en el Delphi**.

### R1.9 Coherencia con el enfoque y con el objetivo general
- En 5.8, cambiar "estimación cualitativa calibrada" por "**estimación ordinal calibrada**". Buscar y corregir cualquier otro uso de "cualitativo" que contradiga el enfoque.
- **Objetivo general:** dice "estudiantes y docentes", pero solo se mide a estudiantes. Elimina únicamente "y docentes" (o la forma equivalente), sin tocar nada más del texto, y propágalo al resumen, la introducción y la matriz de consistencia. Registra en CAMBIOS.md el texto antes/después.
- **Gran escala:** la sección 2.3 y la Tabla 5 afirman que los datos de salud, las categorías especiales y los datos de menores son gran escala de forma directa. Matizarlo con el Oficio SPDP-IRD-2026-0221-O: tratar datos sensibles no implica por sí solo un tratamiento a gran escala. Busca el oficio en el repositorio o en el .bib. Si no está, redacta solo lo que dice la tutora, cítalo como pendiente y anótalo en PENDIENTES.md. No inventes su contenido.

---

## R2. Cuestionario (Anexo B)

- **El anexo está incompleto:** solo se imprimen INF1–INF5; faltan los 18 ítems de CON, DER y CNF. Corrige la tabla en LaTeX (probablemente usar `longtable` o `xltabular` para que pase de página) para que se impriman **todas** las preguntas. Compila y verifica en el PDF que aparezcan todas antes del Anexo C.
- **Ítems de doble contenido:**
  - INF5 ("fácil de encontrar y de entender"): separarlo en dos ítems.
  - INF2 ("Sé quién es el responsable y cómo contactarlo"): separarlo en dos ítems (decisión tomada: separar).
  - Revisar todos los ítems de CON, DER y CNF y separar cualquier otro que mida dos cosas. Lista cada cambio en CAMBIOS.md.
- **H16:** agregar "No estoy seguro" por consistencia con el resto y declarar cómo se codifica.
- Se agregan las preguntas nuevas de filtro de Pichincha, universidad y modalidad (R1.1 y R1.3).
- **Versiones:** el cuestionario pasa a ser la versión 2.1, previa al juicio de expertos. Actualizar el registro de versiones (Tabla 19) con fecha y cambios, y dejar preparado el anexo para la versión final aplicada (`[PENDIENTE]` hasta después del piloto).
- Recalcular y actualizar el número total de preguntas en todo el documento.
- Actualizar `encuesta/cuestionario.md` para que coincida exactamente con el Anexo B.

---

## R3. Cronograma y viabilidad

- Reemplazar la Figura 2 por un cronograma realista desde el 16/11/2026, con estos hitos:
  - Semana del 16/11: convocatoria a jueces y solicitud de verificación ética.
  - Hasta ~26/11: juicio de expertos y V de Aiken; versión 2.2 del cuestionario.
  - Hasta ~4/12: prueba piloto (~30), alfa/omega/KR-20 y versión final.
  - 7/12: inicio de la recolección (solo con la verificación ética resuelta).
  - Avance del 50 % del censo documental y cierre de la encuesta según lo que permita el plazo hasta febrero de 2027.
- Agregar los **4 puntos de control con la tutora:** (1) instrumentos validados, (2) cierre del piloto, (3) 50 % del censo documental, (4) cierre de la encuesta. Usa fechas concretas.
- **Plan B** si en enero no se alcanzan las 384 respuestas: ampliar la difusión con docentes de otras universidades y reportar la potencia efectiva con el n alcanzado (que `analisis/potencia.py` la calcule para cualquier n).

---

## R4. Forma

- Eliminar el texto de instrucciones "[Incluya todas las referencias bibliográficas...]" antes de la bibliografía.
- Unificar el título: el índice dice "REFERENCIAS" y el capítulo "BIBLIOGRAFÍA". Usa el que pida la plantilla UTI.
- Nombre: usar "Ramón" con tilde en todo el documento (portada, declaraciones, resumen, tablas, consentimiento, metadatos del PDF).
- Unificar "Trabajo de Integración Curricular" en todo el documento (incluidas las declaraciones).
- Completar el **Índice de Imágenes/Figuras** (verificar que las figuras usen `\caption` y que el índice se genere).
- Resumen/abstract: redactar el diseño en futuro o en presente y dejar explícito que los resultados están pendientes, para que no parezca un trabajo terminado.
- Población: la observación de 62 vs. 64 universidades queda superada por el cambio a Pichincha; asegúrate de que el número de universidades del censo y el de la población coincidan, o explica la diferencia.

---

## 5. Paquete para los jueces (urgente: la convocatoria es esta semana)

En la carpeta `jueces/`:
- `cuestionario_v2.1.pdf`: cuestionario completo, compilado desde el Anexo B.
- `formato_juicio_expertos.xlsx`: por ítem, pertinencia, claridad y coherencia (escala 1–4) y observaciones, más la hoja de autoevaluación para el coeficiente K (Kc y Ka).
- `instrucciones_jueces.md`: qué se evalúa, plazo de respuesta (5 días), confidencialidad y uso de sus datos solo con fines académicos.
- `correo_invitacion.md`: correo breve y formal de invitación.
- Actualizar `analisis/validacion.py` para leer directamente ese formato.

---

## 6. Verificación ética (debe quedar resuelta y documentada antes del 7/12/2026)

- Redacta `etica/solicitud_verificacion_etica.md`: solicitud formal dirigida a la Coordinación de la carrera / Dirección de Investigación de la UTI (institución del autor), con resumen del estudio, población (estudiantes ≥ 18 años de universidades ecuatorianas, no solo de la UTI), anonimato, consentimiento informado, ausencia de datos identificativos, riesgo mínimo, almacenamiento y eliminación de datos. Pregunta explícitamente si se requiere aprobación de un CEISH o si basta con un aval o una exención. Anexa el cuestionario v2.1 y el consentimiento.
- En el capítulo de Metodología, la sección de consideraciones éticas debe describir ese procedimiento y su resultado: `[PENDIENTE: respuesta de la UTI, fecha y número de oficio]`.
- Crear un anexo "Aval / verificación ética" con el marcador `[PENDIENTE]` para insertar la respuesta.
- PENDIENTES.md, prioridad 1: enviar la solicitud esta semana; la recolección no inicia sin la respuesta documentada.
- No afirmes que la UTI exige o no exige comité: eso lo decide la universidad.

---

## 7. Cierre

1. Compilar con latexmk: 0 errores, 0 referencias indefinidas, Anexo B completo e Índice de Figuras generado.
2. CAMBIOS.md: nueva sección "Retroalimentación v2" con un checklist R1.1–R1.9, R2, R3, R4, sección 5 y sección 6 (✔ / ⚠ / ✘, qué se hizo, dónde).
3. PENDIENTES.md, en este orden: (1) solicitud ética, (2) convocar jueces, (3) capturas G*Power, (4) segundo observador, (5) oficio SPDP si falta, (6) el resto.
4. Actualizar CLAUDE.md / CLAUDEs.md (y la copia de la carpeta superior) con los cambios estructurales: preguntas nuevas, versión 2.1, nueva definición de la brecha, scripts nuevos y carpetas `jueces/` y `etica/`.
5. Commit con mensaje descriptivo y resumen en consola de lo listo y lo que depende de mí.
