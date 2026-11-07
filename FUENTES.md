# FUENTES — Metodología cuantitativa (consulta: 2026-11-07)

DOI verificados en Crossref el 07-11-2026, salvo los dos libros y Holm (1979), que es un artículo de JSTOR sin DOI.

| Referencia | Uso | Clave | DOI / edición |
|---|---|---|---|
| McDonald (1999), *Test Theory: A Unified Treatment*, Erlbaum | Omega | `mcdonald1999test` | Libro |
| Hayes y Coutts (2020), Commun. Methods Meas. 14(1), 1–24 | Preferir omega a alfa | `hayes2020omega` | 10.1080/19312458.2020.1718629 |
| McNeish (2018), Psychol. Methods 23(3), 412–433 | Supuesto de tau-equivalencia del alfa | `mcneish2018alpha` | 10.1037/met0000144 |
| Kuder y Richardson (1937), Psychometrika 2(3), 151–160 | KR-20 | `kuder1937theory` | 10.1007/BF02288391 |
| Mann y Whitney (1947), Ann. Math. Stat. 18(1), 50–60 | Prueba U | `mann1947test` | 10.1214/aoms/1177730491 |
| Spearman (1904), Am. J. Psychol. 15(1), 72–101 | Correlación de rangos | `spearman1904proof` | 10.2307/1412159 |
| Lilliefors (1967), JASA 62(318), 399–402 | KS con parámetros estimados | `lilliefors1967kolmogorov` | 10.1080/01621459.1967.10482916 |
| Fritz, Morris y Richler (2012), J. Exp. Psychol. Gen. 141(1), 2–18 | r = Z/√N | `fritz2012effect` | 10.1037/a0024338 |
| Holm (1979), Scand. J. Stat. 6(2), 65–70 | Corrección de Holm | `holm1979simple` | — |
| Vallat (2018), JOSS 3(31), 1026 | pingouin | `vallat2018pingouin` | 10.21105/joss.01026 |
| Virtanen et al. (2020), Nat. Methods 17(3), 261–272 | SciPy | `virtanen2020scipy` | 10.1038/s41592-019-0686-2 |
| McKinney (2010), Proc. 9th Python in Science Conf., 56–61 | pandas | `mckinney2010pandas` | 10.25080/Majora-92bf1922-00a |

Software probado: Python 3.12.10; pandas 3.1.1; NumPy 2.5.4; SciPy 1.18.1; pingouin 0.7.0; matplotlib 3.11.2; openpyxl 3.1.5 (`analisis/requirements.txt`).
Parámetros de diseño nuevos: V de Aiken ≥ 0,80 (instrumento y guía); α y ω ≥ 0,70 aceptable y ≥ 0,80 bueno; puntuación de dimensión con al menos el 80 % de ítems respondidos; "No recuerdo" = no afirmativo; α = 0,05; Holm en los contrastes exploratorios.

---

# FUENTES — Reestructuración sin caso de estudio (consulta: 2026-11-07)

Tipos: **O** = oficial · **S** = secundaria que cita la fuente oficial · **A** = artículo académico (DOI verificado en Crossref el 07-11-2026). Las fuentes del 27-10-2026 (más abajo) siguen vigentes.

## Población y cifras nuevas

| Dato | Valor usado | Corte | Fuente (clave) | URL | Tipo |
|---|---|---|---|---|---|
| Universidades y escuelas politécnicas | 64 (36 públicas, 20 autofinanciadas, 8 cofinanciadas) | Consultas del 27-10 y del 07-11-2026; el portal no indica corte | `ces2026estadisticas` | https://www.ces.gob.ec/?page_id=5248 | O |
| Estudiantes matriculados en universidades y escuelas politécnicas | 841 404 (62 UEP); 36 % en universidades particulares | Año 2023 | `sumba2025economia` (cita al SIIES-SENESCYT), p. 173 | https://doi.org/10.37135/kai.03.14.09 | S/A |
| Base oficial de matrícula 2015–2023 | Existe y se actualizó el 28-04-2025; **no pudo descargarse** (el host `cloud-pro.senescyt.gob.ec` no resolvió el 07-11-2026) | — | `senescyt2025matricula` | https://www.datosabiertos.gob.ec/dataset/base-de-datos-de-matricula-de-uep-ano-2021 | O |
| Crecimiento de la matrícula 2015–2022 | 4,82 % anual (no se usa en el documento) | — | SIAU-SENESCYT | https://siau.senescyt.gob.ec/universidades-y-escuelas-politecnicas-matriculas/ | O |
| Tamaño de muestra | n = 383,98 → 384 (N = 841 404; Z = 1,96; p = q = 0,5; e = 0,05) | Cálculo propio | `cochran1977sampling` | — | Derivado (verificado en `scripts/analisis_encuesta.js prueba`) |

## LOPDP: artículos verificados en el texto oficial para los indicadores (07-11-2026)

Fuente: `lopdp2021`, edición del RO 5S 459 publicada por el Consejo de Comunicación (https://www.consejodecomunicacion.gob.ec/wp-content/uploads/downloads/2021/07/lotaip/Ley%20Org%C3%A1nica%20de%20Protecci%C3%B3n%20de%20Datos%20Personales.pdf). El texto se extrajo con `pdftotext` y se leyó.

| Artículo | Contenido usado | Indicadores |
|---|---|---|
| 7 | Tratamiento legítimo (bases de legitimación) | ID04 |
| 8 | Consentimiento libre, específico, informado e inequívoco; revocable; pluralidad de finalidades | ID08, ID10, ID14, ID15; IE07–IE09 |
| 10 | Principios: a) juridicidad, c) transparencia, d) finalidad, e) pertinencia y minimización, g) confidencialidad, h) calidad y exactitud, i) conservación, j) seguridad | ID01, ID03, ID05, ID12, ID16; IE01, IE13 |
| 12 | Derecho a la información, nums. 1–17 (fines, base legal, tipos de tratamiento, conservación, …, responsable [8], DPD [9], transferencias [10], revocación [13], derechos [14], portabilidad [15], reclamos [16], decisiones automatizadas y perfiles [17]); información previa en la recogida | ID01–ID11, ID14–ID15; IE02–IE06, IE11, IE12, IE15 |
| 13–17 | Acceso (15 días), rectificación y actualización (15 días), eliminación, oposición, portabilidad | ID07, ID08; IE10, IE11 |
| 20 | Decisiones basadas en valoraciones automatizadas | IE15 |
| 24 | Entidades educativas: información y capacitación | IE12 |
| 25–26 | Categorías especiales; datos sensibles con consentimiento explícito | ID13; IE01, IE02 |
| 33, 55–58 | Transferencias nacionales e internacionales | ID06 |
| 47 | Obligaciones del responsable: num. 1 (apego a la ley), num. 4 (políticas), **num. 5 (metodologías de análisis y gestión de riesgos)**, nums. 10–11 (contratos con encargados) | ID01, ID12; guía (Cap. 5) |
| 48–49 | Casos de DPD obligatorio; funciones (incl. asesorar en el análisis de riesgos) | ID11 |

## Antecedentes nuevos (Cap. 1, Cap. 2)

| Referencia | Uso | Clave | DOI | Tipo |
|---|---|---|---|---|
| Brown y Klein (2020), J. Higher Education 91(7), 1149–1178 | Discursos en políticas universitarias de privacidad (interés educativo legítimo definido por la institución) | `brown2020whose` | 10.1080/00221546.2020.1770045 | A (paráfrasis a partir del resumen) |
| Ifenthaler y Schumacher (2016), ETR&D 64(5), 923–938 | Percepción estudiantil sobre principios de privacidad en la analítica del aprendizaje | `ifenthaler2016student` | 10.1007/s11423-016-9477-y | A (paráfrasis a partir del resumen y la conclusión) |
| Slade y Prinsloo (2013), Am. Behav. Sci. 57(10), 1510–1529 | Debate ético sobre la analítica del aprendizaje | `slade2013learning` | 10.1177/0002764213479366 | A |
| Maguraushe, da Veiga y Martins (2024), ISJ 33(4), 394–424 | Modelo validado de percepción de privacidad de estudiantes | `maguraushe2024model` | 10.1080/19393555.2024.2329554 | A |
| Correia de Barros y Vilela (2025), ICEIS 2025, 308–319 | Encuesta en Brasil (108 estudiantes, 17 docentes; ago.–sep. 2024): consentimiento, acceso a políticas y derechos | `correia2025privacy` | 10.5220/0013426900003929 | A (cifras tomadas del resumen) |

## Métodos (Cap. 3)

| Referencia | Uso | Clave | DOI / edición | Tipo |
|---|---|---|---|---|
| Cochran (1977), *Sampling Techniques*, 3.ª ed., Wiley | Fórmula de población finita | `cochran1977sampling` | Libro | A |
| Likert (1932), Archives of Psychology 22(140) | Escala de Likert | `likert1932technique` | — | A |
| Cronbach (1951), Psychometrika 16(3), 297–334 | Alfa de Cronbach | `cronbach1951coefficient` | 10.1007/BF02310555 | A |
| Taber (2018), Res. Sci. Educ. 48(6), 1273–1296 | Advertencias sobre umbrales de alfa | `taber2018cronbach` | 10.1007/s11165-016-9602-2 | A |
| Johanson y Brooks (2010), EPM 70(3), 394–400 | Tamaño del piloto (≈ 30) | `johanson2010pilot` | 10.1177/0013164409355692 | A |
| Agresti (2019), *An Introduction to Categorical Data Analysis*, 3.ª ed., Wiley | Chi-cuadrado, V de Cramér, prueba exacta de Fisher | `agresti2019categorical` | Libro | A |

## Parámetros de diseño nuevos (no son datos empíricos)

- Ponderación P = 0,5 en el ITD; ID15 e ID16 como indicadores complementarios.
- Meta de recolección +10 % (423); cuotas 64/36 según el porcentaje de matrícula particular (36 %).
- Umbrales: V de Aiken ≥ 0,70; α ≥ 0,70; reverificación del 20 %; activación de escenarios con C_D < 50 %, C_E < 50 % o IE14 ≥ 20 %.

---

# FUENTES — Cifras y artículos usados en la revisión (consulta: 2026-10-27)

Tipo: **O** = oficial (texto normativo o publicación de la autoridad) · **S** = secundaria que cita a la fuente oficial (prensa, firma jurídica, repositorio) · **A** = artículo académico (DOI verificado en Crossref).

## Normativa ecuatoriana

| Dato / artículo | Valor usado | Fuente (clave bib) | URL | Tipo |
|---|---|---|---|---|
| LOPDP: arts. 2, 4, 6, 7, 8, 10 (lit. c, e, i), 12–24, 25, 34, 37, 40–43, 46–49, 51, 55–58, 67–72, 76, 77; disposiciones transitorias 1.ª–2.ª y final | Textos parafraseados | `lopdp2021` (RO 5S 459, 26-05-2021) | https://www.consejodecomunicacion.gob.ec/wp-content/uploads/downloads/2021/07/lotaip/Ley%20Org%C3%A1nica%20de%20Protecci%C3%B3n%20de%20Datos%20Personales.pdf | O (edición Fielweb del RO) |
| Art. 43 LOPDP: 5 días a SPDP; 2 días del encargado | Verificado | `lopdp2021` | ídem, p. 23 | O |
| Art. 46 LOPDP: 3 días a titulares; excepciones | Verificado | `lopdp2021` | ídem, p. 24 | O |
| Reforma del art. 43 (SPDP + organismo de control + CSIRT) | LOFC art. 14 | `lofc2026` (RO 5S 290, 22-05-2026) | https://www.asambleanacional.gob.ec/es/system/files/ro_29.pdf | O |
| 72 h para incidentes de ciberseguridad (entidades públicas y operadores de infraestructura crítica digital; desde la detección; al ente rector) | Art. 20-G LOTDA, añadido por LOFC art. 6 | `lofc2026` | ídem, pp. 39–40 | O |
| Escuelas, colegios y universidades incorporan contenidos de protección de datos | LOFC art. 8 (reforma art. 33 LOTDA) | `lofc2026` | ídem | O |
| RLOPDP: arts. 24–28 (vulneraciones), 29–32 (EIPD), 38–39 (RAT), 41 (contrato), 48–56 (DPD), 71–78 (transferencias), 79–80 (autoridad) | Verificados | `rlopdp2023` (D.E. 904, RO 3S 435, 13-11-2023) | https://rdigital.ueb.edu.ec/bitstreams/9d86d625-57ed-4ce6-9193-5ca8b8ede37f/download | O (copia escaneada del decreto firmado) |
| Res. SPDP-SPD-2026-0040-R: suscrita el 09-09-2026; RO 1S 376, 24-09-2026; SISPDP; clasificación C/I/D y temporal/permanente/irreversible; contenido de la comunicación a titulares | Resumen | `spdp2026vulneraciones` | https://www.lexis.com.ec/noticias/registro-oficial-del-dia-spdp-expide-norma-tecnica-de-notificacion-de-vulneraciones-de-datos ; https://avl.com.ec/nueva-resolucion-emitida-por-la-superintendencia-de-proteccion-de-datos-personales-sobre-la-norma-tecnica-de-notificacion-de-vulneraciones-de-seguridad-de-los-datos-personales/ | S → `[VERIFICAR]` |
| Res. SPDP-SPD-2025-0028-R (reglamento del DPD) | Existencia y año | `spdp2025dpd` | https://spdp.gob.ec/wp-content/uploads/2025/07/028-R.pdf | O (fecha exacta pendiente) |
| Res. 0003-R, 0012-R (guía v1/v2), 0005-R (gran escala) | Ya en la tesis | `spdp2025guia`, `spdp2026guiav2`, `spdp2026granescala` | Ver `referencias.bib` | O |
| Constitución: art. 66 num. 19, 133, 425 | Jerarquía y derecho | `constitucion2008` (RO 449, 20-10-2008) | https://www.gob.ec/regulaciones/constitucion-republica-ecuador ; art. 425 contrastado en https://es.wikisource.org/wiki/Constituci%C3%B3n_de_Ecuador_de_2008/T%C3%8DTULO_IX | O |
| Designación del primer Superintendente (28-03-2024) | Cronología | `cpccs2024superintendente` | https://www.cpccs.gob.ec/2024/03/fabrizio-peralta-superintendente | O |

## Cifras del sector educativo y de la SPDP

| Cifra | Valor | Corte | Fuente (clave) | URL | Tipo |
|---|---|---|---|---|---|
| Instituciones educativas (inicial, básica, bachillerato) | 16 161 | Ciclo 2024-2025 | `eldiario2025estudiantes` (cifras MINEDUC) | https://www.eldiario.ec/ecuador/en-ecuador-hay-mas-de-4-millones-de-estudiantes-de-educacion-basica-y-bachillerado-la-mayoria-asiste-a-instituciones-publicas-23092025/ | S |
| Ídem | 15 400 | Ciclo 2025-2026 (sep. 2025) | ídem | ídem | S |
| Estudiantes / docentes | 4 370 420 / 209 471 | 2024-2025 | ídem | ídem | S |
| CDI en convenio con GAD y OSC | 1 861 | Levantamiento de 2024; informe de nov. 2025 | `cnii2025cdi` | https://www.igualdad.gob.ec/wp-content/uploads/downloads/2025/11/informe_observancia_serv_desarrollo_infantil.pdf | O |
| Niñas y niños < 3 años atendidos por el MIES | ≈ 293 000 (≈ 22 %) | ANII 2021-2025 (citada por CNII 2025) | `cnii2025cdi` | ídem | O |
| Universidades y escuelas politécnicas | 64 (36 públicas, 20 autofinanciadas, 8 cofinanciadas) | Consulta del 27-10-2026 (sin fecha de corte en el portal) | `ces2026estadisticas` | https://www.ces.gob.ec/?page_id=5248 | O |
| Institutos y conservatorios superiores | 216 (62 públicos, 154 particulares) | ídem | ídem | ídem | O |
| DPD registrados ante la SPDP | > 1 150 | Abril de 2025 | `itahora2025spdp` | https://itahora.com/2025/04/16/avances-y-accion-de-la-superintendencia-de-proteccion-de-datos-personales/ | S |
| Cobertura máxima de DPD | 7,0 % = 1 150 / 16 441 (16 161 + 64 + 216) | Cálculo propio | — | — | Derivado |
| Denuncias ante la SPDP | 85 | Abril de 2025 | `itahora2025spdp` | ídem | S |
| Denuncias ante la SPDP | 191 | Septiembre de 2025 | `almeida2025cero` | https://www.primicias.ec/politica/cero-sanciones-ecuador-ley-proteccion-datos-personales-blandengue-104527/ | S |
| Primeras sanciones (LigaPro, FEF) | ≈ USD 454 500 | Diciembre de 2025 | `revelo2025sanciones` | ver bib | S |
| % de universidades que implementaron la LOPDP | No existe dato oficial | — | `piray2026garantias` (solo cualitativo) | https://rus.ucf.edu.cu/index.php/rus/article/view/5877 | A |

## Derecho comparado

| País | Dato | Fuente (clave) | URL | Tipo |
|---|---|---|---|---|
| UE | RGPD arts. 8, 33, 37, 83 | `rgpd2016` | https://eur-lex.europa.eu/eli/reg/2016/679/oj | O (conocido; no se descargó el texto en esta sesión) |
| España | LOPDGDD arts. 7 y 34 | `lopdgdd2018` | https://www.boe.es/eli/es/lo/2018/12/05/3/con | O (ídem) |
| Colombia | Ley 1581 arts. 7, 17, 23; 15 días hábiles (instrucción SIC) | `colombia2012ley1581`, `sic2020incidentes` | https://leyonline.co/laws/ley-1581-de-2012 ; https://www.sic.gov.co/sites/default/files/files/Publicaciones/Guia_gestion_incidentes_dic21_2020.pdf | S / O |
| Perú | 48 h (art. 34 del D.S. 016-2024-JUS); oficial de datos | `peru2024reglamento` | https://lpderecho.pe/reglamento-ley-proteccion-datos-personales-decreto-supremo-016-2024-jus/ | S → `[VERIFICAR]` |
| Chile | Ley 21.719: arts. 14 sexies, 16 quáter, 50, multas (UTM y 2–4 %), vigencia | `chile2024ley21719` | https://www.diariooficial.interior.gob.cl/publicaciones/2024/12/13/44023/01/2583630.pdf | O (texto extraído y leído) |
| Brasil | LGPD arts. 41, 52; Res. CD/ANPD 15/2024 (3 días hábiles) | `brasil2018lgpd`, `anpd2024incidentes` | https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-aprova-o-regulamento-de-comunicacao-de-incidente-de-seguranca | O / S |

## Normas técnicas y métodos

| Referencia | Uso | Clave | URL / DOI | Tipo |
|---|---|---|---|---|
| ISO/IEC 27035-1:2023 (5 fases) | Equivalencia de fases | `iso27035_1_2023` | https://www.iso.org/standard/78973.html | O (catálogo) |
| ISO/IEC 27035-2:2023 | Preparación y lecciones | `iso27035_2_2023` | https://www.iso.org/standard/78974.html | O (catálogo) |
| NIST SP 800-61r3 (03-04-2025; funciones CSF 2.0) | Equivalencia | `nist2025sp80061r3` | doi:10.6028/NIST.SP.800-61r3 | O (Crossref) |
| NIST Privacy Framework 1.1 | Sigue en borrador (IPD 14-04-2025); se mantiene 1.0 | `nist2020privacy` | https://csrc.nist.gov/pubs/cswp/40/nist-privacy-framework-11/ipd | O |
| Coeficiente K | Selección del panel | `cabero2013competencia` | doi:10.13042/brp.2013.65202 | A (Crossref) |
| V de Aiken | Juicio de expertos | `aiken1985three` | doi:10.1177/0013164485451012 | A (Crossref) |
| W de Kendall | Concordancia Delphi | `kendall1939rankings` | doi:10.1214/aoms/1177732186 | A (Crossref) |

## Parámetros de diseño (no son datos empíricos)

Se declaran como decisiones de la metodología y la institución puede ajustarlos:
- Consenso con ≥ 70 % de expertos a ±1 nivel de la mediana.
- V de Aiken ≥ 0,70.
- Plazos de RA-2 (12 meses) y RA-3 (90 días).
- Meta interna de 72 h en la respuesta.
- Metas de los indicadores IV04–IV11 y de la Tabla de indicadores de monitoreo, incluida la disponibilidad ≥ 99,5 %.
