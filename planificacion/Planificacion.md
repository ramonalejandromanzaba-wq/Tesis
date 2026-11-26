# Planificación del proyecto ITI-TFG-B26-0021

> **Versión 4 (25-11-2026): observaciones de revisión v3 y alcance nacional.** Reemplaza la versión 3 (16-11-2026, alcance nacional). Coincide con el cronograma del Cap. 3 (Figura del cronograma y Tabla de puntos de control, 16-11-2026 a 26-02-2027).

**Periodo total:** del 13 de octubre de 2026 al 26 de febrero de 2027. El cronograma del Cap. 3 cubre las 15 semanas que faltan desde el 16-11-2026.
**Archivo para Jira:** `Planificacion_Jira.csv` (6 épicas y 41 tareas, 10 de ellas hitos o puntos de control).
**Diagrama de Gantt:** `Planificacion_Gantt.xlsx`, se regenera desde el CSV con `powershell -ExecutionPolicy Bypass -File scripts/gantt_excel.ps1` (requiere Excel). Regenerado el 16-11-2026 (46 actividades, 20 semanas).
**Días no laborables considerados:** receso del 21 de diciembre de 2026 al 1 de enero de 2027 (el formulario queda abierto, sin tareas con expertos) y Carnaval (8 y 9 de febrero de 2027).

## Cronograma por épica

| Épica | Objetivo | Inicio | Fin | Estado |
|---|---|---|---|---|
| E1 Fundamentación, reestructuración y retroalimentación v2 | — | 13-10-2026 | 20-11-2026 | En curso (observaciones v3 aplicadas el 25-11-2026; falta el visto bueno de la tutora al alcance nacional) |
| E2 Instrumentos validados y verificación ética | OE1 y OE3 | 16-11-2026 | 04-12-2026 | En curso |
| E3 Censo documental nacional (64 universidades) | OE2 | 16-11-2026 | 15-01-2027 | Por hacer |
| E4 Encuesta nacional a estudiantes de grado | OE3 | 07-12-2026 | 27-01-2027 | Por hacer |
| E5 Brechas, metodología y validación | OE4 | 04-01-2027 | 19-02-2027 | Por hacer |
| E6 Documentación final y sustentación | — | 08-02-2027 | 26-02-2027 | Por hacer |

## Hitos y puntos de control con la tutora

| Fecha | Hito | Dependencia |
|---|---|---|
| 16-11-2026 | Retroalimentación v2 atendida; convocatoria a jueces y solicitud de verificación ética | ✔ Documentos listos en `jueces/` y `etica/` |
| 25-11-2026 | Observaciones de revisión v3 aplicadas (alcance nacional, fecha de corte, Anexo M) | ✔ `CAMBIOS.md` |
| 27-11-2026 | Visto bueno de la tutora al alcance nacional, al título y a los objetivos | Revisión de la tutora |
| **27-11-2026** | **PC1: instrumentos validados** (V de Aiken sobre la versión 2.2; ajustes en la 2.3) | Respuesta de los jueces (5 días) |
| **04-12-2026** | **PC2: cierre del piloto** (alfa, omega, KR-20, versión final) y verificación ética documentada | 30 estudiantes; respuesta de la UTI |
| 07-12-2026 | **Inicio de la recolección** (solo con la verificación ética resuelta) | PC2 |
| **11-12-2026** | **PC3: 50 % del censo documental** y primera revisión de la composición | Censo |
| 08-01-2027 | Revisión del plan B (¿se llega a 384?) | Recolección |
| 15-01-2027 | Fecha de corte documental (con segundo observador y kappa) | Censo completo |
| **22-01-2027** | **PC4: cierre de la encuesta** (n válido y potencia efectiva) | Recolección |
| 03-02-2027 | Brechas ponderadas calculadas | Base depurada y registro documental |
| 19-02-2027 | Indicadores de validación IV06–IV10 | Rondas Delphi y juicio de expertos |
| 22-02-2027 | Aprobación de la tutora | Documento completo |
| 25-02-2027 | Aprobación de los lectores | Aprobación de la tutora |
| 26-02-2027 | **Entrega final** | Todo lo anterior |

## Ruta crítica y riesgos

1. **Verificación ética.** Sin la respuesta documentada de la UTI no se inicia la recolección el 07-12-2026. La solicitud se envía la semana del 16-11-2026. Si la UTI exige un CEISH y el trámite no se resuelve antes del 07-12, la recolección se desplaza y el plan B (potencia efectiva) cobra más peso; el censo documental avanza en paralelo porque no depende de la ética.
2. **Jueces.** Invitar a 6 para asegurar entre 3 y 5 respuestas en 5 días; si al 23-11 faltan respuestas, recordatorio y, si es necesario, ampliar el plazo hasta el 26-11.
3. **Tasa de respuesta y sesgo de la muestra.** Revisión semanal de la composición; difusión nacional en universidades de varias provincias y con docentes de otras instituciones. Plan B el 08-01-2027; cierre fijo el 22-01-2027 con potencia efectiva si no se llega a 384.
4. **Sedes y extensiones.** Confirmarlas con fuente oficial antes del 27-11-2026 para cerrar la lista de la pregunta A5 en la versión 2.2.
5. **Disponibilidad del panel en febrero.** Convocar a 7–8 candidatos en enero para asegurar 5 con K > 0,8, y al menos 2 jueces de V2 que no participen en el Delphi.
6. **Cambios en los sitios web.** Guardar copia en PDF de cada evidencia el mismo día.

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

Las tareas en estado **Listo** ya están cumplidas: normativa, estado del arte, cifras, fundamentación, atención de las observaciones, reestructuración y retroalimentación v2. Están **En curso** la épica E1 (falta el visto bueno de la tutora al alcance nacional) y la E2 (instrumentos y verificación ética).
