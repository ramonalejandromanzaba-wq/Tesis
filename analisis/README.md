# Análisis de la encuesta y del censo documental (OE2, OE3 y OE4)

Scripts reproducibles en Python para el análisis cuantitativo (cuestionario **v2.1**, universidades de **Pichincha**). Corresponden a las secciones "Hipótesis" y "Plan de análisis" del Cap. 3. Todo resultado que aparezca en la tesis debe salir de estos scripts **con datos reales**.

**Reporte agregado:** ningún script exporta resultados por universidad. De la pregunta A5 (universidad) solo se informa cuántas instituciones distintas aportaron respuestas; se usa internamente para ponderar la brecha y para asignar el sostenimiento oficial. Las categorías con menos de 5 respuestas se agrupan (`config.MIN_CELDA`).

## Instalación (una vez)

```
python -m venv .venv
.venv\Scripts\activate            # Windows   (Linux/macOS: source .venv/bin/activate)
pip install -r analisis/requirements.txt
```
Probado con Python 3.12.10 y las versiones fijadas en `requirements.txt`. `factor_analyzer` 0.5.1 se usa solo para KMO, Bartlett y la rotación oblimin; la extracción por ejes principales está implementada en `validez_constructo.py` (su `fit` no es compatible con scikit-learn ≥ 1.8).

## Ejecutar todo con un solo comando

| Comando | Qué hace |
|---|---|
| `python analisis/run_all.py --prueba` | Autopruebas con valores de referencia (Aiken 1–4 y 1–5, alfa, omega, KR-20, chi-cuadrado, V de Cramér, U, r, Spearman, Holm, umbrales de Cohen, brecha ponderada, kappa ponderado frente a scikit-learn, potencia) |
| `python analisis/run_all.py --simulado` | Genera datos **SIMULADOS** (respuestas, 4 jueces, registro documental y segundo observador) y corre el flujo completo en `analisis/salida_simulada/`, con marcas "DATOS SIMULADOS — NO USAR" |
| `python analisis/run_all.py` | **Datos reales** (ver entradas) y salida en `analisis/salida/` |
| `python analisis/potencia.py [n] [n_pub] [n_priv]` | Efecto mínimo detectable y potencia para cualquier n (plan B) |

## Datos de entrada (todos fuera del repositorio)

| Archivo | Contenido |
|---|---|
| `analisis/datos/respuestas.xlsx` | Exportación del formulario sin editar; cada pregunta empieza con su código (`[H5a] …`) |
| `analisis/datos/jueces/E01.xlsx`, `E02.xlsx`, … | Copias de `jueces/formato_juicio_expertos.xlsx` devueltas por los jueces (escala 1–4 y hoja de competencia K) |
| `privado/clave_universidades.xlsx` | Clave de codificación U01… (opción de A5 → código y sostenimiento oficial). Se crea con `python scripts/crear_clave_universidades.py` |
| `privado/analisis_documental.xlsx` | Copia llena de la plantilla documental (códigos, S/P/N, URL y fechas; hoja Reverificación) |
| `privado/analisis_documental_observador2.xlsx` | Calificación ciega del segundo observador (plantilla `--observador2`) |
| `analisis/datos/siies_pichincha.csv` (opcional) | `variable,categoria,pct_poblacion`: composición de la matrícula de Pichincha (SIIES) para comparar la muestra |

## Scripts

| Archivo | Función |
|---|---|
| `config.py` | Libro de códigos v2.1: filtros, A1–A7, lista de universidades (A5), hechos, escalas, inversos, textos de los ítems, umbrales (α = 0,05; V ≥ 0,80 con escala 1–4; Cohen) |
| `limpieza.py` | Filtros P00–P02 y posgrado, columnas identificativas, recodificación, H1, inversos, sostenimiento (oficial por A5 o declarado por A1), puntuaciones |
| `validacion.py` | Lee la carpeta de jueces; V de Aiken por ítem y criterio; K de cada juez; alfa (IC 95 %), omega y KR-20 |
| `validez_constructo.py` | AFE: KMO, Bartlett, análisis paralelo, ejes principales (1 factor por escala; 4 factores con oblimin), cargas ≥ 0,40 |
| `descriptivos.py` | Composición (con supresión < 5), datos solicitados, hechos con y sin «No recuerdo», escalas |
| `inferencial.py` | KS-Lilliefors (descriptivo); H1–H3 con tamaño del efecto y magnitud; exploratorios con Holm |
| `documental.py` | Lectura del registro documental e ITD (P configurable) |
| `brechas.py` | C_D, B_N, B_P no ponderada (referencia) y **B_P ponderada** por la composición de la muestra; total y pública/privada |
| `kappa_documental.py` | Kappa de Cohen ponderado (lineal) intra e interobservador; Landis y Koch |
| `sensibilidad_itd.py` | ITD con P = 0; 0,5; 1 y robustez de la conclusión por sostenimiento |
| `potencia.py` | Efecto mínimo detectable y potencia (H1–H3); parámetros de G*Power en `GPOWER_INSTRUCCIONES.md` |
| `graficos.py` / `exportar_latex.py` | Figuras PDF; tablas `.tex` y `frases_resultados.md` (dato → prueba → interpretación) |
| `simular_datos.py` / `run_all.py` | Datos simulados (semilla 2026) / ejecución completa |

## Verificación cruzada

Repite H1–H3 en **jamovi** o **JASP** con `salida/datos_limpios.csv` y anota en `CAMBIOS.md` que los resultados coinciden. Repite la potencia en G*Power 3.1 (`GPOWER_INSTRUCCIONES.md`).

## Advertencias

- Los archivos `*simulado*` y la carpeta `salida_simulada/` son **datos simulados**: no son resultados y nunca se citan en el documento.
- `datos_limpios.csv` contiene el código de universidad de cada respuesta: queda en `salida/` (excluida de git) y no se comparte.
- Si se cambia el cuestionario tras el juicio de expertos o el piloto, se actualiza `config.py` y se vuelve a correr `--prueba` y `--simulado`.
