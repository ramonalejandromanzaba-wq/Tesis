# Planificación del proyecto ITI-TFG-B26-0021

> **Versión 2 (07-11-2026), sin caso de estudio.** Reemplaza el plan del 13-10-2026, que giraba en torno a la autorización y el diagnóstico de la UTI. Coincide con el cronograma del Cap. 3 (Figura del cronograma, 9-11-2026 a 26-02-2027).

**Periodo total:** del 13 de octubre de 2026 (semana 1) al 26 de febrero de 2027 (semana 20). Las semanas 1 a 4 (13-10 a 07-11) ya están cumplidas: fundamentación, observaciones y reestructuración.
**Archivo para Jira:** `Planificacion_Jira.csv` (6 épicas y 39 tareas, 5 de ellas hitos).
**Diagrama de Gantt:** `Planificacion_Gantt.xlsx`, con la hoja *Tareas* (fechas editables) y la hoja *Gantt* (barras semanales que se recalculan solas). Se regenera desde el CSV con `powershell -ExecutionPolicy Bypass -File scripts/gantt_excel.ps1`, que requiere Excel.
**Días no laborables considerados:** receso del 21 de diciembre de 2026 al 1 de enero de 2027 (el formulario de la encuesta queda abierto, pero no se programan tareas con expertos) y Carnaval (8 y 9 de febrero de 2027).

## Cronograma por épica

| Épica | Objetivo | Inicio | Fin | Semanas | Estado |
|---|---|---|---|---|---|
| E1 Fundamentación y reestructuración | — | 13-10-2026 | 13-11-2026 | 1–5 | En curso (solo falta el visto bueno de la tutora) |
| E2 Indicadores e instrumentos validados | OE1 | 09-11-2026 | 04-12-2026 | 5–8 | En curso |
| E3 Análisis documental de las 64 universidades | OE2 | 16-11-2026 | 15-01-2027 | 6–14 | Por hacer |
| E4 Encuesta a estudiantes | OE3 | 07-12-2026 | 20-01-2027 | 9–15 | Por hacer |
| E5 Brechas, guía y validación | OE4 | 04-01-2027 | 19-02-2027 | 13–19 | Por hacer |
| E6 Documentación final y sustentación | — | 08-02-2027 | 26-02-2027 | 18–20 | Por hacer |

## Hitos

| Fecha | Hito | Dependencia |
|---|---|---|
| 07-11-2026 | Reestructuración sin caso de estudio (PR #3) | ✔ Cumplido |
| 13-11-2026 | **Aprobación de la tutora del nuevo título y objetivos** (ruta crítica) | Bloquea la difusión de la encuesta |
| 27-11-2026 | Requisitos éticos verificados y canales de difusión definidos | Respuesta de la UTI o de la carrera |
| 04-12-2026 | Instrumentos validados (Aiken y piloto) | Jueces y 30 estudiantes del piloto |
| 15-01-2027 | Fecha de corte documental y cierre de la encuesta | Censo completo; 384 respuestas válidas |
| 29-01-2027 | Brechas calculadas | Base depurada y plantilla documental |
| 19-02-2027 | Indicadores de validación IV06–IV10 | Rondas Delphi y juicio de expertos |
| 22-02-2027 | Aprobación de la tutora | Documento completo |
| 25-02-2027 | Aprobación de los lectores | Aprobación de la tutora |
| 26-02-2027 | **Entrega final** | Todo lo anterior |

## Ruta crítica y riesgos

1. **Visto bueno de la tutora y requisitos éticos.** Sin ellos no se difunde la encuesta. Si se retrasan más allá del 27-11-2026, el piloto y la primera fase de recolección se desplazan; el análisis documental puede avanzar en paralelo porque no depende de esa aprobación.
2. **Tasa de respuesta en el receso.** Si al 18-12-2026 hay menos de la mitad de la meta (192 válidas), refuerza la difusión en la segunda fase y prioriza la cuota que falte (públicas o particulares). Si no se llega a 384, el resultado se informa con el n obtenido; el diseño ya es descriptivo y no probabilístico.
3. **Disponibilidad del panel en febrero.** Convoca a 7–8 candidatos en enero para asegurar 5 con K > 0,8 y evita programar rondas en Carnaval.
4. **Cambios en los sitios web.** Guarda copia en PDF de cada evidencia el mismo día; la reverificación de enero mide la estabilidad del registro.

## Cómo importar en Jira

1. En Jira, ve a **⚙ Configuración → Sistema → Importación de sistema externo → CSV**.
2. Selecciona `Planificacion_Jira.csv`, que está codificado en UTF-8.
3. En la configuración, usa **coma** como separador y el formato de fecha **`yyyy-MM-dd`**.
4. Asocia cada columna del archivo con su campo de Jira:

   | Columna del archivo | Campo de Jira |
   |---|---|
   | ID | Id. de la incidencia |
   | ID principal | Id. principal (vincula cada tarea con su épica) |
   | Tipo de incidencia | Tipo de incidencia |
   | Resumen | Resumen |
   | Descripción | Descripción |
   | Fecha de inicio | Fecha de inicio |
   | Fecha de vencimiento | Fecha de vencimiento |
   | Prioridad | Prioridad |
   | Etiquetas | Etiquetas (las palabras separadas por espacio se crean como etiquetas distintas) |
   | Estado | Estado |

5. En el paso **Asignar valores de campo**, comprueba que los valores coincidan con los de tu Jira:
   - *Tipo de incidencia*: Épica, Tarea.
   - *Prioridad*: Más alta, Alta, Media.
   - *Estado*: Por hacer, En curso, Listo. Si tu proyecto usa "Tareas por hacer" o "Finalizada", elige el equivalente en la lista desplegable.
6. Si tu proyecto no tiene el campo *Fecha de inicio*, impórtalo como campo personalizado de fecha o déjalo sin asociar. Las fechas de vencimiento bastan para la vista *Cronograma*.
7. Los hitos se importan como *Tarea* con la etiqueta `hito`.

Las tareas en estado **Listo** ya están cumplidas: normativa, estado del arte, cifras, fundamentación, atención de las observaciones y reestructuración sin caso de estudio. Están **En curso** la épica E1 (falta el visto bueno de la tutora) y el ajuste de los instrumentos (E2).
