# Plan de análisis de la encuesta y del análisis documental

> **Versión 2.1 (16-11-2026)**, enfoque cuantitativo; ámbito: universidades de la **provincia de Pichincha**; reporte **solo agregado**. Desarrolla las secciones "Hipótesis" y "Plan de análisis" del Cap. 3. **Ningún resultado es real hasta que se carguen los datos.** Los scripts se probaron solo con valores de referencia y con datos **simulados**.

## 1. Herramientas

| Tarea | Herramienta |
|---|---|
| Recolección | Un solo formulario (Microsoft Forms o Google Forms), sin recopilar correo ni datos identificativos (`cuestionario.md`); difusión por enlace y por código QR |
| Análisis principal | Python 3.12 (pandas, NumPy, SciPy, pingouin, statsmodels, factor_analyzer): `python analisis/run_all.py` |
| Verificación cruzada | jamovi o JASP con `analisis/salida/datos_limpios.csv`; G*Power 3.1 para la potencia (`analisis/GPOWER_INSTRUCCIONES.md`) |
| Juicio de expertos | `jueces/formato_juicio_expertos.xlsx` (escala 1–4) → `analisis/datos/jueces/E0n.xlsx` → `analisis/validacion.py` |
| Registro documental | `analisis_documental/analisis_documental.xlsx` (plantilla) → copia llena en `privado/analisis_documental.xlsx`; clave en `privado/clave_universidades.xlsx` |

## 2. Secuencia

1. **Juicio de expertos (16 a 26-11-2026):** de 3 a 5 jueces, escala 1–4. V de Aiken por ítem y criterio (pertinencia, claridad, coherencia). Se conserva el ítem si V ≥ 0,80 en los tres (≥ 8/9 con 3 jueces; ≥ 12/15 con 5). → versión 2.2; Cap. 4, Tabla de validez de contenido; IV10.
2. **Piloto (30-11 a 04-12-2026):** unos 30 estudiantes fuera de la muestra. Tiempo, preguntas confusas y ajustes; alfa y omega por dimensión y KR-20 de H4, H5a, H5b, H6 y H7. → versión final; Cap. 4, Tablas de ajustes y de confiabilidad.
3. **Verificación ética:** respuesta documentada de la UTI (Anexo «Aval o verificación ética»). **Sin ella no se inicia la recolección.**
4. **Recolección (07-12-2026 a 22-01-2027):** meta de 384 respuestas válidas (423 brutas), con cuotas provisionales de 246 de universidades públicas y 138 de privadas (proporción nacional; se ajustará a la de Pichincha). Revisión **semanal** de la composición (A2, A3, A4, sostenimiento, A6, A7 y número de universidades) con `descriptivos.py`; plan B el 08-01-2027.
5. **Limpieza (`limpieza.py`):** filtros P00–P02 (consentimiento, mayoría de edad, Pichincha) y exclusión del posgrado (A3); eliminación de columnas sin código; conversión de etiquetas a códigos; H1 en columnas binarias; inversos con x' = 6 − x; puntuación de dimensión = media de los ítems si se responde al menos el 80 %. A5 → código U0n (clave privada) y **sostenimiento oficial**; si no se identifica la universidad, se usa A1; «No lo sé» sin universidad = excluido de H1 y H3 (se informa cuántos).
6. **Confiabilidad y validez (`validacion.py`, `validez_constructo.py`):** alfa (IC 95 %) y omega por dimensión (≥ 0,70 aceptable; ≥ 0,80 bueno); KR-20 de la escala dicotómica; AFE con KMO, Bartlett, análisis paralelo, ejes principales (un factor por escala; cuatro con oblimin) y retención con carga ≥ 0,40.
7. **Descriptivos (`descriptivos.py`):** composición de la muestra (con supresión de celdas < 5); H1–H16 en total y por tipo de universidad, **con y sin «No recuerdo»** y el % de «No recuerdo»; Likert con mediana y RIC.
8. **Inferencial (`inferencial.py`), α = 0,05:**

| Propósito | Prueba | Efecto |
|---|---|---|
| Normalidad (solo descriptiva; no cambia la decisión) | Kolmogorov-Smirnov con corrección de Lilliefors | — |
| **H1:** información recibida (INF), pública vs. privada | U de Mann-Whitney | r = \|Z\|/√N |
| **H2:** conocimiento de derechos (DER) y confianza (CNF) | Spearman | ρ |
| **H3:** se pidió consentimiento (H2) × tipo de universidad | Chi-cuadrado de Pearson (Fisher si algún esperado es < 5) | V de Cramér |
| Exploratorio: dimensiones × tipo | U de Mann-Whitney, con Holm | r |
| Exploratorio: indicadores de hechos × tipo | Chi-cuadrado o Fisher, con Holm | V de Cramér |
| Exploratorio: relación entre dimensiones | Spearman, con Holm | ρ |

   **Magnitud (Cohen, 1988):** \|ρ\| o r < 0,10 trivial; 0,10–0,29 débil; 0,30–0,49 moderada; ≥ 0,50 fuerte; V de Cramér (gl = 1), los mismos cortes. **Redacción:** dato → prueba → interpretación (con el artículo de la LOPDP). Con una muestra no probabilística, un resultado significativo es evidencia en la muestra.

9. **Componente documental:** S/P/N por indicador y ITD agregado (total; públicas vs. privadas, con las cofinanciadas agrupadas; media y mediana, sin mínimos ni máximos); sensibilidad con P = 0; 0,5; 1 (`sensibilidad_itd.py`); kappa de Cohen ponderado inter e intraobservador sobre ⌈0,2·U⌉ universidades (4 con U = 18) (`kappa_documental.py`).
10. **Brechas (OE4, `brechas.py`):** C_D, B_N = 100 − C_D; **brecha principal ponderada** B_P^w = C_D^w − C_E^id, con C_D^w = Σ w_u·s_u y w_u = n_u / n_id (encuestados por universidad del censo); B_P = C_D − C_E solo como referencia. Total y por sostenimiento. Pares: ID03–H4, ID02–(H5a y H5b), ID05–H6, ID06–H7, ID14–H8, ID07–DER (% con DER ≥ 4) e ID08–H16.
11. **Potencia (`potencia.py`):** efecto mínimo detectable con el n de diseño y potencia efectiva con el n alcanzado (plan B).
12. **Salidas (`graficos.py`, `exportar_latex.py`):** figuras PDF, tablas `.tex` y `frases_resultados.md`, tomadas solo de `analisis/salida/` (datos reales).

## 3. Criterio de activación de escenarios (Cap. 5)

Un escenario sectorial se **activa** si su indicador activador cumple al menos una de estas condiciones: C_D < 50 %, C_E < 50 % o, en los indicadores de riesgo percibido (IE14), una proporción afirmativa ≥ 20 %. R-06 y R-08 se mantienen siempre. Los umbrales son decisiones de diseño, declaradas antes de conocer los datos.

## 4. Lo que NO se hará

- Publicar resultados por universidad, nombrar universidades en resultados, tablas, figuras, conclusiones o anexos de resultados, o informar el valor mínimo o máximo de grupos pequeños.
- Informar sola una categoría con menos de 5 respuestas.
- Presentar intervalos de confianza como si fueran poblacionales.
- Completar con estimaciones los datos que falten.
- Usar en el documento los datos de `analisis/datos/*simulado*` o de `analisis/salida_simulada/`.
