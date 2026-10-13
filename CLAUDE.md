# Tesis UTI — Contexto y progreso

Trabajo de Titulación (Ingeniería en Tecnologías de la Información, UTI, Quito).
- **Tema:** METODOLOGÍA PARA EL DIAGNÓSTICO Y GESTIÓN DE RIESGOS EN EL TRATAMIENTO DE DATOS PERSONALES (en `main.tex` va en minúsculas; el `.sty` lo pasa a mayúsculas donde corresponde).
- **Autor:** Ramon Alejandro Manzaba Castro · **Tutora:** Cristina Herrera · **Año:** 2026
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
- Commits: `7f7d560` versión inicial · `ef23f9e` .gitignore y limpieza.

## Estado actual (2026-10-13)
- Compila sin errores: `main.pdf` de 30 páginas.
- Portada con título, autor, correo, tutora, ciudad y año ya completados.

## Pendientes detectados
- `\UTIDatosTituloIngles{PROJECT TITLE IN ENGLISH}` sin completar.
- Lectores (`\UTIDatosLector1/2`) siguen con "Nombres Apellidos".
- `\UTISeleccionInvestigacion{0}{0}` sin elegir (probable: `{3}{3}` Gobernanza y seguridad de la información).
- Texto de plantilla aún presente en: Capítulos 01–03 y Preliminares 01–04. Conclusiones, Glosario y Anexo casi vacíos. `referencias.bib` tiene solo 6 entradas.
