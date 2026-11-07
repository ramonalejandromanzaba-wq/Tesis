# Análisis de la encuesta (OE3 y OE4)

Scripts reproducibles en Python para el análisis cuantitativo de la encuesta a estudiantes. Corresponden a las secciones "Hipótesis" y "Plan de análisis" del Cap. 3. Todo resultado que aparezca en la tesis debe salir de estos scripts **con datos reales**.

## Instalación (una vez)

```
python -m venv .venv
.venv\Scripts\activate            # Windows   (Linux/macOS: source .venv/bin/activate)
pip install -r analisis/requirements.txt
```
Probado con Python 3.12.10 y las versiones fijadas en `requirements.txt`.

## Ejecutar todo con un solo comando

| Comando | Qué hace |
|---|---|
| `python analisis/run_all.py --prueba` | Autopruebas con valores de referencia (V de Aiken, alfa, omega, KR-20, chi-cuadrado, V de Cramér, U de Mann-Whitney, r, Spearman, Holm) |
| `python analisis/run_all.py --simulado` | Genera datos **SIMULADOS** y corre el flujo completo en `analisis/salida_simulada/`. Las figuras llevan marca de agua y las tablas, la fila "DATOS SIMULADOS — NO USAR" |
| `python analisis/run_all.py` | **Datos reales**: lee `analisis/datos/respuestas.xlsx` y `analisis/datos/expertos.xlsx` y escribe en `analisis/salida/` |

`.gitignore` excluye los datos reales y las carpetas de salida: **ninguna respuesta individual se sube al repositorio** (Cap. 3, consideraciones éticas).

## Datos de entrada

- **`datos/respuestas.xlsx`**: exportación del formulario (Google Forms o Microsoft Forms) sin editar. Cada pregunta debe empezar con su código entre corchetes, tal como en `encuesta/cuestionario.md` (por ejemplo, `[H4] ¿Le informaron…?`). Las respuestas pueden quedar como texto: `limpieza.py` las convierte con el libro de códigos de `config.py`. Las columnas sin código (correo, nombre, marca temporal, ID) se eliminan.
- **`datos/expertos.xlsx`**: una fila por ítem y criterio, con las columnas `item | criterio | J1 | J2 | …` y calificaciones de 1 a 5. Los criterios son pertinencia, claridad y coherencia. Se puede llenar desde `encuesta/plantilla_juicio_expertos.xlsx` (hoja *Calificaciones*).

## Scripts

| Archivo | Función |
|---|---|
| `config.py` | Libro de códigos: filtros, demográficos, hechos, escalas Likert, ítems inversos, criterios y umbrales (α = 0,05; V ≥ 0,80) |
| `limpieza.py` | Filtros P00–P02, eliminación de columnas identificativas, recodificación de etiquetas, desdoblamiento de H1, inversos (x' = 6 − x) y puntuaciones de dimensión |
| `validacion.py` | V de Aiken por ítem y criterio; alfa de Cronbach (IC 95 %), omega de McDonald (un factor, ejes principales) y KR-20 |
| `descriptivos.py` | Composición de la muestra, datos solicitados, indicadores de hechos, mediana y RIC de las escalas |
| `inferencial.py` | Kolmogorov-Smirnov con corrección de Lilliefors (Monte Carlo); H1 (U de Mann-Whitney, r), H2 (Spearman), H3 (chi-cuadrado o Fisher, V de Cramér); exploratorios con corrección de Holm |
| `graficos.py` | Figuras en PDF (`salida/figuras/`) |
| `exportar_latex.py` | Tablas `tabular` en `salida/tablas/*.tex`, para `\input{}` en el Cap. 4 |
| `simular_datos.py` | Datos simulados (semilla 2026): `datos/ejemplo_simulado.xlsx` y `datos/expertos_simulado.xlsx` |
| `run_all.py` | Ejecuta todo en orden |

## Verificación cruzada

Repite H1–H3 en **jamovi** o **JASP** (gratuitos) con `salida/datos_limpios.csv` y anota en `CAMBIOS.md` que los resultados coinciden.

## Advertencias

- Los archivos `*_simulado.xlsx` y la carpeta `salida_simulada/` son **datos simulados**: no son resultados y nunca se citan en el documento.
- Si se cambia el cuestionario tras el juicio de expertos o el piloto, se actualiza `config.py` y se vuelve a correr `--prueba` y `--simulado`.
