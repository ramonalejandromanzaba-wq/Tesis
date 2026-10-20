# CLAUDE.md — Tesis ITI-TFG-B26-0021

> Archivo de contexto para Claude Code. Colócalo en la raíz del repositorio de la tesis.
> Todo el trabajo académico se produce en **español** (registro formal, tercera persona impersonal).

---

## 1. Identificación del proyecto

| Campo | Valor |
|---|---|
| Código | ITI-TFG-B26-0021 |
| Título | Metodología para el diagnóstico y gestión de riesgos en el tratamiento de datos personales académicos conforme a la LOPDP |
| Estudiante | Ramón Alejandro Manzaba Castro (Nivel 8, Quito) |
| Docente proponente | Jaime Fabrizzio Peñafiel Cano (coordinador) |
| Lectores sugeridos | María Cristina Jiménez Hernández; Franklin Marcelo Tandalla Quimbita |
| Carrera / sede / período | ITI · Quito · B26 · Presencial |
| Modalidad TFG | Desarrollo de un trabajo de integración curricular |
| Institución | Universidad Tecnológica Indoamérica (UTI), Facultad de Ingenierías (institución privada) |
| Línea / sublínea | Gestión de la Información / Gobernanza y seguridad de la información |
| Eje | Tecnologías para la educación |
| Duración prevista | 6 meses, dedicación completa |
| Estado de la propuesta | Enviada (05/08/2026) |

## 2. Objetivos (texto oficial de la ficha — no reformular sin autorización)

**Objetivo general:** Diseñar una metodología de diagnóstico y gestión de riesgos para el tratamiento de datos personales de estudiantes y docentes, aplicable a instituciones de educación superior, alineada a la LOPDP.

**Objetivos específicos:**
1. Revisar los procesos actuales de tratamiento de datos personales en la institución/unidad seleccionada.
2. Diseñar las fases de la metodología (identificación, evaluación, mitigación, monitoreo de riesgos).
3. Aplicar la metodología en un caso de estudio real o simulado dentro de la institución.
4. Elaborar una matriz de riesgos derivada de la aplicación del caso de estudio.
5. Formular recomendaciones de mejora continua alineadas a la LOPDP.

**Versión mejorada en la tesis (autorizada por el autor el 2026-10-20; pendiente de visto bueno de la tutora).** Formato: verbo en infinitivo + qué + cómo (mediante…) + para qué (para…), con referencia a la LOPDP (2021) y su Reglamento General (2023). Mismo contenido y trazabilidad OE1–OE5; texto vigente en `Capítulos/01_Introducción.tex` y `tesis/cap1.md`. Cambio de verbo: OE1 "Revisar" → "Diagnosticar".

**Exclusiones (respetarlas siempre):** no incluye certificación legal ante la autoridad, no cubre la implementación completa de las medidas correctivas, no abarca auditoría externa independiente.

**Producto esperado:** documento metodológico + matriz de riesgos aplicada (plantilla reutilizable en hoja de cálculo o sistema simple de registro).

**Tipo de investigación:** aplicada, descriptivo-propositiva. Fases: (1) diagnóstico situacional, (2) diseño metodológico, (3) aplicación en caso de estudio, (4) validación con actores institucionales, (5) documentación final.

### Trazabilidad objetivo → fase → entregable

| OE | Fase de investigación | Entregable | Capítulo |
|---|---|---|---|
| OE1 | Diagnóstico situacional | Inventario de procesos / RAT preliminar, informe de diagnóstico | Cap. 3–4 |
| OE2 | Diseño metodológico | Documento de la metodología por fases | Cap. 4 |
| OE3 | Aplicación | Expediente del caso de estudio (anonimizado) | Cap. 4 |
| OE4 | Aplicación | Matriz de riesgos (inherente y residual) | Cap. 4 + anexo .xlsx |
| OE5 | Validación + documentación | Plan de tratamiento y mejora continua; validación con actores | Cap. 4–5 |

---

## 3. Marco normativo ecuatoriano (base obligatoria)

> Regla: **nunca citar un número de artículo, resolución o fecha sin verificarlo contra la fuente oficial** (Registro Oficial, spdp.gob.ec). Si no se puede verificar, marcar `[VERIFICAR]`.

### 3.1 Normas principales
- **LOPDP** — Ley Orgánica de Protección de Datos Personales (Registro Oficial, 5.º Suplemento N.º 459, 26-05-2021). [VERIFICAR número de suplemento al citar]
- **RLOPDP** — Reglamento General a la LOPDP (Decreto Ejecutivo N.º 904, nov. 2023). [VERIFICAR datos de publicación]
- Autoridad de control: **Superintendencia de Protección de Datos Personales (SPDP)** — spdp.gob.ec.

### 3.2 Artículos LOPDP más relevantes para la tesis
| Tema | Art. (verificar) | Uso en la tesis |
|---|---|---|
| Definiciones (dato personal, responsable, encargado, DPD) | 4 | Marco conceptual |
| Legitimidad del tratamiento (bases legales) | 7 | Vulnerabilidades jurídicas |
| Consentimiento (libre, específico, informado, inequívoco) | 8 | Escenarios de riesgo jurídico |
| Principios (incl. pertinencia y minimización) | 10 | Criterios de auditoría jurídica |
| Derechos de los titulares | 12–24 aprox. | Mecanismos de ejercicio de derechos |
| Categorías especiales de datos | 25–26 | Datos de salud, discapacidad, NNA, etc. |
| Medidas de seguridad | 37 | Escenarios C-I-D |
| Análisis de riesgo, amenazas y vulnerabilidades | 40 | **Núcleo de la metodología** |
| Evaluación de impacto (EIPD) | 42 | Salida de la etapa de evaluación |
| Notificación de vulneraciones (plazo de 5 días) | 43 | Monitoreo / respuesta |
| Delegado de Protección de Datos | 48 | Gobernanza |
| Infracciones y sanciones | Título de régimen sancionatorio | Impacto para el responsable |

### 3.3 Resoluciones SPDP pertinentes
| Resolución | Contenido | Relevancia |
|---|---|---|
| **SPDP-SPD-2025-0003-R** | **Guía de Gestión de Riesgos y Evaluación de Impacto** (v1 2025; **v2 publicada en 2026**) | **Referencia principal de la metodología** |
| SPDP-SPD-2025-0004-R | Programa profesionalizante de DPD | Gobernanza |
| SPDP-SPD-2025-0006-R | Clausulado obligatorio en contratos | Relación con encargados (proveedores LMS, nube) |
| SPDP-SPD-2025-0022-R | Metodología de cálculo de multas y gravedad | Impacto financiero / jurimetría |
| SPDP-SPD-2025-0028-R | Reglamento del DPD | El DPD no ejecuta la gestión de riesgos; solo emite observaciones no vinculantes |
| SPDP-SPD-2025-0030-R | Seudonimización, anonimización, bloqueo y eliminación | Controles; manejo de datos del caso de estudio |
| SPDP-SPD-2025-0041-R | Interés legítimo como base de legitimación | Bases legales |
| SPDP-SPD-2026-0004-R | Transferencias nacionales e internacionales | Servicios en nube (Google/Microsoft, LMS SaaS) |
| SPDP-SPD-2026-0005-R | Tratamiento a gran escala (Modelo Técnico de Gran Escala) | Determinar si la IES trata a gran escala → EIPD/DPD |
| SPDP-SPD-2026-0009-R (reformada por 0037-R) | Datos personales en sistemas de IA | Proctoring, analítica académica, chatbots |
| SPDP-SPD-2026-0039-R | Datos biométricos | Control de acceso/asistencia biométrica |
| SPDP-SPD-2026-0040-R | Norma técnica de notificación de vulneraciones | Etapa de monitoreo y respuesta |
| Guía DevPrivOps (SPDP, 2025, beta) | Niveles de madurez por principio | Insumo para el diagnóstico de madurez |

Listado oficial: https://spdp.gob.ec/resoluciones2/

---

## 4. La Guía SPDP de gestión de riesgos (v2, 2026) — reglas que la metodología DEBE respetar

Fuente: https://spdp.gob.ec/wp-content/uploads/2026/03/ggrispdp2026v2.pdf (autor: Luis Enríquez Álvarez, SPDP).

1. **Cinco etapas obligatorias** + comunicación y monitoreo: establecimiento del contexto → identificación → análisis → evaluación → tratamiento. La guía recomienda ISO/IEC 27005:2022.
2. **La EIPD no puede hacerse sin las etapas previas** (contexto, identificación, análisis). La guía recomienda hacer EIPD por defecto en cualquier tratamiento.
3. **Rationales obligatorios:** todo valor de probabilidad o impacto debe estar justificado (cuantitativo: frecuentista, bayesiano, Monte Carlo, predicción conformal; cualitativo: opinión de expertos calibrada — Delphi con al menos 5 expertos, modelo Lens).
4. **Una escala 1–3 o 1–5 NO es análisis cuantitativo**; son etiquetas. No presentarlo como tal.
5. **Las matrices de calor sirven para representar, no para calibrar.** No multiplicar probabilidad × impacto por defecto; los riesgos de baja probabilidad y muy alto impacto requieren tratamiento propio (los derechos pesan más que los activos).
6. **Modelos separados para confidencialidad, integridad y disponibilidad.**
7. **Probabilidad siempre referida a un lapso** (p. ej., anual).
8. **Riesgo inherente vs. residual** con definiciones de la guía.
9. **Criterios de evaluación de impacto** a considerar: categorías especiales de datos, grupos vulnerables, número de titulares afectados, naturaleza de la infracción/vulneración, volumen de datos.
10. **Vulnerabilidades en cuatro tipos:** jurídicas, de grupos vulnerables de titulares, organizacionales, técnicas.
11. **Escenarios de riesgo** con: comunidad de amenaza, perfil, vector, vulnerabilidades, impacto primario y secundario (doble perspectiva: titular y responsable).
12. **Lo que importa es el “ser”, no el “deber ser”:** auditar la práctica, no solo la política escrita.
13. Validación de estimaciones: Brier score / log loss.
14. Integración DPD ↔ seguridad de la información ↔ jurídico ↔ riesgos.
15. Auditorías jurídicas, organizacionales y técnicas.

### Mapeo de las fases de la ficha a la guía
| Fase en la ficha (OE2) | Etapa(s) Guía SPDP / ISO 27005 |
|---|---|
| Identificación | Establecimiento del contexto + Identificación de riesgos |
| Evaluación | Análisis de riesgos + Evaluación de riesgos (incl. EIPD) |
| Mitigación | Tratamiento de riesgos (controles jurídicos, organizacionales, técnicos) |
| Monitoreo | Monitoreo y revisión + comunicación (incl. notificación de vulneraciones, Res. 0040-R) |

Proponer explícitamente una **fase 0 de diagnóstico/madurez** (alineada a OE1) antes de la identificación.

---

## 5. Marcos y referencias complementarias

- ISO 31000:2018 (principios de gestión del riesgo); ISO/IEC 31010 (técnicas de evaluación).
- ISO/IEC 27005:2022 (gestión de riesgos de seguridad de la información) — recomendada por la SPDP.
- ISO/IEC 27001:2022 y 27002:2022 (controles; p. ej., 5.15 control de acceso, 8.10 eliminación).
- ISO/IEC 27701 (gestión de privacidad); ISO/IEC 29134 (guía de EIPD).
- FAIR / Open Group O-RT (modelo cuantitativo); ENISA (severidad de violaciones de datos, 2013).
- AEPD: *Gestión del riesgo y evaluación de impacto en tratamientos de datos personales*.
- NIST Privacy Framework; NIST SP 800-30.
- EGSI (Esquema Gubernamental de Seguridad de la Información) — referencia para el sector público ecuatoriano.
- Bibliografía citada por la guía SPDP: Hubbard & Seiersen (2016); Freund & Jones (2015); Gellert (2020); Malgieri (2023); Kahneman et al. (2021).
- Marco de auditoría ya conocido por el estudiante: normas CGE (NCI serie 410), Manual de Auditoría Informática — útil para formatos de hallazgos.

---

## 6. Dominio: datos personales en una IES

**Titulares:** estudiantes (incluidos posibles menores de edad en admisión), docentes, personal administrativo, aspirantes, graduados, padres/representantes.

**Procesos candidatos a inventariar (RAT):** admisión y matrícula; gestión de calificaciones y récord académico; becas y ayudas (datos socioeconómicos, discapacidad); bienestar estudiantil y servicio médico/psicológico (datos de salud = sensibles); LMS / aula virtual; correo y suite institucional en nube; biblioteca y repositorio de tesis; titulación y reportes a entes de control de educación superior; gestión docente (talento humano, evaluaciones docentes); control de acceso o asistencia (posible biometría); videovigilancia; proctoring o analítica con IA; repositorios de código (GitLab institucional).

**Categorías especiales probables:** salud, discapacidad, datos de NNA, datos socioeconómicos, biométricos, etnia (si se recoge en formularios).

**Amenazas típicas del sector:** phishing a cuentas institucionales, credenciales comprometidas en LMS, accesos con privilegios excesivos de personal administrativo, ransomware, exposición de listados de notas o datos en canales públicos, proveedores SaaS sin cláusulas de protección de datos, conservación indefinida de expedientes.

---

## 7. Caso de estudio — decisiones abiertas

- [x] Unidad o proceso a analizar: **proceso de admisión y matrícula de la UTI, sede Quito** (decisión del autor, 2026-10-20).
- [x] Real vs. simulado: **real**, con datos por levantar. [ ] Pendiente: autorización formal de la unidad legal/datos de la UTI.
- [ ] Tutor asignado (confirmar si es el docente proponente).
- [ ] Plantilla institucional de tesis y norma de citación vigente (asumir **APA 7.ª ed.** hasta confirmar).
- [ ] Actores para validación (DPD institucional si existe, TI, jurídico, secretaría académica) y panel de expertos para Delphi (≥ 5).

**Conflicto de interés:** el estudiante tiene rol de sysadmin en la infraestructura institucional (incluido un servidor GitLab CE). Si un sistema que administra entra en el caso de estudio, declararlo en la metodología y usar solo información autorizada.

---

## 8. Confidencialidad y ética (reglas duras)

- **Ningún dato personal real en el repositorio.** Usar datos ficticios, seudonimizados o agregados (ver Res. SPDP-SPD-2025-0030-R).
- Nombres de funcionarios entrevistados → códigos (E01, E02…). Consentimiento informado para entrevistas y encuestas.
- No subir evidencia institucional sensible (capturas, exportes de bases) sin anonimizar.
- Los hallazgos sobre la institución se redactan en términos de procesos y controles, no de personas.

---

## 9. Especificación de la matriz de riesgos (OE4)

Hoja de cálculo reutilizable (.xlsx), una fila por escenario de riesgo:

`ID | Proceso | Actividad de tratamiento | Categorías de datos | ¿Categoría especial? | Titulares (tipo y nº estimado) | Grupo vulnerable | Activo/sistema | Dimensión (C/I/D/Licitud) | Comunidad de amenaza | Vector | Vulnerabilidad (tipo: jurídica/organizacional/técnica/titulares) | Art. LOPDP / norma SPDP | Control existente | Probabilidad inherente (lapso anual) | Rationale prob. | Impacto inherente (titular) | Impacto (responsable) | Rationale impacto | Nivel inherente | Tratamiento (mitigar/transferir/evitar/aceptar) | Control propuesto (ref. ISO 27002) | Responsable | Plazo | Probabilidad residual | Impacto residual | Nivel residual | Indicador de monitoreo | Estado`

Hojas adicionales: criterios de probabilidad, criterios de impacto (cualitativo, basado en ENISA/guía SPDP), criterios de aceptación del riesgo, catálogo de amenazas, catálogo de controles, resultados Delphi, cálculo de Brier score.

Niveles: muy bajo, bajo, medio, alto, muy alto (consistente con la guía SPDP). Incluir regla explícita para baja probabilidad / alto impacto.

---

## 10. Estructura de la tesis (ajustar a la plantilla UTI)

1. Introducción (problema, justificación, objetivos, alcance y limitaciones)
2. Marco teórico y normativo (LOPDP, RLOPDP, normativa SPDP, ISO, estado del arte de metodologías PIA/EIPD, trabajos relacionados en IES)
3. Metodología de la investigación (enfoque, tipo, población/muestra, instrumentos, procedimiento)
4. Resultados: diagnóstico (OE1), metodología propuesta (OE2), aplicación (OE3), matriz (OE4), validación
5. Conclusiones y recomendaciones (OE5)
Referencias · Anexos (instrumentos, matriz, consentimiento, RAT)

### Estructura de repositorio sugerida
```
/tesis           capítulos en .md (borradores) y la versión final .docx
/fuentes         PDF de normas y artículos (+ fichas de lectura .md)
/instrumentos    cuestionario de madurez, guía de entrevista, checklist de auditoría jurídica
/caso-estudio    insumos anonimizados, RAT
/matriz          plantilla y matriz aplicada (.xlsx)
/scripts         utilidades (generación .docx, cálculos Monte Carlo/Brier en Python)
referencias.bib
```

---

## 11. Instrucciones de trabajo para Claude

- Estilo del usuario: conciso, directivo, mínima iteración. Ejecutar de forma autónoma y decidir por defecto; preguntar solo si una decisión es irreversible o depende de información institucional.
- Redacción académica en español; APA 7 salvo indicación contraria; citas parafraseadas.
- **No inventar** referencias, DOIs, artículos de ley ni números de resolución. Si falta la fuente, dejar `[CITA PENDIENTE]` o `[VERIFICAR]`.
- Priorizar fuentes primarias: Registro Oficial, spdp.gob.ec, normas ISO, artículos indexados (Scopus/WoS, 2020+).
- Cada afirmación de la metodología debe trazarse a: un objetivo específico, una etapa de la guía SPDP y un artículo de la LOPDP.
- Documentos .docx: editar **la plantilla institucional original** a nivel XML (Python + zipfile), nunca generar desde cero; preservar logos y encabezados; consolidar runs antes de reemplazos; reempaquetar con `zip -Xr` desde el directorio desempaquetado.
- Hojas de cálculo: fórmulas reales (no valores pegados), validación de datos para listas, formato condicional para niveles.
- Antes de cerrar un capítulo: verificar coherencia con objetivos, alcance y exclusiones de la sección 2.

---

## 12. Fuentes base

- Ficha institucional ITI-TFG-B26-0021 (UTI, generada 13/10/2026).
- SPDP — Resoluciones: https://spdp.gob.ec/resoluciones2/
- SPDP — Guía de gestión de riesgos y EIPD v2 (2026): https://spdp.gob.ec/wp-content/uploads/2026/03/ggrispdp2026v2.pdf
- SPDP — Guía v1 (Res. 0003-R, 2025): https://spdp.gob.ec/resolucion-n-spdp-spd-2025-0003-r-guia-de-gestion-de-riesgos-y-evaluacion-de-impacto-del-tratamiento-de-datos-personales-con-su-anexo/
- SPDP — Guía DevPrivOps (beta, 2025): https://spdp.gob.ec/wp-content/uploads/2025/08/GUIA-DE-DEVPRIVOPSBETA8-28-07-2025.pdf
- AEPD — Gestión del riesgo y EIPD: https://www.aepd.es/guias/gestion-riesgo-y-evaluacion-impacto-en-tratamientos-datos-personales.pdf
