"""Tablas en LaTeX (salida/tablas/*.tex) para incluir con \\input{} en el Cap. 4.

Uso: python analisis/exportar_latex.py salida/ [--simulado]
Cada archivo contiene solo el entorno tabular (el caption, el label y la fuente quedan en el capítulo),
con coma decimal y el mismo estilo de líneas de la plantilla UTI. Con --simulado, cada tabla lleva una
advertencia y una fila final "DATOS SIMULADOS — NO USAR" para que no pueda confundirse con resultados.
"""
import sys
from pathlib import Path

import pandas as pd

import config as C
from comun import carpeta, num, pval

EFECTO = {"r": "$r$", "rho": r"$\rho$", "V de Cramér": "$V_C$"}
AVISO = "% ADVERTENCIA: DATOS SIMULADOS. Solo prueban los scripts; NO deben incluirse en el documento.\n"


def _tabular(cabecera, filas, alineacion, simulado):
    lineas = [AVISO if simulado else "% Generado por analisis/exportar_latex.py a partir de datos reales.\n",
              f"\\begin{{tabular}}{{{alineacion}}}\n", "  \\hline\n",
              "  " + " & ".join(f"\\textbf{{{c}}}" for c in cabecera) + " \\\\ \\hline\n"]
    lineas += ["  " + " & ".join(str(v) for v in f) + " \\\\ \\hline\n" for f in filas]
    if simulado:
        lineas.append(f"  \\multicolumn{{{len(cabecera)}}}{{|c|}}{{\\textbf{{DATOS SIMULADOS --- NO USAR}}}} \\\\ \\hline\n")
    lineas.append("\\end{tabular}\n")
    return "".join(lineas)


def _escribir(salida, nombre, texto):
    (carpeta(salida, "tablas") / nombre).write_text(texto, encoding="utf-8")


def exportar(salida, simulado=False):
    s = Path(salida)
    t = pd.read_csv(s / "desc_datos_solicitados.csv")
    _escribir(salida, "tab_datos_solicitados.tex", _tabular(
        ["Dato solicitado", "Total (\\%)", "Pública (\\%)", "Privada (\\%)"],
        [[r.categoria, num(r.pct_Total, 1), num(r["pct_Pública"], 1), num(r.pct_Privada, 1)] for _, r in t.iterrows()],
        "|p{6.5cm}|c|c|c|", simulado))

    h = pd.read_csv(s / "desc_indicadores_hechos.csv")
    chi = pd.read_csv(s / "inf_expl_chi_cuadrado.csv") if (s / "inf_expl_chi_cuadrado.csv").stat().st_size > 2 else pd.DataFrame()
    pmap = dict(zip(chi.get("variable", []), chi.get("p_holm", [])))
    vmap = dict(zip(chi.get("variable", []), chi.get("V_Cramer", [])))
    _escribir(salida, "tab_hechos.tex", _tabular(
        ["Indicador", "Total (\\%)", "Pública (\\%)", "Privada (\\%)", "$p$ (Holm)", "$V_C$"],
        [[r.indicador, num(r.pct_Total, 1), num(r["pct_Pública"], 1), num(r.pct_Privada, 1),
          pval(pmap.get(r.pregunta)), num(vmap.get(r.pregunta), 2)] for _, r in h.iterrows()],
        "|p{5.6cm}|c|c|c|c|c|", simulado))

    lk = pd.read_csv(s / "desc_likert.csv")
    lk = lk[lk["es_dimension"]]
    mw = pd.read_csv(s / "inf_expl_mann_whitney.csv")
    mw = mw.set_index("variable")
    filas = []
    for _, r in lk.iterrows():
        m = mw.loc[r.variable] if r.variable in mw.index else None
        filas.append([C.DIMENSIONES[r.variable]["nombre"], num(r.mediana, 2), num(r.ric, 2),
                      num(m["mediana_publica"], 2) if m is not None else "---", num(m["mediana_privada"], 2) if m is not None else "---",
                      num(m["U"], 1) if m is not None else "---", pval(m["p_holm"]) if m is not None else "---",
                      num(m["r"], 2) if m is not None else "---"])
    _escribir(salida, "tab_dimensiones.tex", _tabular(
        ["Dimensión", "Mdn", "RIC", "Mdn púb.", "Mdn priv.", "$U$", "$p$ (Holm)", "$r$"], filas, "|l|c|c|c|c|c|c|c|", simulado))

    cf = pd.read_csv(s / "confiabilidad.csv")
    _escribir(salida, "tab_confiabilidad.tex", _tabular(
        ["Escala", "Ítems", "$n$", "$\\alpha$", "$\\omega$", "KR-20"],
        [[r.escala, int(r["items"]), int(r.n), num(r.alfa, 2), num(r.omega, 2), num(r.kr20, 2)] for _, r in cf.iterrows()],
        "|p{5.8cm}|c|c|c|c|c|", simulado))

    hp = pd.read_csv(s / "inf_hipotesis.csv")
    _escribir(salida, "tab_hipotesis.tex", _tabular(
        ["Hipótesis", "Prueba", "Estadístico", "$p$", "Efecto", "Decisión"],
        [[r.hipotesis, r.prueba if isinstance(r.prueba, str) else "---", num(r.estadistico, 3), pval(r.p),
          f"{EFECTO.get(r.medida_efecto, r.medida_efecto)} = {num(r.efecto, 2)}", r.decision] for _, r in hp.iterrows()],
        "|c|l|c|c|c|l|", simulado))

    if (s / "aiken_decision.csv").exists():
        ak = pd.read_csv(s / "aiken_decision.csv")
        cols = [c for c in C.CRITERIOS if c in ak]
        _escribir(salida, "tab_aiken.tex", _tabular(
            ["Ítem"] + [c.capitalize() for c in cols] + ["Decisión"],
            [[r["item"]] + [num(r[c], 2) for c in cols] + [r["decision"]] for _, r in ak.iterrows()],
            "|l|" + "c|" * len(cols) + "l|", simulado))


if __name__ == "__main__":
    exportar(sys.argv[1], "--simulado" in sys.argv)
