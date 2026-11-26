# PROMPT PARA ANTIGRAVITY — Reestructuración a Enfoque Comparado

> **Pegar completo como prompt en Antigravity (Claude Code).**
> Este prompt reemplaza el enfoque cuantitativo-correlacional anterior por un enfoque de investigación documental comparada de derecho.

---

## REGLAS GLOBALES

1. **EL TÍTULO NO SE MODIFICA.** El título es: *"Metodología para el diagnóstico y gestión de riesgos en el tratamiento de datos personales académicos conforme a la LOPDP"*. No se cambia bajo ninguna circunstancia.
2. **El producto final sigue siendo la METODOLOGÍA** de diagnóstico y gestión de riesgos. Lo que cambia es CÓMO se construye: ya no con encuesta + censo, sino con análisis comparado de marcos jurídicos internacionales + validación por expertos (Delphi).
3. **La tesis sigue siendo conforme a la LOPDP.** Las leyes extranjeras son insumo comparativo para identificar buenas prácticas, brechas y elementos que la metodología debe cubrir. No se propone reformar la LOPDP ni adoptar otra ley.
4. **Resultados siempre agregados.** Ninguna universidad se nombra individualmente.
5. **No es un caso de estudio.** La tesis es investigación documental comparada.
6. Lee los archivos `CLAUDE.md` del repositorio antes de empezar.
7. **Preservar coherencia interna:** cada cambio debe reflejarse en objetivos, marco teórico, metodología, resultados y conclusiones.

---

## 1. CAMBIO DE ENFOQUE METODOLÓGICO

### 1.1 Lo que SE ELIMINA

- **Diseño cuantitativo, no experimental, transversal, descriptivo-comparativo-correlacional.** Reemplazar completamente.
- **Encuesta a estudiantes** (el instrumento completo, cálculo muestral n=384, G*Power, cuotas, difusión QR, Anexo C de consentimiento para encuesta, todo lo relacionado).
- **Censo documental de sitios web** de universidades (los 64 sitios, fichas de observación, índice de transparencia, submuestra de confiabilidad).
- **Hipótesis estadísticas** (H1, H2, H3, H4 y todas las pruebas asociadas: chi-cuadrado, Cramér's V, Mann-Whitney, Spearman, etc.).
- **Indicadores de encuesta** (IE01–IE10, dimensiones INF, CON, DER, PER, PLT).
- **Indicadores documentales del censo** (ID01–ID19 en su forma de "revisar sitio web de cada universidad").
- **Análisis estadístico** (Cronbach's α, McDonald's ω, KR-20, EFA, KMO, Bartlett, kappa ponderado).
- **Tablas de resultados estadísticos** (Tablas 30, 44, frecuencias, cruces).
- **Todo lo que dependa de datos empíricos primarios** recolectados por el tesista vía encuesta o censo.
- **Referencias a "Pichincha"** o ámbito geográfico provincial.

### 1.2 Lo que SE MANTIENE

- **El título** (regla #1).
- **El objetivo general** (desarrollar la metodología de diagnóstico y gestión de riesgos en el tratamiento de datos personales académicos conforme a la LOPDP).
- **El marco teórico sobre la LOPDP** (Capítulo II): principios, derechos, obligaciones, SPDP, bases de legitimación, EIPD, delegado, notificación de vulneraciones, sanciones. Esto se amplía con el análisis comparado.
- **Las fases de la metodología** (Diagnóstico D0–D11 y Gestión de Riesgos G1–G11) como producto final. Se mantienen como estructura pero se alimentan del análisis comparado en lugar de datos empíricos.
- **La validación por juicio de expertos** (panel Delphi, V de Aiken ≥ 0.80, coeficiente de competencia K). Esto es lo que da validez a la metodología.
- **El marco de normas ISO** (27005, 31000, 27035) y estándares de referencia (NIST SP 800-61).
- **La plantilla Excel** como producto entregable de la metodología.
- **El Anexo M: Guía de aplicación** (si ya existe; si no, se crea).
- **Las reglas de ética** (ya no hay encuesta a personas, pero la investigación documental también tiene principios éticos: citar correctamente, no plagiar, respetar derechos de autor).

### 1.3 Lo que SE AGREGA (nuevo enfoque)

**Diseño:** investigación documental, cualitativa-comparativa, con enfoque de derecho comparado funcional. No experimental.

**Método:** análisis comparado de marcos jurídicos de protección de datos personales aplicados al sector de educación superior, complementado con validación Delphi.

---

## 2. MARCOS JURÍDICOS A COMPARAR

La comparación se estructura en 5 marcos jurídicos + Ecuador:

### 2.1 Unión Europea — RGPD (Reglamento General de Protección de Datos)

- **Norma:** Reglamento (UE) 2016/679, vigente desde 25/05/2018.
- **Por qué:** referente mundial; la LOPDP se modeló directamente sobre él. Enfoque basado en riesgos. Tiene la mayor cantidad de guías, jurisprudencia y experiencia de implementación.
- **Foco educativo:** universidades europeas sujetas a GDPR como responsables del tratamiento; guías específicas (Future of Privacy Forum, 2020; Microsoft GDPR for Education).
- **Metodologías de riesgo:** GESTIONA (AEPD España), LIINE4DU (AEPD, 2024), guía de análisis de riesgos de la AEPD, CNIL (Francia), ICO (Reino Unido).
- **Elementos clave para la comparación:** bases de legitimación (art. 6), EIPD (arts. 35-36), DPO (arts. 37-39), protección desde el diseño (art. 25), notificación de brechas (arts. 33-34), transferencias internacionales (Cap. V), sanciones (arts. 83-84).

### 2.2 Estados Unidos — FERPA (+ COPPA, CCPA/CPRA, leyes estatales)

- **Norma principal:** Family Educational Rights and Privacy Act (1974), 20 U.S.C. § 1232g.
- **Normas complementarias:** COPPA (menores de 13), CCPA/CPRA (California), SOPIPA (California), leyes estatales de privacidad estudiantil.
- **Por qué:** único país con legislación sectorial específica para datos educativos. Modelo opuesto al europeo: no hay ley general federal, sino leyes sectoriales. Permite comparar dos filosofías regulatorias distintas (derechos del titular vs. control institucional sobre la divulgación).
- **Foco educativo:** FERPA es 100% educativo: cubre "education records", define excepciones de divulgación, derechos de acceso y corrección.
- **Elementos clave:** definición de "education records", directory information, excepciones de divulgación sin consentimiento, enforcement por el Dept. of Education (no hay derecho de acción privada), student privacy pledges del sector privado.

### 2.3 Brasil — LGPD (Lei Geral de Proteção de Dados Pessoais)

- **Norma:** Lei nº 13.709/2018, vigente desde 18/09/2020. Autoridad: ANPD.
- **Por qué:** regional, inspirada en el RGPD; la ANPD ha publicado guías específicas para tratamiento de datos con fines académicos y de investigación (2022, 2023). Múltiples estudios de implementación en universidades federales brasileñas (compliance LGPD en IES).
- **Foco educativo:** tesis y dissertações sobre LGPD en universidades (UFPE 2024, UFSCar 2024, UFMG 2025); la ANPD publicó el "Guia Orientativo sobre Tratamento de Dados Pessoais para Fins Acadêmicos e de Pesquisa" (2022).
- **Elementos clave:** bases legales (art. 7), datos sensibles (art. 11), tratamiento por el poder público (arts. 23-30, relevante para universidades públicas), RIPD (Relatório de Impacto, equivalente a EIPD), encarregado (equivalente al DPO), sanciones (arts. 52-54).

### 2.4 Colombia — Ley Estatutaria 1581 de 2012

- **Norma:** Ley 1581/2012 + Decreto 1377/2013 (compilado en Decreto 1074/2015). Autoridad: SIC (Superintendencia de Industria y Comercio).
- **Por qué:** contexto institucional más similar al ecuatoriano (país andino, universidades públicas y privadas con estructura comparable, misma tradición jurídica). La SIC tiene experiencia de más de 10 años. Universidades colombianas (UNAL, Externado, Rosario, Javeriana) tienen políticas de protección de datos maduras.
- **Foco educativo:** políticas de tratamiento de datos en IES colombianas; la U. del Rosario publicó análisis integral de seguridad y privacidad en IES (2024); tesis de la Javeriana Cali sobre cumplimiento en instituciones educativas.
- **Elementos clave:** autorización (equivalente al consentimiento), datos sensibles (art. 5), datos de menores (art. 7), Registro Nacional de Bases de Datos (RNBD), deberes de los responsables (art. 17), transferencias e transmisiones, régimen sancionatorio.

### 2.5 Chile — Ley 21.719 de 2024

- **Norma:** Ley 21.719 (publicada 13/12/2024), modifica la Ley 19.628 de 1999. Entra en vigor 01/12/2026. Crea la Agencia de Protección de Datos Personales.
- **Por qué:** la más reciente de la región; modelada directamente sobre el RGPD; permite ver cómo un país latinoamericano con contexto similar adopta el estándar europeo actualizado. Las universidades chilenas (U. de Chile, PUC) ya están definiendo hojas de ruta institucionales.
- **Foco educativo:** artículo de La Tercera sobre desafíos en educación superior; curso de implementación de la U. de Chile (2026); tensiones entre LOTAIP chilena (transparencia) y protección de datos — paralelo directo con Ecuador (LOTAIP ecuatoriana).
- **Elementos clave:** bases de licitud, categorías especiales, EIPD, DPD, protección por diseño y por defecto, régimen sancionatorio con infracciones leves/graves/gravísimas, Agencia como organismo autónomo.

### 2.6 Ecuador — LOPDP (referente central)

- **Norma:** LOPDP (R.O. 459, 26/05/2021) + Reglamento General (Decreto 904, 13/11/2023) + normativa secundaria de la SPDP (guías de riesgos, delegado, gran escala, notificación de vulneraciones, protección desde el diseño).
- **Rol en la tesis:** NO es un marco más para comparar. Es el marco de referencia CONTRA el cual se comparan los otros cinco. La metodología se construye conforme a la LOPDP, enriquecida con las mejores prácticas identificadas en la comparación.

---

## 3. ESTRUCTURA DE LA COMPARACIÓN

### 3.1 Dimensiones de análisis (ejes comparativos)

Comparar los 6 marcos en estas dimensiones, creando una tabla comparativa por cada una:

| # | Dimensión | Pregunta guía |
|---|-----------|---------------|
| D1 | Modelo regulatorio | ¿Ley general, sectorial o mixta? ¿Autoridad independiente? |
| D2 | Definición de datos personales y categorías especiales | ¿Qué se considera dato personal? ¿Qué categorías especiales existen? ¿Incluye datos académicos como categoría? |
| D3 | Bases de legitimación / licitud | ¿Cuántas bases? ¿Cuál aplica al tratamiento educativo? ¿El consentimiento es residual o central? |
| D4 | Derechos del titular | ¿Cuáles reconoce? ¿Incluye portabilidad, suspensión, oposición a decisiones automatizadas? |
| D5 | Obligaciones de información / transparencia | ¿Qué debe informar el responsable? ¿Cuántos elementos? ¿Hay formato obligatorio? |
| D6 | Evaluación de impacto (EIPD / DPIA / RIPD) | ¿Es obligatoria? ¿Cuándo? ¿Hay lista de supuestos? ¿Se consulta a la autoridad? |
| D7 | Gestión de riesgos | ¿Se exige? ¿Hay metodología oficial? ¿Qué escala usa? |
| D8 | Delegado / DPO / encarregado | ¿Es obligatorio? ¿En qué supuestos? ¿Qué funciones tiene? |
| D9 | Protección desde el diseño y por defecto | ¿Lo exige la ley? ¿Hay guía oficial? ¿Hay escala de madurez? |
| D10 | Notificación de vulneraciones (brechas) | ¿Plazos? ¿A quién se notifica? ¿Qué contenido? |
| D11 | Transferencias internacionales | ¿Qué mecanismos? ¿Decisiones de adecuación? ¿Cláusulas contractuales? |
| D12 | Régimen sancionatorio | ¿Montos? ¿Diferencia público/privado? ¿Graduación? |
| D13 | Aplicación específica al sector educativo | ¿Hay norma sectorial? ¿Guías para universidades? ¿Jurisprudencia o resoluciones? |

### 3.2 Producto del análisis comparado

Por cada dimensión, producir:
1. **Tabla comparativa** de los 6 marcos (filas = marcos, columnas = elementos de la dimensión).
2. **Análisis de convergencias:** qué elementos son comunes a la mayoría → estos son los MÍNIMOS que la metodología DEBE cubrir.
3. **Análisis de divergencias:** qué elementos son propios de un marco o de pocos → estos son OPCIONALES o AVANZADOS en la metodología.
4. **Brechas de la LOPDP:** qué elementos existen en otros marcos pero NO en la LOPDP → se documentan como limitaciones o recomendaciones legislativas (Trabajos futuros).
5. **Buenas prácticas adoptables:** qué elementos de otros marcos pueden incorporarse a la metodología SIN necesidad de reforma legal (ej. una lista de verificación más completa, una escala de madurez, un procedimiento de notificación más detallado).

---

## 4. OBJETIVOS ESPECÍFICOS (reformulados)

Reformular los objetivos específicos para que reflejen el nuevo enfoque. Propuesta:

- **OE1:** Analizar comparativamente los marcos jurídicos de protección de datos personales de la Unión Europea (RGPD), Estados Unidos (FERPA), Brasil (LGPD), Colombia (Ley 1581/2012) y Chile (Ley 21.719/2024), identificando sus enfoques de gestión de riesgos y obligaciones aplicables al tratamiento de datos en instituciones de educación superior.

- **OE2:** Identificar convergencias, divergencias y buenas prácticas entre los marcos analizados y la LOPDP ecuatoriana, determinando los elementos que la metodología de diagnóstico y gestión de riesgos debe incorporar.

- **OE3:** Diseñar la metodología de diagnóstico y gestión de riesgos para el tratamiento de datos personales académicos conforme a la LOPDP, integrando las buenas prácticas identificadas en el análisis comparado.

- **OE4:** Validar la metodología propuesta mediante juicio de expertos (método Delphi), evaluando su aplicabilidad, completitud y conformidad normativa.

---

## 5. ESTRUCTURA DEL DOCUMENTO (capítulos)

### Capítulo I — El Problema
- 1.1 Introducción: protección de datos personales en educación superior como problema global; breve panorama internacional y situación en Ecuador.
- 1.2 Planteamiento del problema: ausencia de una metodología específica para datos académicos conforme a la LOPDP.
- 1.3 Justificación: por qué es necesario un enfoque comparado (la LOPDP es joven, otros marcos tienen más experiencia, el sector educativo no tiene guías sectoriales en Ecuador).
- 1.4 Objetivos (general y específicos reformulados).
- 1.5 Alcance y delimitaciones: normativa (fecha de corte 16/11/2026), temática (datos académicos en IES), geográfica (la comparación es internacional; la metodología es para Ecuador).

### Capítulo II — Marco Teórico
- 2.1 Protección de datos personales: evolución histórica y generaciones de leyes.
- 2.2 Datos personales en el sector de educación superior: tipos de datos, titulares, flujos.
- 2.3 Definición de "datos personales académicos" (Om-14 del documento anterior).
- 2.4 Marco normativo ecuatoriano: LOPDP + reglamento + normativa SPDP (con tabla de corpus normativo, fecha de corte 16/11/2026).
- 2.5 Marcos internacionales comparados:
  - 2.5.1 Unión Europea — RGPD
  - 2.5.2 Estados Unidos — FERPA y leyes complementarias
  - 2.5.3 Brasil — LGPD
  - 2.5.4 Colombia — Ley 1581/2012
  - 2.5.5 Chile — Ley 21.719/2024
- 2.6 Gestión de riesgos en protección de datos: ISO 31000, ISO/IEC 27005, ISO/IEC 27035, NIST SP 800-61.
- 2.7 Evaluación de impacto en protección de datos (EIPD/DPIA).
- 2.8 Metodologías de referencia: GESTIONA (AEPD), LIINE4DU, guía SPDP Ecuador, guía ANPD Brasil.
- 2.9 Antecedentes investigativos: estudios previos de comparación LOPDP-RGPD, implementación LGPD en universidades, FERPA en la era del big data.

### Capítulo III — Metodología
- 3.1 Enfoque: cualitativo.
- 3.2 Tipo de investigación: documental, comparativa.
- 3.3 Método: derecho comparado funcional (se comparan las FUNCIONES que cumple cada norma en su contexto, no solo la letra).
- 3.4 Técnicas e instrumentos:
  - **Técnica 1 — Análisis documental:** revisión sistemática de las normas, guías oficiales, resoluciones y jurisprudencia relevante de cada marco.
  - **Técnica 2 — Matrices comparativas:** tablas por dimensión de análisis (D1–D13).
  - **Técnica 3 — Método Delphi:** validación de la metodología por panel de expertos (mínimo 5 jueces con experiencia en protección de datos, derecho TIC o seguridad de la información; diversidad regional y de tipo de universidad).
- 3.5 Procedimiento:
  - Fase 1: Recopilación y sistematización de las normas (OE1).
  - Fase 2: Construcción de matrices comparativas y análisis (OE2).
  - Fase 3: Diseño de la metodología (OE3).
  - Fase 4: Validación Delphi (OE4).
- 3.6 Criterios de rigor: triangulación de fuentes (mínimo 3 tipos de fuente por marco: ley, guía oficial, estudio académico), auditoría del proceso, confirmabilidad (anexar las matrices completas).
- 3.7 Validación del instrumento Delphi: V de Aiken ≥ 0.80, coeficiente de competencia K = ½(Kc+Ka).
- 3.8 Consideraciones éticas: citas correctas, respeto a derechos de autor, no plagio, transparencia en criterios de selección.

### Capítulo IV — Resultados
- 4.1 Resultados del análisis comparado (OE1 y OE2):
  - Tablas comparativas por dimensión (D1–D13).
  - Síntesis de convergencias, divergencias, brechas y buenas prácticas.
  - Tabla resumen: "Elementos que la metodología debe cubrir" (derivados de convergencias) vs. "Elementos opcionales/avanzados" (derivados de divergencias).
- 4.2 La metodología propuesta (OE3):
  - Fase P: Preparación normativa (D0–D2 del esquema anterior).
  - Fase 0: Diagnóstico institucional (D3–D11).
  - Fase 1: Gestión de riesgos (G1–G11).
  - Fase 2: Evaluación de impacto (EIPD).
  - Fase 3: Respuesta a vulneraciones.
  - Fase 4: Monitoreo y mejora continua.
  - Cada fase: objetivo, entradas, actividades, productos, roles, referencia normativa LOPDP, referencia a buena práctica internacional de dónde se adoptó.
- 4.3 Resultados de la validación Delphi (OE4):
  - V de Aiken por criterio e ítem.
  - Observaciones cualitativas de los expertos.
  - Ajustes realizados entre rondas.

### Capítulo V — Conclusiones y Recomendaciones
- 5.1 Conclusiones (una por objetivo específico).
- 5.2 Recomendaciones (para universidades, para la SPDP, para futuras investigaciones).
- 5.3 Limitaciones del estudio.
- 5.4 Trabajos futuros: validación empírica (aplicación piloto de la metodología en una universidad), actualización post-reforma, ampliación a otros titulares (docentes, personal).

### Anexos
- Anexo A: Tabla del corpus normativo (OM-02).
- Anexo B: Matrices comparativas completas (D1–D13) con las 6 jurisdicciones.
- Anexo C: Fichas de cada marco jurídico (resumen estructurado por país).
- Anexo D: Tabla "Finalidad → base de legitimación" para universidades ecuatorianas.
- Anexo E: Lista de verificación de EIPD obligatoria.
- Anexo F: Perfil institucional (checklist).
- Anexo G: Escala de madurez de protección de datos.
- Anexo H: Instrumento de validación Delphi + resultados.
- Anexo I: Perfiles de expertos del panel Delphi.
- Anexo J: Plantilla Excel de la metodología (instrucciones hoja por hoja).
- Anexo K: Guía de aplicación de la metodología (Anexo M anterior).

---

## 6. OBSERVACIONES ANTERIORES QUE SE MANTIENEN

Las siguientes observaciones del documento `observaciones_tesis_v3.md` siguen siendo válidas con el nuevo enfoque. Aplicarlas:

| Observación | Qué se mantiene | Adaptación |
|-------------|-----------------|------------|
| OM-02 | Fecha de corte normativa 16/11/2026 + tabla de corpus | Sin cambios |
| OM-03 | Bases de legitimación: consentimiento no es la base de todo + tabla finalidad→base | Sin cambios; ahora se refuerza con la comparación (ej. RGPD art. 6, LGPD art. 7) |
| OM-04 | Derechos faltantes: suspensión (art. 19) y decisiones automatizadas (art. 20) | Sin cambios; la comparación mostrará qué derechos reconoce cada marco |
| OM-05 | Protección desde el diseño; escala de madurez | Sin cambios; la comparación incluye art. 25 RGPD y guía SPDP |
| OM-06 | Lista de supuestos de EIPD independiente de la matriz | Sin cambios; se compara con listas de RGPD art. 35.3 y CNIL |
| OM-08 | Reglas para encuesta institucional (Fase 0 de la metodología) | Se mantiene como parte de la Guía de aplicación |
| OM-09 | Oficio sin respaldo: eliminar afirmación o conseguirlo | Sin cambios |
| Om-10 | Cobertura de los 17 numerales del art. 12 | Sin cambios |
| Om-11 | Inventario de encargados y transferencias | Sin cambios; se enriquece con la comparación de transferencias internacionales |
| Om-12 | Tabla de retención de documentos | Sin cambios |
| Om-13 | LOTAIP y minimización | Sin cambios; se compara con tensión transparencia/privacidad en Chile |
| Om-14 | Definición de "datos personales académicos" | Sin cambios |
| Om-15 | Responsabilidad proactiva (RF13) | Sin cambios; se compara con accountability del RGPD |
| Om-16 | Régimen de sanciones público/privado | Sin cambios; la comparación incluye sanciones de cada marco |
| Om-17 | Escenarios de extracción de datos | Se mantiene en la metodología de riesgos |
| Om-18 | Plataformas educativas (aulas virtuales) | Se mantiene como elemento de la metodología |

**Observaciones que YA NO APLICAN** (porque dependían del censo o la encuesta):
- OM-01: el cambio a ámbito nacional ya no es relevante porque no hay encuesta ni censo.
- OM-07: cumplimiento de la LOPDP en la encuesta de la tesis ya no aplica (no hay encuesta).
- Toda referencia a indicadores IE01–IE10, dimensiones INF/CON/DER/PER/PLT, hipótesis H1–H4, pruebas estadísticas, n=384, cuotas, etc.

---

## 7. FUENTES CLAVE POR MARCO (punto de partida)

### Unión Europea
- Reglamento (UE) 2016/679 (RGPD) — texto oficial EUR-Lex
- AEPD, "Guía de análisis de riesgos en el tratamiento de datos personales" (2024)
- AEPD, "LIINE4DU: metodología para el modelado de amenazas para la privacidad" (2024)
- Future of Privacy Forum, "The GDPR: Analysis and Guidance for US Higher Education" (Zanfir-Fortuna, 2020)
- CNIL, guías de EIPD
- Junta de Andalucía, "Metodología corporativa para la gestión del riesgo de protección de datos" (2026)

### Estados Unidos
- FERPA, 20 U.S.C. § 1232g; 34 CFR Part 99
- COPPA, 15 U.S.C. §§ 6501–6506
- NCES, "Forum Guide to Protecting the Privacy of Student Information" (2004)
- EPIC, análisis de FERPA
- Artículo "Beyond Compliance: Students and FERPA in the Age of Big Data" (Journal of Intellectual Freedom and Privacy)

### Brasil
- Lei nº 13.709/2018 (LGPD)
- ANPD, "Guia Orientativo sobre Tratamento de Dados Pessoais para Fins Acadêmicos e de Pesquisa" (2022)
- ANPD, "Estudo Técnico: A LGPD e o Tratamento de Dados Pessoais para Fins Acadêmicos" (2023)
- Almeida, W.G. (2024), "Implementação de compliance à LGPD em IFES" (UFSCar)
- Barros, Y.C. (2024), "Privacidade de dados em contexto educacional" (UFPE)
- Artículo en Perspectivas em Ciência da Informação (2025), multi-caso en IES

### Colombia
- Ley Estatutaria 1581 de 2012 + Decreto 1377/2013
- Universidad Nacional de Colombia, Resolución 207 de 2021 (Política de Tratamiento de Datos Personales)
- Universidad Externado de Colombia, Resolución Rectoral 058/2024 (Política actualizada)
- Universidad del Rosario, "Una mirada integral a la seguridad y privacidad de los datos personales en IES" (2024)
- Grajales Cuellar (Javeriana Cali), "Recomendaciones para el cumplimiento en IES"

### Chile
- Ley 21.719 (13/12/2024) — texto en BCN
- Gobierno de Chile, "Guía práctica de implementación de la nueva ley de datos personales" (2025)
- U. de Chile, "Hoja de ruta institucional para protección de datos personales" (2026)
- La Tercera, "Educación superior y datos personales: el desafío pendiente en las aulas chilenas"
- DLA Piper, "Chile establece nueva Ley de Protección de Datos" (2024)

### Ecuador
- LOPDP (R.O. 459, 26/05/2021)
- Reglamento General (Decreto 904, R.O. 435, 13/11/2023)
- Guías SPDP: riesgos v1 y v2, delegado, gran escala, notificación, protección desde el diseño
- Artículo en Revista de Privacidad de la AEPD: "Gestión de riesgos y protección de datos: la tecnificación normativa ecuatoriana frente al paradigma europeo"
- García Roldán (ULEAM, 2024), "El impacto del RGPD en las políticas de protección de datos en Ecuador"
- Pérez Vaca (UOC, 2021), "La regulación de protección de datos en Ecuador: análisis comparativo con el RGPD"
- Iza & Mora (UPS, 2023), "Análisis comparativo de la LOPDP con México"

---

## 8. INSTRUCCIONES DE IMPLEMENTACIÓN EN LATEX

1. **Leer todo el .tex actual** antes de hacer cambios.
2. **Hacer backup** del estado actual del repositorio (crear tag o branch).
3. **Trabajar sección por sección**, no todo de golpe. Orden sugerido:
   - Primero: Capítulo III (Metodología) — es el cambio más grande.
   - Segundo: Objetivos específicos (1.4).
   - Tercero: Capítulo II (Marco Teórico) — ampliar con secciones de marcos internacionales.
   - Cuarto: Capítulo I (ajustar planteamiento y justificación).
   - Quinto: Capítulo IV (crear estructura de resultados vacía con tablas comparativas placeholder).
   - Sexto: Eliminar secciones del enfoque anterior que ya no apliquen.
   - Séptimo: Anexos.
4. **No borrar contenido del marco teórico sobre la LOPDP** — ampliarlo.
5. **Marcar con `% TODO:` los contenidos que requieren investigación posterior** (ej. llenar las tablas comparativas con el contenido real de cada norma).
6. **Verificar que todas las referencias bibliográficas se actualicen** en el .bib.
7. **Compilar y verificar** que no haya errores de LaTeX después de cada sección.

---

## 9. LISTA DE VERIFICACIÓN

- [ ] Título intacto
- [ ] Objetivo general intacto
- [ ] Objetivos específicos reformulados (OE1–OE4)
- [ ] Todo contenido de encuesta/censo/hipótesis estadísticas eliminado
- [ ] Capítulo III reescrito con enfoque documental comparado + Delphi
- [ ] Capítulo II ampliado con secciones de marcos internacionales (2.5.1–2.5.5)
- [ ] 13 dimensiones de análisis definidas (D1–D13) con tablas placeholder
- [ ] Tabla de corpus normativo creada (OM-02)
- [ ] Tabla de finalidad → base de legitimación mantenida (OM-03)
- [ ] Fases de la metodología (D0–D11, G1–G11) mantenidas como producto
- [ ] Validación Delphi mantenida y descrita
- [ ] Observaciones vigentes del documento anterior aplicadas
- [ ] Sin referencias a Pichincha, encuesta, censo, n=384, chi-cuadrado, etc.
- [ ] Fuentes clave citadas en .bib
- [ ] Compilación sin errores
