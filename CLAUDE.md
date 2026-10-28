# Tesis UTI — Contexto y progreso

Trabajo de Titulación (Ingeniería en Tecnologías de la Información, UTI, Quito).
- **Tema:** METODOLOGÍA PARA EL DIAGNÓSTICO Y GESTIÓN DE RIESGOS EN EL TRATAMIENTO DE DATOS PERSONALES (en `main.tex` va en minúsculas; el `.sty` lo pasa a mayúsculas donde corresponde).
- **Autor:** Ramon Alejandro Manzaba Castro · **Tutora:** María Cristina Jiménez Hernández, MSc. · **Año:** 2026
- **Repo:** https://github.com/ramonalejandromanzaba-wq/Tesis (rama `main`)

## Estructura
- `main.tex` — documento principal: datos de portada, autores, lectores, línea de investigación e `\input` de cada sección.
- `uti_tfm.sty` — plantilla de formato UTI (macros `\UTIPortada`, `\UTIDatosAutores`, `\UTIFrontMatter`, `\UTIMainMatter`, etc.). Normalmente no se edita.
- `Preliminares/01..09_*.tex` — repositorio digital, aprobaciones, declaración, dedicatoria, agradecimiento, índices, resumen, abstract.
- `Capítulos/01..06_*.tex` — Introducción, Metodología, Implementación, Conclusiones, Referencias, Glosario. Imágenes en `Capítulos/fig/` y `Capítulos/img/`.
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
- **Cap. 3**: dos planos — (1) verificado: plantilla 1 057 fórmulas sin errores + casos T-01…T-06; (2) aplicación en la UTI: protocolo por fase con tablas de resultados `[PENDIENTE]` (madurez, RAT, gran escala condicional, riesgo inherente, EIPD, residual, antes/después), 13 **escenarios candidatos** R-01…R-13 (hipótesis de la literatura, no hallazgos) con controles candidatos e indicadores; cronograma y presupuesto referencial (USD 5 397; normas ISO [VERIFICAR]).
- Escenarios candidatos en `matriz/escenarios_candidatos_UTI.json` → `node scripts/build_matriz.js matriz/Matriz_UTI_preliminar.xlsx matriz/escenarios_candidatos_UTI.json`. Al tener datos reales, completar el JSON (probabilidad, impacto, rationale, residual…) y regenerar; el script imprime los niveles para trasladarlos al Cap. 3. Se eliminaron los archivos del caso simulado IES-S. `main.tex` carga `colortbl` y `amsmath`. PDF: 90 páginas.
- **Formato final (2026-10-22):** se adoptó la plantilla de `Ingenieria_Tecnologias_Informacion.3/` (carpeta de referencia, no versionada): nuevo `uti_tfm.sty` (`\UTIFraseTituloPortada`, preliminares sin sangría, línea en portada), `main.tex` base (portada: "Trabajo de Integración Curricular previo a \UTIFraseTituloPortada") con nuestros datos y paquetes reinsertados, y `Preliminares/02` y `03` (fecha alineada a la derecha, "CERTIFICO" sin negrita). Capítulos, anexos y bib sin cambios de contenido. Los archivos `*(1).*` sueltos en la raíz no son del proyecto.
- `tesis/cap1.md` quedó **desactualizado** respecto del .tex (UTI y estilo argumentativo); el .tex es la fuente vigente.
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
