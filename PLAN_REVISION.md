# PLAN DE REVISIÓN — ITI-TFG-B26-0021

Rama: `revision-tribunal` · Fecha: 2026-10-27 · Fuente de las indicaciones: `indicaciones_revision.md` (raíz del repo).

## 1. Contexto obtenido de los CLAUDE.md

| Archivo | Contexto relevante aplicado |
|---|---|
| `CLAUDE.md` (raíz) | Compilación con `pdflatex → bibtex → pdflatex ×2` (latexmk **no** funciona: falta Perl; prevalece sobre la indicación de usar latexmk). Estructura de carpetas, plantilla UTI (`uti_tfm.sty`, no editar), IEEE con `\cite`, títulos de normas en `.bib` con doble llave. Caso de estudio = admisión y matrícula UTI Quito; ningún dato institucional se estima (`[PENDIENTE]`). Estilo de ensayo argumentativo (tesis explícita, cierre "En síntesis…", objeción). En sed, `\U` rompe macros `\UTI…`: editar con Edit. |
| `CLAUDEs.md` (raíz) y `../CLAUDEs.md` (copia idéntica) | Manda sobre lo demás: no inventar normas, artículos, cifras ni referencias (`[VERIFICAR]`/`[CITA PENDIENTE]`); reglas de la Guía SPDP v2 (rationales, escalas = etiquetas, C/I/D separados, lapso anual, inherente vs. residual, baja probabilidad/alto impacto); exclusiones del proyecto; ética (sin datos reales, códigos E01…, conflicto de interés sysadmin). |
| Subcarpetas | No existen CLAUDE.md en subcarpetas. |
| `~/.claude/CLAUDE.md` | No existe. |

Prevalencia: este plan sigue `indicaciones_revision.md`, salvo convenciones técnicas de compilación/repositorio (CLAUDE.md). La autorización expresa del autor permite reducir los OE de 5 a 4 (indicación de la tutora, 27/10/2026). El **objetivo general vigente** (`Capítulos/01_Introducción.tex`, §Objetivo General) **no se toca**.

Estado inicial: compila sin errores, 90 páginas, sin referencias indefinidas.

## 2. Objetivos específicos nuevos (4)

1. **OE1 – Diagnóstico.** Diagnosticar el tratamiento de datos personales del proceso de admisión y matrícula de la Universidad Tecnológica Indoamérica, sede Quito, mediante la determinación precisa de los requisitos normativos, la información, los instrumentos, las fuentes y los actores necesarios, y su aplicación en revisión documental, entrevistas semiestructuradas y un cuestionario de madurez, para establecer la línea base de cumplimiento respecto de la LOPDP (2021) y su Reglamento General (2023).
2. **OE2 – Universidades.** Analizar la situación de implementación de la protección de datos personales en las universidades ecuatorianas y los referentes normativos y metodológicos nacionales e internacionales, mediante la revisión de fuentes oficiales, estudios indexados y marcos de gestión de riesgos, para fundamentar las fases y los criterios de la metodología.
3. **OE3 – Implementar.** Implementar la metodología en el proceso de admisión y matrícula de la Universidad Tecnológica Indoamérica, sede Quito, mediante la identificación de escenarios de riesgo, su estimación con criterio de expertos y su registro en una matriz de riesgos inherentes y residuales, para formular un plan de tratamiento con controles, responsables, plazos e indicadores trazables a la LOPDP.
4. **OE4 – Evaluar.** Evaluar la metodología mediante un panel Delphi con expertos calibrados, juicio de expertos e indicadores con metas, para determinar su validez y aplicabilidad y formular recomendaciones de mejora continua alineadas a la LOPDP y a la normativa de la SPDP.

Reasignación: antiguo OE1 → OE1; antiguo OE2 (diseño de fases) → se absorbe en el objetivo general y se fundamenta en OE2; antiguos OE3 y OE4 (aplicación y matriz) → OE3; antiguo OE5 (recomendaciones y validación) → OE4.

## 3. Mapa del documento (estado inicial)

| Archivo | Contenido | Estado |
|---|---|---|
| `main.tex` | Portada, paquetes, `\input` | OK; falta macro `\pend` |
| `Preliminares/01–04` | Autorización, aprobaciones, declaración | Fechas `xx` (dato del autor) |
| `Preliminares/05–06` | Dedicatoria, agradecimiento | Texto de plantilla (dato del autor) |
| `Preliminares/07` | Índices | OK |
| `Preliminares/08–09` | Resumen / Abstract | Texto de plantilla |
| `Capítulos/01_Introducción.tex` | Contexto macro/meso/micro, estado del arte (Tablas 1–3), problema, árbol, justificación, objetivos (5 OE), alcance, fundamentación | Sin cifras del sector educativo; 5 OE; fundamentación breve |
| `Capítulos/02_Metodología.tex` | Diagnóstico UTI, DSR, técnicas, Delphi/Brier, ética, RF/RNF, diseño fases 0–4, escalas, decisión, aceptación | Sin fase de preparación, sin equivalencia ISO 27035/NIST, estimaciones parcialmente justificadas |
| `Capítulos/03_Implementación.tex` | Protocolo por fase, RAT, 13 escenarios, controles, indicadores, pruebas T-01…T-06, validación (pendiente), cronograma, presupuesto | Pruebas técnicas y validación mezcladas; sin trazabilidad completa; sin metas de validación |
| `Capítulos/04_Conclusiones.tex` | — | Texto de plantilla |
| `Capítulos/06_Glosario.tex` | — | Texto de plantilla |
| `Anexos/01_Anexo.tex` | Anexos A–H | Referencias a OE antiguos |
| `referencias.bib` | 55 entradas (6 de plantilla no citadas) | Faltan fuentes nuevas |

## 4. Cambios por ubicación exacta

| # | Indicaciones | Archivo → sección | Cambio |
|---|---|---|---|
| 1 | — | `main.tex` (preámbulo) | Macro `\pend{…}` = `\textcolor{red}{[PENDIENTE: …]}` |
| 2 | A1, C12 | Cap. 1 → Contexto meso (párrafo arts. 37/40/42/43) | Plazos verificados: 5 días (art. 43, reformado por LOFC, RO 5.º Supl. 290, 22-05-2026: SPDP + organismo de control + CSIRT); encargado → responsable 2 días; titulares 3 días (art. 46); 72 h = art. 20-G de la Ley Orgánica de Transformación Digital y Audiovisual (sujetos: entidades públicas y operadores de infraestructura crítica digital) |
| 3 | A2, C1–C6, C12 | Cap. 1 → nueva subsección "El sector educativo ecuatoriano en cifras" (contexto micro) | Instituciones (MINEDUC 2024-2025/2025-2026), CDI (CNII 2025), IES (CES), base legal de obligación (LOPDP arts. 2, 4, 23, 24, 25, 48; Res. 0005-R), DPD registrados, denuncias y sanciones, % universidades = `\pend`; Tabla de cifras con fecha de corte; cierre con la brecha |
| 4 | A2 | Cap. 1 → Planteamiento + Justificación | Párrafos con valores numéricos y brecha |
| 5 | A7, C7–C11 | Cap. 1 → Preguntas directrices, Objetivos, Alcance | 4 OE y 4 preguntas; OG intacto |
| 6 | C13 | Cap. 1 → Fundamentación → "Términos legales" | Tabla de definiciones con artículo exacto (LOPDP art. 4, 25, 48–49; RLOPDP arts. 48, 55) |
| 7 | C15 | Cap. 1 → Fundamentación → "Cómo funciona una ley en Ecuador" | Const. art. 425, ley orgánica, reglamento, resoluciones SPDP, vigencia, régimen transitorio |
| 8 | C16, C12 | Cap. 1 → Fundamentación → "Etapa actual" | Cronología verificada con corte a octubre de 2026 |
| 9 | C14 | Cap. 1 → Fundamentación → tabla comparativa | RGPD/España, Colombia, Perú, Chile, Brasil, Ecuador (6 criterios) |
| 10 | A1, A5 | Cap. 1 → Fundamentación → "Gestión de vulneraciones" | Tabla de plazos; SISPDP; clasificación (C/I/D; temporal/permanente/irreversible); comunicación a titulares (contenido mínimo, excepciones art. 46) |
| 11 | A3 | Cap. 2 → Diseño → estructura | Fase P de preparación; figura y Tabla de fases actualizadas; nueva tabla de equivalencia con ISO/IEC 27005/31000, ISO/IEC 27035-1:2023 y NIST SP 800-61r3 |
| 12 | C7, OE1 | Cap. 2 → nueva subsección "Requisitos para ejecutar el diagnóstico" + `REQUISITOS_DIAGNOSTICO.md` | Tabla: requisito, fuente, instrumento, actor, estado |
| 13 | A4 | Cap. 2 → Tabla de caracterización + Ética; Anexo nuevo (autorización) | Autorización formal UTI como anexo `\pend`; prioridad 1 en PENDIENTES.md |
| 14 | B3 | Cap. 2 → Modelo de estimación | Fuentes de información por variable, ecuaciones del impacto ajustado y del nivel (función de tabla), agregación Delphi ponderada, reglas de clasificación y aceptación numeradas |
| 15 | A6, B2, OE4 | Cap. 2 → Delphi | Perfil, coeficiente K = ½(Kc + Ka), rondas, consenso (RIC ≤ 1 y ≥ 70 % de acuerdo; W de Kendall), V de Aiken |
| 16 | — | Cap. 2 → Tablas DSR y técnicas | OE renumerados |
| 17 | B1, B4 | Cap. 3 → Fases 0–3 | Tablas de diagnóstico, inherente y residual separadas (`\pend`); nueva tabla de trazabilidad escenario → artículo → control → responsable (rol) → plazo → seguimiento |
| 18 | A5 | Cap. 3 → Fase 4 | Procedimiento de respuesta con SISPDP, CSIRT, clasificación y comunicación a titulares |
| 19 | A6, B2, B5 | Cap. 3 → Pruebas y Validación | Separación: (a) pruebas técnicas; (b) validación metodológica con 2 escenarios (V1 aplicación real; V2 simulacro de vulneración), tabla de indicadores con fórmula/meta/resultado/cumple, Delphi por ronda, juicio de expertos (V de Aiken) |
| 20 | — | Cap. 3 → Cronograma | Etiquetas OE1–OE4 |
| 21 | B6 | Cap. 4 | Una conclusión por OE, limitaciones, recomendaciones, trabajo futuro |
| 22 | B7 | Preliminares 05–09 | Resumen y Abstract (≤ 300 palabras), descriptores; dedicatoria/agradecimiento `\pend` |
| 23 | B7 | Glosario | Términos y siglas |
| 24 | B7 | Anexos | OE renumerados; Anexo F con criterios pertinencia/claridad/suficiencia/coherencia; nuevos anexos: autoevaluación de competencia (Kc, Ka), protocolo del simulacro V2, matriz de consistencia, autorización institucional |
| 25 | A8, B7 | Todo el documento + `.bib` | Guiones (rangos con `--`, incisos con `---`), referencias cruzadas, entradas nuevas IEEE verificadas, vigencia de normas |
| 26 | — | `scripts/build_matriz.js` (comentario línea 1) | "OE4" → "OE3" |
| 27 | Cierre | Raíz | `CAMBIOS.md`, `PENDIENTES.md`, `FUENTES.md`, `REQUISITOS_DIAGNOSTICO.md`; actualizar `CLAUDE.md`, `CLAUDEs.md` y `../CLAUDEs.md` |

## 5. Orden de ejecución

1. Preámbulo (`\pend`) y `.bib` con las fuentes nuevas verificadas.
2. Cap. 1 (cambios 2–10).
3. Cap. 2 (11–16).
4. Cap. 3 (17–20).
5. Cap. 4, Preliminares, Glosario (21–23).
6. Anexos (24) y script (26).
7. Revisión formal (25); compilación hasta 0 errores y 0 referencias indefinidas.
8. Archivos de control y CLAUDE.md (27); commit en `revision-tribunal`.

## 6. Reglas de integridad aplicadas

- Toda cifra lleva fuente y fecha de corte; lo no verificable en fuente oficial queda en rojo con `\pend{…}` y en `PENDIENTES.md`.
- Ningún resultado empírico de la UTI, del Delphi ni del juicio de expertos se redacta: se dejan estructura, fórmulas, criterios y tablas con `\pend`.
- Las fuentes secundarias (prensa, firmas jurídicas) se usan solo cuando no hay fuente oficial accesible y se identifican como tales en `FUENTES.md`.
