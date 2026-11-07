<!-- Generado automáticamente desde Capítulos/01_Introducción.tex con scripts/tex2md_cap1.js.
     El .tex es la fuente vigente; para actualizar este borrador, compilar main.tex y volver a ejecutar el script. -->

# CAPÍTULO I. INTRODUCCIÓN

El presente trabajo de integración curricular aborda el tema *Diagnóstico y gestión de riesgos en el tratamiento de datos personales de estudiantes universitarios en Ecuador conforme a la LOPDP*. Su objeto son los datos personales que las universidades y escuelas politécnicas ecuatorianas recogen de sus estudiantes, examinados desde dos fuentes legítimas y accesibles: la información que las propias universidades publican y la percepción de los estudiantes como titulares de esos datos.

La tesis que sostiene este trabajo es que el cumplimiento de la Ley Orgánica de Protección de Datos Personales (LOPDP) en las universidades no puede presumirse a partir de la existencia de la ley ni medirse solo con lo que cada institución declara, sino que debe verificarse contrastando tres planos: lo que la norma exige, lo que las universidades publican y lo que los estudiantes efectivamente perciben; y que la distancia entre esos planos es la evidencia sobre la que debe construirse una gestión de riesgos centrada en el titular. Para sostener esta afirmación, el capítulo expone primero la exposición del sector con cifras y fecha de corte, formula después el problema y su justificación, y concluye con los objetivos, el alcance y las limitaciones del estudio.

## 1.1 Contextualización

### 1.1.1 Contexto macro: la exposición del sector educativo a nivel mundial

La educación superior se ha consolidado como uno de los sectores con mayor exposición a incidentes que comprometen datos personales. La edición 2024 del estudio *The State of Ransomware in Education*, basada en una encuesta a 5 000 responsables de tecnología de 14 países, de los cuales 600 pertenecían a organizaciones educativas, reportó que el 66 % de las IES había sufrido un ataque de *ransomware* en el último año, que el 77 % de esos ataques terminó con el cifrado de datos y que el costo medio de recuperación en el subsector alcanzó 4,02 millones de dólares [1]. Estas cifras ubican a las universidades por encima del promedio intersectorial y muestran que el problema no se limita a la disponibilidad de los sistemas, sino que afecta de forma directa la confidencialidad de los registros de los estudiantes.

La literatura académica coincide en ese diagnóstico. La revisión de Ulven y Wangen [2] sintetizó los activos críticos, eventos de amenaza y vulnerabilidades frecuentes en la educación superior, concluyó en nueve riesgos estratégicos de ciberseguridad para el sector y advirtió que la investigación empírica sobre riesgos en este ámbito es escasa. Li et al. [3], con una muestra de universidades chinas, encontraron que la divulgación pública de vulnerabilidades incrementa la frecuencia de brechas, mientras que la adopción de servicios en la nube la reduce; es decir, la exposición depende de decisiones de gestión y no solo de controles técnicos puntuales.

El riesgo, además, no es solo técnico. Liu y Khalil [4] identificaron ocho problemas interrelacionados de privacidad a lo largo del ciclo de vida de los datos de la analítica del aprendizaje, y Brown y Klein [5], tras analizar los documentos de políticas de privacidad de universidades estadounidenses, identificaron discursos recurrentes en los que el interés educativo legítimo que justifica el uso de los datos lo define la propia institución y se aplica de forma amplia, y en los que la protección de la privacidad se hace depender tanto de la responsabilidad institucional como de la iniciativa del estudiante. Desde la perspectiva de los propios estudiantes, Ifenthaler y Schumacher [6] examinaron la disposición de los estudiantes a compartir sus datos con sistemas de analítica del aprendizaje y concluyeron que deben participar en las decisiones sobre su implementación, y Maguraushe et al. [7] propusieron y validaron un modelo de percepción de la privacidad de los estudiantes universitarios basado en su conciencia, sus expectativas y su confianza en las prácticas de la institución. La transparencia hacia el titular es, por tanto, una dimensión del riesgo tan relevante como la seguridad de los sistemas.

### 1.1.2 Contexto meso: América Latina y Ecuador

En América Latina, los incidentes en universidades han pasado de ser casos aislados a eventos con consecuencias públicas visibles. En marzo de 2023, la Universidad Nacional de Colombia sufrió un ataque de *ransomware* que cifró parte de su información y obligó a aislar sus sistemas financiero, académico y de talento humano [8]. En octubre de 2024, la Universidad Técnica Federico Santa María, en Chile, registró un incidente tras el cual se publicaron alrededor de 14 GB de información que incluía listados de estudiantes con su número de identificación, carrera y año de ingreso [9]. En Brasil, una encuesta aplicada entre agosto y septiembre de 2024 a 125 participantes de contextos educativos —108 estudiantes y 17 docentes— encontró incertidumbre sobre las prácticas de consentimiento, dificultad para acceder a las políticas de privacidad y desconocimiento de los derechos de los titulares [10].

Ecuador cuenta con un antecedente nacional que evidenció la magnitud del problema antes de la existencia de una ley específica. En septiembre de 2019 se reportó la exposición de una base de datos de una empresa privada que contenía información de alrededor de 20 millones de personas, incluidos cerca de 6,7 millones de niños, con campos como nombres, fecha de nacimiento, domicilio, teléfonos y nivel de educación [11]. Ese caso aceleró el debate legislativo que culminó con la LOPDP, publicada en el Quinto Suplemento del Registro Oficial N.º 459 el 26 de mayo de 2021 [12]; su reglamento general fue expedido mediante el Decreto Ejecutivo N.º 904 y publicado en el Tercer Suplemento del Registro Oficial N.º 435 el 13 de noviembre de 2023 [13].

La LOPDP establece obligaciones que pueden verificarse desde fuera de la institución y otras que solo pueden verificarse desde dentro. Entre las primeras está el derecho del titular a ser informado, de forma previa a la recogida, sobre los fines, la base legal, el tiempo de conservación, la identidad y el contacto del responsable, las transferencias, la forma de ejercer sus derechos y dónde reclamar [12, art. 12], así como el consentimiento libre, específico, informado e inequívoco cuando este es la base del tratamiento [12, art. 8]. Entre las segundas están el análisis de riesgos, amenazas y vulnerabilidades [12, art. 40] y la obligación del responsable de utilizar metodologías de análisis y gestión de riesgos adaptadas al tratamiento [12, art. 47, num. 5], cuya omisión es infracción grave [12, art. 68]. Esta distinción es decisiva para el diseño del estudio: sin acceso a la información interna de las universidades, lo que puede medirse con rigor es la transparencia hacia el titular y la percepción del titular, y lo que puede proponerse es la gestión de riesgos que esa evidencia vuelve necesaria.

La Superintendencia de Protección de Datos Personales (SPDP) comenzó a emitir normativa técnica entre 2025 y 2026: la *Guía de Gestión de Riesgos y Evaluación de Impacto del Tratamiento de Datos Personales* (Resolución N.º SPDP-SPD-2025-0003-R, publicada el 19 de mayo de 2025), cuyo capítulo I es de cumplimiento obligatorio [14], [15]; su segunda versión (Resolución N.º SPDP-SPD-2026-0012-R, publicada el 30 de marzo de 2026) [16], y el Modelo Técnico de Gran Escala (Resolución N.º SPDP-SPD-2026-0005-R, publicada el 25 de febrero de 2026), que califica directamente como de gran escala los tratamientos de salud y otras categorías especiales y el tratamiento sistemático de datos de niñas, niños y adolescentes en entornos educativos, con la consiguiente obligación de evaluación de impacto y de designar un delegado [17, arts. 12 y 14].

La autoridad ya ejerce su potestad sancionadora. El 1 de diciembre de 2025 se dieron a conocer las primeras sanciones por infracciones graves, impuestas a la Liga Profesional de Fútbol del Ecuador y a la Federación Ecuatoriana de Fútbol por un total cercano a 454 500 dólares [18], [19]; hasta septiembre de 2025, la SPDP había recibido 191 denuncias [20]. En las fuentes públicas consultadas no se identificó, al 7 de noviembre de 2026, un procedimiento sancionador contra una universidad, de modo que para estas instituciones el riesgo jurídico existe, pero aún no se ha materializado.

### 1.1.3 El sector educativo ecuatoriano en cifras

La magnitud del problema se aprecia mejor con cifras. Todos los valores de esta sección se tomaron de fuentes oficiales o, cuando estas no publican el dato, de publicaciones que citan expresamente a la fuente oficial, y cada uno se acompaña de su fecha de corte; los datos que no se hallaron publicados se declaran como no disponibles en lugar de estimarse. La Tabla 1 reúne el universo de instituciones educativas y de estudiantes cuyos datos se tratan en los términos de la LOPDP.

**Tabla 1**
*Instituciones y estudiantes del sistema educativo ecuatoriano.*

| **Nivel** | **Cifra** | **Fecha de corte** | **Fuente** |
| --- | --- | --- | --- |
| Educación inicial, básica y bachillerato (todos los sostenimientos) | 16 161 instituciones; 4 370 420 estudiantes; 209 471 docentes | Ciclo 2024–2025 | Ministerio de Educación, citado en [21] |
| Ídem, por sostenimiento | 12 389 fiscales; 617 fiscomisionales; 112 municipales; 3 022 particulares (total: 16 140) | Estadística Educativa, vol. 5 (octubre de 2024) | [22] |
| Centros de desarrollo infantil (CDI) en convenio con GAD y organizaciones sociales | 1 861 centros | Levantamiento de 2024, informe de noviembre de 2025 | [23] |
| Universidades y escuelas politécnicas | 64 (36 públicas, 20 particulares autofinanciadas, 8 particulares cofinanciadas) | Consultas del 27 de octubre y del 7 de noviembre de 2026 (el portal no indica fecha de corte) | [24] |
| Estudiantes matriculados en universidades y escuelas politécnicas | 841 404 (el 36 % en universidades particulares) | Año 2023 | SIIES-SENESCYT, citado en [25]; base oficial en [26] |
| Institutos técnicos, tecnológicos, pedagógicos, de artes y conservatorios superiores | 216 (62 públicos, 154 particulares) | Consulta del 27 de octubre de 2026 | [24] |

*Elaborado por:* Ramón Alejandro Manzaba Castro. *Fuente:* Elaboración propia a partir de [21], [22], [23], [24], [25].

Todas estas instituciones están obligadas a proteger los datos personales que tratan, y no por analogía, sino por el texto de la ley. La LOPDP se aplica al tratamiento de datos personales contenidos en cualquier tipo de soporte [12, art. 2] y define como responsable a la persona natural o jurídica, pública o privada, que decide sobre la finalidad y el tratamiento [12, art. 4]; toda universidad que matricula estudiantes, registra calificaciones o administra un aula virtual cumple esa definición. La ley añade deberes específicos para el sector: el sistema educativo, incluida la educación superior, debe garantizar la educación digital de estudiantes y docentes [12, art. 23]; las entidades educativas deben proveer información y capacitación sobre el tratamiento de datos [12, art. 24], y las universidades públicas, por pertenecer al sector público, deben designar un delegado de protección de datos [12, art. 48, num. 1]. La reforma de 2026 dispuso, además, que escuelas, colegios y universidades incorporen progresivamente contenidos de protección de datos personales en su oferta educativa [27, art. 8].

Frente a ese universo de obligados, las cifras sobre la capacidad de cumplimiento son escasas. En abril de 2025 se informaba que más de 1 150 delegados de protección de datos estaban registrados ante la SPDP, sumando todos los sectores de la economía [28]; aun si todos trabajaran en educación, cubrirían como máximo el 7,0 % de las 16 441 instituciones educativas y de educación superior de la Tabla 1 (1 150 / 16 441), y no se halló una cifra oficial posterior publicada al 7 de noviembre de 2026. La SPDP había recibido 85 denuncias en abril de 2025 [28] y 191 en septiembre de 2025 [20]. Aunque la ley ordena a la autoridad llevar un registro estadístico de vulneraciones [12, art. 76, num. 14], no se halló una estadística pública de vulneraciones notificadas por el sector educativo. Tampoco existe un informe oficial que indique qué porcentaje de universidades ha implementado la LOPDP: el estudio nacional más reciente describe una adopción desigual de políticas, pero no la cuantifica [29], y en las publicaciones de la SPDP, del CES y del CACES consultadas no se encontró ese porcentaje.

En síntesis, las cifras dibujan una brecha medible y, a la vez, no medida: 64 universidades y escuelas politécnicas que tratan los datos de más de 840 000 estudiantes están obligadas por la ley, pero no existe una sola cifra oficial sobre cuántas informan a sus estudiantes como exige el artículo 12, cuántas han designado un delegado ni qué perciben los estudiantes sobre el tratamiento de sus datos. Esa ausencia de medición es, precisamente, el vacío que este trabajo se propone llenar con fuentes que cualquiera puede verificar.

### 1.1.4 Contexto micro: las universidades ecuatorianas y sus estudiantes como titulares

En el sistema de educación superior ecuatoriano, la evidencia disponible indica que la adecuación a la LOPDP es heterogénea. Álvarez-Carrión y Hernández-Sotomayor [30] concluyeron que, aunque la ley ofrece un marco sólido, su implementación en plataformas educativas enfrenta brechas de infraestructura y de capacitación, con fallos técnicos y error humano como causas principales de las vulneraciones documentadas en universidades del país. Piray Rodríguez et al. [29] encontraron diferencias marcadas entre instituciones en la adopción de políticas internas de protección de datos. Ninguno de estos estudios, sin embargo, mide de forma sistemática la información que cada universidad publica ni consulta a los estudiantes sobre su experiencia como titulares.

El estudiante universitario es un titular particular. Entrega datos de identificación, contacto, rendimiento académico y, con frecuencia, datos socioeconómicos, de salud o de discapacidad para acceder a becas, ayudas o adaptaciones; muchos ingresaron a la universidad siendo menores de edad, categoría especial en la ley [12, art. 25], y su relación con la institución es asimétrica, porque negarse a entregar un dato puede significar no acceder a un servicio. Por esa razón, este trabajo adopta como unidad de observación a las universidades, mediante su información pública, y a los estudiantes mayores de edad, mediante una encuesta anónima, sin recurrir a ningún dato interno de ninguna institución.

En síntesis, la evidencia de los tres niveles converge en una conclusión: la exposición del sector es alta, las obligaciones de transparencia y de gestión de riesgos son exigibles desde 2023 y la normativa técnica que las concreta es reciente, mientras que el grado de cumplimiento de las universidades ecuatorianas no ha sido medido. Medirlo con fuentes legítimas es el primer paso para gestionar el riesgo.

## 1.2 Planteamiento del Problema

Las universidades ecuatorianas tratan los datos personales de más de 840 000 estudiantes [25] sin que exista evidencia pública y verificable de que cumplen las obligaciones de transparencia, consentimiento y atención de derechos de la LOPDP, y sin que se conozca si sus estudiantes, como titulares, son informados, consienten libremente y conocen sus derechos. Esa falta de evidencia impide identificar los riesgos que el tratamiento genera para los titulares y, por tanto, gestionarlos como exigen los artículos 40 y 47 de la ley [12]. El problema afecta a las 64 universidades y escuelas politécnicas del país [24], en un contexto en el que los delegados registrados no superaban los 1 150 en abril de 2025 [28] y no existe una medición oficial del grado de implementación de la ley en las universidades (Sección 1.1.3).

### 1.2.1 Análisis crítico

El análisis del problema se estructuró mediante un árbol de problemas que relaciona sus causas con el problema central y con los efectos que produce. La Tabla 2 presenta esa relación y la Figura 1 la representa de forma gráfica.

**Tabla 2**
*Árbol de problemas: causas, problema central y efectos.*

| **Causas** | **Problema central** | **Efectos** |
| --- | --- | --- |
| C1. Ausencia de una medición oficial del cumplimiento de la LOPDP en las universidades. | **Las universidades tratan datos de sus estudiantes sin evidencia verificable de cumplimiento de la LOPDP y sin conocer la percepción de sus titulares, lo que impide identificar y gestionar los riesgos.** | E1. Exposición a sanciones por infracciones graves (arts. 68 y 72 de la LOPDP). |
| C2. Información al titular incompleta o de difícil acceso en los sitios institucionales. |  | E2. Titulares que no pueden ejercer sus derechos por desconocerlos o por falta de canales. |
| C3. Gestión de la seguridad centrada en activos tecnológicos y no en los derechos de los titulares. |  | E3. Riesgos para los titulares no identificados ni tratados; evaluaciones de impacto omitidas. |
| C4. Escasa cultura de protección de datos en estudiantes y personal. |  | E4. Incapacidad de notificar vulneraciones dentro del término legal. |
| C5. Normativa técnica de la SPDP reciente y uso creciente de plataformas de terceros. |  | E5. Pérdida de confianza de los estudiantes y daño reputacional. |

*Elaborado por:* Ramón Alejandro Manzaba Castro. *Fuente:* Elaboración propia con base en [12], [29], [30], [5].

**Figura 1**
*Árbol de problemas.*

> Diagrama elaborado en TikZ; véase el PDF. Su contenido coincide con la tabla del árbol de problemas.

La primera causa es la ausencia de medición: ni la SPDP ni el CES ni el CACES publican un indicador del cumplimiento de la LOPDP en las universidades (Sección 1.1.3), y sin esa medición no es posible priorizar ni comparar. La segunda causa es de transparencia: el artículo 12 de la ley enumera diecisiete elementos de información que el titular tiene derecho a conocer [12, art. 12], y la literatura internacional muestra que las políticas universitarias suelen definir desde la institución, y de forma amplia, los usos legítimos de los datos de los estudiantes [5]. La tercera causa es de enfoque: los modelos aplicados en el sector, como los descritos por Patiño et al. [31] y López-Vasco et al. [32], valoran el riesgo sobre los activos de la organización. La cuarta causa, vinculada al factor humano, coincide con el peso del error humano en los incidentes de universidades ecuatorianas [30] y con el desconocimiento de derechos observado en estudiantes de la región [10]. La quinta causa responde a la velocidad del cambio normativo entre 2025 y 2026 y a la migración de servicios académicos hacia plataformas de terceros, en las que la universidad sigue siendo responsable.

Entre los efectos destaca la exposición legal: no informar al titular, no atender sus derechos o no utilizar metodologías de análisis y gestión de riesgos son conductas tipificadas, y para una universidad particular las infracciones graves se sancionan con multas de entre el 0,7 % y el 1 % de su volumen de negocio del ejercicio anterior [12, arts. 68 y 72]. A ello se suma que un titular que no conoce sus derechos no puede ejercerlos, y que una institución que no ha identificado sus riesgos difícilmente podrá notificar a tiempo una vulneración.

### 1.2.2 Prognosis

De no abordarse el problema, las universidades continuarían tratando datos de sus estudiantes sin saber si los informan y los respetan como exige la ley, y la autoridad, los propios estudiantes y la comunidad académica seguirían sin un referente para comparar instituciones o medir avances. La tendencia regional de ataques contra universidades [9], [8], [1] y la actividad sancionadora de la SPDP [18] permiten prever que las consecuencias de esa falta de evidencia serán cada vez más tangibles, mientras que las universidades seguirían aplicando criterios propios y no comparables para gestionar sus riesgos.

### 1.2.3 Formulación del problema

¿En qué medida las universidades ecuatorianas cumplen, en lo que publican y en lo que perciben sus estudiantes, las obligaciones de la LOPDP sobre el tratamiento de datos personales de estudiantes, y qué lineamientos de gestión de riesgos se derivan de las brechas encontradas?

### 1.2.4 Preguntas directrices

La investigación se orienta mediante cuatro preguntas directrices, cada una vinculada a un objetivo específico (OE). ¿Qué requisitos de la LOPDP y de su Reglamento son aplicables al tratamiento de datos de estudiantes y cómo se traducen en indicadores verificables desde fuera de la institución? (OE1). ¿Qué información sobre protección de datos publican las universidades ecuatorianas y con qué grado de completitud respecto de esos indicadores? (OE2). ¿Qué datos declaran los estudiantes que les fueron solicitados, qué información recibieron, cómo consintieron y qué conocen de sus derechos? (OE3). ¿Cuál es la brecha entre la norma, lo publicado y lo percibido, y qué guía de gestión de riesgos, validada por expertos, permite atenderla? (OE4).

### 1.2.5 Delimitación

En cuanto al contenido, el estudio pertenece al campo de las tecnologías de la información, en el área de gobernanza y seguridad de la información, y se centra en el tratamiento de datos personales de estudiantes universitarios conforme a la LOPDP, su reglamento y la normativa técnica de la SPDP. En lo espacial, abarca las universidades y escuelas politécnicas del Ecuador registradas en el CES y a estudiantes mayores de edad matriculados en ellas. En lo temporal, el levantamiento se ejecuta entre noviembre de 2026 y febrero de 2027, y se considera la normativa vigente hasta la fecha de cierre del trabajo.

El planteamiento permite concluir que el problema no es la falta de normas, sino la falta de evidencia sobre su cumplimiento: sin saber qué publican las universidades ni qué perciben sus estudiantes, cualquier gestión de riesgos se apoyaría en supuestos. Por ello, la pregunta de investigación combina un diagnóstico verificable con una propuesta derivada de él.

## 1.3 Justificación

La importancia del trabajo radica en que la transparencia hacia el titular y la gestión de riesgos han dejado de ser buenas prácticas opcionales para convertirse en obligaciones jurídicas exigibles desde mayo de 2023. La LOPDP reconoce al titular el derecho a ser informado sobre diecisiete aspectos del tratamiento [12, art. 12], exige consentimiento libre, específico, informado e inequívoco cuando este es la base del tratamiento [12, art. 8] y obliga al responsable a utilizar metodologías de análisis y gestión de riesgos [12, art. 47, num. 5]. La necesidad es cuantificable: 64 universidades y escuelas politécnicas [24] tratan los datos de 841 404 estudiantes matriculados en 2023 [25], y no existe una medición oficial de su cumplimiento. Para una universidad particular, una infracción grave se sanciona con una multa de entre el 0,7 % y el 1 % de su volumen de negocio [12, art. 72], y las dos primeras multas impuestas por la SPDP sumaron cerca de 454 500 dólares [18].

La novedad del aporte reside en la combinación de dos fuentes que la literatura aborda por separado. Los estudios nacionales describen el marco normativo o la adopción de políticas de forma cualitativa [30], [29]; los internacionales analizan las políticas universitarias [5] o la percepción de los estudiantes [6], [7], [10], pero no ambas a la vez. Este trabajo mide con un mismo conjunto de indicadores, derivados artículo por artículo de la LOPDP, lo que las universidades publican y lo que los estudiantes perciben, y convierte la brecha resultante en escenarios de riesgo y en una guía de gestión.

La utilidad del proyecto se expresa en sus productos: una ficha de verificación documental y un cuestionario validados y reutilizables; una línea base pública del cumplimiento de las universidades ecuatorianas, con fecha de corte; y una guía de gestión de riesgos con su plantilla de matriz en hoja de cálculo, que cualquier universidad podrá aplicar a sus propios tratamientos. La factibilidad es técnica, operativa y económica: el estudio se apoya en información de acceso público, en una encuesta anónima difundida por canales propios del autor y en herramientas ofimáticas de uso común, sin requerir autorizaciones de acceso a datos internos.

Los beneficiarios directos son los estudiantes, cuyos derechos se hacen visibles cuando se mide si se respetan, y las universidades, que dispondrán de un referente comparativo y de una guía aplicable; los beneficiarios indirectos son la autoridad de control y la comunidad académica, que contarán con una primera línea base sectorial. El trabajo se inscribe en la línea de investigación Gestión de la Información, sublínea Gobernanza y seguridad de la información, y en el eje Tecnologías para la educación, y contribuye a las competencias del perfil de egreso PE-CP-06 (evaluar proyectos de TI en concordancia con el marco legal vigente), PE-MI-04 (gestionar proyectos de TI aplicando conceptos éticos y legales), PE-IS-04 (realizar proyectos de investigación siguiendo una metodología científica) y PE-PP-05 (implementar sistemas de seguridad informática bajo políticas organizacionales y estándares aceptados).

Podría objetarse que un estudio sin acceso a la información interna de las universidades no puede pronunciarse sobre su cumplimiento. La objeción es válida solo en parte, y por eso el alcance se declara con precisión: el trabajo no audita los sistemas ni los registros internos de ninguna institución, sino las obligaciones que, por definición legal, deben ser visibles para el titular —la información del artículo 12, el consentimiento, los canales para ejercer derechos— y la experiencia del propio titular. Esas obligaciones no necesitan acceso interno para verificarse; al contrario, si el titular no puede verlas, no se están cumpliendo. En consecuencia, el diseño no es una alternativa debilitada a un estudio con acceso interno, sino la forma legítima de medir la dimensión de la ley que mira hacia el titular.

## 1.4 Objetivos
### 1.4.1 Objetivo General

Diagnosticar el cumplimiento de la Ley Orgánica de Protección de Datos Personales (2021) y de su Reglamento General (2023) en el tratamiento de datos personales de estudiantes por parte de las universidades ecuatorianas, mediante el análisis documental de su información pública y una encuesta anónima a estudiantes, para proponer una guía de gestión de riesgos validada por expertos.

### 1.4.2 Objetivos Específicos

1. Determinar los requisitos de la LOPDP (2021) y de su Reglamento General (2023) aplicables a las universidades en el tratamiento de datos personales de estudiantes, mediante el análisis normativo artículo por artículo, para traducirlos en indicadores verificables que sirvan de base a la ficha de análisis documental y al cuestionario.

2. Analizar la información pública sobre protección de datos personales de las universidades y escuelas politécnicas ecuatorianas, mediante una ficha de verificación aplicada a sus sitios web y documentos oficiales con fecha de corte, para establecer su grado de transparencia respecto de los indicadores determinados.

3. Aplicar una encuesta anónima a estudiantes universitarios mayores de edad, mediante un cuestionario estructurado validado por juicio de expertos y prueba piloto, para conocer los datos que les fueron solicitados, la información que recibieron sobre su tratamiento, la forma en que consintieron y su conocimiento de los derechos que les reconoce la ley.

4. Evaluar el nivel de cumplimiento y la brecha entre la norma, la información publicada por las universidades y la percepción de los estudiantes, mediante el contraste de los indicadores de ambas fuentes, para proponer una guía de gestión de riesgos en el tratamiento de datos de estudiantes validada mediante el método Delphi y juicio de expertos.

Los cuatro objetivos guardan una secuencia lógica con el objetivo general: el primero fija qué debe medirse y con qué fundamento; el segundo mide lo que las universidades muestran; el tercero mide lo que los estudiantes perciben, y el cuarto contrasta ambos planos con la norma y convierte la brecha en una propuesta validada.

## 1.5 Alcance del Proyecto

El alcance comprende cuatro componentes, uno por objetivo específico: (1) la matriz de requisitos e indicadores derivada de la LOPDP y de su Reglamento; (2) el análisis documental censal de las universidades y escuelas politécnicas registradas en el CES, con evidencia (URL y fecha de consulta) por indicador; (3) la encuesta anónima a estudiantes, con su instrumento validado, su prueba piloto y su análisis estadístico descriptivo y de asociación, y (4) el índice de brecha entre la norma, lo publicado y lo percibido, junto con una guía de gestión de riesgos aplicada a escenarios construidos a partir de los hallazgos y validada por un panel de expertos.

El proyecto excluye de manera expresa cuatro aspectos. Primero, no utiliza ningún dato interno de ninguna universidad ni audita sus sistemas, registros o contratos. Segundo, no constituye una certificación ni una declaración de cumplimiento ante la autoridad. Tercero, no cubre la implementación de las medidas que proponga la guía, que corresponde a cada institución. Cuarto, no abarca una auditoría externa independiente; los resultados documentales describen lo que cada universidad publica en la fecha de consulta y no lo que hace internamente.

Entre las limitaciones se reconoce, primero, que la encuesta se difunde por canales propios del autor y emplea un muestreo no probabilístico, por lo que sus resultados describen a la muestra y no permiten generalizar con un margen de error conocido a todos los estudiantes del país. Segundo, la percepción del estudiante puede diferir de la práctica real de la institución: un estudiante puede no recordar un aviso que sí recibió. Esta limitación se convierte en dato, porque una información que el titular no percibe difícilmente cumple el principio de transparencia [12, art. 10, lit. c]. Tercero, los sitios web cambian, de modo que cada verificación documental se fecha y se conserva su evidencia. Cuarto, la normativa técnica de la SPDP está en evolución, por lo que el trabajo refleja la vigente a la fecha de cierre.

Delimitar de este modo el alcance no debilita el aporte, sino que lo hace verificable: el trabajo se compromete con lo que puede demostrar con fuentes públicas y con el testimonio anónimo de los titulares, y deja expresamente fuera lo que solo podría establecerse con acceso interno.

## Referencias del capítulo

Numeración IEEE idéntica a la del PDF (`main.pdf`).

[1] Sophos, “The state of ransomware in education 2024,” Sophos, Tech. Rep., 2024. [Online]. Available: https://www.sophos.com/en-us/blog/the-state-of-ransomware-in-education-2024

[2] J. B. Ulven and G. Wangen, “A systematic review of cybersecurity risks in higher education,” *Future Internet*, vol. 13, no. 2, p. 39, 2021.

[3] J. Li, W. Xiao, and C. Zhang, “Data security crisis in universities: identification of key factors affecting data breach incidents,” *Humanities and Social Sciences Communications*, vol. 10, p. 270, May 2023.

[4] Q. Liu and M. Khalil, “Understanding privacy and data protection issues in learning analytics using a systematic review,” *British Journal of Educational Technology*, vol. 54, no. 6, pp. 1715–1747, Nov. 2023.

[5] M. Brown and C. Klein, “Whose data? Which rights? Whose power? A policy discourse analysis of student privacy policy documents,” *The Journal of Higher Education*, vol. 91, no. 7, pp. 1149–1178, 2020.

[6] D. Ifenthaler and C. Schumacher, “Student perceptions of privacy principles for learning analytics,” *Educational Technology Research and Development*, vol. 64, no. 5, pp. 923–938, 2016.

[7] K. Maguraushe, A. da Veiga, and N. Martins, “A personal information privacy perceptions model for university students,” *Information Security Journal: A Global Perspective*, vol. 33, no. 4, pp. 394–424, 2024.

[8] Semana, “Los detalles secretos del grave hackeo que sufrió la Universidad Nacional,” Apr. 2023. [Online]. Available: https://www.semana.com/nacion/articulo/asi-fue-el-hackeo-del-que-fue-victima-la-universidad-nacional/202335/

[9] CNN Chile, “Hackeo a la Universidad Santa María: datos de estudiantes y académicos fueron vulnerados y publicados en la dark web,” Nov. 2024. [Online]. Available: https://www.cnnchile.com/pais/hackeo-universidad-santa-maria-datos-estudiantes-academicos-vulnerados-publicados-dark-web_20241116/

[10] Y. Correia de Barros and J. Vilela, “Data privacy in educational contexts: analyzing perceptions, practices and challenges in personal data protection,” in *Proceedings of the 27th International Conference on Enterprise Information Systems (ICEIS)*. 1em plus 0.5em minus 0.4em SCITEPRESS, 2025, pp. 308–319.

[11] Y. Arciniegas, “Falla informática en Ecuador: los datos de casi toda la población quedaron expuestos,” France 24, Sep. 2019. [Online]. Available: https://www.france24.com/es/20190917-ecuador-datos-expuestos-informacion-filtracion

[12] Asamblea Nacional del Ecuador, “Ley Orgánica de Protección de Datos Personales,” Registro Oficial Quinto Suplemento N.º 459, Quito, Ecuador, May 2021.

[13] Presidencia de la República del Ecuador, “Reglamento General a la Ley Orgánica de Protección de Datos Personales (Decreto Ejecutivo N.º 904),” Registro Oficial Tercer Suplemento N.º 435, Quito, Ecuador, Nov. 2023.

[14] Superintendencia de Protección de Datos Personales, “Guía de Gestión de Riesgos y Evaluación de Impacto del Tratamiento de Datos Personales,” Resolución N.º SPDP-SPD-2025-0003-R, 29 de abril de 2025. Registro Oficial Cuarto Suplemento N.º 41, 19 de mayo de 2025, Quito, Ecuador, 2025. [Online]. Available: https://spdp.gob.ec/wp-content/uploads/2025/05/03.01.01-SPDP-SPD-2025-0003-R-Guia-Gest-de-Riesg-y-Ev-Imp-signed.pdf

[15] Lexis, “Registro Oficial del día: Superintendencia expide guía para gestión de riesgos y evaluación de impacto en tratamiento de datos personales,” 2025. [Online]. Available: https://www.lexis.com.ec/noticias/registro-oficial-del-dia-superintendencia-expide-guia-para-gestion-de-riesgos-y-evaluacion-de-impacto-en-tratamiento-de-datos-personales

[16] Superintendencia de Protección de Datos Personales, “Guía de Gestión de Riesgos y Evaluación de Impacto del Tratamiento de Datos Personales, Versión 2,” Resolución N.º SPDP-SPD-2026-0012-R. Registro Oficial Suplemento N.º 254, 30 de marzo de 2026, Quito, Ecuador, 2026. [Online]. Available: https://spdp.gob.ec/wp-content/uploads/2026/03/ggrispdp2026v2.pdf

[17] –––, “Norma General sobre el Tratamiento de Datos Personales a Gran Escala,” Resolución N.º SPDP-SPD-2026-0005-R, Registro Oficial Suplemento N.º 231, 25 de febrero de 2026, Quito, Ecuador, 2026.

[18] R. Revelo, “Superintendencia de datos sanciona a LigaPro y FEF por infracciones en el tratamiento de datos personales,” Primicias, Dec. 2025. [Online]. Available: https://www.primicias.ec/deportes/futbol/superintendencia-datos-sanciona-ligapro-fef-infracciones-tratamiento-datos-personales-110763/

[19] ECIJA GPA, “Primeras sanciones por vulneración de datos en Ecuador,” Dec. 2025. [Online]. Available: https://www.ecija.com/actualidad-insights/primeras-sanciones-por-vulneracion-de-datos-en-ecuador/

[20] M. Almeida and P. Mena Mena, “Cero sanciones en Ecuador por una ley de protección de datos personales blandengue,” Primicias, Sep. 2025. [Online]. Available: https://www.primicias.ec/politica/cero-sanciones-ecuador-ley-proteccion-datos-personales-blandengue-104527/

[21] El Diario, “En Ecuador hay más de 4 millones de estudiantes de educación básica y bachillerato, la mayoría asiste a instituciones públicas,” El Diario (Ecuador), con cifras del Ministerio de Educación, Sep. 2025. [Online]. Available: https://www.eldiario.ec/ecuador/en-ecuador-hay-mas-de-4-millones-de-estudiantes-de-educacion-basica-y-bachillerado-la-mayoria-asiste-a-instituciones-publicas-23092025/

[22] Ministerio de Educación del Ecuador, “Estadística educativa, volumen 5,” Ministerio de Educación, Quito, Ecuador, Tech. Rep., Oct. 2024. [Online]. Available: https://educacion.gob.ec/wp-content/uploads/downloads/2024/10/Estadistica-Educativa-Vol-5.pdf

[23] Consejo Nacional para la Igualdad Intergeneracional, “Informe de observancia a los centros de desarrollo infantil,” Consejo Nacional para la Igualdad Intergeneracional, Quito, Ecuador, Tech. Rep., Nov. 2025. [Online]. Available: https://www.igualdad.gob.ec/wp-content/uploads/downloads/2025/11/informe_observancia_serv_desarrollo_infantil.pdf

[24] Consejo de Educación Superior, “Estadísticas IES,” Portal institucional del CES, consultado el 27 de octubre y el 7 de noviembre de 2026, Quito, Ecuador, 2026. [Online]. Available: https://www.ces.gob.ec/?page_id=5248

[25] N. Sumba-Nacipucha and A. Sánchez-Bayón, “Economía conductual y la elección de universidades: factores que influyen en la decisión,” *KAIRÓS, Revista de Ciencias Económicas, Jurídicas y Administrativas*, vol. 8, no. 14, pp. 171–192, 2025.

[26] Secretaría de Educación Superior, Ciencia, Tecnología e Innovación, “Base estadística de matrícula de universidades y escuelas politécnicas 2015–2023,” Portal de Datos Abiertos del Ecuador, actualizado el 28 de abril de 2025, consultado el 7 de noviembre de 2026, 2025. [Online]. Available: https://www.datosabiertos.gob.ec/dataset/base-de-datos-de-matricula-de-uep-ano-2021

[27] Asamblea Nacional del Ecuador, “Ley Orgánica para el Fortalecimiento de la Ciberseguridad,” Registro Oficial Quinto Suplemento N.º 290, 22 de mayo de 2026, Quito, Ecuador, 2026. [Online]. Available: https://www.asambleanacional.gob.ec/es/system/files/ro_29.pdf

[28] IT Ahora, “Avances y acción de la Superintendencia de Protección de Datos Personales,” IT Ahora, Apr. 2025. [Online]. Available: https://itahora.com/2025/04/16/avances-y-accion-de-la-superintendencia-de-proteccion-de-datos-personales/

[29] P. O. Piray Rodríguez, S. W. Parra Molina, J. E. Yaulema Colcha, and J. J. Salazar Briones, “Garantías jurídicas de la privacidad informativa en instituciones de educación superior del Ecuador contemporáneo,” *Universidad y Sociedad*, vol. 18, no. 2, p. e5877, 2026. [Online]. Available: https://rus.ucf.edu.cu/index.php/rus/article/view/5877

[30] J. A. Álvarez-Carrión and G. P. Hernández-Sotomayor, “Protección de datos personales en plataformas educativas digitales en el sistema de educación superior de Ecuador,” *MQRInvestigar*, vol. 8, no. 3, pp. 5324–5339, 2024.

[31] S. Patiño, E. F. Solís, S. G. Yoo, and R. Arroyo, “ICT risk management methodology proposal for governmental entities based on ISO/IEC 27005,” in *2018 International Conference on eDemocracy & eGovernment (ICEDEG)*. 1em plus 0.5em minus 0.4em Ambato, Ecuador: IEEE, 2018, pp. 75–82.

[32] F. López-Vasco, M. Angulo-Alvarez, D. I. Sosa Zuñiga, E. Puente Moromenacho, N. Ortiz *et al.*, “Application of ISO/IEC 27,001 in higher education technological institutes: Case-control study,” in *Developments and Advances in Defense and Security (MICRADS 2024)*, ser. Smart Innovation, Systems and Technologies, vol. 423. 1em plus 0.5em minus 0.4em Singapore: Springer, 2025, pp. 179–189.
