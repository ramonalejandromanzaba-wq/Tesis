# PENDIENTES — Lo que debe aportar o decidir el autor (por prioridad)

Corte: **2026-11-25** (observaciones de revisión v3, `uploads/observaciones_tesis_v3.md`: ámbito **nacional**, fecha de corte normativa **16-11-2026**, cuestionario **v2.2**, Anexo M). En el PDF, lo que solo puede aportar el autor aparece como **`[PENDIENTE: …]` en rojo** (macro `\pend` de `main.tex`); las celdas de resultados aún no medidos llevan "---" con una nota de corte. Al resolver un punto: reemplazar la marca, actualizar `CAMBIOS.md` y, si es una cifra, `FUENTES.md`. **La recolección empieza el 7-12-2026 solo si el punto 1 está resuelto.** Esta lista se revisa con la tutora en cada punto de control (Tabla de puntos de control del Cap. 3).

## Marcas `[PENDIENTE]` que quedan en el PDF (OM-09)

Las marcas por datos provinciales (N de Pichincha, sedes y extensiones, proporción pública/privada provincial, mediana de matrícula) y la del oficio SPDP-IRD-2026-0221-O **se eliminaron** al pasar al ámbito nacional y al optar por la opción (b) de OM-09. Antes había 33 marcas; quedan **9**, todas sobre datos que solo puede aportar el autor:

| # | Pendiente | Sección | Fuente | Fecha prevista | Responsable |
|---|---|---|---|---|---|
| 1 | Respuesta de la UTI a la solicitud de verificación ética (tipo, número de oficio y fecha) | Cap. 3 §Consideraciones éticas | Coordinación de la carrera / Dirección de Investigación (UTI) | 04-12-2026 (PC2) | Autor |
| 2 | Verificación ética en el consentimiento de la encuesta | Anexo C | Ídem | 04-12-2026 | Autor |
| 3–8 | Fecha y medio de envío; instancia que responde; tipo de respuesta; n.º de oficio y fecha; condiciones; copia de la respuesta | Anexo L (Aval o verificación ética) | Ídem | 04-12-2026 | Autor |
| 9 | Código del segundo observador y fecha de su calificación ciega (13 instituciones) | Cap. 3 §Confiabilidad del registro | Segundo observador | 11 a 15-01-2027 | Autor |

**Resultados aún no medidos (celdas "---", sin marca roja):** V de Aiken y jueces (Cap. 4); piloto y confiabilidad; AFE; censo documental (S/P/N, ITD, sensibilidad, kappa); encuesta (participación, composición, hechos, dimensiones, hipótesis); brechas; frecuencias de ID17 e ID19 y proporciones de la Tabla de perfiles de referencia (Cap. 5); niveles inherente y residual por perfil; panel Delphi y juicio V2 (IV06–IV11). **El Cap. 4 no puede completarse antes de la recolección** (07-12-2026 a 22-01-2027): OM-09.3 queda abierto hasta entonces.

## Acciones del autor por prioridad

| # | Qué | Dónde se usa | Cómo / fecha |
|---|---|---|---|
| **1** | **Enviar la solicitud de verificación ética** (`etica/solicitud_verificacion_etica.md`, actualizada al 25-11-2026: ámbito nacional, encuesta seudonimizada, cuestionario v2.2). Completar nombres, cargos y fecha. Adjuntar `jueces/cuestionario_v2.2.pdf` y `encuesta/consentimiento_informado.md` (v2.0). **La recolección no inicia sin la respuesta documentada.** | Cap. 3; Anexos C y L | Cuanto antes; respuesta antes del 04-12-2026 |
| **2** | **Aprobación de la tutora** del cambio de alcance **Pichincha → nacional** (observaciones v3), de OE2 y OE3, de H3 (sobre H8) y del cuestionario v2.2. El título **no cambia**. | Cap. 1; Resumen; Abstract; Anexo K | 27-11-2026 (PC1) |
| **3** | **Juicio de expertos sobre la versión 2.2** (no la 2.1): reenviar a los jueces `cuestionario_v2.2.pdf` y el nuevo `formato_juicio_expertos.xlsx` (55 ítems y 23 indicadores). Si algún juez ya calificó la v2.1, pedirle solo los ítems nuevos o cambiados (P00, P02, A5, A8, H1, DER8, DER9, ID04, ID06a, ID06b, ID07, ID13, ID14, ID17–ID22). Los ajustes van a la **versión 2.3**. | Cap. 4, Tabla de validez de contenido; IV10 | 26-11 a 01-12-2026 |
| 4 | **Proveedor del formulario**: decidir Google Forms o Microsoft Forms y nombrarlo en la versión publicada del consentimiento (encargado; servidores fuera del Ecuador). | Anexo C; `encuesta/consentimiento_informado.md` | Antes del piloto |
| 5 | **Capturas de G*Power 3.1** de H1, H2 y H3 (H3 sigue siendo un chi-cuadrado 2×2: los parámetros no cambian) | Cap. 3, Tabla de potencia | PC1 |
| 6 | **Diversificar el panel**: invitar expertos de universidades públicas y privadas y de distintas regiones (Delphi ≥ 5; V2 ≥ 5 con ≥ 2 fuera del Delphi) | Cap. 5 §Validación; IV06–IV11 | 04-01 a 19-02-2027 |
| 7 | **Sitios web oficiales de las 64 instituciones** en la clave privada (`python scripts/crear_clave_universidades.py --forzar` y completar la columna) | Censo documental | Antes del 28-11-2026 |
| 8 | **Segundo observador** (13 instituciones; 15 indicadores principales) | Cap. 3; Cap. 4, Tabla de kappa | 11 a 15-01-2027 |
| 9 | Crear el formulario (55 preguntas; sin correos, sin inicio de sesión, sin carga de archivos; A5 con 64 opciones en orden alfabético; A8 región) y el código QR; planificar la difusión nacional | Cap. 3 §Muestreo | 26-11 a 30-11-2026 |
| 10 | Piloto (~30 estudiantes) → versión final | Cap. 4 | 30-11 a 04-12-2026 |
| 11 | Censo documental de las 64 instituciones: 50 % (32) al 11-12-2026 y cierre el 08-01-2027 | Cap. 4 | 23-11-2026 a 08-01-2027 |
| 12 | Encuesta nacional: 384 válidas (423 brutas), cuotas 246/138; revisión semanal (A2, A5, A6, A8); plan B el 08-01-2027 | Cap. 4 | 07-12-2026 a 22-01-2027 |
| 13 | Completar con datos agregados la Tabla de perfiles de referencia (ID17, ID19, H1, ID13) y la de riesgo por perfil | Cap. 5 | Al cerrar censo y encuesta |
| 14 | Guía de diseño y por defecto de la SPDP (Res. SPDP-SPD-2025-0040-R): conseguir el PDF oficial (el enlace del portal devolvió 404 el 25-11-2026) y confirmar los nombres y cortes de los niveles de madurez, tomados de análisis jurídicos (AVL, Tobar ZVS) | Cap. 2 §Marcos; Cap. 5 §Fase 0 | Antes del PC2 |

## Datos oficiales por confirmar

| # | Dato | Fuente sugerida |
|---|---|---|
| 15 | Base oficial de microdatos de la matrícula SIIES (no descargable el 07 y 16-11-2026); hoy N = 841 404 se toma de `sumba2025economia` | Portal de datos abiertos / SENESCYT |
| 16 | Distribución nacional de la matrícula por área, nivel, edad y modalidad, para comparar la muestra (`analisis/datos/siies_nacional.csv`) | SIIES |
| 17 | Número de Registro Oficial y fecha exacta de la Res. SPDP-SPD-2025-0028-R | spdp.gob.ec |
| 18 | Criterios y niveles de clasificación de la Res. SPDP-SPD-2026-0040-R en el texto oficial | Registro Oficial |
| 19 | Número oficial de DPD registrados y vulneraciones del sector educativo (para la recomendación 7) | Solicitud de acceso a la información pública a la SPDP |
| 20 | (Opcional, OM-09 opción a) Solicitar a la SPDP por LOTAIP el Oficio SPDP-IRD-2026-0221-O. Hoy se aplicó la opción (b): la afirmación se eliminó y el documento se apoya solo en la Res. SPDP-SPD-2026-0005-R | SPDP |

## Preliminares

| # | Qué | Dónde |
|---|---|---|
| 21 | Revisar la dedicatoria y el agradecimiento | `Preliminares/05`, `06` |
| 22 | Fechas de firma (día y mes) | `Preliminares/01`–`04` |
| 23 | Volver a importar `planificacion/Planificacion_Jira.csv` en Jira y regenerar el Gantt (`scripts/gantt_excel.ps1`, requiere Excel) | `planificacion/` |
| 24 | Para la versión final: cambiar `\pend` a negro en `main.tex` o resolver las marcas | `main.tex` |
