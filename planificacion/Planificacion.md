# Planificación del proyecto ITI-TFG-B26-0021

**Periodo:** del 13 de octubre de 2026 (semana 1) al 26 de febrero de 2027 (semana 20), periodo académico B26.
**Archivo para Jira:** `Planificacion_Jira.csv` (5 épicas y 35 tareas o hitos).
**Días no laborables considerados:** 2 y 3 de noviembre (feriados), receso del 21 de diciembre de 2026 al 1 de enero de 2027 y Carnaval (8 y 9 de febrero de 2027). En esas fechas no se programan tareas con informantes ni con el panel.

## Cronograma por épica

| Épica | Objetivo | Inicio | Fin | Semanas |
|---|---|---|---|---|
| E1 Análisis de universidades y diseño metodológico | OE2 | 13-10-2026 | 16-11-2026 | 1–5 |
| E2 Autorización y diagnóstico institucional | OE1 | 27-10-2026 | 14-12-2026 | 3–9 |
| E3 Implementación en la UTI | OE3 | 24-11-2026 | 18-01-2027 | 7–14 |
| E4 Evaluación de la metodología | OE4 | 05-01-2027 | 08-02-2027 | 13–17 |
| E5 Documentación final y sustentación | — | 25-01-2027 | 26-02-2027 | 16–20 |

## Hitos

| Fecha | Hito | Dependencia |
|---|---|---|
| 30-10-2026 | Observaciones del tribunal y de la tutora atendidas | — |
| 06-11-2026 | Solicitud de autorización entregada a la UTI | Visto bueno de la tutora |
| 20-11-2026 | **Oficio de autorización recibido** (ruta crítica) | Bloquea todo el diagnóstico y la implementación |
| 14-12-2026 | Informe de diagnóstico y dictamen de gran escala | Entrevistas y datos agregados |
| 18-12-2026 | Primera ronda Delphi concluida | Panel calibrado |
| 18-01-2027 | Matriz inherente y residual, y plan de tratamiento | Rondas Delphi |
| 22-01-2027 | Simulacro de vulneración V2 ejecutado | Procedimiento de respuesta |
| 08-02-2027 | Indicadores IV01–IV12 y recomendaciones | Juicio de expertos |
| 16-02-2027 | Aprobación de la tutora | Documento completo |
| 22-02-2027 | Aprobación de los lectores | Aprobación de la tutora |
| 26-02-2027 | **Entrega final** | Todo lo anterior |

## Ruta crítica y riesgos

1. **Autorización de la UTI.** Si el oficio llega después del 20-11-2026, las épicas E2 a E4 se desplazan en la misma medida. Para recuperar tiempo, solapa las rondas Delphi 2 y 3 y reduce el simulacro a una sesión.
2. **Disponibilidad del panel en diciembre y enero.** Convoca de 7 a 8 candidatos para asegurar 5 con K > 0,8, y cierra la primera ronda antes del receso.
3. **Revisión de la tutora y de los lectores.** Ten listo el borrador completo el 05-02-2027.

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

Las tareas en estado **Listo** ya están cumplidas: normativa, estado del arte, cifras, fundamentación, diseño de fases, escalas y verificación de la plantilla. La atención a las observaciones está **En curso**.
