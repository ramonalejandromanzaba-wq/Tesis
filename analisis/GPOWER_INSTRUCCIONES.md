# Instrucciones para G*Power 3.1 (capturas pendientes: las hace el autor)

Objetivo: verificar con G*Power 3.1 (Faul et al., 2007, 2009) el efecto mínimo detectable de cada hipótesis con la muestra de diseño (n = 384; 246 de universidades públicas y 138 de privadas), α = 0,05 bilateral y potencia 0,80. Los valores esperados son los que calcula `python analisis/potencia.py` (16-11-2026). Guardar cada captura en `Capítulos/fig/gpower_H1.png`, `gpower_H2.png` y `gpower_H3.png` y avisar para insertarlas en el Cap. 3 (hoy figuran como `[PENDIENTE]`).

En todos los casos: **Type of power analysis = Sensitivity: Compute required effect size given α, power, and sample size**.

## H2 — Correlación DER–CNF (Spearman)

| Campo | Valor |
|---|---|
| Test family | Exact |
| Statistical test | Correlation: Bivariate normal model |
| Tail(s) | Two |
| α err prob | 0.05 |
| Power (1−β err prob) | 0.80 |
| Correlation ρ H0 | 0 |
| Total sample size | 384 |

Valor esperado: |ρ| ≈ 0,143 (la aproximación de Python usa la z de Fisher; G*Power usa el modelo exacto, puede diferir en la tercera cifra). Con la eficiencia de Spearman frente a Pearson (≈ 0,91), el mínimo sube a ≈ 0,149, es decir, **ρ ≥ 0,15**.

## H3 — Consentimiento × sostenimiento (chi-cuadrado 2 × 2)

| Campo | Valor |
|---|---|
| Test family | χ² tests |
| Statistical test | Goodness-of-fit tests: Contingency tables |
| α err prob | 0.05 |
| Power (1−β err prob) | 0.80 |
| Total sample size | 384 |
| Df | 1 |

Valor esperado: **w ≈ 0,143** (con w = 0,15, la potencia es 0,84).

## H1 — Información recibida (INF) pública vs. privada (U de Mann-Whitney)

| Campo | Valor |
|---|---|
| Test family | t tests |
| Statistical test | Means: Wilcoxon-Mann-Whitney test (two groups) |
| Tail(s) | Two |
| Parent distribution | Normal (repetir con *min ARE* para el peor caso) |
| α err prob | 0.05 |
| Power (1−β err prob) | 0.80 |
| Sample size group 1 | 246 |
| Sample size group 2 | 138 |

Valores esperados: **d ≈ 0,306** (distribución madre normal, ARE = 3/π) y **d ≈ 0,321** (min ARE = 0,864). Con d = 0,33, la potencia es 0,86 y 0,82, respectivamente.

## Plan B (enero de 2027): potencia efectiva con el n alcanzado

1. Correr `python analisis/potencia.py <n_total> <n_pública> <n_privada>` (o `run_all.py`, que la calcula sola con los datos reales y escribe `salida/potencia_efectiva.csv`).
2. En G*Power, cambiar a **Post hoc: Compute achieved power** con los mismos parámetros, el n alcanzado y los efectos de referencia (ρ = 0,15; w = 0,15; d = 0,33). Guardar la captura como `gpower_posthoc_<prueba>.png`.

Referencias: Faul, F., Erdfelder, E., Lang, A.-G. y Buchner, A. (2007). *Behavior Research Methods, 39*(2), 175–191. https://doi.org/10.3758/BF03193146 · Faul, F., Erdfelder, E., Buchner, A. y Lang, A.-G. (2009). *Behavior Research Methods, 41*(4), 1149–1160. https://doi.org/10.3758/BRM.41.4.1149
