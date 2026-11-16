"""Ejecuta todo el análisis con un solo comando (cuestionario v2.1).

Datos reales (por defecto):
    python analisis/run_all.py
        lee  analisis/datos/respuestas.xlsx, analisis/datos/jueces/*.xlsx (formato de jueces devuelto),
             privado/clave_universidades.xlsx, privado/analisis_documental.xlsx y, si existe,
             privado/analisis_documental_observador2.xlsx (segundo observador)
        escribe en analisis/salida/  (*.csv, figuras/*.pdf, tablas/*.tex, frases_resultados.md)
Prueba con datos simulados:
    python analisis/run_all.py --simulado
        genera y lee datos simulados (analisis/datos/*simulado*) y escribe en analisis/salida_simulada/
Autopruebas con valores de referencia:
    python analisis/run_all.py --prueba
Ningún paso exporta resultados por universidad (Cap. 3, reporte agregado).
"""
import sys
from pathlib import Path

import pandas as pd

import brechas
import descriptivos
import documental
import exportar_latex
import graficos
import inferencial
import kappa_documental
import limpieza
import potencia
import sensibilidad_itd
import validacion
import validez_constructo
from comun import BASE, carpeta, leer_tabla

PRIV = BASE.parent / "privado"


def main():
    if "--prueba" in sys.argv:
        ok = (validacion.autoprueba() & inferencial.autoprueba() & brechas.autoprueba()
              & kappa_documental.autoprueba() & potencia.autoprueba())
        print("TODAS LAS AUTOPRUEBAS SUPERADAS" if ok else "HAY AUTOPRUEBAS CON ERRORES")
        sys.exit(0 if ok else 1)
    simulado = "--simulado" in sys.argv
    if simulado:
        import simular_datos
        resp, jueces, doc, doc2 = simular_datos.escribir_todo()
        clave, salida = simular_datos.CLAVE_SIM, BASE / "salida_simulada"
    else:
        resp, jueces = BASE / "datos/respuestas.xlsx", BASE / "datos/jueces"
        doc, doc2 = PRIV / "analisis_documental.xlsx", PRIV / "analisis_documental_observador2.xlsx"
        clave, salida = None, BASE / "salida"
    carpeta(salida)

    print(f"1/9 Limpieza: {resp.name}")
    datos, informe = limpieza.limpiar(leer_tabla(resp), clave)
    limpios = salida / "datos_limpios.csv"
    datos.to_csv(limpios, index=False)
    pd.DataFrame([{k: v for k, v in informe.items() if k not in ("columnas_descartadas", "inversos_recodificados")}]
                 ).to_csv(salida / "informe_limpieza.csv", index=False)
    print("    ", {k: v for k, v in informe.items() if k != "columnas_descartadas"})
    print("     Columnas descartadas (identificativas o sin código):", informe["columnas_descartadas"])

    print("2/9 Validez de contenido (V de Aiken, escala 1–4) y competencia de los jueces")
    if Path(jueces).exists():
        ancha, ks = validacion.leer_jueces(jueces)
        larga, decision = validacion.tabla_aiken(ancha)
        larga.to_csv(salida / "aiken_por_criterio.csv", index=False)
        decision.to_csv(salida / "aiken_decision.csv", index=False)
        ks.to_csv(salida / "jueces_competencia.csv", index=False)
        print(f"     Jueces: {len(ks)}. Ítems que se conservan: {(decision['decision'] == 'Se conserva').sum()} de {len(decision)}")
    else:
        print(f"     (sin {jueces}: se omite la V de Aiken)")

    print("3/9 Confiabilidad (alfa, omega y KR-20) y validez de constructo (AFE)")
    conf = validacion.confiabilidad(datos)
    conf.to_csv(salida / "confiabilidad.csv", index=False)
    print(conf[["escala", "items", "n", "alfa", "omega", "kr20"]].round(3).to_string(index=False))
    afe, _, _, glob = validez_constructo.ejecutar(limpios, salida)
    if not afe.empty:
        print(afe[["dimension", "n", "KMO", "bartlett_p", "factores_analisis_paralelo", "varianza_explicada_1f",
                   "items_carga_menor_0_40"]].round(3).to_string(index=False))

    print("4/9 Descriptivos (composición, hechos con y sin «No recuerdo», escalas)")
    descriptivos.ejecutar(limpios, salida, BASE / "datos/siies_pichincha.csv")
    print("5/9 Inferencial (normalidad descriptiva, H1–H3, exploratorios con Holm)")
    res = inferencial.ejecutar(limpios, salida)
    print(res["hipotesis"][["hipotesis", "prueba", "estadistico", "p", "efecto", "magnitud", "decision"]].round(4).to_string(index=False))

    print("6/9 Componente documental (brechas ponderadas, kappa, sensibilidad del ITD)")
    if Path(doc).exists() and not documental.leer_registro(doc).empty:
        reg = documental.leer_registro(doc)
        brechas.calcular(datos, reg).to_csv(salida / "brechas.csv", index=False)
        kappa_documental.calcular(doc, doc2 if Path(doc2).exists() else None).to_csv(salida / "kappa_documental.csv", index=False)
        sensibilidad_itd.calcular(reg).to_csv(salida / "sensibilidad_itd.csv", index=False)
        print(f"     Universidades en el registro: {len(reg)}")
    else:
        print(f"     (sin registro documental en {doc}: se omiten brechas, kappa y sensibilidad)")

    print("7/9 Potencia efectiva con el n alcanzado (plan B)")
    n1 = int((datos["TIPO"] == 1).sum()); n2 = int((datos["TIPO"] == 2).sum())
    if n1 > 2 and n2 > 2:
        pt = potencia.tabla(n1 + n2, n1, n2)
        pt.to_csv(salida / "potencia_efectiva.csv", index=False)
        print(pt[["hipotesis", "n", "efecto_minimo_detectable", "potencia_con_referencia"]].round(3).to_string(index=False))
    print("8/9 Gráficos (PDF)")
    graficos.ejecutar(salida, simulado)
    print("9/9 Tablas LaTeX y frases de resultados (dato → prueba → interpretación)")
    exportar_latex.exportar(salida, simulado)
    print(f"Listo. Resultados en {salida}" + ("  — DATOS SIMULADOS: NO USAR EN EL DOCUMENTO" if simulado else ""))


if __name__ == "__main__":
    main()
