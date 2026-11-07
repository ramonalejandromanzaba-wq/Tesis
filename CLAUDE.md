# Tesis UTI — Contexto y progreso

Trabajo de Titulación (Ingeniería en Tecnologías de la Información, UTI, Quito).
- **Tema (desde 2026-11-07, pendiente de aprobación de la tutora):** DIAGNÓSTICO Y GESTIÓN DE RIESGOS EN EL TRATAMIENTO DE DATOS PERSONALES DE ESTUDIANTES UNIVERSITARIOS EN ECUADOR CONFORME A LA LOPDP (en `main.tex` va en minúsculas; el `.sty` lo pasa a mayúsculas donde corresponde). Tema anterior: "Metodología para el diagnóstico y gestión de riesgos en el tratamiento de datos personales".
- **Autor:** Ramon Alejandro Manzaba Castro · **Tutora:** María Cristina Jiménez Hernández, MSc. · **Año:** 2026
- **Repo:** https://github.com/ramonalejandromanzaba-wq/Tesis (rama `main`; reestructuración en `reestructuracion-sin-caso`)

## METODOLOGÍA CUANTITATIVA (2026-11-07, `uploads/metodologia_cuantitativa.md`) — complementa la reestructuración; prevalece sobre ella
- **Enfoque cuantitativo; no experimental, transversal; descriptivo-correlacional.** Hipótesis H1 (INF pública vs. privada: Mann-Whitney + r), H2 (DER–CNF: Spearman), H3 (consentimiento H2 × tipo: chi-cuadrado o Fisher + V de Cramér); α = 0,05; Holm en los exploratorios; KS-Lilliefors de normalidad.
- **Cuestionario v2.0** (`encuesta/cuestionario.md`): P00–P02, A1–A4, H1–H16 (hechos), Likert INF1–5, CON1–5, DER1–7, CNF1–6; inversos INF4, CON3, DER6, CNF3, CNF6 (x' = 6 − x). Cada pregunta del formulario empieza con `[CÓDIGO]` y las opciones se copian literalmente, porque `analisis/limpieza.py` las reconoce por texto. **El libro de códigos está en `analisis/config.py`: si cambia el cuestionario, se cambia ahí.**
- Validez: 3–5 jueces, V de Aiken ≥ 0,80 (pertinencia, claridad, coherencia): `encuesta/formato_juicio_expertos.md` y `encuesta/plantilla_juicio_expertos.xlsx` (de `scripts/build_plantilla_aiken.js`). Confiabilidad: α y ω por dimensión; KR-20 en H4–H7. La guía (V2) también usa V ≥ 0,80.
- **Análisis en Python** (carpeta `analisis/`; `python analisis/run_all.py [--prueba | --simulado]`). Verificación cruzada en jamovi o JASP. Los datos reales (`analisis/datos/respuestas.xlsx`, `expertos.xlsx`) y las salidas están en `.gitignore`. Los `*_simulado.xlsx` y `salida_simulada/` son SIMULADOS y nunca van al documento. Ya no existe `scripts/analisis_encuesta.js`.
- **Python 3.12.10** quedó instalado para el usuario (winget) en `%LOCALAPPDATA%\Programs\Python\Python312`; el entorno de pruebas se creó fuera del repositorio (`%TEMP%\claude_py`). Para trabajar: `python -m venv .venv` + `pip install -r analisis/requirements.txt` (versiones fijadas). La consola de Windows usa cp1252: `analisis/comun.py` fuerza UTF-8.
- PDF: 133 páginas, 0 errores. `referencias.bib`: 108 entradas.

## REESTRUCTURACIÓN SIN CASO DE ESTUDIO (2026-11-07) — manda sobre las secciones posteriores
- **Se eliminó el caso de estudio de la UTI** (la universidad no da acceso a datos internos). La tesis usa solo **información pública de las universidades** y una **encuesta anónima a estudiantes mayores de edad**. Ningún dato interno de ninguna universidad. Lo que abajo se dice del caso UTI (caracterización, SP1–SP6, D01–D10, autorización, fase P institucional, simulacro) es **histórico** y está en `descartado/caso_estudio/`.
- Instrucción: `uploads/reestructuracion_tesis.md`. Plan: `PLAN_REESTRUCTURACION.md`. Cambios: `CAMBIOS.md` (sección superior, con el estado de A1–C16). Pendientes: `PENDIENTES.md` (prioridad 1: la tutora aprueba el título y los objetivos).
- **Objetivo general:** Diagnosticar el cumplimiento de la LOPDP (2021) y de su Reglamento General (2023) en el tratamiento de datos personales de estudiantes por parte de las universidades ecuatorianas, mediante el análisis documental de su información pública y una encuesta anónima a estudiantes, para proponer una guía de gestión de riesgos validada por expertos.
- **OE:** OE1 Determinar requisitos → 31 indicadores (ID01–ID16 documentales; IE01–IE15 de percepción, cada uno con su artículo) · OE2 Analizar la información pública (censo de las 64 universidades del CES, ficha S/P/N, índice ITD) · OE3 Aplicar la encuesta (N = 841 404 en 2023, citado por `sumba2025economia`; n = 384; no probabilística, con cuotas 64/36; Aiken, piloto n = 30, Cronbach) · OE4 Evaluar la brecha (C_D, B_N, B_P en 7 pares) y proponer la guía (14 escenarios sectoriales R-01…R-14; Delphi V1 y juicio de expertos V2; IV01–IV10, con IV01–IV05 cumplidos).
- **Capítulos:** `01_Introducción` · `02_Fundamentación` (términos legales, ley, etapa, 6 países, vulneraciones, marcos ISO/NIST, antecedentes) · `03_Metodología` · `04_Resultados` (tablas con "---") · `05_Propuesta` (guía, escenarios, pruebas técnicas, validación) · `06_Conclusiones` · `07_Referencias` · `08_Glosario`. Labels de capítulo: `chap:introduccion`, `chap:fundamentacion`, `chap:metodologia`, `chap:resultados`, `chap:propuesta`, `chap:conclusiones`.
- **Anexos A–K** (`Anexos/01_Anexo.tex`): ficha documental (`anx:ficha_documental`), cuestionario (`anx:cuestionario`), consentimiento de la encuesta (`anx:consentimiento_encuesta`), validación del cuestionario (`anx:validacion_cuestionario`), Delphi, calibración, competencia, validación de la guía (`anx:validacion`), consentimiento de expertos (`anx:consentimiento_expertos`), plantilla y consistencia.
- **Archivos nuevos:** `encuesta/cuestionario.md` (con códigos de variable y regla de "afirmativo" por indicador), `encuesta/consentimiento_informado.md`, `encuesta/plan_analisis.md`; `analisis_documental/analisis_documental.xlsx` (de `scripts/build_analisis_documental.js`, 1 410 fórmulas; `--prueba` con datos sintéticos, que nunca se versionan); `scripts/analisis_encuesta.js` (sin dependencias: `prueba` | `aiken jueces.csv` | `encuesta respuestas.csv`); `matriz/escenarios_sectoriales.json` → `matriz/Matriz_escenarios_sectoriales.xlsx`. `build_matriz.js` quedó generalizado (procesos universitarios; las fórmulas no cambiaron).
- Cronograma 09-11-2026 a 26-02-2027 (16 semanas). Presupuesto: USD 80 (IA). PDF: 126 páginas, 0 errores. `referencias.bib`: 96 entradas (13 nuevas).
- Se mantiene la **regla sin rojo** del 27-10-2026, aunque la instrucción nueva pedía `\textcolor{red}`: el autor pidió "sigue el formato como lo venías haciendo".
- En esta máquina, el Bash tool falla con heredocs que contienen comillas o backticks (los heredocs con delimitador entrecomillado que alimentan a Python sí funcionan), y `sed` convierte `\t` en tabulador: para escribir archivos con LaTeX, usar Write o scripts de Node en el scratchpad. En las cadenas de JS, no meter las comillas LaTeX (dos backticks) dentro de template literals.

## Estructura
- `main.tex` — documento principal: datos de portada, autores, lectores, línea de investigación e `\input` de cada sección.
- `uti_tfm.sty` — plantilla de formato UTI (macros `\UTIPortada`, `\UTIDatosAutores`, `\UTIFrontMatter`, `\UTIMainMatter`, etc.). Normalmente no se edita.
- `Preliminares/01..09_*.tex` — repositorio digital, aprobaciones, declaración, dedicatoria, agradecimiento, índices, resumen, abstract.
- `Capítulos/01..08_*.tex` — Introducción, Fundamentación, Metodología, Resultados, Propuesta, Conclusiones, Referencias, Glosario (ver la sección de reestructuración). Imágenes en `Capítulos/fig/` y `Capítulos/img/`.
- `Anexos/01_Anexo.tex`, `referencias.bib` (BibTeX, estilo IEEEtran), `Logos/LOGO-UTI-*.png`.
- `manual/` — `Manual_de_Uso.tex` y `Manual_de_Diseno.tex` de la plantilla (referencia).
- `uploads/ITI_FORMATO PIC v1.docx` — formato oficial de referencia.

## Compilar (Windows, MiKTeX)
`latexmk` NO funciona (falta Perl). Usar en la raíz del proyecto:
```
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```
Errores: buscar líneas que empiezan con `! ` en `main.log`. El aviso "not checked for MiKTeX updates" es inofensivo.

## Git
- Identidad configurada solo en este repo: Ramon Manzaba / ramonalejandromanzaba@gmail.com.
- `.gitignore` excluye auxiliares de LaTeX (`*.aux`, `*.log`, `*.toc`, `*.bbl`, …) y pruebas `tmp_*`. `main.pdf` sí se versiona.
- Commits: `7f7d560` versión inicial · `ef23f9e` .gitignore y limpieza · `3a209f7` título nuevo, correo y CLAUDE.md · luego: título en inglés y línea 3.3.
- Ojo: en sed, `\U` en el reemplazo pasa a mayúsculas; para editar macros `\UTI...` usar Edit, no sed.

## Estado actual (2026-10-13)
- Compila sin errores: `main.pdf` de 30 páginas.
- Portada completa: título (ES e EN), autor, correo, tutora, ciudad, año y línea de investigación {3}{3} (Gobernanza y seguridad de la información).
- Lectores: Andrés Rubio Proaño, PhD. (principal) y Jaime Fabrizzio Peñafiel, MSc. firman en "Aprobación de lectores". Suplente: Juan Pabón, MSc. (la plantilla solo admite 2 lectores; queda como comentario en `main.tex`). Convención de nombres: sin "Ing."; sí el título de cuarto nivel (PhD., MSc.).

## Contexto académico (leer antes de redactar)
- `CLAUDEs.md` (copia en la raíz del repo; original en `../CLAUDEs.md`) — CLAUDE.md completo de la tesis: objetivos oficiales (copiar literal), exclusiones, normativa SPDP, reglas de la guía, ética. **Manda sobre todo lo demás.**
- `../ITI-TFG-B26-0021.pdf` — ficha institucional. Título oficial: "…datos personales **académicos conforme a la LOPDP**" (distinto del de `main.tex`; pendiente con tutora).
- `../REFERENCIAS.md` — 20 referencias verificadas (ya volcadas en `referencias.bib`).
- Plantilla UTI pide IEEE; el usuario pide APA 7 en borradores → decisión pendiente con tutora.
- spdp.gob.ec bloquea descargas automáticas; normas SPDP se obtuvieron vía Lexis/UTPL. Texto LOPDP verificado: consejodecomunicacion.gob.ec.
- Hallazgo clave: LOPDP art. 68 num. 4 = infracción grave no usar metodologías de análisis y gestión de riesgos.

## Capítulos
- **Cap. 1** — borrador en `tesis/cap1.md` (≈4 350 palabras, APA 7, estructura de la plantilla UTI). Pendientes en su sección "Notas para el autor". Fichas en `fuentes/fichas/`. **Ya pasado a `Capítulos/01_Introducción.tex`** con `\cite` (IEEE, numérico); el .md queda como borrador/notas. Si se edita uno, sincronizar el otro.
- 2026-10-20: objetivos reescritos (infinitivo + qué + cómo + para qué; LOPDP 2021 y RLOPDP 2023) y Estado del Arte ampliado a 5 ejes, 22 trabajos, Tablas 1–2 de trabajos y Tabla 3 comparativa de marcos (Sí/Parcial/No). 9 referencias nuevas verificadas (LINDDUN, Bieker, Habbabeh, Guerrero Argote, NIST PF, ENISA, AEPD 2021, ISO/IEC 29134:2023, SIC Colombia 2026). PDF: 50 páginas.
- **Decisión 2026-10-20 (autor):** caso de estudio = **proceso de admisión y matrícula de la UTI, sede Quito, con datos reales por levantar** (autorización formal pendiente). Nada institucional se estima ni se supone: todo dato o resultado de la UTI queda como `[PENDIENTE]` hasta aplicar los instrumentos. Lo único verificado de la UTI: Ley N.º 112, R.O. 373, 31-07-1998, derecho privado, domicilio Ambato, financiamiento por matrículas/pensiones (bib `congreso1998uti`). No se localizó política pública de protección de datos de la UTI (búsqueda oct. 2026).
- **Estilo (pedido del autor):** toda la tesis en formato de **ensayo argumentativo**: cada capítulo abre con una tesis explícita, cada sección cierra con una conclusión ("En síntesis…", "En consecuencia…") y se responde al menos una objeción (justificación, justificación técnica). Mantenerlo en los capítulos que falten.
- **Cap. 2**: caracterización de la UTI (tabla con fuente y `[PENDIENTE]`), modelo de referencia de 6 subprocesos SP1–SP6 "a validar", 8 "aspectos críticos a verificar" (no hallazgos), DSR, informantes (responsables de unidades + panel ≥5), técnicas, Brier, ética (autorización UTI; conflicto de interés sysadmin declarado), RF01–RF11, RNF01–RNF07, diseño fases 0–4, escalas, tabla de decisión, aceptación, matriz; justificación técnica con objeción y conclusión.
- **Cap. 3**: dos planos — (1) verificado: plantilla 1 057 fórmulas sin errores + casos T-01…T-06; (2) aplicación en la UTI: protocolo por fase con tablas de resultados `[PENDIENTE]` (madurez, RAT, gran escala condicional, riesgo inherente, EIPD, residual, antes/después), 13 **escenarios candidatos** R-01…R-13 (hipótesis de la literatura, no hallazgos) con controles candidatos e indicadores; cronograma y presupuesto mínimo: solo movilidad (12 × USD 5) y uso de agentes de IA (5 meses × USD 20) = USD 160, por pedido del autor.
- Escenarios candidatos en `matriz/escenarios_candidatos_UTI.json` → `node scripts/build_matriz.js matriz/Matriz_UTI_preliminar.xlsx matriz/escenarios_candidatos_UTI.json`. Al tener datos reales, completar el JSON (probabilidad, impacto, rationale, residual…) y regenerar; el script imprime los niveles para trasladarlos al Cap. 3. Se eliminaron los archivos del caso simulado IES-S. `main.tex` carga `colortbl` y `amsmath`. PDF: 90 páginas.
- **Formato final (2026-10-22):** se adoptó la plantilla de `Ingenieria_Tecnologias_Informacion.3/` (carpeta de referencia, no versionada): nuevo `uti_tfm.sty` (`\UTIFraseTituloPortada`, preliminares sin sangría, línea en portada), `main.tex` base (portada: "Trabajo de Integración Curricular previo a \UTIFraseTituloPortada") con nuestros datos y paquetes reinsertados, y `Preliminares/02` y `03` (fecha alineada a la derecha, "CERTIFICO" sin negrita). Capítulos, anexos y bib sin cambios de contenido. Los archivos `*(1).*` sueltos en la raíz no son del proyecto.
- `tesis/cap1.md` se **genera** desde el .tex con `node scripts/tex2md_cap1.js` (después de compilar, porque usa main.aux y main.bbl): citas IEEE con la misma numeración del PDF, tablas en Markdown y referencias del capítulo. El .tex es la fuente vigente; no editar el .md a mano.
- IEEEtran separa los números de 5 cifras en el campo `number` ("ISO 31 000"); en el .bib se escriben como `ISO 31{}000:2018`.
- **Anexos A–H** (2026-10-20) en `Anexos/01_Anexo.tex`: A lista de verificación normativa · B guía de entrevista · C cuestionario de madurez (20 ítems, 8 dominios, niveles 1–5) · D formulario Delphi · E 10 afirmaciones de calibración (mismas que la hoja Brier) · F validación por expertos (12 criterios Likert, validado si mediana ≥ 4) · G consentimiento informado · H descripción de la plantilla. Labels `anx:*`. PDF: 78 páginas.
- **Plantilla `.xlsx`**: `matriz/Plantilla_Matriz_Riesgos_LOPDP.xlsx`, generada con `scripts/build_matriz.js` (Node + exceljs 4.4.0 + hyperformula 2.7.1, instalados fuera del repo). Regenerar: `npm install exceljs@4.4.0 hyperformula@2.7.1` en una carpeta temporal y `NODE_PATH=<carpeta>/node_modules node scripts/build_matriz.js matriz/Plantilla_Matriz_Riesgos_LOPDP.xlsx`. El script verifica las 1 057 fórmulas con HyperFormula (QUARTILE se comprueba en JS porque HF no la implementa). Hojas: Instrucciones, Matriz (34 col., filas 5–104, fila 5 = ejemplo), Decisión, Escalas, Amenazas, Controles, Delphi, Brier, Mapa de calor, Listas. No hay Python ni LibreOffice en esta máquina.
- En Git Bash de esta máquina, `\\c` dentro de sed/perl inline se rompe; para regex con `\cite` usar un script `.pl` con `"\x5c"`. No hay Python.
- `main.tex` carga `tabularx`, `array`, `multirow`, `tikz` y `xurl` (añadidos para el Cap. 1). Títulos de normas en el .bib van con doble llave `{{…}}` para que IEEEtran no los pase a minúscula.
- Aviso inofensivo conocido: "Overfull \vbox" en la Tabla 2 (multirow); el PDF se ve bien.

## Revisión del tribunal y de la tutora (2026-10-27, rama `revision-tribunal`)
- Indicaciones originales en `indicaciones_revision.md` (raíz). Plan en `PLAN_REVISION.md`; archivos de control: `CAMBIOS.md` (A1–A8, B1–B7, C1–C16), `PENDIENTES.md` (por prioridad; la n.º 1 es la autorización formal de la UTI), `FUENTES.md` (URL y fecha de consulta de cada cifra o artículo) y `REQUISITOS_DIAGNOSTICO.md` (D01–D10).
- **4 objetivos específicos** (autorizados por el autor, por indicación de la tutora): OE1 Diagnóstico (determinar qué se necesita y diagnosticar), OE2 Universidades (situación y referentes), OE3 Implementar (escenarios, matriz inherente/residual, plan), OE4 Evaluar (Delphi, calibración, juicio de expertos, indicadores). **El objetivo general no se toca.**
- Cap. 1: §"El sector educativo ecuatoriano en cifras" (`sec:cifras_sector`), plazos verificados (5 días art. 43 reformado por la LOFC 2026 con CSIRT; 3 días a titulares art. 46; 72 h = art. 20-G de la LOTDA, solo entidades públicas y operadores de infraestructura crítica), fundamentación con términos legales, funcionamiento de una ley, cronología (corte 27-10-2026), comparativa de 6 países (página horizontal, `pdflscape`) y régimen de vulneraciones (SISPDP, Res. 0040-R).
- Cap. 2: requisitos D01–D10, insumos OE2 → diseño, **fase P de preparación**, equivalencia con ISO/IEC 27035-1:2023 y NIST SP 800-61r3, fuentes por variable, ecuaciones (impacto ajustado, ponderación Brier, K = ½(Kc + Ka), V de Aiken), reglas RA-1…RA-5, consenso (RIC ≤ 1 y ≥ 70 %) con W de Kendall.
- Cap. 3: Fase P; tablas de verificación normativa, riesgo inherente y residual (13 filas), **trazabilidad** escenario → artículo → control → rol → plazo → indicador; procedimiento de respuesta en 6 pasos; pruebas técnicas **separadas** de la §Validación metodológica (V1 aplicación real, V2 simulacro, indicadores IV01–IV12; IV01–IV03 cumplidos).
- Cap. 4 redactado (una conclusión por OE, limitaciones, recomendaciones, trabajos futuros). Resumen y Abstract, Glosario completos.
- Anexos nuevos: competencia (`anx:competencia`), simulacro (`anx:simulacro`), matriz de consistencia (`anx:consistencia`), autorización (`anx:autorizacion`). El Anexo F agrupa en pertinencia, claridad, suficiencia y coherencia.
- `main.tex`: `xcolor`, `pdflscape`; macros `\pend{…}` y `\verif{…}` (rojo). **Regla del autor (27-10-2026): el PDF que presenta no puede llevar nada en rojo ni marcas `[PENDIENTE]`/`[VERIFICAR]`.** Lo no disponible se redacta en negro ("no se halló… al [fecha]" / "no disponible a la fecha de corte"), las celdas vacías llevan "---" con una nota de corte, y nunca se inventan datos. No usar `\pend`/`\verif` en el texto.
- Objetivos específicos sin etiquetas en negrita (pedido del autor).
- Periodo real del proyecto: **13-10-2026 a 26-02-2027** (20 semanas). La planificación detallada está en `planificacion/Planificacion_Jira.csv` (CSV para importar en Jira) y en `planificacion/Planificacion.md`. `amssymb` choca con la plantilla (`\Bbbk` ya definido): no cargarlo.
- PDF: 127 páginas, 0 errores, 0 referencias indefinidas. 24 entradas nuevas en `referencias.bib`.
- Ojo: el 27-10-2026 a las 15:23 un editor externo sobrescribió `01_Introducción.tex` con una versión vieja; se restauró desde git. Cerrar el archivo en otros editores antes de que Claude lo edite.
- En sed de Git Bash, `\t` en el reemplazo genera un tabulador y `\u` pasa a mayúscula: para reemplazos con barras invertidas usar Edit o un script de Node.

## Pendientes detectados
- Ver `PENDIENTES.md`. Dedicatoria, agradecimiento y fechas de firma en Preliminares 01–06 los aporta el autor (marcados en rojo). `referencias.bib` tiene 79 entradas (6 de la plantilla, no citadas).
