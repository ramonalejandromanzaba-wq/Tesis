"""Ejecuta todo el análisis con un solo comando.

Datos reales (por defecto):
    python analisis/run_all.py
        lee  analisis/datos/respuestas.xlsx  y  analisis/datos/expertos.xlsx
        escribe en analisis/salida/  (datos_limpios.csv, *.csv, figuras/*.pdf, tablas/*.tex)
Prueba con datos simulados:
    python analisis/run_all.py --simulado
        genera y lee analisis/datos/ejemplo_simulado.xlsx y expertos_simulado.xlsx
        escribe en analisis/salida_simulada/ con marcas de agua "DATOS SIMULADOS"
Autopruebas con valores de referencia:
    python analisis/run_all.py --prueba
"""
import sys
from pathlib import Path

import descriptivos
import exportar_latex
import graficos
import inferencial
import limpieza
import validacion
from comun import BASE, carpeta, leer_tabla


def main():
    if "--prueba" in sys.argv:
        ok = validacion.autoprueba() & inferencial.autoprueba()
        sys.exit(0 if ok else 1)
    simulado = "--simulado" in sys.argv
    if simulado:
        import simular_datos
        simular_datos.BASE.mkdir(exist_ok=True)
        import pandas as pd
        with pd.ExcelWriter(simular_datos.BASE / "ejemplo_simulado.xlsx") as w:
            simular_datos.LEEME.to_excel(w, sheet_name="LEEME", index=False)
            simular_datos.respuestas().to_excel(w, sheet_name="Respuestas SIMULADAS", index=False)
        with pd.ExcelWriter(simular_datos.BASE / "expertos_simulado.xlsx") as w:
            simular_datos.LEEME.to_excel(w, sheet_name="LEEME", index=False)
            simular_datos.expertos().to_excel(w, sheet_name="Expertos SIMULADOS", index=False)
        resp, expe, salida = BASE / "datos/ejemplo_simulado.xlsx", BASE / "datos/expertos_simulado.xlsx", BASE / "salida_simulada"
    else:
        resp, expe, salida = BASE / "datos/respuestas.xlsx", BASE / "datos/expertos.xlsx", BASE / "salida"
    carpeta(salida)

    print(f"1/6 Limpieza: {resp.name}")
    datos, informe = limpieza.limpiar(leer_tabla(resp))
    limpios = salida / "datos_limpios.csv"
    datos.to_csv(limpios, index=False)
    print("    ", {k: v for k, v in informe.items() if k != "columnas_descartadas"})
    print("     Columnas descartadas (identificativas o sin código):", informe["columnas_descartadas"])

    print("2/6 Validación (V de Aiken; alfa, omega y KR-20)")
    if Path(expe).exists():
        larga, decision = validacion.tabla_aiken(leer_tabla(expe))
        larga.to_csv(salida / "aiken_por_criterio.csv", index=False)
        decision.to_csv(salida / "aiken_decision.csv", index=False)
        print(f"     Ítems que se conservan: {(decision['decision'] == 'Se conserva').sum()} de {len(decision)}")
    else:
        print(f"     (sin {Path(expe).name}: se omite la V de Aiken)")
    conf = validacion.confiabilidad(datos)
    conf.to_csv(salida / "confiabilidad.csv", index=False)
    print(conf[["escala", "items", "n", "alfa", "omega", "kr20"]].round(3).to_string(index=False))

    print("3/6 Descriptivos")
    descriptivos.ejecutar(limpios, salida)
    print("4/6 Inferencial (normalidad, H1–H3, exploratorios con Holm)")
    res = inferencial.ejecutar(limpios, salida)
    print(res["hipotesis"][["hipotesis", "prueba", "estadistico", "p", "efecto", "decision"]].round(4).to_string(index=False))
    print("5/6 Gráficos (PDF)")
    graficos.ejecutar(salida, simulado)
    print("6/6 Tablas LaTeX")
    exportar_latex.exportar(salida, simulado)
    print(f"Listo. Resultados en {salida}" + ("  — DATOS SIMULADOS: NO USAR EN EL DOCUMENTO" if simulado else ""))


if __name__ == "__main__":
    main()
