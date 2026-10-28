# PENDIENTES — Datos que debe aportar el autor (por prioridad)

> Desde el 27-10-2026 (noche), el PDF ya no muestra marcas en rojo. Lo que no está disponible aparece en negro como "no disponible a la fecha de corte" o "no se halló". Esta lista sigue indicando qué falta para completar los resultados.

Corte: 2026-10-27. En el PDF, cada pendiente aparece en **rojo** (`\pend{…}`, `[PEND.]`, `[PENDIENTE]` o `[VERIFICAR: …]`). Al cargar un dato real, sustituye la marca y actualiza `CAMBIOS.md`.

## Prioridad 1: bloquea todo lo demás

| # | Dato | Dónde va | Cómo obtenerlo |
|---|---|---|---|
| 1 | **Oficio de autorización formal de la UTI** para el estudio en admisión y matrícula, sede Quito: instancia, fecha, alcance, condiciones y enlace designado | Anexo "Autorización institucional"; Cap. 2, Tabla de caracterización y requisito D01; Cap. 3, Fase P | Solicitud al Rectorado o la instancia que la UTI indique, con la tutora; usar las condiciones (a)–(e) del anexo |
| 2 | Visto bueno de la tutora a los **4 objetivos específicos nuevos** (redactados en `PLAN_REVISION.md` §2) | Cap. 1 → Objetivos | Revisión con la tutora |

## Prioridad 2: diagnóstico (OE1). Detalle en `REQUISITOS_DIAGNOSTICO.md`

| # | Dato | Dónde va |
|---|---|---|
| 3 | Volumen de aspirantes por periodo y proporción de menores de edad (agregado) | Cap. 2, Tabla de caracterización; Cap. 3, dictamen de gran escala |
| 4 | Estudiantes matriculados en la sede Quito; becas y discapacidad declarada (agregados) | Cap. 2, Tabla de caracterización |
| 5 | Entrevistas por subproceso (SP1–SP6): finalidades, bases de legitimación, encargados y conservación | Cap. 3, Tabla RAT |
| 6 | Documentos: política y avisos de privacidad, formularios, contratos con encargados, tabla de conservación, matriz de accesos, procedimiento de incidentes | Cap. 3, Tabla de verificación normativa |
| 7 | Cuestionario de madurez respondido (20 ítems) | Cap. 3, Tabla de madurez |
| 8 | Historial agregado de incidentes (3 años) | Cap. 2, Tabla de fuentes de estimación |
| 9 | Existencia y registro del DPD de la UTI | Requisito D09 |
| 10 | Número de informantes por subproceso | Cap. 3, Fase P |

## Prioridad 3: implementación y evaluación (OE3, OE4)

| # | Dato | Dónde va |
|---|---|---|
| 11 | Panel de ≥ 5 expertos: perfil, años, Kc, Ka, K y respuestas de calibración (Brier) | Cap. 3, Tabla del panel; hoja Brier |
| 12 | Rondas Delphi: mediana, RIC, consenso y W de Kendall por ronda | Cap. 3, Tabla de rondas Delphi; hoja Delphi |
| 13 | Probabilidad, impacto, agravantes y rationale por escenario (inherente) | Cap. 3, Tabla de riesgo inherente; `matriz/escenarios_candidatos_UTI.json` |
| 14 | Opción de tratamiento y estimación residual por escenario | Cap. 3, Tabla de riesgo residual |
| 15 | Confirmación institucional de roles responsables y plazos | Cap. 3, Tabla de trazabilidad |
| 16 | Dictamen de gran escala y, si procede, EIPD | Cap. 3, Tabla de EIPD |
| 17 | Juicio de expertos: calificaciones V01–V12 y observaciones | Cap. 3, Tabla de juicio de expertos |
| 18 | Resultados del simulacro V2: tiempos y completitud de la notificación | Cap. 3, IV10 e IV11 |
| 19 | Resultados de IV04–IV12 | Cap. 3, Tabla de indicadores de validación; Cap. 4 |
| 20 | Tabla "antes/después" | Cap. 3, Tabla de comparación inicial/proyectada |

## Prioridad 4: cifras sectoriales no publicadas (C2–C6)

| # | Dato | Fuente sugerida |
|---|---|---|
| 21 | ✔ Resuelto (MINEDUC, vol. 5): instituciones educativas por sostenimiento (fiscal, fiscomisional, municipal, particular), ciclo 2024-2025 | Base AMIE del MINEDUC (educacion.gob.ec, "Datos abiertos"); el sitio dio error de certificado el 27-10-2026 |
| 22 | Número de CDI de atención directa del MIES | MIES / Ministerio de Desarrollo Humano; solicitud de acceso a la información |
| 23 | Número oficial de DPD registrados ante la SPDP en 2026 y su distribución por sector | Solicitud de acceso a la información pública a la SPDP |
| 24 | Vulneraciones notificadas a la SPDP por el sector educativo | Solicitud a la SPDP (art. 76 num. 14 LOPDP: registro estadístico) |
| 25 | % de universidades con política, DPD y RAT | Solicitud a SPDP, CES o CACES, o revisión propia de los sitios web de las 64 universidades |

## Prioridad 5: verificación contra texto oficial (`[VERIFICAR]`)

| # | Punto | Dónde |
|---|---|---|
| 26 | Criterios y niveles de clasificación de la Res. SPDP-SPD-2026-0040-R (texto oficial, RO 1S 376) | Cap. 1 → Régimen de vulneraciones |
| 27 | ✔ Resuelto: Colombia: obligación reglamentaria de designar una persona o área responsable (Decreto 1377 de 2013) | Tabla comparativa |
| 28 | Perú: supuestos del oficial de datos, tope de multas en UIT, edad de consentimiento de menores (D.S. 016-2024-JUS) | Tabla comparativa |
| 29 | ✔ Resuelto: Brasil: dispensas para agentes de pequeño porte; reglas de consentimiento del art. 14 LGPD | Tabla comparativa |
| 30 | Fecha exacta de la Res. SPDP-SPD-2025-0028-R | Cronología; `referencias.bib` |

## Prioridad 6: preliminares (personales)

| # | Dato | Dónde |
|---|---|---|
| 31 | Revisar el borrador de la dedicatoria | `Preliminares/05_Dedicatoria.tex` |
| 32 | Revisar el borrador del agradecimiento | `Preliminares/06_Agradecimiento.tex` |
| 33 | Fechas de firma (día y mes) | `Preliminares/01`–`04` |
| 34 | Costo de las normas ISO/IEC (presupuesto, `[VERIFICAR]`) | Cap. 3, Tabla de presupuesto |
