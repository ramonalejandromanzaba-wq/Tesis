# Plan de análisis de la encuesta y del análisis documental

> Versión 2.0 (07-11-2026), enfoque cuantitativo. Desarrolla las secciones "Hipótesis" y "Plan de análisis" del Cap. 3. **Ningún resultado es real hasta que se carguen los datos.** Los scripts se probaron solo con valores de referencia y con datos **simulados**.

## 1. Herramientas

| Tarea | Herramienta |
|---|---|
| Recolección | Microsoft Forms o Google Forms, sin recopilar correo ni datos identificativos (`cuestionario.md`) |
| Análisis principal | Python 3.12, con pandas, NumPy, SciPy y pingouin: carpeta `analisis/`, un solo comando `python analisis/run_all.py` |
| Verificación cruzada | jamovi o JASP (gratuitos), con `analisis/salida/datos_limpios.csv` |
| Juicio de expertos | `encuesta/plantilla_juicio_expertos.xlsx` (V de Aiken automática) y `analisis/validacion.py` |
| Registro documental | `analisis_documental/analisis_documental.xlsx` (índice de cumplimiento por universidad) |

## 2. Secuencia

1. **Juicio de expertos (S2–S3):** de 3 a 5 jueces. V de Aiken por ítem y criterio (pertinencia, claridad, coherencia). Se conserva el ítem si V ≥ 0,80 en los tres. → Cap. 4, Tabla de validez de contenido; IV10.
2. **Piloto (S4):** unos 30 estudiantes fuera de la muestra. Se registran el tiempo, las preguntas confusas y los ajustes. Se calculan el alfa y el omega por dimensión Likert y el KR-20 de H4–H7. → Cap. 4, Tablas de ajustes y de confiabilidad.
3. **Recolección (S5–S10):** meta de 384 respuestas válidas (423 brutas), con cuotas de unas 246 de universidades públicas y 138 de privadas.
4. **Limpieza (`limpieza.py`):** filtros P00–P02; eliminación de las columnas sin código (correo, nombre, marca temporal, ID); conversión de etiquetas a códigos; H1 en columnas binarias; inversos con x' = 6 − x; puntuación de dimensión = media de los ítems si se responde al menos el 80 %.
5. **Confiabilidad (`validacion.py`):** alfa de Cronbach con IC 95 % y omega de McDonald por dimensión (≥ 0,70 aceptable; ≥ 0,80 bueno); KR-20 de la escala dicotómica H4–H7. El alfa no se aplica a los ítems de sí/no porque su fórmula general supone ítems con varianza en una escala de varias categorías; para ítems dicotómicos, su caso particular es el KR-20. Las preguntas de hechos que no forman una escala se informan una por una, sin coeficiente de confiabilidad.
6. **Descriptivos (`descriptivos.py`):** frecuencias y porcentajes de H1–H16, en total y por tipo de universidad. Para las escalas Likert, mediana y RIC; la media y la DE solo como complemento.
7. **Inferencial (`inferencial.py`), α = 0,05:**

| Propósito | Prueba | Efecto |
|---|---|---|
| Normalidad de las puntuaciones de dimensión | Kolmogorov-Smirnov con corrección de Lilliefors (Monte Carlo, n > 50) | — |
| **H1:** información recibida (INF), pública vs. privada | U de Mann-Whitney | r = \|Z\|/√N |
| **H2:** conocimiento de derechos (DER) y confianza (CNF) | Spearman | ρ |
| **H3:** se pidió consentimiento (H2) × tipo de universidad | Chi-cuadrado de Pearson (Fisher si algún esperado es < 5) | V de Cramér |
| Exploratorio: las cuatro dimensiones × tipo | U de Mann-Whitney, con corrección de Holm | r |
| Exploratorio: indicadores de hechos × tipo | Chi-cuadrado o Fisher, con corrección de Holm | V de Cramér |
| Exploratorio: relación entre dimensiones | Spearman, con corrección de Holm | ρ |

   Las Likert son ordinales, así que las pruebas principales son no paramétricas sea cual sea el resultado de normalidad. La prueba de normalidad se informa para justificarlo. **Interpretación:** con una muestra no probabilística, un resultado significativo es evidencia en la muestra y no se generaliza a la población.

8. **Brechas (OE4):** C_D (plantilla documental, hoja Resumen), C_E (% afirmativo del indicador de hechos equivalente), B_N = 100 − C_D y B_P = C_D − C_E para los 7 pares: ID03–H4, ID02–H5, ID05–H6, ID06–H7, ID14–H8, ID07–DER (% con DER ≥ 4) e ID08–H16.
9. **Salidas (`graficos.py`, `exportar_latex.py`):** figuras PDF y tablas `.tex` para `\input{}` en el Cap. 4, tomadas solo de `analisis/salida/` (datos reales).

## 3. Criterio de activación de escenarios (Cap. 5)

Un escenario sectorial se **activa** si su indicador activador cumple al menos una de estas condiciones: C_D < 50 %, C_E < 50 % o, en los indicadores de riesgo percibido (IE14), una proporción afirmativa ≥ 20 %. R-06 y R-08 se mantienen siempre. Los umbrales son decisiones de diseño, declaradas antes de conocer los datos.

## 4. Lo que NO se hará

- Publicar resultados por universidad identificada.
- Presentar intervalos de confianza como si fueran poblacionales.
- Completar con estimaciones los datos que falten.
- Usar en el documento los datos de `analisis/datos/*_simulado.xlsx` o de `analisis/salida_simulada/`.
