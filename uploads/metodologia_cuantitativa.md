# Metodología cuantitativa — ITI-TFG-B26-0021

Complementa `uploads/reestructuracion_tesis.md` (que sigue vigente). Lee primero los CLAUDE.md / CLAUDEs.md y ese archivo. Trabaja de forma autónoma en la rama `reestructuracion-sin-caso`. Si algo de aquí contradice la sección 4 de reestructuracion_tesis.md, prevalece este archivo.

Contexto que debes tener claro:
- No hay caso de estudio: no hay acceso a datos internos de ninguna universidad.
- La tesis se basa en información pública de universidades y en una encuesta anónima solo a estudiantes, mayores de 18 años, sobre qué datos les pidieron, si fueron informados, si dieron su consentimiento y si conocen sus derechos.
- Se mantienen 4 objetivos específicos: diagnóstico → universidades → implementar → evaluar.
- Plazo: noviembre de 2026 a febrero de 2027.

---

## 1. Tipo de investigación (redactar en el capítulo de Metodología)

- Enfoque cuantitativo; diseño no experimental, transversal; alcance descriptivo-correlacional.
- Justifica cada término con referencias metodológicas reconocidas (p. ej., Hernández-Sampieri y Mendoza), verificadas.

## 2. Instrumento: cuestionario

- **Preguntas de hechos** (sí / no / no recuerdo, selección múltiple): qué datos les pidieron (identificación, contacto, socioeconómicos, salud, discapacidad, biometría, fotografía, familiares, plataformas virtuales), si se les pidió consentimiento y cómo, si les informaron la finalidad, el responsable, el tiempo de conservación y si sus datos se comparten con terceros.
- **Escalas Likert de 5 puntos** (de 1 = Totalmente en desacuerdo a 5 = Totalmente de acuerdo), agrupadas en dimensiones, con al menos 4 o 5 ítems cada una: información recibida, consentimiento, conocimiento de derechos (acceso, rectificación, eliminación, oposición, portabilidad; LOPDP y SPDP) y confianza / percepción de seguridad.
- Incluye 1 o 2 ítems inversos por dimensión y documenta su recodificación.
- Datos demográficos no identificativos: tipo de universidad (pública/privada), área, semestre, rango de edad. Pregunta filtro de edad ≥ 18.
- Tabla de operacionalización: variable → dimensión → indicador → ítem → escala → artículo de la LOPDP.
- Entregable: `encuesta/cuestionario.md`, listo para Microsoft Forms o Google Forms.

## 3. Validez y confiabilidad

- **Validez de contenido:** juicio de 3 a 5 expertos (protección de datos, seguridad, metodología) que califican la pertinencia, claridad y coherencia de cada ítem. Calcula la **V de Aiken** por ítem; se conserva con V ≥ 0,80 y se corrige o elimina por debajo. Entregables: `encuesta/formato_juicio_expertos.md` y una plantilla de cálculo.
- **Prueba piloto:** unos 30 estudiantes; registra los ajustes realizados.
- **Confiabilidad:** **alfa de Cronbach** por dimensión Likert (≥ 0,70 aceptable, ≥ 0,80 bueno) y **omega de McDonald**. Para las preguntas dicotómicas, **KR-20**. Aclara en el texto por qué el alfa no se aplica a los ítems de sí/no.
- Los resultados reales quedan como `[PENDIENTE]` hasta que yo cargue los datos.

## 4. Población y muestra

- Población: matrícula oficial de estudiantes universitarios (SENESCYT/SIIES), con fuente y fecha de corte. Si conviene, limita a Quito/Pichincha y justifícalo.
- Fórmula de población finita: 95 % de confianza (Z = 1,96), 5 % de error, p = q = 0,5. Muestra el cálculo completo.
- Muestreo no probabilístico por conveniencia / bola de nieve: decláralo como limitación y no generalices fuera de la muestra.

## 5. Hipótesis

Formula hipótesis de trabajo y nulas, por ejemplo:
- H1: existe diferencia significativa en la información recibida sobre el tratamiento de datos entre estudiantes de universidades públicas y privadas.
- H2: existe relación entre el conocimiento de derechos y la confianza en la protección de datos de la universidad.
- H3: la proporción de estudiantes a quienes se les pidió consentimiento difiere según el tipo de universidad.
Nivel de significancia α = 0,05.

## 6. Plan de análisis

| Propósito | Prueba |
|---|---|
| Datos solicitados, consentimiento, información recibida | Frecuencias y porcentajes |
| Dimensiones Likert | Mediana, rango intercuartílico (datos ordinales); medias solo como complemento |
| Normalidad | Kolmogorov-Smirnov (n > 50) |
| Pública vs. privada (sí/no) | Chi-cuadrado (Fisher si las frecuencias esperadas son < 5); tamaño del efecto V de Cramér |
| Pública vs. privada (Likert) | U de Mann-Whitney; tamaño del efecto r |
| Relación entre dimensiones | Correlación de Spearman |
| Información pública de las universidades | Índice de cumplimiento (% de indicadores cumplidos por universidad) |

## 7. Herramientas (declararlas en la metodología)

- Recolección: Microsoft Forms o Google Forms, configurado para no recoger correo ni datos identificativos.
- Análisis principal: Python (pandas, scipy, pingouin), reproducible.
- Verificación cruzada: jamovi o JASP (gratuitos).
- Registro documental: `analisis_documental.xlsx`.

## 8. Scripts (carpeta `analisis/`)

- `requirements.txt` (pandas, numpy, scipy, pingouin, matplotlib, openpyxl).
- `limpieza.py`: lee el Excel exportado del formulario (`datos/respuestas.xlsx`), elimina a quienes no consintieron o son menores de 18, recodifica Likert e ítems inversos y elimina cualquier columna identificativa.
- `validacion.py`: V de Aiken a partir de `datos/expertos.xlsx`; alfa, omega y KR-20 por dimensión.
- `descriptivos.py`, `inferencial.py`: todas las pruebas de la sección 6 con tamaños de efecto.
- `graficos.py`: figuras en PDF para LaTeX.
- `exportar_latex.py`: tablas en `.tex` para incluir con `\input{}`.
- `datos/ejemplo_simulado.xlsx` con datos **simulados solo para probar los scripts**, marcados claramente como SIMULADOS. Nunca se usan en el documento.
- `analisis/README.md`: cómo ejecutar todo con un solo comando.

## 9. Integridad y ética

- Prohibido inventar respuestas, coeficientes o resultados. Todo resultado del documento sale de los scripts con datos reales; mientras tanto, `[PENDIENTE]`.
- Mantén el apartado de consideraciones éticas: anonimato, consentimiento informado, mayores de 18, minimización, almacenamiento seguro y plazo de eliminación de las respuestas.

## 10. Cierre

1. Compila con latexmk sin errores.
2. Actualiza CAMBIOS.md, PENDIENTES.md (expertos por contactar, piloto, recolección, aprobación de la tutora) y FUENTES.md.
3. Actualiza el cronograma nov 2026 – feb 2027 con: juicio de expertos → piloto → recolección → análisis → redacción → revisión.
4. Actualiza CLAUDE.md / CLAUDEs.md (y la copia de la carpeta superior) con la metodología, las herramientas y la carpeta `analisis/`.
5. Commit y resumen en consola de lo que quedó listo y lo que depende de mí.
