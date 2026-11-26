"""Tablas en LaTeX (salida/tablas/*.tex) y frases de resultados (salida/frases_resultados.md) para el Cap. 4.

Uso: python analisis/exportar_latex.py salida/ [--simulado]
Cada tabla contiene solo el entorno tabular (el caption, el label y la fuente quedan en el capítulo), con coma
decimal y el mismo estilo de líneas de la plantilla UTI. Con --simulado, cada tabla lleva una advertencia y una
fila final "DATOS SIMULADOS — NO USAR".
Reporte agregado: ninguna tabla ni frase nombra o desglosa universidades; solo total y pública/privada (y la
composición por área, semestre, edad, sostenimiento y modalidad, con supresión de celdas < 5).
Frases en el orden dato → prueba → interpretación (Cap. 3, plan de análisis); la interpretación se completa a mano
con el artículo de la LOPDP indicado.
"""
import sys
from pathlib import Path

import pandas as pd

import config as C
from comun import carpeta, num, pval

EFECTO = {"r": "$r$", "rho": r"$\rho$", "V de Cramér": "$V_C$"}
AVISO = "% ADVERTENCIA: DATOS SIMULADOS. Solo prueban los scripts; NO deben incluirse en el documento.\n"
ARTICULO = {"H1": "art. 12 (derecho a la información)", "H2": "arts. 13 a 17 (derechos) y 37 (seguridad)",
            "H3": "arts. 7 y 8 (bases de legitimación y consentimiento por finalidad)"}


def _tabular(cabecera, filas, alineacion, simulado):
    lineas = [AVISO if simulado else "% Generado por analisis/exportar_latex.py a partir de datos reales (solo agregados).\n",
              f"\\begin{{tabular}}{{{alineacion}}}\n", "  \\hline\n",
              "  " + " & ".join(f"\\textbf{{{c}}}" for c in cabecera) + " \\\\ \\hline\n"]
    lineas += ["  " + " & ".join(str(v) for v in f) + " \\\\ \\hline\n" for f in filas]
    if simulado:
        lineas.append(f"  \\multicolumn{{{len(cabecera)}}}{{|c|}}{{\\textbf{{DATOS SIMULADOS --- NO USAR}}}} \\\\ \\hline\n")
    lineas.append("\\end{tabular}\n")
    return "".join(lineas)


def _escribir(salida, nombre, texto):
    (carpeta(salida, "tablas") / nombre).write_text(texto, encoding="utf-8")


def _leer(s, nombre):
    p = Path(s) / nombre
    return pd.read_csv(p) if p.exists() and p.stat().st_size > 2 else pd.DataFrame()


def _n(v):
    return v if isinstance(v, str) else num(int(v)) if not pd.isna(v) else "---"


def exportar(salida, simulado=False):
    s = Path(salida)
    frases = ["# Frases de resultados (generadas; revisar y completar la interpretación)\n",
              "> " + ("DATOS SIMULADOS — NO USAR.\n" if simulado else "Datos reales; solo agregados.\n")]

    comp = _leer(s, "desc_composicion.csv")
    if not comp.empty:
        filas = [[r.variable, r.categoria if isinstance(r.categoria, str) else "", _n(r.n), num(r.pct, 1),
                  num(r.get("pct_poblacion"), 1) if "pct_poblacion" in comp else "---"] for _, r in comp.iterrows()]
        _escribir(salida, "tab_composicion.tex", _tabular(
            ["Variable", "Categoría", "$n$", "Muestra (\\%)", "Matrícula nacional (\\%)"], filas, "|p{4.2cm}|p{4.6cm}|c|c|c|", simulado))
        nu = comp[comp["variable"].str.startswith("Universidades del censo")]["n"]
        if len(nu):
            frases.append(f"- Composición: respondieron estudiantes de {nu.iloc[0]} universidades y escuelas politécnicas "
                          f"del Ecuador (n válidas = {comp.iloc[0].n}); no se informa ningún resultado por universidad.\n")

    t = _leer(s, "desc_datos_solicitados.csv")
    if not t.empty:
        _escribir(salida, "tab_datos_solicitados.tex", _tabular(
            ["Dato solicitado", "Total (\\%)", "Pública (\\%)", "Privada (\\%)"],
            [[r.categoria, num(r.pct_Total, 1), num(r["pct_Pública"], 1), num(r.pct_Privada, 1)] for _, r in t.iterrows()],
            "|p{6.5cm}|c|c|c|", simulado))

    h = _leer(s, "desc_indicadores_hechos.csv")
    chi = _leer(s, "inf_expl_chi_cuadrado.csv")
    pmap = dict(zip(chi.get("variable", []), chi.get("p_holm", [])))
    vmap = dict(zip(chi.get("variable", []), chi.get("V_Cramer", [])))
    if not h.empty:
        _escribir(salida, "tab_hechos.tex", _tabular(
            ["Indicador", "Total (\\%)", "Sin NR (\\%)", "NR (\\%)", "Pública (\\%)", "Privada (\\%)", "$p$ (Holm)", "$V_C$"],
            [[r.indicador, num(r.pct_Total, 1), num(r.pct_sin_NR_Total, 1), num(r.pct_NR_Total, 1), num(r["pct_Pública"], 1),
              num(r.pct_Privada, 1), pval(pmap.get(r.pregunta)), num(vmap.get(r.pregunta), 2)] for _, r in h.iterrows()],
            "|p{4.6cm}|c|c|c|c|c|c|c|", simulado))
        for _, r in h.iterrows():
            if pd.isna(r.pct_Total):
                continue
            v = vmap.get(r.pregunta)
            frases.append(f"- {r.indicador}: en las universidades del Ecuador, el {num(r.pct_Total, 1)} % de los estudiantes "
                          f"respondió afirmativamente (n = {int(r.n_Total)}; {num(r.pct_sin_NR_Total, 1)} % sin contar «No recuerdo»). "
                          f"Pública {num(r['pct_Pública'], 1)} % vs. privada {num(r.pct_Privada, 1)} %"
                          + (f" (p de Holm = {pval(pmap.get(r.pregunta)).replace('$', '')}; V de Cramér = {num(v, 2)}, "
                             f"efecto {C.magnitud(v)})." if v is not None and not pd.isna(v) else ".")
                          + " Interpretación: [completar con el artículo de la LOPDP del indicador].\n")

    lk = _leer(s, "desc_likert.csv")
    mw = _leer(s, "inf_expl_mann_whitney.csv")
    if not lk.empty:
        lk = lk[lk["es_dimension"]]
        mw = mw.set_index("variable") if not mw.empty else mw
        filas = []
        for _, r in lk.iterrows():
            m = mw.loc[r.variable] if not mw.empty and r.variable in mw.index else None
            filas.append([C.DIMENSIONES[r.variable]["nombre"], num(r.mediana, 2), num(r.ric, 2),
                          num(m["mediana_publica"], 2) if m is not None else "---", num(m["mediana_privada"], 2) if m is not None else "---",
                          num(m["U"], 1) if m is not None else "---", pval(m["p_holm"]) if m is not None else "---",
                          num(m["r"], 2) if m is not None else "---"])
        _escribir(salida, "tab_dimensiones.tex", _tabular(
            ["Dimensión", "Mdn", "RIC", "Mdn púb.", "Mdn priv.", "$U$", "$p$ (Holm)", "$r$"], filas, "|l|c|c|c|c|c|c|c|", simulado))

    cf = _leer(s, "confiabilidad.csv")
    if not cf.empty:
        _escribir(salida, "tab_confiabilidad.tex", _tabular(
            ["Escala", "Ítems", "$n$", "$\\alpha$", "$\\omega$", "KR-20"],
            [[r.escala, int(r["items"]), int(r.n), num(r.alfa, 2), num(r.omega, 2), num(r.kr20, 2)] for _, r in cf.iterrows()],
            "|p{5.8cm}|c|c|c|c|c|", simulado))

    afe = _leer(s, "afe_por_escala.csv")
    if not afe.empty:
        _escribir(salida, "tab_afe.tex", _tabular(
            ["Escala", "$n$", "KMO", "Bartlett $p$", "Factores (paralelo)", "Var. expl. (\\%)", "Cargas $< 0{,}40$"],
            [[r.nombre, int(r.n), num(r.KMO, 2), pval(r.bartlett_p), int(r.factores_analisis_paralelo),
              num(100 * r.varianza_explicada_1f, 1), int(r.items_carga_menor_0_40)] for _, r in afe.iterrows()],
            "|p{4.6cm}|c|c|c|c|c|c|", simulado))

    hp = _leer(s, "inf_hipotesis.csv")
    if not hp.empty:
        _escribir(salida, "tab_hipotesis.tex", _tabular(
            ["Hipótesis", "Prueba", "Estadístico", "$p$", "Efecto", "Magnitud", "Decisión"],
            [[r.hipotesis, r.prueba if isinstance(r.prueba, str) else "---", num(r.estadistico, 3), pval(r.p),
              f"{EFECTO.get(r.medida_efecto, r.medida_efecto)} = {num(r.efecto, 2)}", r.get("magnitud", "---"), r.decision]
             for _, r in hp.iterrows()],
            "|c|l|c|c|c|c|l|", simulado))
        for _, r in hp.iterrows():
            if pd.isna(r.p):
                continue
            frases.append(f"- {r.hipotesis}: {r.prueba}, estadístico = {num(r.estadistico, 3)}, p = {pval(r.p).replace('$', '')}, "
                          f"{r.medida_efecto} = {num(r.efecto, 2)} (efecto {r.get('magnitud', '---')}, Cohen, 1988; n = {int(r.n)}). "
                          f"{r.decision}. Interpretación: [qué significa para la protección de datos en las universidades de "
                          f"Ecuador; LOPDP, {ARTICULO.get(r.hipotesis, '')}].\n")

    br = _leer(s, "brechas.csv")
    if not br.empty:
        tot = br[br["grupo"] == "Total"]
        _escribir(salida, "tab_brechas.tex", _tabular(
            ["Elemento (par)", "$C_D$", "$B_N$", "$C_E$", "$B_P$", "$C_D^w$", "$C_E^{id}$", "$B_P^w$"],
            [[f"{r.elemento} ({r.par})", num(r.C_D, 1), num(r.B_N, 1), num(r.C_E, 1), num(r.B_P_no_ponderada, 1),
              num(r.C_D_ponderado, 1), num(r.C_E_identificados, 1), num(r.B_P_ponderada, 1)] for _, r in tot.iterrows()],
            "|p{4.4cm}|c|c|c|c|c|c|c|", simulado))
        sost = br[br["grupo"] != "Total"]
        _escribir(salida, "tab_brechas_sostenimiento.tex", _tabular(
            ["Elemento", "Grupo", "$C_D^w$", "$C_E^{id}$", "$B_P^w$", "$n$"],
            [[r.elemento, r.grupo, num(r.C_D_ponderado, 1), num(r.C_E_identificados, 1), num(r.B_P_ponderada, 1),
              int(r.n_identificados)] for _, r in sost.iterrows()], "|p{4.4cm}|l|c|c|c|c|", simulado))
        for _, r in tot.iterrows():
            frases.append(f"- Brecha {r.elemento}: lo publicado, ponderado por la composición de la muestra, alcanza "
                          f"{num(r.C_D_ponderado, 1)} % y lo percibido {num(r.C_E_identificados, 1)} % (n = {int(r.n_identificados)} "
                          f"estudiantes de {int(r.universidades_en_muestra)} universidades); B_P^w = {num(r.B_P_ponderada, 1)} puntos "
                          f"(no ponderada, solo referencia: {num(r.B_P_no_ponderada, 1)}). Interpretación: [art. 10, lit. c, y art. 12].\n")

    kp = _leer(s, "kappa_documental.csv")
    if not kp.empty:
        _escribir(salida, "tab_kappa.tex", _tabular(
            ["Confiabilidad", "Universidades", "Calificaciones", "Acuerdo (\\%)", "$\\kappa_w$", "Interpretación"],
            [[r.tipo, int(r.universidades), int(r.calificaciones_comparadas), num(r.acuerdo_bruto_pct, 1),
              num(r.kappa_ponderado_lineal, 2), r.interpretacion] for _, r in kp.iterrows()], "|p{4.8cm}|c|c|c|c|l|", simulado))

    sn = _leer(s, "sensibilidad_itd.csv")
    if not sn.empty:
        _escribir(salida, "tab_sensibilidad_itd.tex", _tabular(
            ["Escenario", "Mdn total", "Mdn pública", "Mdn privada", "Diferencia", "$p$ (U)"],
            [[r.escenario, num(r.mediana_total, 1), num(r.mediana_publica, 1), num(r.mediana_privada, 1),
              num(r.diferencia_medianas_pub_menos_priv, 1), pval(r.p_mann_whitney)] for _, r in sn.iterrows()],
            "|l|c|c|c|c|c|", simulado))
        frases.append(f"- Sensibilidad del ITD: la conclusión por sostenimiento {'no cambia' if sn['conclusion_robusta'].iloc[0] else 'CAMBIA'} "
                      f"al usar P = 0, 0,5 o 1 para el nivel parcial.\n")

    ak = _leer(s, "aiken_decision.csv")
    if not ak.empty:
        cols = [c for c in C.CRITERIOS if c in ak]
        _escribir(salida, "tab_aiken.tex", _tabular(
            ["Instrumento", "Ítem"] + [c.capitalize() for c in cols] + ["Decisión"],
            [[r.get("instrumento", "Cuestionario"), r["item"]] + [num(r[c], 2) for c in cols] + [r["decision"]] for _, r in ak.iterrows()],
            "|l|l|" + "c|" * len(cols) + "l|", simulado))

    (Path(salida) / "frases_resultados.md").write_text("".join(frases), encoding="utf-8")


if __name__ == "__main__":
    exportar(sys.argv[1], "--simulado" in sys.argv)
