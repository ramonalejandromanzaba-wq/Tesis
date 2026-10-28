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
