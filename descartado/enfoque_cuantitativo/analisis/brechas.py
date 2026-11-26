"""Brechas entre la norma, lo publicado y lo percibido (Cap. 3, Ecuaciones de la brecha; R1.1).

Uso: python analisis/brechas.py salida/datos_limpios.csv [privado/analisis_documental.xlsx] salida/
Para cada uno de los siete pares de indicadores equivalentes calcula:
  C_D   cumplimiento documental no ponderado: todas las universidades del censo pesan igual (descriptivo).
  B_N   brecha normativa = 100 − C_D.
  C_D^w cumplimiento documental ponderado por la composición de la muestra: w_u = n_u / n_id, donde n_u es el
        número de encuestados de la universidad u y n_id el de encuestados con universidad del censo identificada.
  C_E^id porcentaje de respuestas afirmativas entre esos mismos n_id encuestados.
  B_P^w brecha de percepción ponderada (PRINCIPAL) = C_D^w − C_E^id: compara las mismas universidades en ambos planos.
  B_P   brecha no ponderada (solo referencia) = C_D − C_E (C_E sobre todos los encuestados válidos).
También por sostenimiento (pública / privada). Nunca se exporta un valor por universidad; los grupos con menos de
5 encuestados se suprimen (config.MIN_CELDA).
"""
import sys

import numpy as np
import pandas as pd

import config as C
import documental as D
from comun import carpeta

# (elemento, indicador documental, regla de "afirmativo" en la encuesta)
PARES = [
    ("Fines", "ID03", lambda d: d["H4"] == 1, ["H4"]),
    ("Responsable y su contacto", "ID02", lambda d: (d["H5a"] == 1) & (d["H5b"] == 1), ["H5a", "H5b"]),
    ("Conservación", "ID05", lambda d: d["H6"] == 1, ["H6"]),
    ("Terceros (promedio de ID06a e ID06b)", "ID06", lambda d: d["H7"] == 1, ["H7"]),
    ("Consentimiento por finalidad", "ID14", lambda d: d["H8"] == 1, ["H8"]),
    ("Derechos (DER ≥ 4)", "ID07", lambda d: d["DER"] >= 4, ["DER"]),
    ("Canal de derechos", "ID08", lambda d: d["H16"] == 1, ["H16"]),
]


def _ce(enc, regla, cols):
    d = enc.dropna(subset=cols)
    return (100 * regla(d).mean(), len(d)) if len(d) >= C.MIN_CELDA else (np.nan, len(d))


def calcular(enc: pd.DataFrame, reg: pd.DataFrame, p=0.5) -> pd.DataFrame:
    enc = enc.copy()
    filas = []
    grupos = {"Total": (None, None), "Pública": (1, 1), "Privada": (2, 2)}
    for elemento, idd, regla, cols in PARES:
        s_u = dict(zip(reg["codigo"], D.puntaje_indicador(reg, idd, p)))
        for g, (t_enc, t_reg) in grupos.items():
            r_g = reg if t_reg is None else reg[reg["tipo"] == t_reg]
            e_g = enc if t_enc is None else enc[enc[C.TIPO] == t_enc]
            s = D.puntaje_indicador(r_g, idd, p).dropna()
            cd = 100 * s.mean() if len(s) else np.nan
            ce, n_ce = _ce(e_g, regla, cols)
            # ponderación por la composición real de la muestra
            ident = e_g[e_g["UNIV"].isin([k for k, v in s_u.items() if not pd.isna(v)])].dropna(subset=cols)
            if len(ident) >= C.MIN_CELDA:
                w = ident["UNIV"].value_counts(normalize=True)
                cdw = 100 * sum(w[u] * s_u[u] for u in w.index)
                cei = 100 * regla(ident).mean()
                n_univ = int(w.size)
            else:
                cdw = cei = np.nan
                n_univ = int(ident["UNIV"].nunique())
            filas.append({"elemento": elemento, "par": f"{idd}–{'/'.join(cols)}", "grupo": g,
                          "universidades_censo": int(len(s)), "C_D": cd, "B_N": 100 - cd if not pd.isna(cd) else np.nan,
                          "n_encuestados": n_ce, "C_E": ce, "B_P_no_ponderada": cd - ce,
                          "n_identificados": int(len(ident)), "universidades_en_muestra": n_univ,
                          "C_D_ponderado": cdw, "C_E_identificados": cei, "B_P_ponderada": cdw - cei})
    return pd.DataFrame(filas)


def autoprueba():
    """Dos universidades: U01 publica (S) y U02 no (N). 30 encuestados de U01 (20 afirman) y 10 de U02 (0 afirman).
    C_D = 50; C_D^w = 0,75·100 + 0,25·0 = 75; C_E^id = 20/40 = 50; B_P^w = 25; B_P no ponderada = 50 − 50 = 0."""
    reg = pd.DataFrame({"codigo": ["U01", "U02"], "sostenimiento": ["Pública", "Pública"], "tipo": [1, 1],
                        **{i: ["S", "N"] for i in D.TODOS}})
    enc = pd.DataFrame({"UNIV": ["U01"] * 30 + ["U02"] * 10, C.TIPO: 1,
                        "H4": [1] * 20 + [2] * 10 + [2] * 10})
    for c in ("H5a", "H5b", "H6", "H7", "H8", "H16", "DER"):
        enc[c] = enc["H4"]
    t = calcular(enc, reg)
    f = t[(t["par"].str.startswith("ID03")) & (t["grupo"] == "Total")].iloc[0]
    ok = all(abs(a - b) < 1e-9 for a, b in [(f.C_D, 50), (f.C_D_ponderado, 75), (f.C_E_identificados, 50),
                                             (f.B_P_ponderada, 25), (f.B_P_no_ponderada, 0)])
    print(("OK " if ok else "ERR") + f" brecha ponderada: C_D = {f.C_D:.1f}; C_D^w = {f.C_D_ponderado:.1f}; "
          f"C_E^id = {f.C_E_identificados:.1f}; B_P^w = {f.B_P_ponderada:.1f}; B_P = {f.B_P_no_ponderada:.1f}")
    return ok


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "prueba":
        sys.exit(0 if autoprueba() else 1)
    limpios = sys.argv[1]
    reg = D.leer_registro(sys.argv[2] if len(sys.argv) > 3 else None)
    salida = sys.argv[-1]
    t = calcular(pd.read_csv(limpios), reg)
    t.to_csv(carpeta(salida) / "brechas.csv", index=False)
    print(t.round(1).to_string(index=False))
