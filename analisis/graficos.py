"""Figuras en PDF para LaTeX (salida/figuras/). Uso: python analisis/graficos.py salida/ [--simulado]"""
import sys
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

import config as C
from comun import carpeta

plt.rcParams.update({"font.family": "serif", "font.size": 9, "axes.spines.top": False, "axes.spines.right": False})
GRIS = ["#4d4d4d", "#a6a6a6"]


def _marca(fig, simulado):
    if simulado:
        fig.text(0.5, 0.5, "DATOS SIMULADOS\nNO USAR", ha="center", va="center", fontsize=28, color="red", alpha=0.25, rotation=25)


def datos_solicitados(salida, simulado):
    t = pd.read_csv(Path(salida) / "desc_datos_solicitados.csv")
    t = t[t["codigo"] != "IE01"].sort_values("pct_Total")
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    y = range(len(t))
    ax.barh([i + 0.2 for i in y], t["pct_Pública"], height=0.4, color=GRIS[0], label="Pública")
    ax.barh([i - 0.2 for i in y], t["pct_Privada"], height=0.4, color=GRIS[1], label="Privada")
    ax.set_yticks(list(y), t["categoria"].str.replace(r" \(.*\)", "", regex=True))
    ax.set_xlabel("% de estudiantes a quienes se les solicitó")
    ax.set_xlim(0, 100)
    ax.legend(frameon=False, loc="lower right")
    _marca(fig, simulado)
    fig.tight_layout()
    fig.savefig(carpeta(salida, "figuras") / "fig_datos_solicitados.pdf")
    plt.close(fig)


def dimensiones(salida, simulado):
    df = pd.read_csv(Path(salida) / "datos_limpios.csv")
    fig, axes = plt.subplots(1, len(C.DIMENSIONES), figsize=(6.4, 2.6), sharey=True)
    for ax, (d, info) in zip(axes, C.DIMENSIONES.items()):
        datos = [df.loc[df[C.TIPO] == g, d].dropna() for g in (1, 2)]
        ax.boxplot(datos, tick_labels=["Púb.", "Priv."], widths=0.5, medianprops={"color": "black"})
        ax.set_title("\n".join(textwrap.wrap(info["nombre"], 16)), fontsize=8)
        ax.set_ylim(0.8, 5.2)
    axes[0].set_ylabel("Puntuación (1–5)")
    _marca(fig, simulado)
    fig.tight_layout()
    fig.savefig(carpeta(salida, "figuras") / "fig_dimensiones_por_tipo.pdf")
    plt.close(fig)


def ejecutar(salida, simulado=False):
    datos_solicitados(salida, simulado)
    dimensiones(salida, simulado)


if __name__ == "__main__":
    ejecutar(sys.argv[1], "--simulado" in sys.argv)
