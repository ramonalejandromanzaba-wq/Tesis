"""Genera el cartel en PDF con el código QR del formulario de la encuesta.

Uso:
  python scripts/cartel_qr.py <enlace público del formulario>    → encuesta/cartel_encuesta.pdf
  python scripts/cartel_qr.py --ejemplo                           → encuesta/cartel_encuesta_EJEMPLO.pdf

Con --ejemplo usa un enlace ficticio y marca el cartel con "EJEMPLO — NO IMPRIMIR": sirve solo para revisar el diseño.
El QR lo dibuja LaTeX (paquete qrcode de MiKTeX) con corrección de errores alta, para que se lea aunque el papel
se arrugue. El texto resume la primera pantalla del consentimiento; no reemplaza al consentimiento del formulario.
"""
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CARPETA = RAIZ / "encuesta"
ENLACE_EJEMPLO = "https://docs.google.com/forms/d/e/EJEMPLO-ENLACE-FICTICIO/viewform"

PLANTILLA = r"""\documentclass[12pt,a4paper]{article}
\usepackage[spanish,es-noshorthands]{babel}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[margin=1.6cm]{geometry}
\usepackage{xcolor}
\usepackage{qrcode}
\usepackage{tikz}
\usepackage[hidelinks]{hyperref}
\definecolor{azul}{HTML}{1F3864}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\begin{document}
@@MARCA@@
\begin{center}
{\color{azul}\fontsize{30}{36}\selectfont\bfseries ¿Qué hace tu universidad\\[2pt] con tus datos personales?\par}
\vspace{10pt}
{\Large Encuesta para estudiantes universitarios del Ecuador\par}
\vspace{16pt}
\fcolorbox{azul}{white}{\parbox{0.86\textwidth}{\centering\large
\vspace{4pt}
\textbf{¿Quién puede responder?}\\ Estudiantes de \textbf{grado}, de \textbf{18 años o más}, de \textbf{cualquier}\\ universidad o escuela politécnica del país, pública o privada.\\[6pt]
\textbf{Tiempo:} 13 a 15 minutos \quad\textbullet\quad \textbf{Participación voluntaria}\\[6pt]
No se piden nombre, cédula, correo ni matrícula.\\
Los resultados se publican solo en conjunto, nunca por universidad.
\vspace{4pt}}}
\vspace{18pt}

\qrset{height=8.8cm, level=H}
\qrcode{@@URL@@}

\vspace{10pt}
{\Large\bfseries Escanea el código para participar\par}
\vspace{6pt}
{\small\ttfamily\color{gray}@@URL_VISIBLE@@\par}
\vfill
{\small Trabajo de Integración Curricular --- Ingeniería en Tecnologías de la Información,\\
Universidad Tecnológica Indoamérica. Responsable: Ramón Alejandro Manzaba Castro\\
(ramonalejandromanzaba@gmail.com), bajo la tutoría de María Cristina Jiménez Hernández, MSc.\\
Verificación ética: @@ETICA@@\par}
\end{center}
\end{document}
"""

MARCA = r"""\begin{tikzpicture}[remember picture, overlay]
\node[rotate=40, scale=6.5, text opacity=0.18, color=red, font=\bfseries] at (current page.center) {EJEMPLO};
\node[anchor=north, yshift=-0.5cm, fill=red!85, text=white, font=\bfseries\large, inner sep=6pt] at (current page.north) {EJEMPLO --- NO IMPRIMIR: el código QR lleva a un enlace ficticio};
\end{tikzpicture}"""


def esc_tt(s):
    return "".join("\\" + c if c in "#%&_{}$" else c for c in s).replace("~", r"\textasciitilde{}")


def main():
    args = sys.argv[1:]
    ejemplo = "--ejemplo" in args
    urls = [a for a in args if not a.startswith("--")]
    if not ejemplo and len(urls) != 1:
        sys.exit("Uso: python scripts/cartel_qr.py <enlace público> | --ejemplo")
    url = ENLACE_EJEMPLO if ejemplo else urls[0]
    if not ejemplo and not url.startswith("https://"):
        sys.exit("El enlace debe empezar con https://")
    etica = ("en trámite (ejemplo)" if ejemplo else
             (sys.argv[sys.argv.index("--etica") + 1] if "--etica" in sys.argv else "ver la primera pantalla del formulario"))
    nombre = "cartel_encuesta_EJEMPLO" if ejemplo else "cartel_encuesta"
    tex = (PLANTILLA.replace("@@MARCA@@", MARCA if ejemplo else "")
           .replace("@@URL@@", url.replace("#", r"\#").replace("%", r"\%"))
           .replace("@@URL_VISIBLE@@", esc_tt(url)).replace("@@ETICA@@", etica))
    ruta = CARPETA / f"{nombre}.tex"
    ruta.write_text(tex, encoding="utf-8")
    for _ in range(2):  # remember picture necesita dos pasadas
        subprocess.run(["pdflatex", "-interaction=nonstopmode", ruta.name], cwd=CARPETA, capture_output=True)
    log = (CARPETA / f"{nombre}.log").read_text(encoding="latin-1")
    errores = [l for l in log.splitlines() if l.startswith("! ")]
    for ext in (".aux", ".log", ".out", ".tex"):
        (CARPETA / (nombre + ext)).unlink(missing_ok=True)
    print("Errores:", errores or "ninguno", "| PDF:", CARPETA / f"{nombre}.pdf", "| enlace:", url)


if __name__ == "__main__":
    main()
