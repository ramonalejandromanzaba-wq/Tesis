# PLAN DE REESTRUCTURACIÓN — Tesis sin caso de estudio (2026-11-07)

Rama: `reestructuracion-sin-caso` (creada desde `main`, commit `4b4d67b`).
Instrucción: `uploads/reestructuracion_tesis.md`, autorizada por el autor el 07-11-2026. La autorización cubre el título, el objetivo general y los objetivos específicos, y prevalece sobre la regla de CLAUDE.md/CLAUDEs.md que prohibía reformularlos.

## 0. Estado inicial

- Compilación con `pdflatex → bibtex → pdflatex ×2`. `latexmk` está instalado, pero no funciona porque falta Perl (CLAUDE.md). Resultado: **0 errores**, `main.pdf` de **128 páginas**, sin referencias indefinidas.
- Motivo del cambio: la UTI no dará acceso a sus datos internos. El caso de estudio (admisión y matrícula, sede Quito) no es viable.

## 1. Contexto tomado de los archivos de control

- **CLAUDE.md (raíz):** compilación con MiKTeX y sin latexmk; IEEE; convenciones del .bib (doble llave en títulos de normas; `ISO 31{}000`); estilo de ensayo argumentativo (tesis al inicio de cada capítulo, conclusión al final de cada sección y al menos una objeción respondida); **regla del autor del 27-10-2026: el PDF no lleva nada en rojo ni marcas [PENDIENTE]**; lo que no está disponible se escribe en negro ("no disponible a la fecha de corte") y las celdas vacías llevan "---" con una nota.
- **CLAUDEs.md (raíz = carpeta superior):** objetivos oficiales de la ficha; exclusiones (sin certificación legal, sin implementación completa de medidas, sin auditoría externa); reglas de la guía SPDP v2; ética (ningún dato personal real en el repositorio).
- **indicaciones_revision.md:** indicaciones A1–A8, B1–B7 y C1–C16. Se conservan las que no dependen del caso (sección 3).
- **CAMBIOS / PENDIENTES / FUENTES:** cifras ya verificadas al 27-10-2026 (16 161 IE, 64 universidades, 216 institutos, más de 1 150 DPD, denuncias, sanciones), plazos (5 días, 3 días, 72 h) y derecho comparado.

**Conflicto resuelto.** La instrucción nueva pide `\textcolor{red}{[PENDIENTE: …]}`. El autor pidió en el mismo mensaje "sigue el formato como lo venías haciendo", y la regla vigente del 27-10-2026 prohíbe el rojo en el PDF. Por eso se mantiene la convención en negro: "---" en las tablas, una nota de corte y el registro en `PENDIENTES.md`. Si el autor prefiere el rojo, basta con usar `\pend{…}` (la macro sigue definida en `main.tex`).

## 2. Título y objetivo general

> **SUPERADO el 2026-11-07 por indicación del autor:** no se cambian ni el título ni el objetivo general. Se mantiene el título de la ficha con el añadido "en universidades ecuatorianas" y el objetivo general queda textual (no mencionaba a la UTI). El producto vuelve a ser la metodología. Ver `CAMBIOS.md` (sección superior). Lo que sigue en este apartado es histórico.

### Alternativas de título
1. **Diagnóstico y gestión de riesgos en el tratamiento de datos personales de estudiantes universitarios en Ecuador conforme a la LOPDP** ← elegida
2. Brecha entre la LOPDP, la información pública de las universidades ecuatorianas y la percepción de los estudiantes: lineamientos para la gestión de riesgos en el tratamiento de datos personales
3. Cumplimiento de la Ley Orgánica de Protección de Datos Personales en universidades ecuatorianas: análisis documental, percepción estudiantil y guía de gestión de riesgos

### Alternativas de objetivo general
1. **Diagnosticar el cumplimiento de la Ley Orgánica de Protección de Datos Personales (2021) y de su Reglamento General (2023) en el tratamiento de datos personales de estudiantes por parte de las universidades ecuatorianas, mediante el análisis documental de su información pública y una encuesta anónima a estudiantes, para proponer una guía de gestión de riesgos validada por expertos.** ← elegido
2. Evaluar la brecha entre las obligaciones de la LOPDP, la información que publican las universidades ecuatorianas y la percepción de sus estudiantes como titulares de datos, para formular lineamientos de gestión de riesgos.
3. Analizar el grado de transparencia y de respeto de los derechos de los titulares en el tratamiento de datos personales de estudiantes universitarios en Ecuador, para diseñar una guía de gestión de riesgos alineada con la normativa de la SPDP.

### Justificación de la elección
- **Continuidad con la ficha institucional** (ITI-TFG-B26-0021: "…diagnóstico y gestión de riesgos en el tratamiento de datos personales académicos conforme a la LOPDP"). Se conservan el núcleo "diagnóstico y gestión de riesgos" y la referencia a la LOPDP, y se cambian solo el objeto (estudiantes universitarios en Ecuador) y el método. Así el cambio es más fácil de aprobar como ajuste de alcance y no como tema nuevo.
- El objetivo 1 tiene la estructura exigida (infinitivo + qué + cómo + para qué). Nombra las dos fuentes de datos legítimas (información pública y encuesta anónima) y conserva el producto propositivo (guía de gestión de riesgos), que permite reutilizar la metodología y la plantilla `.xlsx` ya construidas.
- La alternativa 2 depende de que exista la brecha antes de medirla. La alternativa 3 deja fuera el diagnóstico de cumplimiento, que es lo que mide la ficha documental.
- **Requiere aprobación de la tutora** → `PENDIENTES.md`, prioridad 1.

Título en inglés: *Diagnosis and risk management in the processing of university students' personal data in Ecuador under the LOPDP*.

## 3. Qué se conserva, qué se elimina y qué se crea

### Se conserva y se adapta
| Elemento | Origen | Destino |
|---|---|---|
| Contexto macro/meso, cifras del sector con corte (C1–C6, C12) | Cap. 1 | Cap. 1 (+ matrícula universitaria y 64 universidades como población) |
| Términos legales, cómo funciona una ley, etapa de Ecuador, contraste de 6 países (C13–C16) | Cap. 1, Fundamentación | Cap. 2 |
| Plazos 5 días / 3 días / 72 h, SISPDP y comunicación a titulares (A1, A5) | Cap. 1 | Cap. 2 |
| Estado del arte (22 trabajos) + estudios nuevos sobre percepción estudiantil y políticas de privacidad | Cap. 1 | Cap. 2, "Antecedentes investigativos" |
| Equivalencia ISO 31000/27005, ISO/IEC 27035, NIST SP 800-61r3 (A3), como marco de referencia | Cap. 2 | Cap. 2 (marco) y Cap. 5 (fases de la guía) |
| Modelo de estimación, tabla de decisión, RA-1…RA-5, matriz | Cap. 2 | Cap. 5 (propuesta) |
| Delphi, K = ½(Kc + Ka), Brier, W de Kendall, V de Aiken (A6, B2, B5) | Cap. 2–3 | Cap. 3 (validación del instrumento) y Cap. 5 (validación de la guía) |
| Pruebas técnicas de la plantilla (1 057 fórmulas, T-01…T-06) | Cap. 3 | Cap. 5, separadas de la validación metodológica |
| 13 escenarios R-01…R-13 | Cap. 3 (UTI) | Cap. 5, reformulados como **escenarios sectoriales** activados por indicadores |
| Anexos Delphi, calibración, competencia, validación, plantilla, consistencia | Anexos | Anexos (adaptados) |

### Se elimina o se reemplaza → `descartado/caso_estudio/`
- Caracterización de la UTI, modelo SP1–SP6, aspectos críticos, requisitos D01–D10 (`REQUISITOS_DIAGNOSTICO.md`), fase P institucional, madurez, RAT, gran escala, EIPD de la UTI, trazabilidad con roles de la UTI, simulacro con responsables de la UTI y autorización institucional (A4, B1, B4 en su versión institucional).
- Anexos de entrevista, cuestionario de madurez, simulacro y autorización.
- `matriz/escenarios_candidatos_UTI.json` y `matriz/Matriz_UTI_preliminar.xlsx`.
- Copias íntegras de los capítulos, anexos, resumen y glosario anteriores (`*_version_caso_UTI.tex`).

### Se crea
- Capítulos nuevos: `02_Fundamentación.tex`, `04_Resultados.tex` y `05_Propuesta.tex`. Se reescriben `01_Introducción.tex`, `03_Metodología.tex` y `06_Conclusiones.tex`.
- Indicadores de OE1: **16 documentales (ID01–ID16)** y **15 de percepción (IE01–IE15)**, cada uno con su artículo de la LOPDP.
- `encuesta/cuestionario.md`, `encuesta/consentimiento_informado.md` y `encuesta/plan_analisis.md`.
- `analisis_documental/analisis_documental.xlsx` (ficha de registro con fórmulas), generada con `scripts/build_analisis_documental.js`.
- `scripts/analisis_encuesta.js` (frecuencias, alfa de Cronbach, chi-cuadrado, V de Aiken), probado solo con datos sintéticos.
- `matriz/escenarios_sectoriales.json` y `matriz/Matriz_escenarios_sectoriales.xlsx`. La plantilla `.xlsx` se generaliza (ya no se refiere a admisión y matrícula).

## 4. Nuevo esquema del documento

| Cap. | Título | Contenido | OE |
|---|---|---|---|
| 1 | Introducción | Contexto con cifras y corte, problema, justificación, objetivos, alcance y limitaciones | todos |
| 2 | Fundamentación teórica y legal | Términos legales, cómo funciona una ley, etapa de Ecuador, contraste internacional, vulneraciones, gestión de riesgos, ISO/NIST, antecedentes en universidades | OE1 |
| 3 | Metodología | Enfoque, población y muestra (censo de 64 universidades; encuesta n = 384), indicadores ID/IE, instrumentos, trazabilidad pregunta → indicador → artículo, validación (Aiken, piloto, Cronbach), procedimiento, ética, plan de análisis, cronograma, presupuesto | OE1–OE3 |
| 4 | Resultados | Análisis documental, encuesta y brechas (estructura completa; resultados "---" hasta tener datos) | OE2–OE4 |
| 5 | Propuesta y validación | Guía de gestión de riesgos (fases, escalas, decisión, aceptación), escenarios sectoriales, pruebas técnicas y validación por expertos | OE4 |
| 6 | Conclusiones y recomendaciones | Una conclusión por OE, limitaciones, recomendaciones, trabajos futuros | todos |

Trazabilidad objetivo → capítulo → instrumento → indicador → evidencia: tabla en el Cap. 3 y matriz de consistencia en los anexos.

## 5. Población y muestra (resumen)

- **Documental:** censo de las 64 universidades y escuelas politécnicas registradas en el CES (36 públicas, 20 particulares autofinanciadas, 8 cofinanciadas; consulta del 07-11-2026, el portal no indica fecha de corte).
- **Encuesta:** población de 841 404 estudiantes matriculados en universidades y escuelas politécnicas en 2023 (SIIES-SENESCYT, citado por Sumba-Nacipucha y Sánchez-Bayón, 2025). Con 95 % de confianza, 5 % de error y p = q = 0,5, n = 384. El muestreo es no probabilístico (por conveniencia con cuotas por sostenimiento), así que las inferencias se limitan a la muestra. La base oficial de SENESCYT (datos abiertos, 2015–2023) no pudo descargarse desde esta sesión: queda pendiente contrastar N.

## 6. Orden de ejecución

1. Rama, compilación inicial y este plan. ✔
2. Mover el material del caso a `descartado/caso_estudio/`. ✔
3. Verificar fuentes nuevas (matrícula, CES, LOPDP arts. 8, 10, 12–17, 26, 47–49, estudios sobre percepción y políticas de privacidad) y añadirlas al `.bib` en IEEE.
4. Reescribir el Cap. 1 y crear el Cap. 2 (con material trasladado del Cap. 1 anterior).
5. Escribir los Caps. 3, 4, 5 y 6.
6. Rehacer los anexos: ficha documental, cuestionario, consentimiento de la encuesta, validación del cuestionario, Delphi, calibración, competencia, validación de la guía, consentimiento de expertos, plantilla, consistencia.
7. Resumen, Abstract, Glosario y `main.tex` (título, inputs).
8. Generar la plantilla documental, la matriz sectorial y el script de análisis; probar con datos sintéticos.
9. Carpeta `encuesta/`.
10. Compilar hasta 0 errores y 0 referencias indefinidas; regenerar `tesis/cap1.md`.
11. CAMBIOS, PENDIENTES, FUENTES, CLAUDE.md, CLAUDEs.md (raíz = carpeta superior).
12. Commit en `reestructuracion-sin-caso`.
