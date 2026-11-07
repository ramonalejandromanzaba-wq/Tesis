# Plan de análisis de la encuesta y del análisis documental

> Versión 1.0 (07-11-2026). Desarrolla la sección "Plan de análisis" del Cap. 3 (`sec:plan_analisis`). **Ningún resultado de este archivo es real hasta que se carguen los datos.** Las pruebas del script se hicieron solo con valores de referencia y datos sintéticos.

## 1. Software

| Tarea | Herramienta |
|---|---|
| Recolección | Google Forms o Microsoft Forms, configurado como anónimo (ver `cuestionario.md`) |
| Tabulación, tablas dinámicas y gráficos | Microsoft Excel |
| Indicadores IE01–IE15, alfa de Cronbach (KR-20), chi-cuadrado, V de Cramér, V de Aiken | `scripts/analisis_encuesta.js` (Node.js, sin dependencias) |
| Registro documental, ITD, C_D, B_N y acuerdo de la reverificación | `analisis_documental/analisis_documental.xlsx` (fórmulas verificadas) |
| Contraste opcional | JASP o R, si el tribunal lo solicita |

Comandos:
```
node scripts/analisis_encuesta.js prueba                      # autoprueba (no son resultados)
node scripts/analisis_encuesta.js aiken  jueces.csv           # validez de contenido del cuestionario
node scripts/analisis_encuesta.js encuesta respuestas.csv     # piloto o muestra definitiva
```
`jueces.csv`: columnas `item,criterio,J1,J2,J3,J4,J5[,J6,…]`, con calificaciones de 1 a 5 y una fila por ítem y criterio (claridad, pertinencia, coherencia).
`respuestas.csv`: exportación del formulario con los **códigos de variable** (P00…F9) como encabezados y los **códigos numéricos** de `cuestionario.md`. Si el formulario exporta textos, se recodifican en Excel antes de correr el script.

## 2. Secuencia

1. **Validez de contenido (S2–S3).** Al menos 5 jueces. Se calcula la V de Aiken por ítem y criterio. Se conserva el ítem si V ≥ 0,70 en los tres criterios; si no, se reformula o se elimina. Resultado → Cap. 4, tabla `tab:aiken_resultados`; indicador IV10.
2. **Piloto (S4).** 30 estudiantes que no forman parte de la muestra definitiva. Se registran el tiempo medio, las preguntas señaladas como confusas, el alfa de F1–F5 y el KR-20 de E1 (aceptable ≥ 0,70, informado con r ítem-total y alfa si se elimina el ítem). Resultado → `tab:confiabilidad`.
3. **Recolección (S5–S10).** Meta: 384 respuestas válidas (423 brutas), con cuotas aproximadas de 246 de universidades públicas y 138 de particulares. Seguimiento semanal de la cuota con la variable A1.
4. **Depuración.** Se excluyen los casos con P00, P01 o P02 distintos de 1. Los casos incompletos se conservan y cada indicador se calcula con su propio denominador (sin imputación). Resultado → `tab:muestra_obtenida`.
5. **Descriptivos.** Indicadores IE01–IE15 según la regla de "respuesta afirmativa" de `cuestionario.md`, en total y por sostenimiento. Para las escalas Likert se informan la mediana y el RIC. Resultado → `tab:res_encuesta`.
6. **Asociación (exploratoria).** Chi-cuadrado de Pearson (α = 0,05) y V de Cramér entre el sostenimiento (pública o particular) y IE03, IE07, IE11 e IE13. Si más del 20 % de las celdas tiene un esperado menor que 5, se agrupan categorías o se usa la prueba exacta de Fisher en las tablas de 2 × 2. Cruces secundarios: nivel (A4) y modalidad (A6). **Interpretación:** con una muestra no probabilística, una asociación significativa es un indicio en la muestra, no una propiedad de la población.
7. **Brechas (OE4).** Para los 7 pares (ID03–IE03, ID02–IE04, ID05–IE05, ID06–IE06, ID14–IE08, ID07–IE10, ID08–IE11):
   - C_D = cumplimiento documental del indicador (hoja Resumen de la plantilla documental);
   - C_E = % de estudiantes con respuesta afirmativa;
   - B_N = 100 − C_D (brecha normativa); B_P = C_D − C_E (brecha de percepción).
   Resultado → `tab:brechas`. Las brechas más altas activan y priorizan los escenarios R-01…R-14 del Cap. 5 (`matriz/escenarios_sectoriales.json`).

## 3. Criterio de activación de escenarios (Cap. 5)

Un escenario sectorial se considera **activado por los hallazgos** cuando su indicador activador (columna "Vulnerabilidad" del JSON) cumple al menos una condición: C_D < 50 %, C_E < 50 % o, en los indicadores de riesgo percibido (IE14), una proporción afirmativa ≥ 20 %. Los escenarios activados por la literatura (R-06, R-08) se mantienen siempre. Los umbrales del 50 % y del 20 % son decisiones de diseño, declaradas antes de conocer los datos.

## 4. Lo que NO se hará

- No se publicarán resultados por universidad identificada; los resultados documentales se agregan por sostenimiento.
- No se calcularán intervalos de confianza presentados como poblacionales.
- No se completará ningún valor faltante con estimaciones.
