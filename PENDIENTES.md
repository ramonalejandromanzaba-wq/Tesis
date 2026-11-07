# PENDIENTES — Lo que debe aportar o decidir el autor (por prioridad)

Corte: 2026-11-07 (reestructuración sin caso de estudio). En el PDF **no hay marcas en rojo**: lo no disponible aparece como "---" en las tablas, con una nota de corte, o en el texto como "no disponible a la fecha de corte". Al cargar un dato real, reemplaza el "---", actualiza `CAMBIOS.md` y, si es una cifra, `FUENTES.md`.
La lista anterior (caso UTI, 27-10-2026) quedó obsoleta. Sus puntos vigentes se trasladaron aquí; la autorización institucional de la UTI **ya no se necesita**.

## Prioridad 1: requiere aprobación de la tutora (bloquea la difusión)

| # | Qué | Dónde | Cómo |
|---|---|---|---|
| 1 | **Nuevo título, nuevo objetivo general y 4 objetivos específicos** (alternativas y justificación en `PLAN_REESTRUCTURACION.md` §2). **Requiere aprobación de la tutora** y, si corresponde, actualizar la ficha ITI-TFG-B26-0021 | `main.tex` (portada); Cap. 1 → Objetivos | Revisión con la tutora; si pide cambios, ajustar también el Resumen, el Abstract, la matriz de consistencia (Anexo K) y el Cap. 6 |

## Prioridad 2: ética y difusión de la encuesta (antes del S5, 7-12-2026)

| # | Qué | Dónde |
|---|---|---|
| 2 | Verificar si la UTI o la carrera exigen la aprobación de un **comité de ética** (u otra instancia) para encuestas anónimas a mayores de edad, y documentar la respuesta (oficio o correo) | Cap. 3 → Consideraciones éticas (último párrafo) |
| 3 | Definir los **canales de difusión**: propios (redes, grupos estudiantiles, docentes conocidos) o institucionales. Si son institucionales de alguna universidad, pedir autorización previa | Cap. 3 → Tipo de muestreo; Consideraciones éticas |
| 4 | Crear el formulario (Google Forms o Microsoft Forms) con la configuración anónima de `encuesta/cuestionario.md` y probar que no registra correos | `encuesta/` |

## Prioridad 3: expertos

| # | Qué | Dónde |
|---|---|---|
| 5 | **Jueces (≥ 5)** para validar el cuestionario y la ficha (claridad, pertinencia, coherencia) → `jueces.csv` | Cap. 4, Tabla de validez de contenido (V de Aiken); IV10 |
| 6 | **Panel Delphi (≥ 5; invitar a 7–8)**: perfil, años, Kc, Ka, K y calibración (Brier) | Cap. 5, Tabla del panel; hojas Brier y Delphi de `matriz/Matriz_escenarios_sectoriales.xlsx`; IV07–IV08 |
| 7 | Rondas Delphi (mediana, RIC, consenso, W de Kendall) y probabilidad, impacto y rationale de los escenarios activados | Cap. 5, Tablas de rondas Delphi y de riesgo inherente y residual; IV06 |
| 8 | Juicio de expertos sobre la guía (V01–V12) | Cap. 5, Tabla de juicio de expertos; IV09 |

## Prioridad 4: datos por recolectar

| # | Qué | Fechas | Dónde |
|---|---|---|---|
| 9 | Listado nominal de las 64 universidades (archivo descargable del CES) el día de inicio | 16-11-2026 | `analisis_documental.xlsx`, Registro (col. B) |
| 10 | **Análisis documental** de las 64 universidades: S/P/N, URL y fecha por indicador, más copia en PDF de la evidencia (no subir los PDF al repositorio si contienen datos de personas) | 16-11 a 24-12-2026 | Cap. 4, Tablas de resultados documentales y de ITD |
| 11 | Reverificación del 20 % (13 universidades) | 11 a 15-01-2027 | Hoja Reverificación; Cap. 4 |
| 12 | **Prueba piloto** (30 estudiantes): tiempo, preguntas confusas, alfa de F1–F5 y KR-20 de E1 | 30-11 a 04-12-2026 | Cap. 4, Tabla de confiabilidad |
| 13 | **Encuesta**: meta de 384 válidas (423 brutas), cuotas 246 públicas / 138 particulares | 07-12-2026 a 15-01-2027 | Cap. 4, Tablas de muestra y de indicadores de percepción |
| 14 | Análisis estadístico y brechas (C_D, C_E, B_N, B_P) | 18 a 29-01-2027 | Cap. 4, Tabla de brechas |
| 15 | Activación de escenarios (criterio de `encuesta/plan_analisis.md` §3) y regenerar la matriz con P, I y rationale | 25-01 a 05-02-2027 | Cap. 5; `matriz/escenarios_sectoriales.json` → `node scripts/build_matriz.js …` |
| 16 | Redactar los resultados en el Cap. 4 y completar las conclusiones del Cap. 6 con cifras | 08 a 26-02-2027 | Caps. 4 y 6; Resumen y Abstract |

## Prioridad 5: cifras oficiales por confirmar

| # | Dato | Fuente sugerida |
|---|---|---|
| 17 | Matrícula oficial 2023 (y 2024 si existe), nacional y por sostenimiento, desde la base de la SENESCYT (hoy se usa 841 404, citado por una fuente secundaria). El enlace `cloud-pro.senescyt.gob.ec` no resolvió desde esta máquina el 07-11-2026 | datosabiertos.gob.ec → "Base estadística de matrícula de UEP 2015-2023" (XLSX) |
| 18 | Número oficial de DPD registrados ante la SPDP en 2026 y por sector | Solicitud de acceso a la información pública a la SPDP |
| 19 | Vulneraciones notificadas a la SPDP por el sector educativo | Solicitud a la SPDP (LOPDP art. 76 num. 14) |
| 20 | Criterios y niveles de clasificación de la Res. SPDP-SPD-2026-0040-R en el texto oficial (RO 1S 376) | Registro Oficial |
| 21 | Perú: supuestos del oficial de datos, tope de multas y edad de consentimiento (D.S. 016-2024-JUS) | Texto oficial en El Peruano |
| 22 | Fecha exacta de la Res. SPDP-SPD-2025-0028-R | spdp.gob.ec |

## Prioridad 6: preliminares y planificación

| # | Qué | Dónde |
|---|---|---|
| 23 | Revisar la dedicatoria y el agradecimiento | `Preliminares/05`, `06` |
| 24 | Fechas de firma (día y mes) | `Preliminares/01`–`04` |
| 25 | `planificacion/` (Jira CSV, Gantt `.xlsx`, `Planificacion.md`) refleja el plan anterior (caso UTI, 13-10-2026). Rehacerla con el cronograma nuevo del Cap. 3 si la tutora la pide | `planificacion/` |
