<!-- Generado automáticamente desde Capítulos/01_Introducción.tex con scripts/tex2md_cap1.js.
     El .tex es la fuente vigente; para actualizar este borrador, compilar main.tex y volver a ejecutar el script. -->

# CAPÍTULO I. INTRODUCCIÓN

El presente Trabajo de Integración Curricular aborda el tema *Metodología para el diagnóstico y gestión de riesgos en el tratamiento de datos personales académicos conforme a la LOPDP*. Su producto es una metodología de diagnóstico y gestión de riesgos para el tratamiento de los datos personales que las universidades y escuelas politécnicas recogen de sus estudiantes, aplicable por cualquier universidad del país, construida conforme a la Ley Orgánica de Protección de Datos Personales (LOPDP) a partir de un análisis comparado de los marcos jurídicos de la Unión Europea, Estados Unidos, Brasil, Colombia y Chile, y validada por un panel de expertos. El estudio es documental y no se centra en ninguna institución.

La tesis que sostiene este trabajo es que las universidades ecuatorianas necesitan una metodología específica para gestionar los riesgos de los datos de sus estudiantes, porque la LOPDP es reciente y su normativa técnica es general, y que esa metodología no tiene por qué improvisarse: otros marcos jurídicos ya han resuelto el mismo problema con guías, herramientas y experiencia de aplicación, y compararlos por la función que cumplen permite identificar qué elementos son mínimos, cuáles son opcionales y cuáles pueden adoptarse sin reformar la ley. Para sostener esta afirmación, el capítulo expone primero la exposición del sector y la situación del país, formula después el problema y su justificación, y concluye con los objetivos, el alcance y las limitaciones del estudio.

## 1.1 Contextualización

### 1.1.1 Contexto macro: la exposición del sector educativo a nivel mundial

La educación superior se ha consolidado como uno de los sectores con mayor exposición a incidentes que comprometen datos personales. La edición 2024 del estudio *The State of Ransomware in Education*, basada en una encuesta a 5 000 responsables de tecnología de 14 países, de los cuales 600 pertenecían a organizaciones educativas, reportó que el 66 % de las IES había sufrido un ataque de *ransomware* en el último año, que el 77 % de esos ataques terminó con el cifrado de datos y que el costo medio de recuperación en el subsector alcanzó 4,02 millones de dólares [1]. Por tratarse de una encuesta de un proveedor comercial de seguridad, estas cifras se usan solo como contexto de la exposición del sector y no para estimar la probabilidad anual de ningún escenario de riesgo (Sección 4.2.4).

Entre esos incidentes, los ataques de *extracción* de datos merecen atención propia, porque su daño recae sobre el titular y no solo sobre la institución. Sus caminos de entrada son conocidos: credenciales del personal o de los estudiantes robadas mediante *phishing*, vulnerabilidades sin parchear en servicios expuestos a Internet, accesos remotos de proveedores y programas de *ransomware* que, además de cifrar, copian la información para extorsionar con su publicación; la revisión de Ulven y Wangen identifica a las credenciales comprometidas y a las vulnerabilidades técnicas entre los eventos de amenaza recurrentes en la educación superior [2]. Cuando los datos extraídos se publican, como ocurrió con los listados de estudiantes de una universidad chilena en 2024 [3], las consecuencias para el titular —suplantación de identidad, fraude, discriminación o exposición de su salud— son difíciles de revertir, y se agravan cuando la información incluye datos sensibles o categorías especiales [4, arts. 4 y 25], como los de salud, discapacidad o condición socioeconómica que las universidades recogen para becas y bienestar. Por eso la metodología propuesta valora el impacto de la extracción desde la perspectiva del titular y la trata como un escenario base que toda universidad debe analizar.

La literatura académica coincide en ese diagnóstico. La revisión de Ulven y Wangen [2] sintetizó los activos críticos, eventos de amenaza y vulnerabilidades frecuentes en la educación superior, concluyó en nueve riesgos estratégicos de ciberseguridad para el sector y advirtió que la investigación empírica sobre riesgos en este ámbito es escasa. Li et al. [5], con una muestra de universidades chinas, encontraron que la divulgación pública de vulnerabilidades incrementa la frecuencia de brechas, mientras que la adopción de servicios en la nube la reduce; es decir, la exposición depende de decisiones de gestión y no solo de controles técnicos puntuales.

El riesgo, además, no es solo técnico. Liu y Khalil [6] identificaron ocho problemas interrelacionados de privacidad a lo largo del ciclo de vida de los datos de la analítica del aprendizaje, y Brown y Klein [7], tras analizar los documentos de políticas de privacidad de universidades estadounidenses, identificaron discursos recurrentes en los que el interés educativo legítimo que justifica el uso de los datos lo define la propia institución y se aplica de forma amplia, y en los que la protección de la privacidad se hace depender tanto de la responsabilidad institucional como de la iniciativa del estudiante. Desde la perspectiva de los propios estudiantes, Ifenthaler y Schumacher [8] examinaron la disposición de los estudiantes a compartir sus datos con sistemas de analítica del aprendizaje y concluyeron que deben participar en las decisiones sobre su implementación, y Maguraushe et al. [9] propusieron y validaron un modelo de percepción de la privacidad de los estudiantes universitarios basado en su conciencia, sus expectativas y su confianza en las prácticas de la institución. La transparencia hacia el titular es, por tanto, una dimensión del riesgo tan relevante como la seguridad de los sistemas.

### 1.1.2 Contexto meso: América Latina y Ecuador

En América Latina, los incidentes en universidades han pasado de ser casos aislados a eventos con consecuencias públicas visibles. En marzo de 2023, la Universidad Nacional de Colombia sufrió un ataque de *ransomware* que cifró parte de su información y obligó a aislar sus sistemas financiero, académico y de talento humano [10]. En octubre de 2024, la Universidad Técnica Federico Santa María, en Chile, registró un incidente tras el cual se publicaron alrededor de 14 GB de información que incluía listados de estudiantes con su número de identificación, carrera y año de ingreso [3]. En Brasil, una encuesta aplicada entre agosto y septiembre de 2024 a 125 participantes de contextos educativos —108 estudiantes y 17 docentes— encontró incertidumbre sobre las prácticas de consentimiento, dificultad para acceder a las políticas de privacidad y desconocimiento de los derechos de los titulares [11].

Ecuador cuenta con un antecedente nacional que evidenció la magnitud del problema antes de la existencia de una ley específica. En septiembre de 2019 se reportó la exposición de una base de datos de una empresa privada que contenía información de alrededor de 20 millones de personas, incluidos cerca de 6,7 millones de niños, con campos como nombres, fecha de nacimiento, domicilio, teléfonos y nivel de educación [12]. Ese caso aceleró el debate legislativo que culminó con la LOPDP, publicada en el Quinto Suplemento del Registro Oficial N.º 459 el 26 de mayo de 2021 [4]; su reglamento general fue expedido mediante el Decreto Ejecutivo N.º 904 y publicado en el Tercer Suplemento del Registro Oficial N.º 435 el 13 de noviembre de 2023 [13].

La LOPDP establece obligaciones que pueden verificarse desde fuera de la institución y otras que solo pueden verificarse desde dentro. Entre las primeras está el derecho del titular a ser informado, de forma previa a la recogida, sobre los fines, la base legal, el tiempo de conservación, la identidad y el contacto del responsable, las transferencias, la forma de ejercer sus derechos y dónde reclamar [4, art. 12], así como el consentimiento libre, específico, informado e inequívoco cuando este es la base del tratamiento [4, art. 8]. Entre las segundas están el análisis de riesgos, amenazas y vulnerabilidades [4, art. 40] y la obligación del responsable de utilizar metodologías de análisis y gestión de riesgos adaptadas al tratamiento [4, art. 47, num. 5], cuya omisión es infracción grave [4, art. 68]. Esta distinción es decisiva para el diseño del estudio: las obligaciones internas, como el análisis de riesgos, no pueden verificarse desde fuera, pero sí pueden dotarse de una metodología que la propia universidad aplique, y eso es lo que este trabajo construye.

La Superintendencia de Protección de Datos Personales (SPDP) comenzó a emitir normativa técnica entre 2025 y 2026: la *Guía de Gestión de Riesgos y Evaluación de Impacto del Tratamiento de Datos Personales* (Resolución N.º SPDP-SPD-2025-0003-R, publicada el 19 de mayo de 2025), cuyo capítulo I es de cumplimiento obligatorio [14], [15]; su segunda versión (Resolución N.º SPDP-SPD-2026-0012-R, publicada el 30 de marzo de 2026) [16], y el Modelo Técnico de Gran Escala (Resolución N.º SPDP-SPD-2026-0005-R, publicada el 25 de febrero de 2026), que vincula con el tratamiento a gran escala ciertos supuestos —entre ellos, los tratamientos de salud y otras categorías especiales y el tratamiento sistemático de datos de niñas, niños y adolescentes en entornos educativos— y, con ello, la obligación de evaluación de impacto y de designar un delegado [17, arts. 12 y 14]. Esa vinculación no exime de verificar los supuestos y umbrales de la norma: cada institución debe comprobar en su propio tratamiento si alcanza la gran escala (Sección 2.4.3).

La autoridad ya ejerce su potestad sancionadora. El 1 de diciembre de 2025 se dieron a conocer las primeras sanciones por infracciones graves, impuestas a la Liga Profesional de Fútbol del Ecuador y a la Federación Ecuatoriana de Fútbol por un total cercano a 454 500 dólares [18], [19]; hasta septiembre de 2025, la SPDP había recibido 191 denuncias [20]. En las fuentes públicas consultadas no se identificó, al 7 de noviembre de 2026, un procedimiento sancionador contra una universidad, de modo que para estas instituciones el riesgo jurídico existe, pero aún no se ha materializado.

### 1.1.3 El sector educativo ecuatoriano en cifras

La magnitud del problema se aprecia mejor con cifras. La fecha de corte normativa del estudio es el 16 de noviembre de 2026 (Sección 2.4.4); las cifras de contexto, en cambio, llevan la fecha de su propia consulta, porque proceden de fuentes estadísticas que se actualizan con otra periodicidad y no forman parte del análisis normativo. Todos los valores de esta sección se tomaron de fuentes oficiales o, cuando estas no publican el dato, de publicaciones que citan expresamente a la fuente oficial, y cada uno se acompaña de su fecha de corte; los datos que no se hallaron publicados se declaran como no disponibles en lugar de estimarse. La Tabla 1 reúne el universo de instituciones educativas y de estudiantes cuyos datos se tratan en los términos de la LOPDP.

**Tabla 1**
*Instituciones y estudiantes del sistema educativo ecuatoriano.*

| **Nivel** | **Cifra** | **Fecha de corte** | **Fuente** |
| --- | --- | --- | --- |
| Educación inicial, básica y bachillerato (todos los sostenimientos) | 16 161 instituciones; 4 370 420 estudiantes; 209 471 docentes | Ciclo 2024–2025 | Ministerio de Educación, citado en [21] |
| Ídem, por sostenimiento | 12 389 fiscales; 617 fiscomisionales; 112 municipales; 3 022 particulares (total: 16 140) | Estadística Educativa, vol. 5 (octubre de 2024) | [22] |
| Centros de desarrollo infantil (CDI) en convenio con GAD y organizaciones sociales | 1 861 centros | Levantamiento de 2024, informe de noviembre de 2025 | [23] |
| Universidades y escuelas politécnicas | 64 (36 públicas, 20 particulares autofinanciadas, 8 particulares cofinanciadas) | Consulta del 16 de noviembre de 2026, confirmada el 25 de noviembre de 2026 (el portal no indica fecha de corte) | [24], [25] |
| Estudiantes matriculados en universidades y escuelas politécnicas | 841 404 (el 36 % en universidades particulares) | Año 2023 | SIIES-SENESCYT, citado en [26]; base oficial en [27] |
| Institutos técnicos, tecnológicos, pedagógicos, de artes y conservatorios superiores | 218 (62 públicos, 156 particulares) | Consulta del 25 de noviembre de 2026 (el 27 de octubre de 2026 el portal mostraba 216) | [24] |

*Elaborado por:* Ramón Alejandro Manzaba Castro. *Fuente:* Elaboración propia a partir de [21], [22], [23], [24], [26], [25].

Todas estas instituciones están obligadas a proteger los datos personales que tratan, y no por analogía, sino por el texto de la ley. La LOPDP se aplica al tratamiento de datos personales contenidos en cualquier tipo de soporte [4, art. 2] y define como responsable a la persona natural o jurídica, pública o privada, que decide sobre la finalidad y el tratamiento [4, art. 4]; toda universidad que matricula estudiantes, registra calificaciones o administra un aula virtual cumple esa definición. La ley añade deberes específicos para el sector: el sistema educativo, incluida la educación superior, debe garantizar la educación digital de estudiantes y docentes [4, art. 23]; las entidades educativas deben proveer información y capacitación sobre el tratamiento de datos [4, art. 24], y las universidades públicas, por pertenecer al sector público, deben designar un delegado de protección de datos [4, art. 48, num. 1]. La reforma de 2026 dispuso, además, que escuelas, colegios y universidades incorporen progresivamente contenidos de protección de datos personales en su oferta educativa [28, art. 8].

Frente a ese universo de obligados, las cifras sobre la capacidad de cumplimiento son escasas. En abril de 2025 se informaba que más de 1 150 delegados de protección de datos estaban registrados ante la SPDP, sumando todos los sectores de la economía [29]; aun si todos trabajaran en educación, cubrirían como máximo el 7,0 % de las 16 443 instituciones educativas y de educación superior de la Tabla 1 (1 150 / 16 443), y no se halló una cifra oficial posterior publicada al 7 de noviembre de 2026. La SPDP había recibido 85 denuncias en abril de 2025 [29] y 191 en septiembre de 2025 [20]. Aunque la ley ordena a la autoridad llevar un registro estadístico de vulneraciones [4, art. 76, num. 14], no se halló una estadística pública de vulneraciones notificadas por el sector educativo. Tampoco existe un informe oficial que indique qué porcentaje de universidades ha implementado la LOPDP: el estudio nacional más reciente describe una adopción desigual de políticas, pero no la cuantifica [30], y en las publicaciones de la SPDP, del CES y del CACES consultadas no se encontró ese porcentaje.

En síntesis, las cifras dibujan un sector amplio y obligado por la ley, pero sin una referencia común para cumplirla: 64 universidades y escuelas politécnicas que tratan los datos de más de 840 000 estudiantes deben aplicar metodologías de análisis y gestión de riesgos [4, art. 47, num. 5], y no existe una cifra oficial sobre cuántas lo hacen ni una guía de la autoridad dirigida al sector educativo.

### 1.1.4 Contexto micro: las universidades ecuatorianas y sus estudiantes como titulares

En el sistema de educación superior ecuatoriano, la evidencia disponible indica que la adecuación a la LOPDP es heterogénea. Álvarez-Carrión y Hernández-Sotomayor [31] concluyeron que, aunque la ley ofrece un marco sólido, su implementación en plataformas educativas enfrenta brechas de infraestructura y de capacitación, con fallos técnicos y error humano como causas principales de las vulneraciones documentadas en universidades del país. Piray Rodríguez et al. [30] encontraron diferencias marcadas entre instituciones en la adopción de políticas internas de protección de datos. Ninguno de estos estudios, sin embargo, propone una metodología de gestión de riesgos específica para el sector ni contrasta la LOPDP con las soluciones que otros marcos han dado al mismo problema.

El estudiante universitario es un titular particular. Entrega datos de identificación, contacto, rendimiento académico y, con frecuencia, datos socioeconómicos, de salud o de discapacidad para acceder a becas, ayudas o adaptaciones; muchos ingresaron a la universidad siendo menores de edad, categoría especial en la ley [4, art. 25], y su relación con la institución es asimétrica, porque negarse a entregar un dato puede significar no acceder a un servicio. Otros países han respondido a esa particularidad con reglas propias: Estados Unidos tiene una ley dedicada a los registros educativos desde 1974 [32], y la autoridad brasileña publicó una guía sobre el tratamiento de datos con fines académicos [33]. En Ecuador no existe todavía una guía equivalente.

En síntesis, la evidencia de los tres niveles converge en una conclusión: la exposición del sector es alta, las obligaciones de gestión de riesgos son exigibles desde 2023 y la normativa técnica que las concreta es reciente y general, mientras que otros marcos ya ofrecen soluciones probadas para el sector educativo. Aprovecharlas, conforme a la LOPDP, es el camino más corto para que las universidades gestionen sus riesgos con fundamento.

## 1.2 Planteamiento del Problema

Las universidades ecuatorianas tratan los datos personales de más de 840 000 estudiantes [26] y están obligadas a utilizar metodologías de análisis y gestión de riesgos adaptadas a las particularidades de sus tratamientos [4, art. 47, num. 5], cuya omisión es infracción grave [4, art. 68]; sin embargo, no disponen de una metodología específica para los datos académicos. La guía de la SPDP es de aplicación general y no se dirige a ningún sector [16], la LOPDP lleva pocos años de aplicación y no existen prácticas sectoriales consolidadas en el país (Sección 1.1.3). Sin una metodología que traduzca las obligaciones de la ley a los procesos universitarios —admisión, matrícula, evaluación, bienestar, becas, plataformas virtuales y titulación—, cada institución aplica criterios propios y no comparables, y los riesgos para los titulares quedan sin identificar ni gestionar. El problema afecta a las 64 universidades y escuelas politécnicas del país [24].

### 1.2.1 Análisis crítico

El análisis del problema se estructuró mediante un árbol de problemas que relaciona sus causas con el problema central y con los efectos que produce. La Tabla 2 presenta esa relación y la Figura 1 la representa de forma gráfica.

**Tabla 2**
*Árbol de problemas: causas, problema central y efectos.*

| **Causas** | **Problema central** | **Efectos** |
| --- | --- | --- |
| C1. LOPDP reciente y normativa técnica general, sin guías para el sector educativo. | **Las universidades carecen de una metodología específica para diagnosticar y gestionar los riesgos del tratamiento de datos académicos conforme a la LOPDP.** | E1. Exposición a sanciones por infracciones graves (arts. 68 y 72 de la LOPDP). |
| C2. Las soluciones de otros marcos jurídicos no se han sistematizado para el contexto ecuatoriano. |  | E2. Titulares que no pueden ejercer sus derechos por desconocerlos o por falta de canales. |
| C3. Gestión de la seguridad centrada en activos tecnológicos y no en los derechos de los titulares. |  | E3. Riesgos para los titulares no identificados ni tratados; evaluaciones de impacto omitidas. |
| C4. Escasa cultura de protección de datos en estudiantes y personal. |  | E4. Incapacidad de notificar vulneraciones dentro del término legal. |
| C5. Normativa técnica de la SPDP reciente y uso creciente de plataformas de terceros. |  | E5. Pérdida de confianza de los estudiantes y daño reputacional. |

*Elaborado por:* Ramón Alejandro Manzaba Castro. *Fuente:* Elaboración propia con base en [4], [16], [30], [31].

**Figura 1**
*Árbol de problemas.*

> Diagrama elaborado en TikZ; véase el PDF. Su contenido coincide con la tabla del árbol de problemas.

La primera causa es normativa: la LOPDP entró plenamente en vigencia en 2023 y la normativa técnica de la SPDP se expidió entre 2025 y 2026, con un alcance general que no desciende a los procesos de ningún sector (Sección 2.4.3). La segunda causa es la falta de sistematización de los referentes: el RGPD, la FERPA, la LGPD y las leyes colombiana y chilena han producido guías y experiencia sobre el mismo problema [34], [33], [35], pero los estudios ecuatorianos que comparan la LOPDP con otros marcos son generales o se limitan a uno solo [36], [37], [38]. La tercera causa es de enfoque: los modelos aplicados en el sector, como los descritos por Patiño et al. [39] y López-Vasco et al. [40], valoran el riesgo sobre los activos de la organización. La cuarta causa, vinculada al factor humano, coincide con el peso del error humano en los incidentes de universidades ecuatorianas [31]. La quinta causa responde a la migración de servicios académicos hacia plataformas de terceros, en las que la universidad sigue siendo responsable.

Entre los efectos destaca la exposición legal: no informar al titular, no atender sus derechos o no utilizar metodologías de análisis y gestión de riesgos son conductas tipificadas, y para una universidad particular las infracciones graves se sancionan con multas de entre el 0,7 % y el 1 % de su volumen de negocio del ejercicio anterior, y en una universidad pública, con multas de 10 a 20 salarios básicos unificados a los servidores o funcionarios responsables, sin perjuicio de la responsabilidad extracontractual del Estado [4, arts. 68 y 72]. A ello se suma que un titular que no conoce sus derechos no puede ejercerlos, y que una institución que no ha identificado sus riesgos difícilmente podrá notificar a tiempo una vulneración.

### 1.2.2 Prognosis

De no abordarse el problema, las universidades continuarían gestionando —o dejando de gestionar— los riesgos de los datos de sus estudiantes con criterios propios y no comparables, sin aprovechar la experiencia de otros marcos, y la autoridad y la comunidad académica seguirían sin un referente sectorial. La tendencia regional de ataques contra universidades [3], [10], [1] y la actividad sancionadora de la SPDP [18] permiten prever que las consecuencias de esa ausencia serán cada vez más tangibles.

### 1.2.3 Formulación del problema

¿Cómo diagnosticar y gestionar de forma sistemática los riesgos del tratamiento de datos personales académicos en las universidades ecuatorianas, conforme a la LOPDP y a la normativa técnica de la SPDP, aprovechando las soluciones que otros marcos jurídicos han dado al mismo problema?

### 1.2.4 Preguntas directrices

La investigación se orienta mediante cuatro preguntas directrices, cada una vinculada a un objetivo específico (OE). ¿Cómo regulan la Unión Europea, Estados Unidos, Brasil, Colombia y Chile la protección de los datos personales y la gestión de sus riesgos en las instituciones de educación superior? (OE1). ¿Qué elementos comparten esos marcos con la LOPDP, en qué difieren y cuáles de sus prácticas pueden adoptarse sin reformar la ley ecuatoriana? (OE2). ¿Qué fases, pasos, reglas y herramientas debe tener una metodología de diagnóstico y gestión de riesgos para los datos académicos conforme a la LOPDP? (OE3). ¿Qué aplicabilidad, completitud y conformidad normativa atribuyen los expertos a esa metodología? (OE4).

### 1.2.5 Delimitación

En cuanto al contenido, el estudio pertenece al campo de las tecnologías de la información, en el área de gobernanza y seguridad de la información. En lo **temático**, se centra en el tratamiento de los datos personales académicos en las instituciones de educación superior (Sección 2.3). En lo **normativo**, considera la normativa publicada hasta el **16 de noviembre de 2026** (fecha de corte normativa), detallada en la Tabla 5 y en el Anexo A; las normas posteriores no modifican el análisis, y si alguna altera sustancialmente un elemento comparado, se registra en una nota de vigencia y se considera trabajo futuro. En lo **geográfico**, la comparación es internacional —Ecuador, Unión Europea, Estados Unidos, Brasil, Colombia y Chile—, pero la metodología se diseña para las universidades y escuelas politécnicas del Ecuador, conforme a la LOPDP. En lo **temporal**, el trabajo se ejecuta del 26 de noviembre de 2026 al 26 de febrero de 2027.

El planteamiento permite concluir que el problema no es la falta de normas, sino la falta de una herramienta que las traduzca a los procesos universitarios. Por ello, la pregunta de investigación busca una metodología construida conforme a la LOPDP, alimentada por la experiencia comparada y validada por expertos.

## 1.3 Justificación

La importancia del trabajo radica en que la gestión de riesgos ha dejado de ser una buena práctica opcional para convertirse en una obligación jurídica exigible desde mayo de 2023: la LOPDP obliga al responsable a utilizar metodologías de análisis y gestión de riesgos [4, art. 47, num. 5] y a evaluar el impacto de los tratamientos de alto riesgo antes de iniciarlos [4, art. 42]. La necesidad es cuantificable: 64 universidades y escuelas politécnicas [24] tratan los datos de 841 404 estudiantes matriculados en 2023 [26]. Para una universidad particular, una infracción grave se sanciona con una multa de entre el 0,7 % y el 1 % de su volumen de negocio, y en una pública, con multas de 10 a 20 salarios básicos unificados a los servidores responsables [4, art. 72]; además, las dos primeras multas impuestas por la SPDP sumaron cerca de 454 500 dólares [18].

El **enfoque comparado** se justifica por tres razones. La LOPDP es joven, mientras que el RGPD, la ley colombiana o la FERPA acumulan años de aplicación, guías de sus autoridades y estudios sobre su implementación en universidades [34], [41], [42]; el sector educativo ecuatoriano no tiene guías sectoriales, y otros países sí las tienen [33], [35], y la propia LOPDP se inspiró en el modelo europeo, lo que vuelve comparables sus instituciones. La **novedad** del aporte reside en que los estudios ecuatorianos que comparan la LOPDP con otros marcos son generales o se limitan a uno solo [36], [37], [43], [38], y ninguno traduce la comparación en una metodología para el sector educativo.

La utilidad del proyecto se expresa en su producto principal —la metodología de diagnóstico y gestión de riesgos, con su plantilla de matriz en hoja de cálculo y su guía de aplicación, que cualquier universidad podrá aplicar a sus propios tratamientos— y en los productos que la sustentan: el corpus normativo comparado, las fichas de los seis marcos y las matrices comparativas en trece dimensiones, reutilizables por otros investigadores y por la autoridad. La factibilidad es técnica, operativa y económica: el estudio se apoya en normas, guías y estudios de acceso público, en herramientas ofimáticas de uso común y en consultas en línea a expertos, sin requerir autorizaciones de acceso a datos internos.

Los beneficiarios directos son las universidades, que dispondrán de una metodología aplicable y fundamentada, y sus estudiantes, cuyos riesgos se gestionarán desde su perspectiva como titulares; los beneficiarios indirectos son la autoridad de control y la comunidad académica, que contarán con un análisis comparado del sector. El trabajo se inscribe en la línea de investigación Gestión de la Información, sublínea Gobernanza y seguridad de la información, y en el eje Tecnologías para la educación, y contribuye a las competencias del perfil de egreso PE-CP-06 (evaluar proyectos de TI en concordancia con el marco legal vigente), PE-MI-04 (gestionar proyectos de TI aplicando conceptos éticos y legales), PE-IS-04 (realizar proyectos de investigación siguiendo una metodología científica) y PE-PP-05 (implementar sistemas de seguridad informática bajo políticas organizacionales y estándares aceptados).

Podría objetarse que un estudio documental, sin datos de universidades ecuatorianas, no puede proponer una metodología útil para ellas. La objeción es válida solo en parte. La utilidad de una metodología depende de que cubra las obligaciones de la ley y de que sus elementos hayan funcionado en la práctica, y ambas cosas pueden establecerse con fuentes documentales: las obligaciones, con el texto de la LOPDP, y la experiencia, con las guías, herramientas y estudios de los marcos comparados. Lo que el estudio no puede probar es su eficacia en una institución concreta, y por eso la somete al juicio de expertos y deja su aplicación piloto como trabajo futuro. En consecuencia, el diseño no es una alternativa debilitada a un estudio empírico, sino la forma adecuada de construir una herramienta para un marco jurídico joven.

## 1.4 Objetivos
### 1.4.1 Objetivo General

Diseñar una metodología de diagnóstico y gestión de riesgos para el tratamiento de datos personales de estudiantes en instituciones de educación superior, mediante la integración de las etapas de la guía de gestión de riesgos y evaluación de impacto de la SPDP con la norma ISO/IEC 27005:2022, para contribuir al cumplimiento de las obligaciones de análisis de riesgos y evaluación de impacto establecidas en la Ley Orgánica de Protección de Datos Personales (2021) y en su Reglamento General (2023).

### 1.4.2 Objetivos Específicos

1. Analizar comparativamente los marcos jurídicos de protección de datos personales de la Unión Europea (RGPD), Estados Unidos (FERPA), Brasil (LGPD), Colombia (Ley 1581 de 2012) y Chile (Ley 21.719 de 2024), identificando sus enfoques de gestión de riesgos y las obligaciones aplicables al tratamiento de datos en instituciones de educación superior.

2. Identificar las convergencias, divergencias y buenas prácticas entre los marcos analizados y la LOPDP ecuatoriana, determinando los elementos que la metodología de diagnóstico y gestión de riesgos debe incorporar.

3. Diseñar la metodología de diagnóstico y gestión de riesgos para el tratamiento de datos personales académicos conforme a la LOPDP, integrando las buenas prácticas identificadas en el análisis comparado.

4. Validar la metodología propuesta mediante juicio de expertos (método Delphi), evaluando su aplicabilidad, completitud y conformidad normativa.

Los cuatro objetivos guardan una secuencia lógica con el objetivo general, cuyo producto es la metodología: los dos primeros reúnen los insumos —qué exigen y cómo resuelven el problema los marcos con más experiencia, y qué de ello es mínimo, opcional o adoptable sin reforma legal—, el tercero la construye conforme a la LOPDP y el cuarto la somete al juicio de expertos con criterios fijados de antemano.

## 1.5 Alcance del Proyecto

El alcance comprende cuatro componentes, uno por objetivo específico: (1) el análisis documental de los marcos jurídicos de protección de datos de la Unión Europea, Estados Unidos, Brasil, Colombia y Chile, con su corpus normativo y una ficha por marco; (2) la comparación de esos marcos con la LOPDP en trece dimensiones, con la identificación de convergencias, divergencias, brechas y buenas prácticas adoptables; (3) la metodología de diagnóstico y gestión de riesgos conforme a la LOPDP, con su plantilla de matriz y su guía de aplicación (Anexo K), y (4) su validación por un panel Delphi. La fecha de corte normativa es el **16 de noviembre de 2026**.

El objeto se delimita con la noción de **datos personales académicos**: los que la institución de educación superior trata con ocasión de la admisión, la formación, la evaluación, el bienestar y la titulación de sus estudiantes (Sección 2.3). La metodología cubre a los aspirantes —incluidos los menores de edad, cuyos datos son categoría especial y se rigen por reglas propias [4, arts. 21 y 25]—, los estudiantes, sus padres o representantes y los graduados, y, de forma opcional, a los docentes y al personal administrativo, cuyos datos la universidad también trata.

El proyecto excluye de manera expresa cinco aspectos. Primero, no utiliza datos internos de ninguna universidad, no recoge datos de estudiantes ni audita sistemas, registros o contratos. Segundo, no constituye una certificación ni una declaración de cumplimiento ante la autoridad. Tercero, no cubre la implementación de las medidas que proponga la metodología, que corresponde a cada institución. Cuarto, no abarca una auditoría externa independiente. Quinto, no propone reformar la LOPDP ni adoptar otra ley: las brechas que se identifiquen se documentan como recomendaciones para trabajos futuros.

Entre las limitaciones se reconoce, en primer lugar, que **la metodología no se aplicó en una institución real**: su validación descansa en el juicio de expertos, y su aplicación piloto en una universidad queda como trabajo futuro. En segundo lugar, la comparación se limita a cinco marcos extranjeros seleccionados con criterios explícitos; otros marcos de la región, como el peruano, no se analizan. En tercer lugar, el análisis se apoya en la letra de las normas y en las guías y estudios disponibles, y no en la práctica efectiva de las autoridades extranjeras, que solo se conoce de forma indirecta; por eso, un elemento se registra como presente solo si consta en la norma o en una fuente oficial. En cuarto lugar, algunos marcos están en evolución —la ley chilena entra en vigor el 1 de diciembre de 2026 y la normativa técnica de la SPDP sigue desarrollándose—, de modo que el trabajo refleja la normativa publicada hasta la fecha de corte, y las normas posteriores se tratan con la regla de la nota de vigencia (Sección 2.4.4).

Delimitar de este modo el alcance no debilita el aporte, sino que lo hace verificable: el trabajo se compromete con lo que puede demostrar con fuentes que cualquiera puede consultar y con el juicio estructurado de expertos, y deja expresamente fuera lo que solo podría establecerse con una aplicación en una institución real.

## Referencias del capítulo

Numeración IEEE idéntica a la del PDF (`main.pdf`).

[1] Sophos, “The state of ransomware in education 2024,” Sophos, Tech. Rep., 2024. [Online]. Available: https://www.sophos.com/en-us/blog/the-state-of-ransomware-in-education-2024

[2] J. B. Ulven and G. Wangen, “A systematic review of cybersecurity risks in higher education,” *Future Internet*, vol. 13, no. 2, p. 39, 2021.

[3] CNN Chile, “Hackeo a la Universidad Santa María: datos de estudiantes y académicos fueron vulnerados y publicados en la dark web,” Nov. 2024. [Online]. Available: https://www.cnnchile.com/pais/hackeo-universidad-santa-maria-datos-estudiantes-academicos-vulnerados-publicados-dark-web_20241116/

[4] Asamblea Nacional del Ecuador, “Ley Orgánica de Protección de Datos Personales,” Registro Oficial Quinto Suplemento N.º 459, Quito, Ecuador, May 2021.

[5] J. Li, W. Xiao, and C. Zhang, “Data security crisis in universities: identification of key factors affecting data breach incidents,” *Humanities and Social Sciences Communications*, vol. 10, p. 270, May 2023.

[6] Q. Liu and M. Khalil, “Understanding privacy and data protection issues in learning analytics using a systematic review,” *British Journal of Educational Technology*, vol. 54, no. 6, pp. 1715–1747, Nov. 2023.

[7] M. Brown and C. Klein, “Whose data? Which rights? Whose power? A policy discourse analysis of student privacy policy documents,” *The Journal of Higher Education*, vol. 91, no. 7, pp. 1149–1178, 2020.

[8] D. Ifenthaler and C. Schumacher, “Student perceptions of privacy principles for learning analytics,” *Educational Technology Research and Development*, vol. 64, no. 5, pp. 923–938, 2016.

[9] K. Maguraushe, A. da Veiga, and N. Martins, “A personal information privacy perceptions model for university students,” *Information Security Journal: A Global Perspective*, vol. 33, no. 4, pp. 394–424, 2024.

[10] Semana, “Los detalles secretos del grave hackeo que sufrió la Universidad Nacional,” Apr. 2023. [Online]. Available: https://www.semana.com/nacion/articulo/asi-fue-el-hackeo-del-que-fue-victima-la-universidad-nacional/202335/

[11] Y. Correia de Barros and J. Vilela, “Data privacy in educational contexts: analyzing perceptions, practices and challenges in personal data protection,” in *Proceedings of the 27th International Conference on Enterprise Information Systems (ICEIS)*. 1em plus 0.5em minus 0.4em SCITEPRESS, 2025, pp. 308–319.

[12] Y. Arciniegas, “Falla informática en Ecuador: los datos de casi toda la población quedaron expuestos,” France 24, Sep. 2019. [Online]. Available: https://www.france24.com/es/20190917-ecuador-datos-expuestos-informacion-filtracion

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

[25] –––, “Universidades y escuelas politécnicas públicas, particulares autofinanciadas y particulares cofinanciadas (listados con provincia y cantón),” Portal institucional del CES, páginas 328, 1540 y 5398, consultadas el 16 de noviembre de 2026, Quito, Ecuador, 2026. [Online]. Available: https://www.ces.gob.ec/?page_id=328

[26] N. Sumba-Nacipucha and A. Sánchez-Bayón, “Economía conductual y la elección de universidades: factores que influyen en la decisión,” *KAIRÓS, Revista de Ciencias Económicas, Jurídicas y Administrativas*, vol. 8, no. 14, pp. 171–192, 2025.

[27] Secretaría de Educación Superior, Ciencia, Tecnología e Innovación, “Base estadística de matrícula de universidades y escuelas politécnicas 2015–2023,” Portal de Datos Abiertos del Ecuador, actualizado el 28 de abril de 2025, consultado el 7 de noviembre de 2026, 2025. [Online]. Available: https://www.datosabiertos.gob.ec/dataset/base-de-datos-de-matricula-de-uep-ano-2021

[28] Asamblea Nacional del Ecuador, “Ley Orgánica para el Fortalecimiento de la Ciberseguridad,” Registro Oficial Quinto Suplemento N.º 290, 22 de mayo de 2026, Quito, Ecuador, 2026. [Online]. Available: https://www.asambleanacional.gob.ec/es/system/files/ro_29.pdf

[29] IT Ahora, “Avances y acción de la Superintendencia de Protección de Datos Personales,” IT Ahora, Apr. 2025. [Online]. Available: https://itahora.com/2025/04/16/avances-y-accion-de-la-superintendencia-de-proteccion-de-datos-personales/

[30] P. O. Piray Rodríguez, S. W. Parra Molina, J. E. Yaulema Colcha, and J. J. Salazar Briones, “Garantías jurídicas de la privacidad informativa en instituciones de educación superior del Ecuador contemporáneo,” *Universidad y Sociedad*, vol. 18, no. 2, p. e5877, 2026. [Online]. Available: https://rus.ucf.edu.cu/index.php/rus/article/view/5877

[31] J. A. Álvarez-Carrión and G. P. Hernández-Sotomayor, “Protección de datos personales en plataformas educativas digitales en el sistema de educación superior de Ecuador,” *MQRInvestigar*, vol. 8, no. 3, pp. 5324–5339, 2024.

[32] United States Congress, “Family Educational Rights and Privacy Act of 1974 (FERPA),” 20 U.S.C. 1232g, 1974. [Online]. Available: https://studentprivacy.ed.gov/ferpa

[33] Autoridade Nacional de Proteção de Dados, “Guia Orientativo: Tratamento de Dados Pessoais para Fins Acadêmicos e para a Realização de Estudos e Pesquisas,” Brasília, Brasil, Jun. 2023. [Online]. Available: https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/web-guia-anpd-tratamento-de-dados-para-fins-academicos.pdf

[34] G. Zanfir-Fortuna, “The general data protection regulation: Analysis and guidance for US higher education institutions,” Future of Privacy Forum, Washington, DC, USA, Tech. Rep., May 2020. [Online]. Available: https://fpf.org/wp-content/uploads/2020/05/FPF_GDPR-Report-Final.pdf

[35] National Forum on Education Statistics, “Forum guide to protecting the privacy of student information: State and local education agencies,” National Center for Education Statistics, Washington, DC, USA, NCES 2004-330, 2004. [Online]. Available: https://nces.ed.gov/forum/pub_2004330.asp

[36] E. R. Pérez Vaca, “La regulación de la protección de datos personales en la legislación ecuatoriana y su análisis comparativo con el RGPD,” Trabajo final de máster, Universitat Oberta de Catalunya, Barcelona, España, 2021. [Online]. Available: https://openaccess.uoc.edu/handle/10609/128046

[37] J. E. García Roldán, “El impacto del RGPD en las políticas y prácticas de protección de datos en Ecuador,” Trabajo de titulación de grado, Universidad Laica Eloy Alfaro de Manabí, Manta, Ecuador, 2024. [Online]. Available: https://repositorio.uleam.edu.ec/handle/123456789/6426

[38] D. Echeverría Muñoz, “Gestión de riesgos y protección de datos: la tecnificación normativa ecuatoriana frente al paradigma europeo,” *Revista de Privacidad, Innovación y Tecnología*, no. 1, Apr. 2026. [Online]. Available: https://revista.aepd.es/revistaprivacidad/article/download/30/5/179

[39] S. Patiño, E. F. Solís, S. G. Yoo, and R. Arroyo, “ICT risk management methodology proposal for governmental entities based on ISO/IEC 27005,” in *2018 International Conference on eDemocracy & eGovernment (ICEDEG)*. 1em plus 0.5em minus 0.4em Ambato, Ecuador: IEEE, 2018, pp. 75–82.

[40] F. López-Vasco, M. Angulo-Alvarez, D. I. Sosa Zuñiga, E. Puente Moromenacho, N. Ortiz *et al.*, “Application of ISO/IEC 27,001 in higher education technological institutes: Case-control study,” in *Developments and Advances in Defense and Security (MICRADS 2024)*, ser. Smart Innovation, Systems and Technologies, vol. 423. 1em plus 0.5em minus 0.4em Singapore: Springer, 2025, pp. 179–189.

[41] W. G. d. Almeida, “Implementação de compliance \`a LGPD em instituiç\ oes federais de ensino superior: proposta de um processo estruturado para conformidade,” Dissertação de mestrado, Universidade Federal de São Carlos, São Carlos, Brasil, 2024. [Online]. Available: https://repositorio.ufscar.br/handle/20.500.14289/20686

[42] M. M. Correa Zabala, M. V. Cano Fresneda, and N. Rivera Cuervo, “Universidad del Rosario: una mirada integral a la seguridad y privacidad de los datos personales en las instituciones de educación superior,” Nova et Vetera, Universidad del Rosario, Jan. 2024. [Online]. Available: https://urosario.edu.co/revista-nova-et-vetera/omnia/universidad-del-rosario-una-mirada-integral-la-seguridad-y-privacidad-de-los-datos-personales

[43] L. M. Iza Noroña and G. A. Mora Cedeño, “Análisis comparativo de la Ley Orgánica de Protección de Datos Personales del Ecuador con la legislación de México,” Trabajo de titulación de maestría en Seguridad de la Información, Universidad Politécnica Salesiana, Cuenca, Ecuador, 2023. [Online]. Available: https://dspace.ups.edu.ec/handle/123456789/26605
