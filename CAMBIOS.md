# CAMBIOS — Metodología cuantitativa (2026-11-07, segunda parte)

Instrucción: `uploads/metodologia_cuantitativa.md`, aplicada **encima** de la reestructuración sin caso de estudio (sección siguiente). Donde contradice la sección 4 de `uploads/reestructuracion_tesis.md`, prevalece esta. Rama `reestructuracion-sin-caso`.

| Cambio | Antes | Ahora | Ubicación |
|---|---|---|---|
| Enfoque | Mixto con predominio cuantitativo; descriptivo-exploratorio | **Cuantitativo; no experimental, transversal; descriptivo-correlacional**, con cada término justificado (Hernández-Sampieri y Mendoza) | Cap. 3 §Enfoque; Resumen; Abstract |
| Cuestionario | v1.0: 6 dimensiones, sobre todo de opción única | **v2.0**: 46 preguntas: acceso (3), demográficos (4: tipo, área, semestre, edad), **16 de hechos** (sí/no/no recuerdo; selección múltiple) y **23 ítems Likert** en 4 dimensiones (INF 5, CON 5, DER 7, CNF 6), con **5 ítems inversos** (INF4, CON3, DER6, CNF3, CNF6) recodificados como x' = 6 − x | `encuesta/cuestionario.md`; Anexo B; Cap. 3 |
| Operacionalización | Tabla de trazabilidad pregunta → indicador → artículo | **Variable → dimensión → indicador → ítem → escala → artículo de la LOPDP** (`tab:operacionalizacion`) | Cap. 3 |
| Validez de contenido | ≥ 5 jueces; claridad, pertinencia, coherencia; V ≥ 0,70 | **3–5 jueces** (protección de datos, seguridad, metodología); pertinencia, claridad, coherencia; **V ≥ 0,80**. Plantilla de cálculo y formato | Cap. 3; Anexo D; `encuesta/formato_juicio_expertos.md`; `encuesta/plantilla_juicio_expertos.xlsx` (784 fórmulas, 0 errores) |
| Validación de la guía (V2) | V ≥ 0,70 | V ≥ 0,80, unificado con el cuestionario para usar un solo criterio | Cap. 5; Anexo H |
| Confiabilidad | Alfa (y KR-20 en E1) | **Alfa y omega de McDonald por dimensión Likert** (≥ 0,70 aceptable; ≥ 0,80 bueno); **KR-20** en la escala dicotómica H4–H7; explicación de por qué el alfa no se aplica a ítems de sí/no | Cap. 3 (Ecs. de alfa, omega y KR-20); Cap. 4 |
| Hipótesis | No había | **H1** (INF pública vs. privada; Mann-Whitney, r), **H2** (DER–CNF; Spearman), **H3** (consentimiento × tipo; chi-cuadrado o Fisher, V de Cramér), con sus H0; α = 0,05 | Cap. 3 §Hipótesis; Cap. 4 (`tab:res_hipotesis`) |
| Plan de análisis | Descriptivos y chi-cuadrado | Tabla de pruebas: frecuencias; mediana y RIC; **KS-Lilliefors**; **chi-cuadrado/Fisher + V de Cramér**; **U de Mann-Whitney + r**; **Spearman**; índice documental; exploratorios con **Holm** | Cap. 3 (`tab:pruebas_estadisticas`) |
| Herramientas | Excel + script de Node | **Python 3.12 (pandas, SciPy, pingouin)**; verificación cruzada en **jamovi o JASP**; Forms sin correo; `analisis_documental.xlsx` | Cap. 3 |
| Scripts | `scripts/analisis_encuesta.js` | Carpeta **`analisis/`**: `config.py`, `limpieza.py`, `validacion.py`, `descriptivos.py`, `inferencial.py`, `graficos.py`, `exportar_latex.py`, `simular_datos.py`, `run_all.py`, `requirements.txt`, `README.md`, `datos/ejemplo_simulado.xlsx` y `datos/expertos_simulado.xlsx` (SIMULADOS). El script de Node se eliminó | `analisis/` |
| Pruebas de los scripts | — | `run_all.py --prueba`: 12 valores de referencia superados. `run_all.py --simulado`: flujo completo (420 respuestas simuladas; 13 excluidas por los filtros; columnas de correo y hora eliminadas; 5 inversos recodificados); figuras y tablas `.tex` compilan | `analisis/README.md` |
| Resultados (Cap. 4) | Tabla única de percepción | Tablas de Aiken por bloque, ajustes del piloto, confiabilidad (α, ω, KR-20), hechos, dimensiones (Mdn, RIC, KS, U, r), hipótesis y brechas con los pares ID–H | Cap. 4 |
| Brechas | Pares ID–IE | Pares ID03–H4, ID02–H5, ID05–H6, ID06–H7, ID14–H8, ID07–DER (≥ 4), ID08–H16 | Cap. 3; Cap. 4 |
| Bibliografía | 96 entradas | **108** (12 nuevas con DOI verificado en Crossref, salvo dos libros y Holm 1979): mcdonald1999test, hayes2020omega, mcneish2018alpha, kuder1937theory, mann1947test, spearman1904proof, lilliefors1967kolmogorov, fritz2012effect, vallat2018pingouin, virtanen2020scipy, mckinney2010pandas, holm1979simple | `referencias.bib` |
| Planificación | 38 tareas | 39 tareas (+ verificación cruzada en jamovi o JASP); tareas de Aiken, piloto y análisis actualizadas; Gantt regenerado | `planificacion/` |
| Entorno | Sin Python | Python 3.12.10 instalado para el usuario con winget, con autorización del autor; entorno virtual fuera del repositorio | — |
| `.gitignore` | — | Excluye `analisis/datos/respuestas.*`, `expertos.*`, `analisis/salida*/` y `__pycache__/` | `.gitignore` |

PDF: **133 páginas, 0 errores, 0 referencias indefinidas**. Se mantiene la regla sin rojo: lo pendiente va como "---" con una nota de corte, aunque la instrucción pedía `[PENDIENTE]`.

---

# CAMBIOS — Reestructuración sin caso de estudio (2026-11-07)

Rama `reestructuracion-sin-caso`, creada desde `main` (`4b4d67b`). Instrucción: `uploads/reestructuracion_tesis.md`, autorizada por el autor (incluye el título, el objetivo general y los objetivos específicos). Plan: `PLAN_REESTRUCTURACION.md`.

## Qué cambió y por qué

**Motivo.** La UTI no dará acceso a sus datos internos, así que el caso de estudio (admisión y matrícula, sede Quito) no es viable. La tesis pasa a ser una investigación con **información pública de las universidades** y una **encuesta anónima solo a estudiantes**.

| Cambio | Detalle | Ubicación |
|---|---|---|
| Título | "Diagnóstico y gestión de riesgos en el tratamiento de datos personales de estudiantes universitarios en Ecuador conforme a la LOPDP" (EN: *Diagnosis and risk management in the processing of university students' personal data in Ecuador under the LOPDP*). Pendiente de aprobación de la tutora | `main.tex` |
| Objetivo general | Diagnosticar el cumplimiento de la LOPDP y del RLOPDP en el tratamiento de datos de estudiantes por las universidades ecuatorianas, mediante análisis documental y encuesta anónima, para proponer una guía de gestión de riesgos validada por expertos | Cap. 1 |
| 4 OE | OE1 Determinar requisitos → indicadores; OE2 Analizar la información pública; OE3 Aplicar la encuesta; OE4 Evaluar la brecha y proponer la guía | Cap. 1 |
| Esquema | 6 capítulos: 1 Introducción · 2 Fundamentación teórica y legal · 3 Metodología · 4 Resultados · 5 Propuesta y validación · 6 Conclusiones | `Capítulos/01`–`08` |
| Indicadores (OE1) | 16 documentales ID01–ID16 y 15 de percepción IE01–IE15, cada uno con su artículo de la LOPDP. Se verificaron en el texto oficial los arts. 8, 10, 12 (17 numerales), 13–17, 26 y 47–49 | Cap. 3, Tablas de indicadores |
| Componente documental | Censo de las 64 universidades (CES), ficha S/P/N con URL y fecha, índice ITD, reverificación del 20 % | Cap. 3; Anexo A; `analisis_documental/analisis_documental.xlsx` |
| Encuesta | N = 841 404 (2023, SIIES, citado por Sumba-Nacipucha y Sánchez-Bayón, 2025); n = 384 (+10 % = 423); muestreo no probabilístico con cuotas 64/36 y limitaciones declaradas; 6 dimensiones; validación con Aiken, piloto (n = 30) y Cronbach | Cap. 3; Anexos B–D; `encuesta/` |
| Ética de la encuesta | Anónima (sin nombre, cédula, correo, matrícula ni universidad), consentimiento con salida, filtro de 18+, minimización, almacenamiento cifrado y eliminación | Cap. 3, §Consideraciones éticas; Anexo C |
| Plan de análisis | Descriptivos, chi-cuadrado y V de Cramér (Fisher si hay esperados < 5), brechas C_D, B_N y B_P en 7 pares | Cap. 3; `encuesta/plan_analisis.md`; `scripts/analisis_encuesta.js` |
| Resultados | Estructura completa (validación, documental, encuesta, brechas), con "---" y nota de corte; nada inventado | Cap. 4 |
| Propuesta | Guía de 6 fases (P, 0–4) que reutiliza la metodología y la plantilla; 14 escenarios sectoriales R-01…R-14, cada uno con su indicador activador; criterio de activación fijado de antemano | Cap. 5; `matriz/escenarios_sectoriales.json`; `matriz/Matriz_escenarios_sectoriales.xlsx` |
| Validación | V1 Delphi calibrado (K, Brier, Kendall) sobre los escenarios; V2 juicio de expertos sobre la guía; IV01–IV10 (IV01–IV05 cumplidos) | Cap. 5 |
| Plantilla `.xlsx` | Generalizada: sin referencias a admisión y matrícula ni a la UTI; fórmulas sin cambios (1 057, 0 errores) | `scripts/build_matriz.js` |
| Cronograma | 9-11-2026 a 26-02-2027 (16 semanas) | Cap. 3, Figura de cronograma |
| Presupuesto | USD 80 (IA, 4 meses × 20). Se elimina la movilidad porque no hay visitas | Cap. 3 |
| Material descartado | Caps. 1–4, anexos, resumen, abstract y glosario anteriores; `REQUISITOS_DIAGNOSTICO.md`; `escenarios_candidatos_UTI.json`; `Matriz_UTI_preliminar.xlsx` | `descartado/caso_estudio/` |
| Bibliografía | 13 entradas nuevas en IEEE (DOI verificados en Crossref o publicación oficial): sumba2025economia, senescyt2025matricula, cochran1977sampling, agresti2019categorical, likert1932technique, cronbach1951coefficient, taber2018cronbach, johanson2010pilot, ifenthaler2016student, slade2013learning, brown2020whose, correia2025privacy, maguraushe2024model | `referencias.bib` |
| Formato | Se mantiene la regla del autor del 27-10-2026: nada en rojo en el PDF. Lo no disponible va en negro ("---" + nota). La instrucción nueva pedía `\textcolor{red}{[PENDIENTE]}`; prevalece "sigue el formato como lo venías haciendo" | Todo el documento |

Estado final: **0 errores**, **0 referencias indefinidas**, `main.pdf` de **126 páginas** (antes: 128).

## Estado de las indicaciones A1–A8, B1–B7 y C1–C16 tras el cambio de enfoque

Leyenda: **Vigente** (se conserva tal como estaba) · **Adaptada** (se conserva con otro objeto) · **Obsoleta** (dependía del caso de estudio).

| ID | Estado | Cómo queda |
|---|---|---|
| A1 | Vigente | Plazos de 5 días, 3 días y 72 h verificados; Tabla de plazos en el Cap. 2 (§Régimen de vulneraciones) y procedimiento de respuesta en el Cap. 5 |
| A2 | Adaptada | El problema se respalda con cifras con corte (64 universidades, 841 404 estudiantes, más de 1 150 DPD, denuncias, sanciones) y con la falta de una medición oficial del cumplimiento, que el estudio produce |
| A3 | Adaptada | Fase P y equivalencia con ISO 31000/27005, ISO/IEC 27035-1 y NIST SP 800-61r3 como marco de referencia de la guía (Cap. 2, Tabla de equivalencia; Cap. 5) |
| A4 | Obsoleta | Ya no hay institución del caso ni carta de aval. Se reemplaza por la verificación de los requisitos éticos de la UTI para la encuesta (PENDIENTES n.º 2) |
| A5 | Vigente | SISPDP, clasificación de vulneraciones y comunicación a titulares en el Cap. 2; indicador IE14 (vulneración comunicada) |
| A6 | Adaptada | Dos instancias de validación (V1 Delphi, V2 juicio sobre la guía) más la validación del instrumento; IV01–IV10 con metas; V de Aiken |
| A7 | Adaptada | Nuevos verbos de Bloom (Determinar, Analizar, Aplicar, Evaluar). El objetivo general sí cambió, con autorización expresa del autor (07-11-2026) |
| A8 | Vigente | Guiones, numeración, IEEE y ampliación de la bibliografía (13 entradas nuevas) |
| B1 | Adaptada | Lo que eran resultados del diagnóstico institucional, escenarios y matriz pasa a ser resultados documentales y de la encuesta (Cap. 4) y escenarios sectoriales con riesgo inherente y residual (Cap. 5). Estructura completa; datos por levantar |
| B2 | Vigente | Delphi, calibración (Brier, K) y juicio de expertos sobre la guía (Cap. 5); resultados por obtener |
| B3 | Vigente | Criterios de probabilidad e impacto, fuentes (ahora incluyen las brechas del diagnóstico) y reglas RA-1…RA-5 (Cap. 5) |
| B4 | Adaptada | La trazabilidad ya no tiene roles de la UTI: escenario → artículo → control → rol tipo → plazo (regla) → indicador (Cap. 5); trazabilidad de la investigación OE → capítulo → instrumento → indicador → evidencia (Cap. 3) |
| B5 | Vigente | Pruebas técnicas (1 057 + 1 410 fórmulas; T-01…T-06; autoprueba del script) separadas de la validación metodológica (Cap. 5) |
| B6 | Vigente | Una conclusión por OE, sin generalizar más allá de la muestra (Cap. 6) |
| B7 | Vigente | Consistencia formal; matriz de consistencia rehecha (Anexo K) |
| C1 | Vigente | Justificación con valores numéricos (Cap. 1) |
| C2 | Vigente | Instituciones por nivel (16 161; por sostenimiento; 1 861 CDI; 64 universidades; 216 institutos) |
| C3 | Vigente | Obligación de todas según los arts. 2, 4, 23, 24 y 48 (Cap. 1) |
| C4 | Vigente | Más de 1 150 DPD (abril de 2025); la cifra oficial de 2026 sigue pendiente |
| C5 | Vigente | Denuncias (85 y 191) y sanciones; no hay estadística de vulneraciones del sector |
| C6 | Adaptada | No existe el porcentaje oficial. **El censo documental lo producirá** para las 64 universidades (ID01, ITD) |
| C7 | Adaptada | OE1 = determinar con precisión qué se mide (31 indicadores con artículo) |
| C8 | Vigente | OE2 = universidades (censo documental) |
| C9 | Adaptada | OE3 = aplicar (la encuesta), en lugar de implementar en la UTI |
| C10 | Vigente | Exactamente 4 OE |
| C11 | Vigente | OE4 = evaluar (brecha, Delphi y juicio de expertos) |
| C12 | Vigente | Fechas de corte explícitas (27-10-2026 para las cifras ya verificadas; 07-11-2026 para las nuevas) |
| C13 | Vigente | Términos legales con artículo (Cap. 2) |
| C14 | Vigente | Contraste de 6 países (Cap. 2) |
| C15 | Vigente | Cómo funciona una ley (Cap. 2) |
| C16 | Vigente | Etapa de Ecuador (cronología, Cap. 2) |

---

# CAMBIOS — Revisión del tribunal y de la tutora (2026-10-27)

Rama `revision-tribunal`. Leyenda: ✔ atendida · ⚠ parcial (la estructura está completa, pero falta un dato que solo puede aportar el autor o la institución) · ✘ pendiente.
Las fuentes se detallan en `FUENTES.md`; los datos faltantes, en `PENDIENTES.md`.

## A. Tabla de prioridades

| ID | Estado | Qué se hizo | Ubicación | Fuente |
|---|---|---|---|---|
| A1 | ✔ | Plazos verificados en el texto oficial. **5 días** (término): art. 43 LOPDP, notificación del responsable desde que tiene constancia, dirigida a la SPDP, al organismo de regulación y control y al CSIRT (reforma de la LOFC de 2026). **2 días**: del encargado al responsable. **3 días**: a los titulares (art. 46). **72 horas**: no pertenece a la LOPDP; es el art. 20-G de la Ley Orgánica de Transformación Digital y Audiovisual (añadido por la LOFC), corre desde la detección y obliga a entidades públicas y operadores de infraestructura crítica digital. **Corrección:** el documento solo mencionaba "5 días a la autoridad"; se añadieron destinatarios, sujetos obligados e inicio del cómputo. | Cap. 1 → Contexto meso; Cap. 1 → Fundamentación → Régimen de vulneraciones (Tabla de plazos); Cap. 3 → Fase 4 | LOPDP RO 5S 459 (arts. 43, 46); LOFC RO 5S 290, 22-05-2026 (arts. 6 y 14); RLOPDP arts. 24–28 |
| A2 | ⚠ | Planteamiento y justificación respaldados con cifras con fecha de corte: 16 161 IE (2024-2025), 15 400 (2025-2026), 64 universidades, 216 institutos, 1 861 CDI, más de 1 150 DPD, 85 y 191 denuncias, primeras sanciones. Falta el % de universidades que implementaron la ley (no existe dato oficial). | Cap. 1 → nueva §"El sector educativo ecuatoriano en cifras" (Tabla de cifras); Planteamiento; Justificación | MINEDUC (vía El Diario), CNII 2025, CES, IT Ahora, Primicias |
| A3 | ✔ | Fase P (preparación) añadida a la metodología (figura, tabla de fases y Cap. 3). Nueva tabla de equivalencia: metodología ↔ ISO 31000/ISO/IEC 27005 ↔ ISO/IEC 27035-1:2023 ↔ NIST SP 800-61r3 (CSF 2.0). | Cap. 2 → Diseño → Estructura; §Equivalencia con marcos; Cap. 3 → Fase P | ISO/IEC 27035-1/2:2023; NIST SP 800-61r3 (abr. 2025) |
| A4 | ⚠ | Institución definida: UTI, sede Quito, proceso de admisión y matrícula. La autorización formal se incorporó como anexo y como requisito D01, en rojo, con la lista de condiciones que debe cubrir. **Falta el oficio.** | Cap. 2 → Tabla de caracterización, requisitos D01, ética (a); nuevo Anexo "Autorización institucional"; PENDIENTES.md n.º 1 | — |
| A5 | ⚠ | Se incorporaron el SISPDP, la clasificación de vulneraciones (C/I/D; temporal, permanente o irreversible), la comunicación a titulares (contenido mínimo, excepciones del art. 46) y el contenido de la notificación (art. 26 RLOPDP). La clasificación detallada de la Res. 0040-R se tomó de fuentes secundarias y está marcada `[VERIFICAR]`. | Cap. 1 → Régimen de vulneraciones; Cap. 3 → Fase 4; Anexo del simulacro | Res. SPDP-SPD-2026-0040-R (RO 1S 376, 24-09-2026, vía Lexis y AVL); RLOPDP arts. 24–28 |
| A6 | ⚠ | Validación reforzada: dos escenarios (V1, aplicación real; V2, simulacro de vulneración); 12 indicadores con fórmula, meta, resultado y cumplimiento; juicio de expertos con V de Aiken. IV01–IV03 cumplidos; IV04–IV12 pendientes de aplicación. | Cap. 3 → §Validación metodológica (Tabla de indicadores de validación); Anexo del simulacro | Aiken (1985); Kendall y Babington Smith (1939) |
| A7 | ✔ | OE reescritos con verbos de Bloom (Diagnosticar, Analizar, Implementar, Evaluar). **El objetivo general no se modificó** (verificado byte a byte frente a `ba4ed8e`). | Cap. 1 → Objetivos | Indicación de la tutora |
| A8 | ✔ | Guiones normalizados (rangos con `--`, incisos con `---`, sin rayas Unicode sueltas); artículos exactos en la lista de verificación (Anexo A); 24 entradas nuevas en formato IEEE; referencias cruzadas sin indefinidas; tabla comparativa en página horizontal; cajas desbordadas corregidas (rutas con `\path`, firmas y tablas). | Todo el documento; `referencias.bib`; Anexo A | — |

## B. Observaciones del tribunal

| ID | Estado | Qué se hizo | Ubicación | Fuente |
|---|---|---|---|---|
| B1 | ⚠ | Estructura completa para los resultados del diagnóstico (madurez y verificación normativa), escenarios (13) y matriz con tablas **separadas** de riesgo inherente y residual (13 filas cada una). Los valores dependen del levantamiento: `[PEND.]` en rojo. | Cap. 3 → Fase 0 (Tablas de madurez y de verificación normativa); Fase 2 (riesgo inherente); Fase 3 (riesgo residual) | — |
| B2 | ⚠ | Delphi, calibración y juicio de expertos especificados: coeficiente K = ½(Kc + Ka), criterio de consenso (RIC ≤ 1 y ≥ 70 % a ±1 nivel), W de Kendall con χ², ponderación por Brier (ecuación) y V de Aiken (ecuación). Formatos de reporte por experto, por ronda y por criterio. La validez **no** se afirma sin evidencia. | Cap. 2 → Delphi y juicio de expertos; Cap. 3 → Método Delphi y Juicio de expertos; nuevo Anexo de competencia | Cabero y Barroso (2013); Aiken (1985); Kendall (1939); Brier (1950) |
| B3 | ✔ | Estimaciones justificadas: tabla de fuentes de información y reglas por variable, ecuación del impacto ajustado, nivel como función de decisión N = T(P, I_aj), agravante (b) anclado al Modelo Técnico de Gran Escala y reglas de aceptación RA-1 a RA-5 con plazos. | Cap. 2 → Modelo de estimación; Determinación del nivel | Guía SPDP v2; Res. 0005-R; ENISA |
| B4 | ✔ | Nueva tabla de trazabilidad: escenario → artículo → control ISO/IEC 27002 → rol responsable → regla de plazo → indicador y frecuencia (13/13). Roles propuestos, a confirmar por la institución. | Cap. 3 → §Trazabilidad del plan de tratamiento | LOPDP, RLOPDP, ISO/IEC 27002:2022 |
| B5 | ✔ | Pruebas técnicas (fórmulas, casos T-01…T-06, requisitos en el diseño) separadas de la validación metodológica en secciones distintas, con texto explícito sobre la diferencia. | Cap. 3 → §Pruebas y Validación vs. §Validación Metodológica | — |
| B6 | ✔ | Conclusiones reescritas: una por OE, con resultados verificables y separación explícita entre lo verificado y lo pendiente; limitaciones; recomendaciones derivadas; trabajos futuros. Sin generalizar fuera del caso. | Cap. 4 | — |
| B7 | ⚠ | Resumen y abstract (≤ 300 palabras) y descriptores; glosario completo; matriz de consistencia; vigencia de normas revisada (ISO/IEC 27005:2022, 27002:2022, 27701:2025, 29134:2023, 27035-1/2:2023, NIST SP 800-61r3; NIST PF 1.1 sigue en borrador, se mantiene 1.0). **Pendientes del autor:** dedicatoria, agradecimiento y fechas de firma (en rojo). | Preliminares 05, 06, 08, 09 y 01–04; Glosario; Anexo "Matriz de consistencia" | — |

## C. Indicaciones de la tutora (27/10/2026)

| ID | Estado | Qué se hizo | Ubicación | Fuente |
|---|---|---|---|---|
| C1 | ✔ | Valores numéricos incorporados en la justificación (280 IES, ≤ 7,0 % de cobertura de DPD, multas del 0,7–1 %, USD 454 500 en las primeras sanciones) y en el planteamiento. | Cap. 1 → Justificación; Planteamiento | CES; IT Ahora; LOPDP art. 72; Primicias |
| C2 | ⚠ | Instituciones educativas: 16 161 (2024-2025) y 15 400 (2025-2026); CDI en convenio: 1 861; universidades: 64; institutos: 216. **Falta** el desglose por sostenimiento (AMIE) y el número de CDI directos del MIES. | Cap. 1 → Tabla de cifras del sector | MINEDUC (vía El Diario); CNII 2025; CES |
| C3 | ✔ | Argumentado con base legal que todas tienen la obligación: LOPDP arts. 2, 4, 23, 24, 25 y 48; Res. 0005-R arts. 12 y 14; LOFC art. 8. | Cap. 1 → §Cifras (2.º párrafo) | LOPDP; Res. 0005-R; LOFC |
| C4 | ⚠ | Más de 1 150 DPD registrados (abril de 2025) y cálculo de cobertura máxima del 7,0 %. **Falta** la cifra oficial de 2026 (posterior al registro privado). | Cap. 1 → §Cifras | IT Ahora (2025); Res. 0028-R |
| C5 | ⚠ | Estadísticas: 85 denuncias (abr. 2025), 191 (sep. 2025), primeras sanciones (dic. 2025). **Falta** la estadística de vulneraciones notificadas (la ley obliga a la SPDP a llevarla, art. 76 num. 14, pero no se publica). | Cap. 1 → §Cifras | IT Ahora; Primicias |
| C6 | ⚠ | No existe un informe oficial con el porcentaje de universidades que implementaron la ley; se declara como vacío y se usa como argumento de la brecha. **Falta** el dato (fuente sugerida en PENDIENTES.md). | Cap. 1 → §Cifras; Cap. 4 → Trabajos futuros | Piray et al. (2026) |
| C7 | ✔ | OE1 redactado para determinar con precisión qué se necesita y ejecutarlo; tabla de requisitos D01–D10 y `REQUISITOS_DIAGNOSTICO.md`. | Cap. 1 → Objetivos; Cap. 2 → §Requisitos para ejecutar el diagnóstico | — |
| C8 | ✔ | OE2 centrado en las universidades (situación, porcentaje si existe, referentes) y su traducción a decisiones de diseño. | Cap. 1 → Objetivos; Cap. 2 → §Insumos del análisis de universidades | — |
| C9 | ✔ | OE3 = implementar (escenarios, matriz inherente/residual, plan de tratamiento). | Cap. 1 → Objetivos; Cap. 3 | — |
| C10 | ✔ | Exactamente 4 OE; trazabilidad, DSR, técnicas, cronograma, anexos y script actualizados. | Cap. 1–4; Anexos; `scripts/build_matriz.js` (comentario) | — |
| C11 | ✔ | OE4 = evaluar (Delphi, calibración, juicio de expertos, indicadores con metas). | Cap. 1 → Objetivos; Cap. 2–3 | — |
| C12 | ✔ | Fecha de corte explícita en cada cifra y en las tablas de cronología y plazos (corte: 27-10-2026). | Cap. 1 → Tabla de cifras, cronología, plazos | — |
| C13 | ✔ | Tabla de términos legales con artículo exacto: dato personal, sensibles, categorías especiales, NNA, titular, tratamiento, responsable, encargado, DPD (definición, obligatoriedad, funciones, requisitos), vulneración, EIPD, RAT, autoridad. | Cap. 1 → Fundamentación → §Términos legales | LOPDP arts. 4, 21, 24, 25, 42, 48, 49, 76, 77; RLOPDP arts. 29–32, 38–41, 48, 55 |
| C14 | ⚠ | Tabla comparativa con 6 países y 6 criterios (año, autoridad, DPD, plazo de notificación, sanciones, menores y educación). Cinco celdas de Perú, Brasil y Colombia están marcadas `[VERIFICAR]` porque no se pudo consultar el texto oficial. | Cap. 1 → §Contraste con otros países (página horizontal) | RGPD; LOPDGDD; Ley 1581 y guía SIC; Ley 29733 y D.S. 016-2024-JUS; Ley 21.719 (Diario Oficial); LGPD y Res. CD/ANPD 15/2024 |
| C15 | ✔ | Cómo funciona una ley: jerarquía (Const. art. 425), ley orgánica (art. 133), reglamento, resoluciones de la SPDP (art. 76 num. 5), normas técnicas voluntarias (art. 37), vigencia y régimen transitorio. | Cap. 1 → Fundamentación → §Cómo funciona una ley | Constitución 2008; LOPDP |
| C16 | ✔ | Etapa actual: cronología verificada (2008 → 24-09-2026) y caracterización como "consolidación regulatoria con aplicación incipiente". | Cap. 1 → Fundamentación → §Etapa actual (Tabla de cronología) | Constitución; LOPDP; RLOPDP; CPCCS; resoluciones SPDP; LOFC |

## Otros cambios

- `main.tex`: paquetes `xcolor` y `pdflscape`; macros `\pend{}` (dato pendiente, rojo) y `\verif{}` (verificar contra texto oficial, rojo).
- Nuevos anexos: autoevaluación de competencia (K), protocolo del simulacro (V2), matriz de consistencia y autorización institucional.
- Anexo F: criterios reagrupados en pertinencia, claridad, suficiencia y coherencia, con V de Aiken.
- Compilación final: 0 errores, 0 referencias indefinidas, 127 páginas. Quedan cajas desbordadas menores: el árbol de problemas (conocida e inofensiva) y dos párrafos de 10–15 pt en el Cap. 2.
- Incidente: a las 15:23 un proceso externo sobrescribió `Capítulos/01_Introducción.tex` con una versión antigua. Por decisión del autor se restauró desde `ba4ed8e` y se reaplicaron los cambios. La copia sobrescrita quedó en el scratchpad de la sesión.

## Actualización del 2026-10-27 (noche): documento sin marcas en rojo

A pedido del autor, el PDF ya no contiene marcas `[PENDIENTE]`, `[VERIFICAR]` ni texto en rojo:
- **Datos encontrados e incorporados:**
  - instituciones por sostenimiento (12 389 fiscales, 617 fiscomisionales, 112 municipales, 3 022 particulares; MINEDUC, Estadística Educativa vol. 5);
  - rendición de cuentas 2025 de la SPDP (49 trámites de titulares, 22 de 48 convenios);
  - Colombia (Decreto 1377/2013, art. 23);
  - Perú (multas hasta 100 UIT, art. 39 de la Ley 29733);
  - Brasil (dispensa del encargado, Res. CD/ANPD 2/2022, art. 11; art. 14 de la LGPD).
- **Datos que no existen publicados:** se redactan en negro como "no se halló … al 27 de octubre de 2026". Son el número de CDI directos del MIES, los DPD registrados en 2026, las vulneraciones del sector educativo, el porcentaje de universidades y la regla peruana sobre menores.
- **Resultados de la UTI aún no levantados:** en las tablas aparecen como "---", con una nota en negro sobre la fecha de corte; en el texto, como "no disponible a la fecha de corte". No se inventó ningún valor.
- **Preliminares:** se redactaron una dedicatoria y un agradecimiento breves, que el autor puede ajustar, y las fechas de firma quedan como línea en blanco.
- **Objetivos específicos:** sin las etiquetas en negrita.
- **Cronograma:** ajustado al periodo real (13-10-2026 a 26-02-2027, 20 semanas), con el presupuesto reducido a movilidad y uso de agentes de IA (USD 160). Planificación detallada en `planificacion/` (CSV para Jira y guía).
