# Tesis UTI — Contexto y progreso

Trabajo de Titulación (Ingeniería en Tecnologías de la Información, UTI, Quito).
- **Tema:** METODOLOGÍA PARA EL DIAGNÓSTICO Y GESTIÓN DE RIESGOS EN EL TRATAMIENTO DE DATOS PERSONALES (en `main.tex` va en minúsculas; el `.sty` lo pasa a mayúsculas donde corresponde).
- **Autor:** Ramon Alejandro Manzaba Castro · **Tutora:** Ing. Cristina Jiménez, MSc. · **Año:** 2026
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
- Lectores: Ing. Andrés Rubio Proaño, PhD. (principal) e Ing. Jaime Fabrizzio Peñafiel, MSc. firman en "Aprobación de lectores". Suplente: Ing. Juan Pabón, MSc. (la plantilla solo admite 2 lectores; queda como comentario en `main.tex`).

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
- **Cap. 2** (2026-10-20) redactado directamente en `Capítulos/02_Metodología.tex` (sin borrador .md). Caso de estudio **simulado** sobre **admisión y matrícula** de una IES ficticia "IES-S" (parámetros ficticios, Tabla de parámetros). Contiene: diagnóstico (6 subprocesos SP1–SP6, 8 limitaciones), área de estudio, DSR (Hevner; Peffers) ↔ fases ↔ OE, muestra intencional ≥5 expertos (Delphi), técnicas/instrumentos, Brier (ec.), ética, RF01–RF11 y RNF01–RNF07, diseño: fases 0–4 (figura TikZ), escalas de probabilidad (anual) e impacto (titular, adaptada de ENISA), agravantes, tabla de decisión de nivel (no multiplica; impacto muy alto ⇒ ≥ alto), criterios de aceptación, bloques de la matriz; justificación técnica. Las escalas son "versión inicial a calibrar por el Delphi". PDF: 64 páginas.
- **Anexos A–H** (2026-10-20) en `Anexos/01_Anexo.tex`: A lista de verificación normativa · B guía de entrevista · C cuestionario de madurez (20 ítems, 8 dominios, niveles 1–5) · D formulario Delphi · E 10 afirmaciones de calibración (mismas que la hoja Brier) · F validación por expertos (12 criterios Likert, validado si mediana ≥ 4) · G consentimiento informado · H descripción de la plantilla. Labels `anx:*`. PDF: 78 páginas.
- **Plantilla `.xlsx`**: `matriz/Plantilla_Matriz_Riesgos_LOPDP.xlsx`, generada con `scripts/build_matriz.js` (Node + exceljs 4.4.0 + hyperformula 2.7.1, instalados fuera del repo). Regenerar: `npm install exceljs@4.4.0 hyperformula@2.7.1` en una carpeta temporal y `NODE_PATH=<carpeta>/node_modules node scripts/build_matriz.js matriz/Plantilla_Matriz_Riesgos_LOPDP.xlsx`. El script verifica las 1 057 fórmulas con HyperFormula (QUARTILE se comprueba en JS porque HF no la implementa). Hojas: Instrucciones, Matriz (34 col., filas 5–104, fila 5 = ejemplo), Decisión, Escalas, Amenazas, Controles, Delphi, Brier, Mapa de calor, Listas. No hay Python ni LibreOffice en esta máquina.
- **Cap. 3** (2026-10-20) en `Capítulos/03_Implementación.tex`: fase 0 (madurez global 1 "Inicial"; checklist 0 C / 5 P / 10 N), RAT de 6 subprocesos, dictamen de gran escala (Res. 0005-R arts. 12 y 14 ⇒ EIPD y DPD obligatorios), 13 escenarios R-01…R-13, riesgo inherente (4 MA, 7 A, 2 M) y residual proyectado (1 A [R-09], 7 M, 3 B, 2 MB), mapas de calor TikZ, EIPD de SP3, plan de tratamiento, indicadores, procedimiento de notificación, 6 casos de prueba T-01…T-06, verificación RF01–RF11, cronograma (24 semanas) y presupuesto referencial (USD 5 397; normas ISO [VERIFICAR]). **Validación Delphi y por expertos: [PENDIENTE]** — las estimaciones son preliminares del investigador; no inventar resultados del panel.
- Escenarios en `matriz/escenarios_IES-S.json` → `node scripts/build_matriz.js matriz/Matriz_Aplicada_IES-S.xlsx matriz/escenarios_IES-S.json` imprime los niveles calculados; si se cambian escenarios, regenerar y actualizar las tablas del Cap. 3. `main.tex` carga ahora `colortbl` y `amsmath`. PDF: 88 páginas.
- En Git Bash de esta máquina, `\\c` dentro de sed/perl inline se rompe; para regex con `\cite` usar un script `.pl` con `"\x5c"`. No hay Python.
- `main.tex` carga `tabularx`, `array`, `multirow`, `tikz` y `xurl` (añadidos para el Cap. 1). Títulos de normas en el .bib van con doble llave `{{…}}` para que IEEEtran no los pase a minúscula.
- Aviso inofensivo conocido: "Overfull \vbox" en la Tabla 2 (multirow); el PDF se ve bien.

## Pendientes detectados
- Texto de plantilla aún presente en: Capítulos 02–03 y Preliminares 01–04. Conclusiones, Glosario y Anexo casi vacíos. `referencias.bib` tiene 40 entradas (29 fichas en `fuentes/fichas/`).
