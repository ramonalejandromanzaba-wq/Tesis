"""Genera encuesta/consentimiento_informado.pdf a partir de encuesta/consentimiento_informado.md.

Uso: python scripts/consentimiento_pdf.py
Convierte el Markdown (títulos, negritas, cursivas, listas y separadores) a LaTeX y lo compila con pdflatex
(MiKTeX). Los numerales del art. 12 entre corchetes se muestran como nota pequeña al final de cada párrafo;
la nota interna del encabezado (líneas que empiezan con ">") no se incluye. La marca [PENDIENTE: …] de la
verificación ética se reemplaza por un texto de "en trámite", porque este PDF acompaña a la propia solicitud.
"""
import re
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
MD = RAIZ / "encuesta" / "consentimiento_informado.md"
TEX = RAIZ / "encuesta" / "consentimiento_informado.tex"


def esc(s):
    s = s.replace("\\", r"\textbackslash{}")
    for a, b in [("&", r"\&"), ("%", r"\%"), ("#", r"\#"), ("_", r"\_"), ("$", r"\$")]:
        s = s.replace(a, b)
    return s


def inline(s):
    s = esc(s)
    s = re.sub(r"\[PENDIENTE:[^\]]*\]", "en trámite; se completará con la respuesta a la solicitud de verificación ética "
               "presentada a la Universidad Tecnológica Indoamérica. La encuesta no se publica sin ella", s)
    s = re.sub(r"\[(nums?\.[^\]]*)\]", r"{\\footnotesize\\color{gray}(LOPDP, art.~12, \1)}", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", s)
    s = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"\\textit{\1}", s)
    s = re.sub(r"`([^`]+)`", r"\\texttt{\1}", s)
    s = s.replace(" · ", " \\textperiodcentered{} ")
    return s


def convertir(md):
    out, en_lista = [], False
    for ln in md.splitlines():
        if ln.startswith(">"):
            continue
        if ln.startswith("- "):
            if not en_lista:
                out.append(r"\begin{itemize}")
                en_lista = True
            out.append(r"  \item " + inline(ln[2:]))
            continue
        if en_lista:
            out.append(r"\end{itemize}")
            en_lista = False
        if ln.startswith("# "):
            out.append(r"\begin{center}{\large\bfseries " + inline(ln[2:]) + r"}\end{center}")
        elif ln.strip() == "---":
            out.append(r"\medskip\noindent\rule{\textwidth}{0.4pt}\medskip")
        else:
            out.append(inline(ln))
    if en_lista:
        out.append(r"\end{itemize}")
    return "\n".join(out)


PRE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[spanish,es-noshorthands]{babel}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[margin=2.3cm]{geometry}
\usepackage{xcolor}
\usepackage{textcomp}
\usepackage[hidelinks]{hyperref}
\hypersetup{pdfauthor={Ramón Alejandro Manzaba Castro}, pdftitle={Consentimiento informado de la encuesta (versión 2.1)}}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\begin{document}
{\small\textit{Texto de la primera pantalla del formulario en línea. Versión 2.1, 25 de noviembre de 2026. Trabajo de Integración Curricular: Metodología para el diagnóstico y gestión de riesgos en el tratamiento de datos personales académicos conforme a la LOPDP en universidades ecuatorianas. Las notas grises indican el numeral del art.~12 de la LOPDP que cubre cada párrafo y no se muestran al participante.}}
\medskip
"""

if __name__ == "__main__":
    TEX.write_text(PRE + convertir(MD.read_text(encoding="utf-8")) + "\n\\end{document}\n", encoding="utf-8")
    for _ in range(2):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", TEX.name], cwd=TEX.parent,
                           capture_output=True, text=True, encoding="latin-1")
    log = (TEX.parent / "consentimiento_informado.log").read_text(encoding="latin-1")
    errores = [l for l in log.splitlines() if l.startswith("! ")]
    for ext in (".aux", ".log", ".out"):
        (TEX.parent / ("consentimiento_informado" + ext)).unlink(missing_ok=True)
    print("Errores:", errores or "ninguno", "| PDF:", TEX.with_suffix(".pdf"))
