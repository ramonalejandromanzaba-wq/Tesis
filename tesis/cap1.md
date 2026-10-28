<!-- Generado automáticamente desde Capítulos/01_Introducción.tex con scripts/tex2md_cap1.js.
     El .tex es la fuente vigente; para actualizar este borrador, compilar main.tex y volver a ejecutar el script. -->

# CAPÍTULO I. INTRODUCCIÓN

El presente trabajo de integración curricular aborda el tema *Metodología para el diagnóstico y gestión de riesgos en el tratamiento de datos personales*, circunscrito a los datos personales de estudiantes y docentes que tratan las instituciones de educación superior (IES) ecuatorianas en el marco de la Ley Orgánica de Protección de Datos Personales (LOPDP).

La tesis que sostiene este trabajo es que las IES ecuatorianas no pueden cumplir la LOPDP con políticas escritas o con controles de seguridad aislados, sino que necesitan una metodología sistemática que diagnostique su situación real, valore los riesgos desde la perspectiva de los titulares y documente las decisiones de tratamiento conforme a las etapas definidas por la Superintendencia de Protección de Datos Personales (SPDP). Para sostener esta afirmación, el capítulo expone primero la evidencia sobre la exposición del sector, contrasta después las soluciones existentes en la literatura y concluye con el problema, los objetivos y los fundamentos que orientan la propuesta, que se aplica al proceso de admisión y matrícula de la Universidad Tecnológica Indoamérica.

## 1.1 Contextualización

### 1.1.1 Contexto macro: la exposición del sector educativo a nivel mundial

La educación superior se ha consolidado como uno de los sectores con mayor exposición a incidentes que comprometen datos personales. La edición 2024 del estudio *The State of Ransomware in Education*, basada en una encuesta a 5 000 responsables de tecnología de 14 países, de los cuales 600 pertenecían a organizaciones educativas, reportó que el 66 % de las IES había sufrido un ataque de *ransomware* en el último año, que el 77 % de esos ataques terminó con el cifrado de datos y que el costo medio de recuperación en el subsector alcanzó 4,02 millones de dólares [1]. Estas cifras ubican a las universidades por encima del promedio intersectorial y muestran que el problema no se limita a la disponibilidad de los sistemas, sino que afecta de forma directa la confidencialidad de los registros de estudiantes y docentes.

La literatura académica coincide en ese diagnóstico. La revisión de Ulven y Wangen [2] sintetizó los activos críticos, eventos de amenaza y vulnerabilidades frecuentes en la educación superior, concluyó en nueve riesgos estratégicos de ciberseguridad para el sector y advirtió que ya se han producido brechas de datos graves que probablemente se repetirán sin una gestión de riesgos adecuada; los autores señalan, además, que la investigación empírica sobre riesgos en este sector es escasa y presenta vacíos importantes. En la misma línea, Li et al. [3] partieron de que los entornos digitales universitarios, complejos y dinámicos, son altamente vulnerables a brechas de datos y, con una muestra de universidades chinas, encontraron que la divulgación pública de vulnerabilidades incrementa la frecuencia de brechas, mientras que la adopción de servicios en la nube la reduce; es decir, la exposición depende de decisiones de gestión sobre vulnerabilidades y plataformas, lo que refuerza la necesidad de un enfoque de gestión de riesgos y no solo de controles técnicos puntuales.

El crecimiento de las plataformas digitales de aprendizaje amplía la superficie de tratamiento. Liu y Khalil [4], en una revisión sistemática sobre analítica del aprendizaje, identificaron ocho problemas interrelacionados de privacidad y protección de datos a lo largo del ciclo de vida de esos datos, desde la recolección hasta la explotación de resultados. Por su parte, Fernandes et al. [5] estudiaron la implementación del Reglamento General de Protección de Datos (RGPD) en universidades públicas portuguesas y determinaron dieciséis factores críticos de éxito, entre los que destacan el compromiso de la alta dirección y la cultura organizacional de protección de datos; su hallazgo sugiere que, incluso en jurisdicciones con larga tradición normativa, la adecuación de las IES depende más de la gestión que de la tecnología disponible.

### 1.1.2 Contexto meso: América Latina y Ecuador

En América Latina, los incidentes en universidades han pasado de ser casos aislados a eventos con consecuencias públicas visibles. En marzo de 2023, la Universidad Nacional de Colombia sufrió un ataque de *ransomware* que cifró parte de su información y obligó a aislar sus sistemas financiero, académico y de talento humano mientras se restablecían los servicios [6]. En octubre de 2024, la Universidad Técnica Federico Santa María, en Chile, registró un incidente atribuido al grupo RansomHub, tras el cual se publicaron en la *dark web* alrededor de 14 GB de información que incluía listados de estudiantes con su número de identificación, carrera y año de ingreso, así como datos de deudores del fondo de crédito estudiantil [7]. En el ámbito académico, Zappelini et al. [8] mostraron que, en Brasil, el uso de medios digitales para la docencia y la evaluación remota en IES plantea riesgos específicos cuando los titulares son adolescentes, situación análoga al régimen de categorías especiales que establece la normativa ecuatoriana.

Ecuador cuenta con un antecedente nacional que evidenció la magnitud del problema antes de la existencia de una ley específica. En septiembre de 2019 se reportó la exposición de una base de datos de una empresa privada de mercadeo y analítica que contenía información de alrededor de 20 millones de personas, incluidos cerca de 6,7 millones de niños, con campos como nombres, fecha de nacimiento, domicilio, teléfonos y nivel de educación [9]. Ese caso aceleró el debate legislativo que culminó con la expedición de la LOPDP, publicada en el Quinto Suplemento del Registro Oficial N.º 459 el 26 de mayo de 2021 [10]. Su reglamento general fue expedido mediante el Decreto Ejecutivo N.º 904 y publicado en el Tercer Suplemento del Registro Oficial N.º 435 el 13 de noviembre de 2023 [11].

La LOPDP establece obligaciones que inciden directamente en la gestión de riesgos. El artículo 37 exige al responsable identificar la probabilidad de riesgos e implementar un proceso de verificación, evaluación y valoración continua de las medidas de seguridad; el artículo 40 obliga a utilizar una metodología de análisis de riesgos, amenazas y vulnerabilidades que considere las particularidades del tratamiento, de las partes involucradas y las categorías y volumen de datos; y el artículo 42 vuelve obligatoria la evaluación de impacto cuando exista tratamiento a gran escala de categorías especiales de datos [10, arts. 37, 40 y 42]. A ello se suma la obligación de notificar las vulneraciones de seguridad, cuyos plazos se verificaron en el texto oficial porque suelen confundirse. El responsable debe notificar a la autoridad tan pronto sea posible y, a más tardar, en el término de cinco días contados desde que tuvo constancia de la vulneración; el encargado debe avisar al responsable en el término de dos días [10, art. 43], y el titular debe ser notificado sin dilación, dentro del término de tres días desde que se conoció el riesgo [10, art. 46]. La Ley Orgánica para el Fortalecimiento de la Ciberseguridad, publicada el 22 de mayo de 2026, sustituyó el primer inciso del artículo 43 para que la notificación se dirija a la autoridad de protección de datos, al organismo de regulación y control competente y, con fines informativos y de coordinación técnica, al CSIRT correspondiente, sin modificar el término de cinco días [12, art. 14]. El plazo de 72 horas, en cambio, no pertenece a la LOPDP: lo introdujo esa misma ley en el artículo 20-G de la Ley Orgánica de Transformación Digital y Audiovisual para los incidentes de ciberseguridad, se cuenta desde la detección del incidente y obliga a las entidades públicas y a los operadores de infraestructura crítica digital [12]. La Disposición Transitoria Primera difirió por dos años la vigencia del régimen sancionatorio, con lo que el periodo de adecuación concluyó en mayo de 2023 [10].

La Superintendencia de Protección de Datos Personales (SPDP) comenzó a emitir normativa técnica entre 2025 y 2026. Mediante la Resolución N.º SPDP-SPD-2025-0003-R, del 29 de abril de 2025, publicada en el Cuarto Suplemento del Registro Oficial N.º 41 el 19 de mayo de 2025, expidió la *Guía de Gestión de Riesgos y Evaluación de Impacto del Tratamiento de Datos Personales*, cuyo capítulo I es de cumplimiento obligatorio y cuyo capítulo II ofrece metodologías referenciales [13], [14]; posteriormente, mediante la Resolución N.º SPDP-SPD-2026-0012-R, publicada en el Suplemento del Registro Oficial N.º 254 el 30 de marzo de 2026, expidió la segunda versión (V.2) de la guía [15]. Asimismo, la Resolución N.º SPDP-SPD-2026-0005-R, publicada en el Suplemento del Registro Oficial N.º 231 el 25 de febrero de 2026, definió el Modelo Técnico de Gran Escala y estableció que constituyen tratamiento a gran escala, de forma directa, los tratamientos relativos a la salud y a otras categorías especiales, así como el tratamiento sistemático de datos de niñas, niños y adolescentes en entornos educativos; esa calificación vuelve obligatorias la evaluación de impacto previa y la designación de un delegado de protección de datos [16, arts. 12 y 14].

La autoridad ya ha ejercido su potestad sancionadora. El 1 de diciembre de 2025 se dieron a conocer las primeras sanciones por infracciones graves de la LOPDP, impuestas a la Liga Profesional de Fútbol del Ecuador y a la Federación Ecuatoriana de Fútbol por un total cercano a 454 500 dólares, con fundamento en el artículo 68 de la ley y por no implementar medidas administrativas, técnicas y físicas suficientes para garantizar un tratamiento adecuado [17], [18]. Aunque ninguno de esos casos corresponde a una IES, demuestran que las obligaciones de la ley son exigibles. Debe subrayarse, además, que el mismo artículo 68 tipifica como infracción grave del responsable, en su numeral 4, no utilizar metodologías de análisis y gestión de riesgos adaptadas a la naturaleza de los datos personales, a las particularidades del tratamiento y a las partes involucradas [10, art. 68], de modo que la ausencia de una metodología constituye, por sí misma, una conducta sancionable. La aplicación de este régimen es reciente: hasta septiembre de 2025 la SPDP había recibido 191 denuncias sin haber impuesto sanción alguna, porque la ley prevé que ante una infracción grave se ordenen primero medidas correctivas y solo se sancione si estas no se cumplen [19]. En las fuentes públicas consultadas no se identificó, a la fecha de redacción, un procedimiento sancionador contra una IES, por lo que para estas instituciones el riesgo jurídico se mantiene latente y aún no se ha materializado.

### 1.1.3 El sector educativo ecuatoriano en cifras

La magnitud del problema se aprecia mejor con cifras. Todos los valores de esta sección se tomaron de fuentes oficiales o, cuando estas no publican el dato, de medios que citan expresamente a la fuente oficial, y cada uno se acompaña de su fecha de corte; los datos que no se hallaron publicados se señalan como pendientes en lugar de estimarse. La Tabla 1 reúne el universo de instituciones educativas que, como se argumenta enseguida, son responsables del tratamiento de datos personales en los términos de la LOPDP.

**Tabla 1**
*Instituciones del sistema educativo ecuatoriano que tratan datos personales.*

| **Nivel** | **Cifra** | **Fecha de corte** | **Fuente** |
| --- | --- | --- | --- |
| Educación inicial, básica y bachillerato (todos los sostenimientos) | 16 161 instituciones; 4 370 420 estudiantes; 209 471 docentes | Ciclo 2024–2025 | Ministerio de Educación, citado en [20] |
| Ídem, inicio del ciclo siguiente | 15 400 instituciones | Ciclo 2025–2026 (septiembre de 2025) | Ministerio de Educación, citado en [20] |
| Ídem, por sostenimiento | 12 389 fiscales; 617 fiscomisionales; 112 municipales; 3 022 particulares (total: 16 140) | Estadística Educativa, vol. 5 (octubre de 2024) | [21] |
| Centros de desarrollo infantil (CDI) en convenio con GAD y organizaciones sociales | 1 861 centros | Levantamiento de 2024, informe de noviembre de 2025 | [22] |
| CDI de atención directa del MIES | No se halló una cifra publicada; el informe del CNII los excluyó de su levantamiento | Consulta del 27 de octubre de 2026 | [22] |
| Niñas y niños menores de 3 años atendidos por el MIES | Cerca de 293 000 (cobertura cercana al 22 %) | Agenda Nacional para la Igualdad Intergeneracional 2021–2025 | [22] |
| Universidades y escuelas politécnicas | 64 (36 públicas, 20 particulares autofinanciadas, 8 particulares cofinanciadas) | Consulta del 27 de octubre de 2026 (el portal no indica fecha de corte) | [23] |
| Institutos técnicos, tecnológicos, pedagógicos, de artes y conservatorios superiores | 216 (62 públicos, 154 particulares) | Consulta del 27 de octubre de 2026 | [23] |

*Elaborado por:* Ramón Alejandro Manzaba Castro. *Fuente:* Elaboración propia a partir de [20], [22], [23].

Todas estas instituciones están obligadas a proteger los datos personales que tratan, y no por analogía, sino por el texto de la ley. La LOPDP se aplica al tratamiento de datos personales contenidos en cualquier tipo de soporte, automatizado o no [10, art. 2], y define como responsable a la persona natural o jurídica, pública o privada, que decide sobre la finalidad y el tratamiento [10, art. 4]; toda escuela, colegio, centro infantil, instituto o universidad que matricula estudiantes, registra calificaciones o contrata docentes cumple esa definición. La ley añade deberes específicos para el sector: los datos de niñas, niños y adolescentes son una categoría especial [10, art. 25]; las entidades educativas deben proveer información y capacitación sobre el tratamiento de esos datos a sus titulares y representantes [10, art. 24], y el sistema educativo, incluida la educación superior, debe garantizar la educación digital de estudiantes y docentes [10, art. 23]. Las instituciones fiscales y las universidades públicas, por pertenecer al sector público, deben designar un delegado de protección de datos [10, art. 48, num. 1]. A ello se suma la Resolución SPDP-SPD-2026-0005-R, que califica directamente como tratamiento a gran escala el tratamiento sistemático de datos de niñas, niños y adolescentes en entornos educativos, con la consiguiente obligación de realizar una evaluación de impacto previa y de designar un delegado [16, arts. 12 y 14]. Por último, la reforma de 2026 dispuso que escuelas, colegios y universidades incorporen progresivamente contenidos de protección de datos personales en su oferta educativa [12, art. 8].

Frente a ese universo de obligados, las cifras disponibles sobre la capacidad de cumplimiento son escasas. En abril de 2025 se informaba que más de 1 150 delegados de protección de datos estaban registrados ante la SPDP, sumando todos los sectores de la economía [24]. Aun si todos ellos trabajaran en educación, cubrirían como máximo el 7,0 % de las 16 441 instituciones educativas y de educación superior de la Tabla 1 (1 150 / 16 441), sin contar los CDI. La cifra es anterior al plazo de registro de delegados del sector privado fijado por la normativa de la SPDP [25], y no se halló una cifra oficial posterior publicada al 27 de octubre de 2026. El informe de rendición de cuentas de 2025 de la SPDP reporta, entre otros datos, 49 trámites de solicitudes de titulares y 22 convenios suscritos de 48 gestionados [26]. En cuanto a la actividad de control, la SPDP había recibido 85 denuncias en abril de 2025 [24] y 191 en septiembre de 2025 [19], e impuso sus dos primeras sanciones por infracciones graves en diciembre de 2025 [17]. Aunque la ley ordena a la autoridad llevar un registro estadístico de vulneraciones [10, art. 76, num. 14], no se halló, al 27 de octubre de 2026, una estadística pública de vulneraciones notificadas por el sector educativo. Tampoco existe un informe oficial que indique qué porcentaje de universidades ha implementado la LOPDP: el estudio nacional más reciente describe una adopción desigual de políticas, pero no la cuantifica [27], y en las publicaciones de la SPDP, del CES y del CACES consultadas al 27 de octubre de 2026 no se encontró ese porcentaje.

En síntesis, las cifras dibujan una brecha medible: más de 16 000 instituciones educativas obligadas por la ley —todas las de educación inicial, básica y bachillerato tratan de forma sistemática datos de niñas, niños y adolescentes y se sitúan, por tanto, en el supuesto de gran escala—, frente a poco más de un millar de delegados registrados en todo el país, unas primeras sanciones que solo llegaron en diciembre de 2025 y ninguna estadística oficial sobre el cumplimiento del sector. Esa distancia entre una obligación universal y una capacidad escasa y no medida es la que justifica una metodología específica, aplicable con los recursos de una institución educativa.

### 1.1.4 Contexto micro: las IES ecuatorianas y la unidad de análisis

En el sistema de educación superior ecuatoriano, la evidencia disponible indica que la adecuación a la LOPDP es heterogénea. Álvarez-Carrión y Hernández-Sotomayor [28] analizaron la protección de datos en plataformas educativas digitales y concluyeron que, aunque la ley ofrece un marco sólido, su implementación enfrenta brechas de infraestructura y de capacitación en ciberseguridad; al revisar vulneraciones documentadas en universidades del país, identificaron los fallos técnicos y el error humano como causas principales. Piray Rodríguez et al. [27], mediante revisión documental y análisis normativo, encontraron diferencias marcadas entre instituciones en la adopción de políticas internas de protección de datos y observaron que solo un número limitado de universidades las aplica de manera destacada. A nivel de gestión de riesgos, López-Vasco et al. [29] documentaron la aplicación de ISO/IEC 27001 en institutos tecnológicos de educación superior del Ecuador, lo que constituye un antecedente de diagnóstico y planificación de controles en el sector, aunque centrado en la seguridad de la información y no en los derechos de los titulares.

La unidad de análisis de este trabajo es la Universidad Tecnológica Indoamérica (UTI), creada mediante la Ley N.º 112, publicada en el Registro Oficial N.º 373 del 31 de julio de 1998, como entidad de derecho privado con domicilio principal en Ambato y cuyo patrimonio incluye los recursos provenientes de matrículas, pensiones y aranceles [30]. La universidad cuenta además con una sede en Quito, en la que se desarrolla este trabajo. Como toda IES, la UTI trata datos de estudiantes, aspirantes, graduados, docentes y personal administrativo en procesos como admisión y matrícula, registro de calificaciones, becas, bienestar estudiantil, aula virtual y titulación, y varios de esos procesos involucran categorías especiales en los términos del artículo 25 de la LOPDP, como datos de salud, de discapacidad o de adolescentes que ingresan a la universidad [10, art. 25]. El caso de estudio es el **proceso de admisión y matrícula de la sede Quito**, elegido porque concentra en pocas semanas la recolección masiva de datos de personas que aún no tienen vínculo con la institución. La información institucional se obtendrá con autorización formal de la universidad y se tratará de forma anonimizada o agregada, sin datos personales reales ni identificación de funcionarios.

En síntesis, la evidencia de los tres niveles converge en una misma conclusión: la exposición del sector es alta y creciente, la obligación jurídica de gestionar el riesgo es exigible desde 2023 y la normativa técnica que la concreta es reciente, mientras que la adecuación de las universidades ecuatorianas es todavía desigual. Esa combinación convierte la gestión de riesgos sobre datos personales en una necesidad inmediata para instituciones como la UTI y no en una mejora opcional.

## 1.2 Estado del Arte

La revisión de antecedentes se realizó en bases de datos académicas (IEEE Xplore, ScienceDirect, SpringerLink, Scopus, SciELO y Google Académico) y en los sitios oficiales de autoridades de protección de datos y de organismos de normalización. Se priorizaron publicaciones de 2019 en adelante, sin excluir los trabajos seminales, y solo se incluyeron fuentes con DOI o con publicación oficial verificable. Los criterios de inclusión fueron tres: que el trabajo propusiera o evaluara un método de gestión de riesgos o de evaluación de impacto sobre datos personales, que abordara el tratamiento de datos en instituciones de educación superior, o que aportara evidencia normativa o empírica del contexto latinoamericano y ecuatoriano. Los trabajos seleccionados se organizaron en cinco ejes: (1) marcos de referencia para la evaluación de impacto y el riesgo de privacidad; (2) métodos de estimación del riesgo; (3) gestión de riesgos de seguridad de la información en el sector público y educativo; (4) protección de datos personales en IES, y (5) antecedentes latinoamericanos y ecuatorianos. Las Tablas 2 y 3 resumen los trabajos académicos analizados y la Tabla 4 compara los principales marcos metodológicos con los requisitos de este proyecto.

**Tabla 2**
*Trabajos relacionados con los marcos, la estimación y la gestión de riesgos (ejes 1 a 3).*

| **Eje** | **Trabajo** | **Enfoque y aporte** | **Limitación respecto de este proyecto** |
| --- | --- | --- | --- |
| 1 | Deng et al. [31] | Marco LINDDUN de modelado de amenazas a la privacidad con siete categorías y árboles de amenaza. | Orientado al diseño de software; no estima probabilidad ni impacto. |
| 1 | Bieker et al. [32] | Proceso adaptable de EIPD derivado de los requisitos del RGPD. | Marco europeo; sin aplicación sectorial. |
| 1 | Vemou y Karyda [33] | Comparación de métodos PIA de autoridades, normas y academia; criterios de buenas prácticas. | Criterios generales, sin aplicación a un caso. |
| 1 | Wairimu et al. [34] | Revisión sistemática de metodologías PIA y PRA y de la forma en que se han evaluado. | No se centra en un sector ni en la normativa ecuatoriana. |
| 1 | Iwaya et al. [35] | *Scoping review* sobre la aplicación práctica de las PIA/EIPD, sus beneficios y dificultades. | Evidencia mayoritariamente europea; no aborda IES. |
| 1 | Wairimu et al. [36] | Percepción de profesionales sobre el uso de categorías de daño a la privacidad en la evaluación de riesgos. | No propone escalas de impacto aplicables a un sector. |
| 2 | Wang et al. [37] | Implementación del modelo FAIR mediante redes bayesianas para estimar frecuencia y magnitud de pérdidas. | Perspectiva financiera del responsable; no considera el daño a titulares. |
| 3 | Patiño et al. [38] | Metodología de gestión de riesgos TIC basada en ISO/IEC 27005 para entidades gubernamentales ecuatorianas. | Orientada a activos de información, no a derechos de titulares. |
| 3 | Ulven y Wangen [2] | Revisión sistemática de riesgos de ciberseguridad en educación superior; nueve riesgos estratégicos. | Identifica riesgos, pero no define un proceso de gestión. |
| 3 | Li et al. [3] | Factores que explican las brechas de datos en universidades chinas. | Análisis explicativo; no ofrece una metodología. |
| 3 | López-Vasco et al. [29] | Diagnóstico y plan de controles ISO/IEC 27001 en institutos tecnológicos de Ecuador. | Enfoque de seguridad de la información; no integra la LOPDP. |

*Elaborado por:* Ramón Alejandro Manzaba Castro. *Fuente:* Elaboración propia a partir de las fuentes citadas.

**Tabla 3**
*Trabajos relacionados con la protección de datos personales en IES y antecedentes regionales (ejes 4 y 5).*

| **Eje** | **Trabajo** | **Enfoque y aporte** | **Limitación respecto de este proyecto** |
| --- | --- | --- | --- |
| 4 | Gursoy et al. [39] | Técnicas de anonimización y privacidad diferencial para analítica del aprendizaje. | Controles técnicos aislados de un proceso de riesgos. |
| 4 | Habbabeh et al. [40] | Instrumento de 44 controles para medir la alineación de una IES con el RGPD. | Mide cumplimiento, no riesgo; no distingue riesgo inherente y residual. |
| 4 | Vanezi et al. [41] | Cumplimiento del RGPD desde el diseño en una plataforma de *e-learning*. | Limitado a una plataforma; no abarca la institución. |
| 4 | Tsai et al. [42] | Expectativas y conductas de privacidad de estudiantes frente a la analítica del aprendizaje. | Estudio de percepción; no evalúa riesgos. |
| 4 | Fernandes et al. [5] | Factores críticos de éxito para implementar el RGPD en universidades públicas. | Marco europeo; no propone una metodología de riesgos. |
| 4 | Liu y Khalil [4] | Revisión sistemática de problemas de privacidad en el ciclo de vida de la analítica del aprendizaje. | Catálogo de problemas, sin valoración del riesgo. |
| 4 | Maguraushe et al. [43] | Encuesta diagnóstica de conciencia, expectativas y confianza de estudiantes sobre privacidad. | Diagnóstico de percepción; no cubre procesos ni controles. |
| 5 | Guerrero Argote [44] | Adopción de *e-proctoring* y riesgos para la privacidad en universidades de Argentina, Chile y Perú. | Estudio exploratorio; análisis jurídico preliminar. |
| 5 | Zappelini et al. [8] | Datos de adolescentes en IES brasileñas bajo la LGPD; docencia y evaluación remota. | Análisis jurídico; sin método de riesgos. |
| 5 | Álvarez-Carrión y Hernández-Sotomayor [28] | Protección de datos en plataformas educativas de IES ecuatorianas. | Diagnóstico normativo; no define un proceso de gestión de riesgos. |
| 5 | Piray Rodríguez et al. [27] | Garantías de privacidad y políticas internas en IES ecuatorianas. | Revisión documental; sin aplicación de un método de riesgos. |

*Elaborado por:* Ramón Alejandro Manzaba Castro. *Fuente:* Elaboración propia a partir de las fuentes citadas.

### 1.2.1 Marcos de referencia para la evaluación de impacto y el riesgo de privacidad

Los marcos normativos y de autoridades de control constituyen el primer referente para cualquier metodología. La norma ISO/IEC 29134:2023 ofrece directrices para el proceso de evaluación de impacto en la privacidad y para la estructura y el contenido del informe resultante, aplicables a organizaciones de cualquier tipo y tamaño [45]. En el ámbito iberoamericano, la Agencia Española de Protección de Datos (AEPD) publicó en 2021 una guía que unifica la gestión del riesgo y la evaluación de impacto, aplicable a cualquier tratamiento con independencia de su nivel de riesgo y que, para los tratamientos de alto riesgo, orienta la realización de la EIPD y la eventual consulta previa a la autoridad [46]. El NIST Privacy Framework, por su parte, es una herramienta voluntaria basada en riesgos y resultados, organizada en un núcleo, perfiles y niveles de implementación, que no está ligada a un sector ni a una jurisdicción concretos [47]. Para la valoración del impacto de una vulneración, ENISA propuso una metodología de severidad que combina el contexto del tratamiento, la facilidad de identificación de los titulares y las circunstancias de la vulneración [48], criterios que resultan útiles para graduar el impacto sobre los titulares.

Desde la academia, LINDDUN aporta un marco sistemático para identificar amenazas a la privacidad a partir de un modelo de flujos de información del sistema, con siete categorías —vinculabilidad, identificabilidad, no repudio, detectabilidad, divulgación de información, desconocimiento e incumplimiento— y catálogos de árboles de amenaza asociados a tecnologías de mejora de la privacidad [31]. Bieker et al. [32] analizaron las disposiciones del RGPD sobre la EIPD y propusieron un proceso adaptable que integra los requisitos ya establecidos con los nuevos de la regulación. Las revisiones posteriores matizan la madurez de este campo: Wairimu et al. [34] muestran que existe una amplia variedad de metodologías PIA y PRA, pero que su validación empírica es limitada y heterogénea, lo que dificulta elegir una de ellas sin adaptación; Iwaya et al. [35], tras sintetizar 45 estudios sobre evaluaciones de impacto aplicadas en organizaciones reales, constatan que aún falta evidencia empírica sobre su adopción y efectividad; y Vemou y Karyda [33] proponen criterios para valorar la calidad de un método PIA, útiles como referencia para evaluar la metodología que este trabajo diseñe. Finalmente, Wairimu et al. [36] concluyen que las categorías de daño a la privacidad son un complemento crítico de las metodologías PIA, EIPD y PRA, aunque recomiendan priorizarlas para distribuir adecuadamente el tiempo y los recursos de la evaluación; este hallazgo respalda la definición de escalas de impacto centradas en el titular.

### 1.2.2 Métodos de estimación del riesgo

La forma de estimar la probabilidad y el impacto es uno de los puntos más débiles de las metodologías de uso corriente. La mayoría de marcos emplea escalas ordinales y matrices de calor, mientras que los enfoques cuantitativos, como el modelo FAIR, estiman la frecuencia y la magnitud de las pérdidas; Wang et al. [37] implementaron y ampliaron FAIR mediante redes bayesianas, lo que permite incorporar dependencias causales y actualizar las estimaciones con nueva evidencia. La segunda versión de la guía de la SPDP recoge esta discusión y fija reglas que condicionan el diseño de la metodología: toda estimación de probabilidad o impacto debe acompañarse de su justificación (*rationale*); una escala de 1 a 3 o de 1 a 5 no constituye un análisis cuantitativo, sino un conjunto de etiquetas; las matrices de calor sirven para representar el riesgo, no para calibrarlo; la probabilidad debe referirse a un lapso definido, y la confidencialidad, la integridad y la disponibilidad deben modelarse por separado [15]. Cuando no se dispone de datos históricos suficientes, la guía admite la opinión de expertos calibrada, por ejemplo mediante el método Delphi, y su validación con métricas como el *Brier score* [15]. Ninguno de los trabajos aplicados al sector educativo revisados incorpora estas exigencias.

### 1.2.3 Gestión de riesgos de seguridad de la información en el sector público y educativo

Patiño et al. [38] constituyen el antecedente ecuatoriano más directo de adaptación de ISO/IEC 27005 a un contexto institucional, mediante una guía por pasos para entidades del sector público. López-Vasco et al. [29] trasladan ese tipo de enfoque a la educación superior tecnológica, con un diagnóstico y un plan de controles basados en ISO/IEC 27001. En el plano internacional, la revisión de Ulven y Wangen [2] sintetiza los activos críticos, las amenazas y las vulnerabilidades más frecuentes en universidades y concluye en nueve riesgos estratégicos, mientras que Li et al. [3] identifican factores organizacionales que explican la ocurrencia de brechas de datos en universidades, como la divulgación de vulnerabilidades y el uso de servicios en la nube. Estos trabajos proporcionan catálogos de amenazas y evidencia útil para estimar la probabilidad, pero valoran el riesgo desde la perspectiva de los activos de la organización y no desde el daño a los titulares, que es el eje de la LOPDP y de la guía de la SPDP.

### 1.2.4 Protección de datos personales en instituciones de educación superior

Un conjunto de estudios aborda la protección de datos en las IES desde el cumplimiento normativo. Habbabeh et al. [40] constataron que la literatura ofrecía escasa orientación para que las universidades verificaran su cumplimiento del RGPD y, siguiendo los lineamientos de la ciencia del diseño, construyeron un instrumento de 44 controles cuya puntuación total indica el grado de alineación de la institución con el reglamento y que puede emplearse como herramienta de gestión para el seguimiento de medidas. Fernandes et al. [5] identificaron dieciséis factores críticos de éxito para implementar el RGPD en universidades públicas portuguesas, entre ellos el compromiso de la alta dirección y la cultura de protección de datos. Vanezi et al. [41] documentaron la incorporación de requisitos del RGPD desde el diseño en una plataforma de aprendizaje en línea.

Otro grupo de trabajos se concentra en los tratamientos derivados de la analítica del aprendizaje. Gursoy et al. [39] examinaron técnicas de anonimización y de privacidad diferencial aplicadas a datos educativos; Tsai et al. [42] analizaron la brecha entre las expectativas de privacidad de los estudiantes y su conducta efectiva, con énfasis en la transparencia y la confianza; y Liu y Khalil [4] identificaron ocho problemas interrelacionados de privacidad a lo largo del ciclo de vida de esos datos. Desde la perspectiva de los titulares, Maguraushe et al. [43] aplicaron una encuesta diagnóstica sobre conciencia, expectativas y confianza de los estudiantes en materia de privacidad en el sector de educación superior de un país en desarrollo, instrumento que puede adaptarse a la fase de diagnóstico. En conjunto, estos estudios aportan controles, factores de éxito e instrumentos de medición, pero miden el cumplimiento o la percepción y no el riesgo, por lo que no distinguen entre riesgo inherente y residual ni priorizan el tratamiento.

### 1.2.5 Antecedentes latinoamericanos y ecuatorianos

En América Latina, Guerrero Argote [44] mapeó 267 universidades de Argentina, Chile y Perú y encontró que 46 utilizaban *software* de supervisión remota de exámenes (*e-proctoring*), con mayor adopción en las universidades privadas; ocho de los nueve productos identificados incorporaban reconocimiento facial y trataban imágenes, voz, rasgos faciales y datos de navegación, y el autor reportó un bajo cumplimiento de las obligaciones de registro de bases de datos. Zappelini et al. [8] mostraron que, en Brasil, el uso de medios digitales para la docencia y la evaluación remota plantea riesgos específicos cuando los titulares son adolescentes. En Colombia, la Superintendencia de Industria y Comercio presentó en 2026 una guía sobre el tratamiento de datos personales en el contexto universitario, que recuerda que las IES son responsables del tratamiento de los datos de su comunidad, exige separar las finalidades necesarias para el servicio educativo de las opcionales y recomienda designar un oficial de protección de datos y reforzar la seguridad de la información sensible [49]. Estos antecedentes confirman que los riesgos identificados en Europa se reproducen en la región, con el agravante de marcos de control aún en consolidación.

En Ecuador, Álvarez-Carrión y Hernández-Sotomayor [28] concluyeron que la LOPDP ofrece un marco sólido, pero que su implementación en plataformas educativas enfrenta brechas de infraestructura y de capacitación, con fallos técnicos y error humano como causas principales de las vulneraciones documentadas; Piray Rodríguez et al. [27] observaron una adopción desigual de políticas internas de protección de datos entre universidades. La normativa técnica de la SPDP —la guía de gestión de riesgos en sus dos versiones y la norma de gran escala— es posterior a la mayoría de estos estudios [13], [15], [16], por lo que ningún antecedente nacional la ha incorporado todavía.

### 1.2.6 Análisis comparativo y brecha identificada

La Tabla 4 contrasta los marcos y trabajos más cercanos con seis criterios que se derivan de la LOPDP y de la guía de la SPDP: la valoración del riesgo desde la perspectiva de los titulares; la cobertura del ciclo completo de gestión (contexto, identificación, análisis, evaluación y tratamiento); la integración de la EIPD; la exigencia de estimaciones justificadas; la aplicación al sector de la educación superior, y la alineación con la normativa ecuatoriana.

**Tabla 4**
*Comparación de marcos y trabajos relacionados con los requisitos del proyecto.*

| **Marco o trabajo** | **Enfoque titulares** | **Ciclo completo** | **EIPD** | **Estimación justificada** | **Sector IES** | **Normativa Ecuador** |
| --- | --- | --- | --- | --- | --- | --- |
| ISO/IEC 27005:2022 [50] | No | Sí | No | Parcial | No | No |
| ISO/IEC 29134:2023 [45] | Sí | Parcial | Sí | No | No | No |
| AEPD (2021) [46] | Sí | Sí | Sí | Parcial | No | No |
| NIST Privacy Framework [47] | Sí | Parcial | No | No | No | No |
| LINDDUN [31] | Sí | Parcial | No | No | No | No |
| FAIR bayesiano [37] | No | Parcial | No | Sí | No | No |
| Guía SPDP V.2 [15] | Sí | Sí | Sí | Sí | No | Sí |
| Patiño et al. [38] | No | Sí | No | No | No | Sí |
| López-Vasco et al. [29] | No | Parcial | No | No | Sí | Sí |
| Habbabeh et al. [40] | Parcial | No | No | No | Sí | No |
| **Metodología propuesta** | **Sí** | **Sí** | **Sí** | **Sí** | **Sí** | **Sí** |

*Elaborado por:* Ramón Alejandro Manzaba Castro. *Fuente:* Elaboración propia a partir de las fuentes citadas.

La comparación muestra que ningún marco ni trabajo revisado satisface a la vez los seis criterios. Los marcos internacionales de privacidad adoptan la perspectiva de los titulares, pero no responden a la normativa ecuatoriana ni a las particularidades de una IES; los modelos de seguridad de la información aplicados en el país cubren el ciclo de gestión, pero sobre activos de la organización; los estudios sectoriales miden el cumplimiento o la percepción, no el riesgo; y la guía de la SPDP, aunque fija el marco obligatorio, es deliberadamente general y no ofrece una aplicación al sector educativo. El vacío que se identifica, por tanto, es la ausencia de una metodología que integre la evaluación de riesgos sobre los derechos de los titulares, las obligaciones de la LOPDP y de su reglamento, y las etapas y reglas de estimación definidas por la SPDP en el contexto específico de una IES ecuatoriana. Este trabajo se orienta a cubrir ese vacío.

## 1.3 Planteamiento del Problema

Las IES tratan grandes volúmenes de datos personales académicos, administrativos y de salud sin contar necesariamente con procesos sistemáticos de diagnóstico y gestión de riesgos alineados a la LOPDP, lo que genera exposición legal y vulnerabilidad de la información. La normativa exige una metodología de análisis de riesgos y, en los casos de tratamiento a gran escala de categorías especiales, una evaluación de impacto previa [10], [16]; no obstante, la evidencia nacional muestra una adopción desigual de políticas y brechas de capacidad técnica y humana en las universidades [28], [27]. En términos cuantitativos, el problema afecta a 64 universidades y escuelas politécnicas y a 216 institutos superiores [23], dentro de un sistema educativo de 16 161 instituciones en el ciclo 2024–2025 [20], mientras que los delegados de protección de datos registrados ante la SPDP no superaban los 1 150 en abril de 2025 [24] y no existe una medición oficial del grado de implementación de la ley en las universidades (Sección 1.1.3).

### 1.3.1 Análisis crítico

El análisis del problema se estructuró mediante un árbol de problemas que relaciona sus causas con el problema central y con los efectos que produce. La Tabla 5 presenta esa relación y la Figura 1 la representa de forma gráfica.

**Tabla 5**
*Árbol de problemas: causas, problema central y efectos.*

| **Causas** | **Problema central** | **Efectos** |
| --- | --- | --- |
| C1. Ausencia de un inventario o registro de actividades de tratamiento que identifique procesos, datos y titulares. | **Las IES tratan grandes volúmenes de datos personales sin procesos sistemáticos de diagnóstico y gestión de riesgos alineados a la LOPDP, lo que genera exposición legal y vulnerabilidad de la información.** | E1. Exposición a sanciones por infracciones graves (arts. 68 y 72 de la LOPDP). |
| C2. Enfoque de seguridad centrado en activos tecnológicos y no en los derechos de los titulares. |  | E2. Vulnerabilidad de la información ante incidentes de confidencialidad, integridad y disponibilidad. |
| C3. Desconocimiento de la normativa técnica reciente de la SPDP (guía de riesgos, gran escala). |  | E3. Evaluaciones de impacto omitidas o realizadas sin las etapas previas exigidas. |
| C4. Brechas de capacitación y cultura de protección de datos en el personal. |  | E4. Incapacidad de notificar vulneraciones dentro del término legal de cinco días. |
| C5. Uso creciente de plataformas en la nube y servicios de terceros sin evaluación de riesgos. |  | E5. Pérdida de confianza de estudiantes y docentes y daño reputacional. |

*Elaborado por:* Ramón Alejandro Manzaba Castro. *Fuente:* Elaboración propia con base en [10], [16], [28], [2].

**Figura 1**
*Árbol de problemas.*

> Diagrama elaborado en TikZ; véase el PDF. Su contenido coincide con la tabla del árbol de problemas.

La primera causa es la falta de un inventario de tratamientos. Sin conocer qué procesos tratan datos, qué categorías intervienen y cuántos titulares se ven afectados, no es posible aplicar los criterios del artículo 40 de la LOPDP ni calcular si un tratamiento alcanza el umbral de gran escala definido por la SPDP [16]. La segunda causa es de enfoque: los modelos aplicados en el sector, como los descritos por Patiño et al. [38] y López-Vasco et al. [29], valoran el riesgo sobre los activos de la organización, mientras que la LOPDP pone en el centro los derechos y libertades de los titulares. La tercera causa obedece a la velocidad del cambio normativo, pues entre 2025 y 2026 la SPDP expidió la guía de riesgos, su segunda versión y la norma de gran escala, lo que supone una carga de actualización para las IES. La cuarta causa, vinculada al factor humano, coincide con el hallazgo de Álvarez-Carrión y Hernández-Sotomayor [28] sobre el peso del error humano en los incidentes de universidades ecuatorianas y con la relevancia que Fernandes et al. [5] asignan a la capacitación y a la cultura de protección de datos. La quinta causa responde a la migración de servicios académicos hacia plataformas de terceros, en las que la IES sigue siendo responsable del tratamiento.

Entre los efectos destaca la exposición legal, que en este caso es directa: carecer de una metodología de análisis y gestión de riesgos ya configura la infracción grave del artículo 68, numeral 4. Para una IES particular, las infracciones graves se sancionan con multas de entre el 0,7 % y el 1 % de su volumen de negocio del ejercicio anterior [10, art. 72], y las primeras sanciones impuestas por la SPDP demuestran que la autoridad ya aplica ese régimen [17]. A ello se suman la vulnerabilidad técnica, con la consecuente afectación a titulares, y la incapacidad de responder a tiempo ante una vulneración, dado que el plazo de notificación es breve y presupone que la institución ha identificado de antemano sus escenarios de riesgo.

### 1.3.2 Prognosis

De no abordarse el problema, las IES continuarían tratando datos de estudiantes y docentes sin conocer con certeza cuáles de sus tratamientos son de alto riesgo ni cuáles exigen una evaluación de impacto previa, con lo que quedarían en situación de incumplimiento frente a los artículos 40 y 42 de la LOPDP y a la Resolución SPDP-SPD-2026-0005-R. En un escenario de incidente, la ausencia de escenarios de riesgo y de un procedimiento de respuesta dificultaría cumplir el término de notificación de cinco días del artículo 43, lo que agravaría la responsabilidad de la institución. La tendencia regional de ataques contra universidades [7], [6], [1] permite prever que la probabilidad de un incidente no disminuirá por sí sola, y la actividad sancionadora de la SPDP [17] indica que las consecuencias jurídicas de no gestionar el riesgo serán cada vez más tangibles. En el plano institucional, cada unidad seguiría aplicando criterios propios y no comparables, lo que impediría priorizar inversiones en controles y demostrar responsabilidad proactiva ante la autoridad.

### 1.3.3 Formulación del problema

¿Cómo diagnosticar y gestionar de forma sistemática los riesgos del tratamiento de datos personales de estudiantes y docentes en una institución de educación superior, de modo que se cumplan las exigencias de la LOPDP y de la normativa técnica de la SPDP?

### 1.3.4 Preguntas directrices

La investigación se orienta mediante cuatro preguntas directrices, cada una vinculada a un objetivo específico (OE). ¿Qué requisitos, información, instrumentos y actores se necesitan para diagnosticar el tratamiento de datos personales del proceso de admisión y matrícula de la UTI, y qué línea base de cumplimiento arroja ese diagnóstico? (OE1). ¿En qué situación se encuentra la implementación de la protección de datos personales en las universidades ecuatorianas y qué referentes nacionales e internacionales deben orientar las fases y los criterios de la metodología? (OE2). ¿Qué escenarios de riesgo, niveles de riesgo inherente y residual y medidas de tratamiento resultan de implementar la metodología en el proceso de admisión y matrícula de la UTI? (OE3). ¿Qué validez y aplicabilidad atribuyen a la metodología los expertos calibrados y los indicadores definidos, y qué mejoras se derivan de esa evaluación? (OE4).

### 1.3.5 Delimitación

En cuanto al contenido, el estudio pertenece al campo de las tecnologías de la información, en el área de gobernanza y seguridad de la información, y se centra en la gestión de riesgos sobre el tratamiento de datos personales de estudiantes y docentes conforme a la LOPDP, su reglamento y la normativa técnica de la SPDP. En lo espacial, se desarrolla en la Universidad Tecnológica Indoamérica, sede Quito, sobre el proceso de admisión y matrícula. En lo temporal, se ejecuta durante el periodo académico B26, entre el 13 de octubre de 2026 y el 26 de febrero de 2027, y considera la normativa vigente hasta la fecha de cierre del trabajo.

El planteamiento permite concluir que el problema no es la falta de normas, sino la falta de un procedimiento que las convierta en decisiones verificables dentro de la institución. Por ello, la pregunta de investigación no se limita a qué controles aplicar, sino a cómo diagnosticar y gestionar el riesgo de forma sistemática, trazable y centrada en los titulares.

## 1.4 Justificación

La importancia del trabajo radica en que la gestión de riesgos ha dejado de ser una buena práctica opcional para convertirse en una obligación jurídica. La LOPDP exige al responsable una metodología de análisis de riesgos y un proceso de evaluación continua de sus medidas de seguridad [10, arts. 37 y 40], y la SPDP ha concretado esa exigencia mediante una guía con un capítulo de cumplimiento obligatorio [13] y una norma que califica directamente como de gran escala los tratamientos de datos de salud y de adolescentes en entornos educativos [16]. Las IES, que tratan estos datos de forma habitual, requieren una herramienta que traduzca esas obligaciones a su realidad operativa. La necesidad es cuantificable: el sistema de educación superior cuenta con 280 instituciones —64 universidades y escuelas politécnicas y 216 institutos y conservatorios— [23], todas responsables del tratamiento de datos de su comunidad, mientras que el número de delegados de protección de datos registrados en todo el país, en abril de 2025, equivalía como máximo al 7,0 % de las instituciones educativas obligadas (Sección 1.1.3). Para una IES particular, además, una infracción grave se sanciona con una multa de entre el 0,7 % y el 1 % de su volumen de negocio del ejercicio anterior [10, art. 72], y las dos primeras multas impuestas por la SPDP sumaron cerca de 454 500 dólares [17].

La novedad del aporte reside en la integración de elementos que la literatura aborda por separado. Los antecedentes revisados ofrecen metodologías generales de evaluación de impacto [35], [34] o modelos de seguridad de la información centrados en activos [29], [38], pero no una metodología específica para IES ecuatorianas que adopte la perspectiva de los titulares exigida por la LOPDP y siga las etapas de la guía de la SPDP. Este vacío coincide con la escasez de investigación empírica sobre riesgos en la educación superior señalada por Ulven y Wangen [2].

La utilidad del proyecto se expresa en sus productos: un documento metodológico por fases y una matriz de riesgos aplicada, concebida como plantilla reutilizable en hoja de cálculo, que la institución podrá emplear para priorizar controles, documentar su responsabilidad proactiva y preparar evaluaciones de impacto. La factibilidad es técnica, operativa y económica, porque el trabajo se apoya en normas de acceso público, en herramientas ofimáticas de uso común y en el acceso a información institucional bajo las debidas autorizaciones, sin requerir infraestructura adicional.

Los beneficiarios directos son la institución, en su calidad de responsable del tratamiento, y las unidades académicas y administrativas que intervienen en el caso de estudio; los beneficiarios indirectos son los estudiantes y docentes, cuyos derechos se protegen mejor cuando los riesgos se identifican y tratan de forma anticipada, así como otras IES que podrán replicar la metodología. El impacto esperado es la reducción de la exposición legal y de la vulnerabilidad de la información, junto con una mejora de la confianza de la comunidad universitaria.

El trabajo se inscribe en la línea de investigación Gestión de la Información, sublínea Gobernanza y seguridad de la información, y en el eje de aplicación Tecnologías para la educación. Asimismo, contribuye a las competencias del perfil de egreso PE-CP-06, que consiste en evaluar proyectos de TI en el ámbito de las buenas prácticas y en concordancia con el marco legal vigente; PE-MI-04, relativa a gestionar proyectos de TI aplicando conceptos éticos, legales, económicos y financieros para la toma de decisiones; PE-IS-04, referida a realizar proyectos de investigación sobre problemas técnicos de la profesión siguiendo una metodología científica; y PE-PP-05, que corresponde a implementar sistemas de seguridad informática bajo políticas organizacionales y estándares aceptados, con ética y responsabilidad.

Podría objetarse que la guía de la SPDP ya ofrece a las instituciones todo lo necesario y que, por tanto, una metodología adicional resulta redundante. La objeción no se sostiene por dos razones. Primero, la guía es deliberadamente general: fija etapas y reglas de estimación aplicables a cualquier responsable, pero no indica qué procesos, titulares, amenazas ni controles son característicos de una universidad. Segundo, la propia guía exige que la metodología se adapte a la naturaleza del tratamiento y a las partes involucradas, como también lo hace el artículo 40 de la LOPDP [10, art. 40]. En consecuencia, el trabajo no duplica la guía, sino que la vuelve operativa para el contexto de una IES, y en ello reside su justificación.

## 1.5 Objetivos
### 1.5.1 Objetivo General

Diseñar una metodología de diagnóstico y gestión de riesgos para el tratamiento de datos personales de estudiantes y docentes en instituciones de educación superior, mediante la integración de las etapas de la guía de gestión de riesgos y evaluación de impacto de la SPDP con la norma ISO/IEC 27005:2022, para contribuir al cumplimiento de las obligaciones de análisis de riesgos y evaluación de impacto establecidas en la Ley Orgánica de Protección de Datos Personales (2021) y en su Reglamento General (2023).

### 1.5.2 Objetivos Específicos

1. Diagnosticar el tratamiento de datos personales del proceso de admisión y matrícula de la Universidad Tecnológica Indoamérica, sede Quito, mediante la determinación precisa de los requisitos normativos, la información, los instrumentos, las fuentes y los actores necesarios, y su aplicación en revisión documental, entrevistas semiestructuradas y un cuestionario de madurez, para establecer la línea base de cumplimiento respecto de la LOPDP (2021) y su Reglamento General (2023).

2. Analizar la situación de implementación de la protección de datos personales en las universidades ecuatorianas y los referentes normativos y metodológicos nacionales e internacionales, mediante la revisión de fuentes oficiales, estudios indexados y marcos de gestión de riesgos, para fundamentar las fases y los criterios de la metodología.

3. Implementar la metodología en el proceso de admisión y matrícula de la Universidad Tecnológica Indoamérica, sede Quito, mediante la identificación de escenarios de riesgo, su estimación con criterio de expertos y su registro en una matriz de riesgos inherentes y residuales, para formular un plan de tratamiento con controles, responsables, plazos e indicadores trazables a la LOPDP.

4. Evaluar la metodología mediante un panel Delphi con expertos calibrados, juicio de expertos e indicadores con metas, para determinar su validez y aplicabilidad y formular recomendaciones de mejora continua alineadas a la LOPDP y a la normativa de la SPDP.

Los cuatro objetivos guardan una secuencia lógica con el objetivo general: el primero establece qué se necesita saber y cuál es el punto de partida; el segundo sitúa la propuesta frente a la realidad de las universidades y a los referentes disponibles; el tercero pone a prueba el diseño en un proceso real, y el cuarto determina, con evidencia documentada, si la metodología es válida y cómo mejorarla.

## 1.6 Alcance del Proyecto

El alcance del proyecto comprende cuatro componentes, uno por objetivo específico: (1) la determinación de los requisitos del diagnóstico y su ejecución sobre las actividades de tratamiento del proceso de admisión y matrícula de la UTI; (2) el análisis de la situación de las universidades ecuatorianas y de los referentes normativos y metodológicos, que fundamenta una metodología con una fase de preparación, una fase de diagnóstico de madurez y fases de identificación, evaluación, mitigación y monitoreo articuladas con las etapas de la guía de la SPDP; (3) la implementación de la metodología en el proceso de admisión y matrícula de la UTI, sede Quito, con su matriz de riesgos inherentes y residuales en una plantilla reutilizable y su plan de tratamiento, y (4) la evaluación de la metodología mediante un panel Delphi calibrado, juicio de expertos e indicadores con metas, de la que se derivan las recomendaciones de mejora continua.

El proyecto excluye de manera expresa tres aspectos. En primer lugar, no incluye la certificación legal formal ante la autoridad de protección de datos, por lo que sus resultados no constituyen una declaración de cumplimiento ante la SPDP. En segundo lugar, no cubre la implementación completa de todas las medidas correctivas recomendadas, que corresponderá a la institución según sus prioridades y recursos. En tercer lugar, no abarca una auditoría externa independiente; las revisiones que se realicen tendrán carácter interno y académico.

Entre las limitaciones se reconoce, primero, que el acceso a información institucional depende de la autorización formal de la universidad y de la disponibilidad de los responsables del proceso; toda evidencia se tratará de forma anonimizada o agregada y ningún dato personal real se incorporará al documento. Segundo, la estimación de probabilidades e impactos se apoyará en criterio de expertos, con la incertidumbre propia de ese tipo de juicio, aunque cada valor se acompañará de su justificación conforme exige la guía de la SPDP. Tercero, la normativa técnica de la SPDP se encuentra en evolución, por lo que la metodología se ajustará a la vigente a la fecha de cierre del trabajo.

Delimitar de este modo el alcance no debilita el aporte, sino que lo hace verificable: el trabajo se compromete con lo que puede demostrar —un método, una herramienta y su aplicación en un proceso real— y deja expresamente fuera aquello que corresponde a la institución o a la autoridad.

## 1.7 Fundamentación Teórica

La fundamentación parte de una premisa: una metodología de gestión de riesgos sobre datos personales solo es aplicable si quienes la usan comprenden con precisión los términos legales, el lugar de cada norma en el ordenamiento y la etapa en que se encuentra su aplicación en el país. Por ello, esta sección define primero los términos legales, explica después cómo opera una ley en Ecuador, sitúa la etapa actual con fecha de corte, contrasta el régimen ecuatoriano con el de otros países y detalla el régimen de vulneraciones, antes de presentar los fundamentos de la gestión de riesgos.

### 1.7.1 Términos legales

La Tabla 6 define los términos legales que emplea la metodología con la cita del artículo que los establece. Las definiciones se parafrasean del texto oficial de la LOPDP y de su Reglamento General.

**Tabla 6**
*Términos legales de la protección de datos personales en Ecuador.*

| **Término** | **Definición y alcance** | **Base legal** |
| --- | --- | --- |
| Dato personal | Dato que identifica o hace identificable a una persona natural, directa o indirectamente. | LOPDP, art. 4 |
| Datos sensibles | Datos relativos a etnia, identidad de género, identidad cultural, religión, ideología, filiación política, pasado judicial, condición migratoria, orientación sexual, salud, datos biométricos y genéticos, y aquellos cuyo tratamiento indebido pueda originar discriminación. | LOPDP, art. 4 |
| Categorías especiales | Datos sensibles; datos de niñas, niños y adolescentes; datos de salud, y datos de personas con discapacidad y de sus sustitutos. | LOPDP, art. 25 |
| Datos de niñas, niños y adolescentes | Categoría especial. Los adolescentes pueden consentir por sí mismos desde los 15 años si se les especifican con claridad los fines; entre los 12 y los 15 años, y en el caso de niñas y niños, ejercen sus derechos mediante su representante legal. | LOPDP, arts. 21, 24 y 25 |
| Titular | Persona natural cuyos datos son objeto de tratamiento. | LOPDP, art. 4 |
| Tratamiento | Cualquier operación o conjunto de operaciones sobre datos personales, automatizada o no: recogida, registro, conservación, consulta, comunicación, supresión, destrucción y, en general, cualquier uso. | LOPDP, art. 4 |
| Responsable del tratamiento | Persona natural o jurídica, pública o privada, autoridad u organismo que, solo o con otros, decide sobre la finalidad y el tratamiento. | LOPDP, art. 4 |
| Encargado del tratamiento | Persona natural o jurídica, pública o privada, que trata datos a nombre y por cuenta del responsable; su relación se rige por un contrato escrito. | LOPDP, art. 4; RLOPDP, art. 41 |
| Delegado de protección de datos (DPD) | Persona natural que informa al responsable o al encargado sobre sus obligaciones, supervisa el cumplimiento y coopera con la autoridad como punto de contacto. Es obligatorio en el sector público, cuando las actividades requieren un control permanente y sistematizado, en el tratamiento a gran escala de categorías especiales y en otros casos que fije la autoridad. Entre sus funciones está asesorar en el análisis de riesgos y la evaluación de impacto. Requiere título de tercer nivel en Derecho, Sistemas de Información, Comunicación o Tecnologías y al menos cinco años de experiencia profesional. | LOPDP, arts. 4, 48 y 49; RLOPDP, arts. 48 y 55 |
| Vulneración de la seguridad de los datos | Incidente de seguridad que afecta la confidencialidad, la disponibilidad o la integridad de los datos personales. | LOPDP, art. 4 |
| Evaluación de impacto (EIPD) | Análisis preventivo con el que el responsable valora los impactos del tratamiento; es obligatoria, entre otros casos, en el tratamiento a gran escala de categorías especiales y debe realizarse antes del inicio del tratamiento. | LOPDP, art. 42; RLOPDP, arts. 29 a 32 |
| Registro de actividades de tratamiento (RAT) | Registro escrito o electrónico de los fines, titulares, categorías de datos, destinatarios, transferencias, bases de legitimación, plazos de conservación y medidas de seguridad. Obligatorio con cien o más trabajadores y, con menos, cuando el tratamiento implica riesgo, no es ocasional o incluye categorías especiales. | RLOPDP, arts. 38 y 39 |
| Autoridad de Protección de Datos Personales | Autoridad pública independiente que supervisa la aplicación de la ley, el reglamento y sus resoluciones; en Ecuador la ejerce la Superintendencia de Protección de Datos Personales (SPDP). | LOPDP, arts. 4, 76 y 77 |

*Elaborado por:* Ramón Alejandro Manzaba Castro. *Fuente:* Elaboración propia a partir de [10], [11].

En una IES, la institución actúa como responsable, los proveedores de plataformas académicas suelen actuar como encargados y el delegado actúa como asesor y supervisor independiente, no como ejecutor de la gestión de riesgos. Esta distinción tiene consecuencias metodológicas: la metodología asigna las decisiones de tratamiento del riesgo a la máxima autoridad y a los responsables de proceso, y reserva al delegado la emisión de observaciones previas.

### 1.7.2 Cómo funciona una ley en el ordenamiento ecuatoriano

La Constitución establece el orden jerárquico de aplicación de las normas: la Constitución; los tratados y convenios internacionales; las leyes orgánicas; las leyes ordinarias; las normas regionales y las ordenanzas distritales; los decretos y reglamentos; las ordenanzas; los acuerdos y las resoluciones, y los demás actos de los poderes públicos; en caso de conflicto, prevalece la norma de mayor jerarquía [51, art. 425]. La protección de datos personales es un derecho constitucional [51, art. 66, num. 19], y por eso se regula mediante una ley orgánica, categoría que la Constitución reserva, entre otras materias, a la regulación del ejercicio de los derechos constitucionales [51, art. 133].

En el caso concreto, la cadena normativa funciona en cuatro niveles. La LOPDP fija principios, derechos, obligaciones, infracciones y sanciones, y entró en vigencia con su publicación en el Registro Oficial [10, disposición final]. El Reglamento General, expedido por el Presidente de la República mediante decreto ejecutivo, desarrolla la ley sin poder contradecirla ni limitar los derechos que reconoce [10, art. 6], [11]. La SPDP, como autoridad de control, emite normativa general o técnica para el ejercicio de sus competencias [10, art. 76, num. 5], y lo hace mediante resoluciones, como la guía de gestión de riesgos o la norma de gran escala. Por último, las normas técnicas internacionales —ISO/IEC o NIST— no son obligatorias por sí mismas, pero la ley permite a los responsables acogerse a estándares internacionales de gestión de riesgos [10, art. 37] y la guía de la SPDP recomienda ISO/IEC 27005 [15].

El tiempo también forma parte del funcionamiento de una ley. La LOPDP previó un régimen transitorio: sus disposiciones sobre medidas correctivas y régimen sancionatorio entraron en vigencia dos años después de su publicación, plazo durante el cual responsables y encargados debían adecuarse, y los tratamientos anteriores a la ley también contaban con dos años para ajustarse [10, disposiciones transitorias primera y segunda]. En consecuencia, desde mayo de 2023 la ley es plenamente exigible, y cada resolución posterior de la SPDP rige desde su publicación en el Registro Oficial, salvo que disponga otra cosa.

### 1.7.3 Etapa actual de la protección de datos en Ecuador

Para responder en qué etapa se encuentra el país, la Tabla 7 reconstruye la cronología normativa e institucional con fecha de corte al 27 de octubre de 2026. Solo se incluyen hitos verificados en el Registro Oficial, en documentos de la autoridad o en fuentes que citan esos documentos.

**Tabla 7**
*Cronología de la protección de datos personales en Ecuador (corte: 27 de octubre de 2026).*

| **Fecha** | **Hito** | **Fuente** |
| --- | --- | --- |
| 20-10-2008 | La Constitución reconoce el derecho a la protección de datos de carácter personal (art. 66, num. 19). | [51] |
| 26-05-2021 | Publicación de la LOPDP en el Quinto Suplemento del Registro Oficial N.º 459. | [10] |
| Mayo de 2023 | Vencen los dos años de adecuación; entran en vigencia las medidas correctivas y el régimen sancionatorio. | [10] |
| 13-11-2023 | Publicación del Reglamento General (Decreto Ejecutivo N.º 904). | [11] |
| 28-03-2024 | El CPCCS designa al primer Superintendente de Protección de Datos Personales. | [52] |
| 19-05-2025 | Publicación de la Guía de Gestión de Riesgos y Evaluación de Impacto (Res. SPDP-SPD-2025-0003-R). | [13], [14] |
| 2025 | Reglamento del delegado de protección de datos (Res. SPDP-SPD-2025-0028-R). | [25] |
| Diciembre de 2025 | Primeras sanciones por infracciones graves (cerca de 454 500 dólares en total). | [17] |
| 25-02-2026 | Norma de tratamiento a gran escala (Res. SPDP-SPD-2026-0005-R). | [16] |
| 30-03-2026 | Segunda versión de la guía de gestión de riesgos (Res. SPDP-SPD-2026-0012-R). | [15] |
| 22-05-2026 | La Ley Orgánica para el Fortalecimiento de la Ciberseguridad reforma el art. 43 de la LOPDP (notificación al CSIRT) e introduce el plazo de 72 horas para incidentes de ciberseguridad. | [12] |
| 24-09-2026 | Norma técnica de notificación de vulneraciones (Res. SPDP-SPD-2026-0040-R), con canal digital SISPDP. | [53] |

*Elaborado por:* Ramón Alejandro Manzaba Castro. *Fuente:* Elaboración propia a partir de las fuentes citadas.

La cronología permite caracterizar la etapa actual como de *consolidación regulatoria con aplicación incipiente*. La fase legislativa concluyó en 2021 y la de adecuación en 2023; la autoridad de control existe desde 2024 y, entre 2025 y 2026, expidió la normativa secundaria que vuelve operativas las obligaciones de gestión de riesgos, evaluación de impacto, delegado y notificación de vulneraciones. Sin embargo, la aplicación efectiva apenas comienza: las primeras sanciones son de diciembre de 2025 y no existen estadísticas públicas sobre el cumplimiento de los sectores regulados (Sección 1.1.3). Para las instituciones educativas, esto significa que las reglas ya están definidas y son exigibles, pero aún no existen prácticas sectoriales consolidadas que les sirvan de referencia.

### 1.7.4 Contraste con otros países

La Tabla 8 compara el régimen ecuatoriano con los de la Unión Europea (con la particularidad de España), Colombia, Perú, Chile y Brasil en seis criterios relevantes para una institución educativa. Los datos se tomaron de los textos legales o de las autoridades de cada país; los que no pudieron contrastarse con el texto oficial se señalan para su verificación.

**Tabla 8**
*Comparación de regímenes de protección de datos personales.*

| **País y norma (año)** | **Autoridad** | **Delegado (DPD)** | **Notificación de vulneraciones** | **Sanción máxima** | **Menores y educación** |
| --- | --- | --- | --- | --- | --- |
| Unión Europea: RGPD (2016, aplicable desde 2018); España: LOPDGDD (2018) [54], [55] | Autoridad nacional de control (en España, la AEPD) | Obligatorio en autoridades públicas y en tratamientos a gran escala de categorías especiales o de observación sistemática (RGPD, art. 37); en España, obligatorio para centros docentes y universidades públicas y privadas (LOPDGDD, art. 34) | 72 horas desde que se tiene constancia (RGPD, art. 33) | 20 millones de euros o 4 % del volumen de negocio anual mundial (RGPD, art. 83) | Consentimiento propio desde los 16 años, que cada Estado puede reducir hasta 13 (RGPD, art. 8); en España, 14 años (LOPDGDD, art. 7) |
| Colombia: Ley 1581 (2012) [56], [57], [58] | Superintendencia de Industria y Comercio (SIC) | Todo responsable y encargado debe designar una persona o área que asuma la función de protección de datos (Decreto 1377 de 2013, art. 23; Decreto 1074 de 2015, art. 2.2.2.25.4.4) | 15 días hábiles desde la detección, por instrucción de la SIC | 2 000 salarios mínimos mensuales (art. 23) | Tratamiento proscrito salvo datos de naturaleza pública, con respeto de los derechos prevalentes (art. 7) |
| Perú: Ley 29733 (2011); reglamento D.S. 016-2024-JUS [59], [60] | Autoridad Nacional de Protección de Datos Personales | Figura del oficial de datos personales incorporada por el reglamento de 2024 | 48 horas desde que se toma conocimiento (reglamento, art. 34) | Hasta 100 UIT, sin superar el 10 % de los ingresos brutos anuales (Ley 29733, art. 39) | No se halló el texto oficial de la regla sobre menores en las fuentes consultadas |
| Chile: Ley 21.719 (2024; vigencia desde el 1-12-2026) [61] | Agencia de Protección de Datos Personales | Voluntario: el responsable “podrá designar” un delegado (art. 50) | “Por los medios más expeditos posibles y sin dilaciones indebidas” (art. 14 sexies), sin plazo en horas | 20 000 UTM; en reincidencia de empresas que no son de menor tamaño, hasta el 4 % de los ingresos anuales | Niños menores de 14 años: consentimiento de sus padres; datos sensibles de adolescentes menores de 16 años: igual regla; prima el interés superior (art. 16 quáter) |
| Brasil: LGPD (2018) [62], [63], [64] | Autoridad Nacional de Protección de Datos (ANPD) | Obligatorio el encargado (*encarregado*) (art. 41), con dispensa para agentes de pequeño porte (Res. CD/ANPD 2/2022, art. 11) | 3 días hábiles desde que se conoce que el incidente afectó datos personales (Res. CD/ANPD 15/2024) | 2 % de la facturación en Brasil, con un tope de 50 millones de reales por infracción (art. 52) | Tratamiento en el mejor interés del menor; para niños, consentimiento específico de al menos uno de los padres o del responsable legal (art. 14) |
| Ecuador: LOPDP (2021) [10], [12], [16] | Superintendencia de Protección de Datos Personales (SPDP) | Obligatorio en el sector público, con control permanente y sistematizado y en gran escala de categorías especiales (art. 48); los entornos educativos con datos de menores son gran escala (Res. 0005-R) | Término de 5 días a la SPDP, al organismo de control y al CSIRT (art. 43); 3 días a los titulares (art. 46) | Privados: 0,7 % a 1 % del volumen de negocio por infracción grave (art. 72) | Categoría especial (art. 25); consentimiento propio desde los 15 años (art. 21); deberes de las entidades educativas (arts. 23 y 24) |

*Elaborado por:* Ramón Alejandro Manzaba Castro. *Fuente:* Elaboración propia a partir de las fuentes citadas.

El contraste arroja tres conclusiones. Primero, el término ecuatoriano de cinco días para notificar a la autoridad es más amplio que el europeo (72 horas), el peruano (48 horas) y el brasileño (3 días hábiles), lo que no reduce la exigencia: presupone que la institución ha identificado sus escenarios de riesgo de antemano para poder evaluar y notificar dentro de ese término. Segundo, de acuerdo con los textos revisados, Ecuador se sitúa, junto con España, entre los regímenes que vinculan expresamente el tratamiento de datos de menores en el ámbito educativo con obligaciones reforzadas —gran escala, evaluación de impacto y delegado—, lo que coloca a las instituciones educativas ecuatorianas en el nivel más alto de exigencia de la región. Tercero, mientras Chile mantiene el delegado como figura voluntaria y Colombia carece de un plazo legal en horas, Ecuador combina un delegado obligatorio en los supuestos educativos con plazos legales fijos, de modo que la metodología debe producir evidencia verificable de cumplimiento y no solo buenas prácticas.

### 1.7.5 Régimen de vulneraciones: plazos, SISPDP y comunicación a los titulares

La Tabla 9 sintetiza los plazos verificados en los textos oficiales, con el sujeto obligado, el destinatario y el momento en que empieza a correr cada plazo. Su lectura conjunta despeja una confusión frecuente: el plazo de 72 horas no es de protección de datos, sino de ciberseguridad, y no obliga a una universidad particular salvo que sea operadora de infraestructura crítica digital.

**Tabla 9**
*Plazos de notificación de vulneraciones e incidentes vigentes en Ecuador (corte: 27 de octubre de 2026).*

| **Obligación** | **Sujeto obligado** | **Destinatario** | **Plazo** | **Inicio del cómputo** | **Base legal** |
| --- | --- | --- | --- | --- | --- |
| Notificar la vulneración | Responsable del tratamiento | SPDP; organismo de regulación y control competente; CSIRT correspondiente (con fines informativos y de coordinación) | Tan pronto sea posible; máximo término de 5 días | Desde que tuvo constancia de la vulneración | LOPDP, art. 43, reformado por la LOFC, art. 14 |
| Notificar al responsable | Encargado del tratamiento | Responsable | Tan pronto sea posible; máximo término de 2 días | Desde que tuvo conocimiento | LOPDP, art. 43; RLOPDP, art. 27 |
| Notificar al titular | Responsable del tratamiento | Titulares afectados | Sin dilación; término de 3 días | Desde que tuvo conocimiento del riesgo | LOPDP, art. 46; RLOPDP, art. 28 |
| Notificar un incidente de ciberseguridad | Entidades públicas y operadores de infraestructura crítica digital | Ente rector de la ciberseguridad (a través del órgano de control especializado, si lo hay) | De inmediato; máximo 72 horas | Desde la detección del incidente | Ley Orgánica de Transformación Digital y Audiovisual, art. 20-G, incorporado por la LOFC, art. 6 |

*Elaborado por:* Ramón Alejandro Manzaba Castro. *Fuente:* Elaboración propia a partir de [10], [11], [12].

El Reglamento General precisa tres elementos que la metodología incorpora. Primero, la notificación procede cuando es probable que la vulneración constituya un riesgo para los derechos de las personas, y se presume ese riesgo cuando los datos fueron destruidos o dejaron de estar disponibles, fueron alterados o quedaron incompletos, el responsable perdió su control o acceso, o el tratamiento no fue autorizado o es ilícito [11, art. 24]. Segundo, la notificación debe contener la naturaleza y el tipo de vulneración, los titulares afectados, el detalle inicial de los sistemas vulnerados, la causa presunta, el volumen y los tipos de datos comprometidos, las medidas adoptadas y previstas, la evaluación del riesgo para los titulares y otros aspectos que determine la autoridad [11, art. 26]. Tercero, la comunicación al titular contiene la misma información, en lenguaje claro y sencillo [11, art. 28]. La ley exceptúa la comunicación al titular cuando el responsable aplicó medidas que se demuestran efectivas sobre los datos afectados, cuando adoptó medidas que garantizan que el riesgo no se materializará —ambas excepciones deben ser calificadas por la autoridad— o cuando la comunicación individual exige un esfuerzo desproporcionado, caso en que procede una comunicación pública [10, art. 46].

La Resolución SPDP-SPD-2026-0040-R concretó el procedimiento: la notificación se presenta por medios digitales a través del Sistema Nacional de Registro de Datos Personales (SISPDP), y su omisión constituye una infracción grave; las vulneraciones se clasifican según la dimensión afectada —confidencialidad, integridad o disponibilidad— y según su carácter temporal, permanente o irreversible; y la comunicación a los titulares debe informar la naturaleza del incidente, las fechas estimadas, las medidas de mitigación y las recomendaciones de protección, según el texto publicado en el Registro Oficial y los análisis jurídicos de la norma [53]. Para la metodología, estas reglas convierten la fase de monitoreo en un procedimiento con plazos verificables: la clasificación de la vulneración reutiliza la separación por dimensiones de la matriz, y la evaluación del riesgo exigida en la notificación reutiliza las escalas de impacto sobre el titular.

### 1.7.6 Gestión de riesgos y evaluación de impacto

La gestión de riesgos se entiende como el conjunto de actividades coordinadas para dirigir y controlar una organización con respecto al riesgo [65]. La norma ISO/IEC 27005:2022 desarrolla ese marco para la seguridad de la información mediante un proceso que comprende el establecimiento del contexto, la identificación, el análisis, la evaluación y el tratamiento de riesgos, junto con su comunicación y seguimiento [50]; la guía de la SPDP adopta esas mismas etapas y las orienta hacia la protección de los derechos de los titulares [13]. La norma ISO/IEC 27701:2025 complementa el enfoque con requisitos para un sistema de gestión de la información de privacidad [66].

La evaluación de impacto relativa a la protección de datos (EIPD) es el análisis previo de un tratamiento que probablemente conlleve un alto riesgo para los derechos y libertades de los titulares [10, art. 42]. La literatura la distingue del análisis de riesgos de seguridad porque su objeto es el daño a las personas y no la pérdida para la organización [34]. En cuanto a la estimación del riesgo, coexisten enfoques cualitativos, basados en escalas y criterio de expertos, y enfoques cuantitativos como el modelo FAIR, que estima la frecuencia y la magnitud de las pérdidas mediante simulación y redes bayesianas [37]. Distinguir entre riesgo inherente, previo a los controles, y riesgo residual, posterior a ellos, permite medir el efecto de las medidas propuestas, que es precisamente lo que el artículo 37 de la LOPDP exige evidenciar.

De estos fundamentos se desprende la premisa conceptual de todo el trabajo: en materia de datos personales, el riesgo relevante no es la pérdida que sufre la organización, sino el daño que puede sufrir el titular. Una metodología que no adopte esa premisa podrá proteger sistemas, pero no cumplirá la LOPDP. Sobre esa base se construye el diseño metodológico que se presenta en el capítulo siguiente.

## Referencias del capítulo

Numeración IEEE idéntica a la del PDF (`main.pdf`).

[1] Sophos, “The state of ransomware in education 2024,” Sophos, Tech. Rep., 2024. [Online]. Available: https://www.sophos.com/en-us/blog/the-state-of-ransomware-in-education-2024

[2] J. B. Ulven and G. Wangen, “A systematic review of cybersecurity risks in higher education,” *Future Internet*, vol. 13, no. 2, p. 39, 2021.

[3] J. Li, W. Xiao, and C. Zhang, “Data security crisis in universities: identification of key factors affecting data breach incidents,” *Humanities and Social Sciences Communications*, vol. 10, p. 270, May 2023.

[4] Q. Liu and M. Khalil, “Understanding privacy and data protection issues in learning analytics using a systematic review,” *British Journal of Educational Technology*, vol. 54, no. 6, pp. 1715–1747, Nov. 2023.

[5] J. Fernandes, C. Machado, and L. Amaral, “Identifying critical success factors for the general data protection regulation implementation in higher education institutions,” *Digital Policy, Regulation and Governance*, vol. 24, no. 4, pp. 355–379, 2022.

[6] Semana, “Los detalles secretos del grave hackeo que sufrió la Universidad Nacional,” Apr. 2023. [Online]. Available: https://www.semana.com/nacion/articulo/asi-fue-el-hackeo-del-que-fue-victima-la-universidad-nacional/202335/

[7] CNN Chile, “Hackeo a la Universidad Santa María: datos de estudiantes y académicos fueron vulnerados y publicados en la dark web,” Nov. 2024. [Online]. Available: https://www.cnnchile.com/pais/hackeo-universidad-santa-maria-datos-estudiantes-academicos-vulnerados-publicados-dark-web_20241116/

[8] T. D. Zappelini, L.-M. Schippers, and A. P. da Silva, “Personal data of adolescents in higher education: The LGPD and the use of digital media for teaching activities and remote testing,” *Revista Direito GV*, vol. 19, p. e2335, 2023.

[9] Y. Arciniegas, “Falla informática en Ecuador: los datos de casi toda la población quedaron expuestos,” France 24, Sep. 2019. [Online]. Available: https://www.france24.com/es/20190917-ecuador-datos-expuestos-informacion-filtracion

[10] Asamblea Nacional del Ecuador, “Ley Orgánica de Protección de Datos Personales,” Registro Oficial Quinto Suplemento N.º 459, Quito, Ecuador, May 2021.

[11] Presidencia de la República del Ecuador, “Reglamento General a la Ley Orgánica de Protección de Datos Personales (Decreto Ejecutivo N.º 904),” Registro Oficial Tercer Suplemento N.º 435, Quito, Ecuador, Nov. 2023.

[12] Asamblea Nacional del Ecuador, “Ley Orgánica para el Fortalecimiento de la Ciberseguridad,” Registro Oficial Quinto Suplemento N.º 290, 22 de mayo de 2026, Quito, Ecuador, 2026. [Online]. Available: https://www.asambleanacional.gob.ec/es/system/files/ro_29.pdf

[13] Superintendencia de Protección de Datos Personales, “Guía de Gestión de Riesgos y Evaluación de Impacto del Tratamiento de Datos Personales,” Resolución N.º SPDP-SPD-2025-0003-R, 29 de abril de 2025. Registro Oficial Cuarto Suplemento N.º 41, 19 de mayo de 2025, Quito, Ecuador, 2025. [Online]. Available: https://spdp.gob.ec/wp-content/uploads/2025/05/03.01.01-SPDP-SPD-2025-0003-R-Guia-Gest-de-Riesg-y-Ev-Imp-signed.pdf

[14] Lexis, “Registro Oficial del día: Superintendencia expide guía para gestión de riesgos y evaluación de impacto en tratamiento de datos personales,” 2025. [Online]. Available: https://www.lexis.com.ec/noticias/registro-oficial-del-dia-superintendencia-expide-guia-para-gestion-de-riesgos-y-evaluacion-de-impacto-en-tratamiento-de-datos-personales

[15] Superintendencia de Protección de Datos Personales, “Guía de Gestión de Riesgos y Evaluación de Impacto del Tratamiento de Datos Personales, Versión 2,” Resolución N.º SPDP-SPD-2026-0012-R. Registro Oficial Suplemento N.º 254, 30 de marzo de 2026, Quito, Ecuador, 2026. [Online]. Available: https://spdp.gob.ec/wp-content/uploads/2026/03/ggrispdp2026v2.pdf

[16] –––, “Norma General sobre el Tratamiento de Datos Personales a Gran Escala,” Resolución N.º SPDP-SPD-2026-0005-R, Registro Oficial Suplemento N.º 231, 25 de febrero de 2026, Quito, Ecuador, 2026.

[17] R. Revelo, “Superintendencia de datos sanciona a LigaPro y FEF por infracciones en el tratamiento de datos personales,” Primicias, Dec. 2025. [Online]. Available: https://www.primicias.ec/deportes/futbol/superintendencia-datos-sanciona-ligapro-fef-infracciones-tratamiento-datos-personales-110763/

[18] ECIJA GPA, “Primeras sanciones por vulneración de datos en Ecuador,” Dec. 2025. [Online]. Available: https://www.ecija.com/actualidad-insights/primeras-sanciones-por-vulneracion-de-datos-en-ecuador/

[19] M. Almeida and P. Mena Mena, “Cero sanciones en Ecuador por una ley de protección de datos personales blandengue,” Primicias, Sep. 2025. [Online]. Available: https://www.primicias.ec/politica/cero-sanciones-ecuador-ley-proteccion-datos-personales-blandengue-104527/

[20] El Diario, “En Ecuador hay más de 4 millones de estudiantes de educación básica y bachillerato, la mayoría asiste a instituciones públicas,” El Diario (Ecuador), con cifras del Ministerio de Educación, Sep. 2025. [Online]. Available: https://www.eldiario.ec/ecuador/en-ecuador-hay-mas-de-4-millones-de-estudiantes-de-educacion-basica-y-bachillerado-la-mayoria-asiste-a-instituciones-publicas-23092025/

[21] Ministerio de Educación del Ecuador, “Estadística educativa, volumen 5,” Ministerio de Educación, Quito, Ecuador, Tech. Rep., Oct. 2024. [Online]. Available: https://educacion.gob.ec/wp-content/uploads/downloads/2024/10/Estadistica-Educativa-Vol-5.pdf

[22] Consejo Nacional para la Igualdad Intergeneracional, “Informe de observancia a los centros de desarrollo infantil,” Consejo Nacional para la Igualdad Intergeneracional, Quito, Ecuador, Tech. Rep., Nov. 2025. [Online]. Available: https://www.igualdad.gob.ec/wp-content/uploads/downloads/2025/11/informe_observancia_serv_desarrollo_infantil.pdf

[23] Consejo de Educación Superior, “Estadísticas IES,” Portal institucional del CES, consultado el 27 de octubre de 2026, Quito, Ecuador, 2026. [Online]. Available: https://www.ces.gob.ec/?page_id=5248

[24] IT Ahora, “Avances y acción de la Superintendencia de Protección de Datos Personales,” IT Ahora, Apr. 2025. [Online]. Available: https://itahora.com/2025/04/16/avances-y-accion-de-la-superintendencia-de-proteccion-de-datos-personales/

[25] Superintendencia de Protección de Datos Personales, “Reglamento del Delegado de Protección de Datos Personales,” Resolución N.º SPDP-SPD-2025-0028-R, Quito, Ecuador, 2025. [Online]. Available: https://spdp.gob.ec/wp-content/uploads/2025/07/028-R.pdf

[26] –––, “Informe de rendición de cuentas 2025 (Informe n.º INF-SPDP-PIN-GE-2026-0035),” Superintendencia de Protección de Datos Personales, Quito, Ecuador, Tech. Rep., Apr. 2026. [Online]. Available: https://spdp.gob.ec/wp-content/uploads/2026/04/INFORME-RC-SPDP-2025-VF-17-04-2026-1.pdf

[27] P. O. Piray Rodríguez, S. W. Parra Molina, J. E. Yaulema Colcha, and J. J. Salazar Briones, “Garantías jurídicas de la privacidad informativa en instituciones de educación superior del Ecuador contemporáneo,” *Universidad y Sociedad*, vol. 18, no. 2, p. e5877, 2026. [Online]. Available: https://rus.ucf.edu.cu/index.php/rus/article/view/5877

[28] J. A. Álvarez-Carrión and G. P. Hernández-Sotomayor, “Protección de datos personales en plataformas educativas digitales en el sistema de educación superior de Ecuador,” *MQRInvestigar*, vol. 8, no. 3, pp. 5324–5339, 2024.

[29] F. López-Vasco, M. Angulo-Alvarez, D. I. Sosa Zuñiga, E. Puente Moromenacho, N. Ortiz *et al.*, “Application of ISO/IEC 27,001 in higher education technological institutes: Case-control study,” in *Developments and Advances in Defense and Security (MICRADS 2024)*, ser. Smart Innovation, Systems and Technologies, vol. 423. 1em plus 0.5em minus 0.4em Singapore: Springer, 2025, pp. 179–189.

[30] Congreso Nacional del Ecuador, “Ley de Creación de la Universidad Tecnológica Indoamérica (Ley N.º 112),” Registro Oficial N.º 373, 31 de julio de 1998, Quito, Ecuador, 1998. [Online]. Available: https://www.indoamerica.edu.ec/wp-content/uploads/2023/02/leydecreaciondelauti.pdf

[31] M. Deng, K. Wuyts, R. Scandariato, B. Preneel, and W. Joosen, “A privacy threat analysis framework: supporting the elicitation and fulfillment of privacy requirements,” *Requirements Engineering*, vol. 16, no. 1, pp. 3–32, 2011.

[32] F. Bieker, M. Friedewald, M. Hansen, H. Obersteller, and M. Rost, “A process for data protection impact assessment under the European General Data Protection Regulation,” in *Privacy Technologies and Policy (APF 2016)*, ser. Lecture Notes in Computer Science, vol. 9857. 1em plus 0.5em minus 0.4em Cham: Springer, 2016, pp. 21–37.

[33] K. Vemou and M. Karyda, “Evaluating privacy impact assessment methods: guidelines and best practice,” *Information and Computer Security*, vol. 28, no. 1, pp. 35–53, 2020.

[34] S. Wairimu, L. H. Iwaya, L. Fritsch, and S. Lindskog, “On the evaluation of privacy impact assessment and privacy risk assessment methodologies: A systematic literature review,” *IEEE Access*, vol. 12, pp. 19 625–19 650, Feb. 2024.

[35] L. H. Iwaya, A. S. Alaqra, M. Hansen, and S. Fischer-H\"ubner, “Privacy impact assessments in the wild: A scoping review,” *Array*, vol. 23, p. 100356, Sep. 2024.

[36] S. Wairimu, L. H. Iwaya, L. Fritsch, and S. Lindskog, “Understanding practitioner perspectives on using privacy harm categories for privacy risk assessment,” *Journal of Information Security and Applications*, vol. 93, p. 104174, Sep. 2025.

[37] J. Wang, M. Neil, and N. Fenton, “A bayesian network approach for cybersecurity risk assessment implementing and extending the FAIR model,” *Computers & Security*, vol. 89, p. 101659, Feb. 2020.

[38] S. Patiño, E. F. Solís, S. G. Yoo, and R. Arroyo, “ICT risk management methodology proposal for governmental entities based on ISO/IEC 27005,” in *2018 International Conference on eDemocracy & eGovernment (ICEDEG)*. 1em plus 0.5em minus 0.4em Ambato, Ecuador: IEEE, 2018, pp. 75–82.

[39] M. E. Gursoy, A. Inan, M. E. Nergiz, and Y. Saygin, “Privacy-preserving learning analytics: Challenges and techniques,” *IEEE Transactions on Learning Technologies*, vol. 10, no. 1, pp. 68–81, 2017.

[40] A. Habbabeh, B. Schneider, and P. M. Asprion, “Data privacy assessment: An exemplary case for higher education institutions,” *International Journal of Management, Knowledge and Learning*, vol. 8, no. 2, pp. 221–241, 2019. [Online]. Available: https://www.issbs.si/press/ISSN/2232-5697/8_221-241.pdf

[41] E. Vanezi, D. Kouzapas, G. M. Kapitsaki, T. Costi, A. Yeratziotis, C. Mettouris, A. Philippou, and G. A. Papadopoulos, “GDPR compliance in the design of the INFORM e-learning platform: A case study,” in *2019 13th International Conference on Research Challenges in Information Science (RCIS)*. 1em plus 0.5em minus 0.4em Brussels, Belgium: IEEE, May 2019, pp. 1–12.

[42] Y.-S. Tsai, A. Whitelock-Wainwright, and D. Ga\'c, “The privacy paradox and its implications for learning analytics,” in *Proceedings of the 10th International Conference on Learning Analytics & Knowledge (LAK '20)*. 1em plus 0.5em minus 0.4em Frankfurt, Germany: ACM, Mar. 2020, pp. 230–239.

[43] K. Maguraushe, A. Da Veiga, and N. Martins, “Assessing information privacy awareness, expectations, and confidence of students: Evidence from a diagnostic survey in a developing country's higher education sector,” *Journal of Cybersecurity and Privacy*, vol. 6, no. 2, p. 62, Apr. 2026.

[44] C. Guerrero Argote, “Impacto en la privacidad a partir del uso de tecnologías de e-proctoring en la región de Latinoamérica: estudio del caso en universidades de Argentina, Chile y Perú,” *Revista Latinoamericana de Economía y Sociedad Digital*, no. 2, 2021.

[45] *Information technology – Security techniques – Guidelines for privacy impact assessment*, International Organization for Standardization Std. ISO/IEC 29134:2023, May 2023. [Online]. Available: https://www.iso.org/standard/86012.html

[46] Agencia Española de Protección de Datos, “Gestión del riesgo y evaluación de impacto en tratamientos de datos personales,” Guía, Madrid, Jun. 2021. [Online]. Available: https://www.aepd.es/guias/gestion-riesgo-y-evaluacion-impacto-en-tratamientos-datos-personales.pdf

[47] K. R. Boeckl and N. B. Lefkovitz, “NIST privacy framework: A tool for improving privacy through enterprise risk management, version 1.0,” National Institute of Standards and Technology, Gaithersburg, MD, Cybersecurity White Paper CSWP 01162020, Jan. 2020.

[48] European Union Agency for Network and Information Security, “Recommendations for a methodology of the assessment of severity of personal data breaches,” ENISA, Working document v1.0, Dec. 2013. [Online]. Available: https://www.enisa.europa.eu/publications/dbn-severity

[49] Superintendencia de Industria y Comercio, “La SIC presenta una guía para fortalecer la protección de los datos personales en las Instituciones de Educación Superior,” Comunicado de prensa, Bogotá, Colombia, Aug. 2026. [Online]. Available: https://sedeelectronica.sic.gov.co/comunicado/la-sic-presenta-una-guia-para-fortalecer-la-proteccion-de-los-datos-personales-en-las-instituciones-de-educacion-superior

[50] *Information security, cybersecurity and privacy protection – Guidance on managing information security risks*, International Organization for Standardization Std. ISO/IEC 27005:2022, Oct. 2022. [Online]. Available: https://www.iso.org/standard/80585.html

[51] Asamblea Constituyente, “Constitución de la República del Ecuador,” Registro Oficial N.º 449, 20 de octubre de 2008, Montecristi, Ecuador, 2008. [Online]. Available: https://www.gob.ec/regulaciones/constitucion-republica-ecuador

[52] Consejo de Participación Ciudadana y Control Social, “El CPCCS designa a Fabrizio Peralta Díaz como superintendente de Protección de Datos Personales,” Boletín institucional, 28 de marzo de 2024, Quito, Ecuador, 2024. [Online]. Available: https://www.cpccs.gob.ec/2024/03/fabrizio-peralta-superintendente

[53] Superintendencia de Protección de Datos Personales, “Norma Técnica de Notificación de Vulneraciones de Seguridad de los Datos Personales,” Resolución N.º SPDP-SPD-2026-0040-R, 9 de septiembre de 2026. Registro Oficial Primer Suplemento N.º 376, 24 de septiembre de 2026, Quito, Ecuador, 2026. [Online]. Available: https://www.lexis.com.ec/noticias/registro-oficial-del-dia-spdp-expide-norma-tecnica-de-notificacion-de-vulneraciones-de-datos

[54] Parlamento Europeo y Consejo de la Unión Europea, “Reglamento (UE) 2016/679 relativo a la protección de las personas físicas en lo que respecta al tratamiento de datos personales y a la libre circulación de estos datos (Reglamento General de Protección de Datos),” Diario Oficial de la Unión Europea, L 119, 4 de mayo de 2016, pp. 1–88, 2016. [Online]. Available: https://eur-lex.europa.eu/eli/reg/2016/679/oj

[55] Cortes Generales de España, “Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales,” Boletín Oficial del Estado, n.º 294, 6 de diciembre de 2018, 2018. [Online]. Available: https://www.boe.es/eli/es/lo/2018/12/05/3/con

[56] Congreso de la República de Colombia, “Ley Estatutaria 1581 de 2012, por la cual se dictan disposiciones generales para la protección de datos personales,” 17 de octubre de 2012, Bogotá, Colombia, 2012. [Online]. Available: https://leyonline.co/laws/ley-1581-de-2012

[57] Presidencia de la República de Colombia, “Decreto 1377 de 2013, por el cual se reglamenta parcialmente la Ley 1581 de 2012,” Compilado en el Decreto 1074 de 2015, art. 2.2.2.25.4.4, Bogotá, Colombia, 2013. [Online]. Available: https://normativa.colpensiones.gov.co/colpensiones/compilacion/docs/decreto_1377_2013.htm

[58] Superintendencia de Industria y Comercio, “Guía para la gestión de incidentes de seguridad en el tratamiento de datos personales,” Bogotá, Colombia, 2020. [Online]. Available: https://www.sic.gov.co/sites/default/files/files/Publicaciones/Guia_gestion_incidentes_dic21_2020.pdf

[59] Congreso de la República del Perú, “Ley N.º 29733, Ley de Protección de Datos Personales,” Diario Oficial El Peruano, 3 de julio de 2011, Lima, Perú, 2011.

[60] Ministerio de Justicia y Derechos Humanos del Perú, “Decreto Supremo N.º 016-2024-JUS, Reglamento de la Ley N.º 29733, Ley de Protección de Datos Personales,” Diario Oficial El Peruano, 30 de noviembre de 2024, Lima, Perú, 2024. [Online]. Available: https://lpderecho.pe/reglamento-ley-proteccion-datos-personales-decreto-supremo-016-2024-jus/

[61] Congreso Nacional de Chile, “Ley N.º 21.719, que regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales,” Diario Oficial, 13 de diciembre de 2024, Santiago, Chile, 2024. [Online]. Available: https://www.diariooficial.interior.gob.cl/publicaciones/2024/12/13/44023/01/2583630.pdf

[62] Presidência da República do Brasil, “Lei N.º 13.709, de 14 de agosto de 2018, Lei Geral de Proteção de Dados Pessoais (LGPD),” Diário Oficial da União, 15 de agosto de 2018, Brasília, Brasil, 2018. [Online]. Available: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm

[63] Autoridade Nacional de Proteção de Dados, “Resolução CD/ANPD N.º 15, de 24 de abril de 2024, Regulamento de Comunicação de Incidente de Segurança,” Brasília, Brasil, 2024. [Online]. Available: https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-aprova-o-regulamento-de-comunicacao-de-incidente-de-seguranca

[64] –––, “Resolução CD/ANPD N.º 2, de 27 de janeiro de 2022, Regulamento de aplicação da LGPD para agentes de tratamento de pequeno porte,” Brasília, Brasil, 2022. [Online]. Available: https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022

[65] *Risk management – Guidelines*, International Organization for Standardization Std. ISO 31000:2018, 2018. [Online]. Available: https://www.iso.org/standard/65694.html

[66] *Information security, cybersecurity and privacy protection – Privacy information management systems – Requirements and guidance*, International Organization for Standardization Std. ISO/IEC 27701:2025, Oct. 2025. [Online]. Available: https://www.iso.org/standard/27701
