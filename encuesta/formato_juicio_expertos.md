# Formato de juicio de expertos — validez de contenido del cuestionario

> Versión 1.0 (07-11-2026). Corresponde al Anexo "Validación del cuestionario y de la ficha por juicio de expertos". Las calificaciones se registran en `encuesta/plantilla_juicio_expertos.xlsx` (V de Aiken automática) y se procesan con `analisis/validacion.py`.

## 1. Carta de invitación (modelo)

Estimado(a) experto(a):

Le invito a participar como juez en la validación del cuestionario de mi trabajo de integración curricular *Diagnóstico y gestión de riesgos en el tratamiento de datos personales de estudiantes universitarios en Ecuador conforme a la LOPDP* (Ingeniería en Tecnologías de la Información, Universidad Tecnológica Indoamérica; tutora: María Cristina Jiménez Hernández, MSc.). El cuestionario es anónimo, está dirigido a estudiantes mayores de edad y mide qué datos les piden sus universidades, qué información reciben, cómo consienten y qué conocen de sus derechos. Su participación consiste en calificar cada ítem (unos 40 minutos) y es voluntaria. En el documento le identificaré solo con un código (J1, J2, …).

Atentamente, Ramón Alejandro Manzaba Castro · ramonalejandromanzaba@gmail.com

## 2. Perfil de los jueces

- **Número:** de 3 a 5. Se invita a 6 para asegurar al menos 3 respuestas completas.
- **Perfiles:** (a) protección de datos personales o derecho informático; (b) seguridad de la información; (c) metodología de la investigación o psicometría. Debe haber al menos un juez de cada perfil.
- **Requisitos:** título de tercer nivel en el área y al menos 3 años de experiencia. Sin conflicto de interés.

Datos del juez (no se publican): código J__ · perfil (a/b/c) · años de experiencia · fecha.

## 3. Criterios y escala

Califique cada ítem en los tres criterios, de 1 a 5:

| Criterio | Pregunta al juez | 1 | 3 | 5 |
|---|---|---|---|---|
| **Pertinencia** | ¿El ítem mide el indicador al que está asignado (tabla de operacionalización)? | No lo mide | Lo mide en parte | Lo mide plenamente |
| **Claridad** | ¿El ítem se entiende sin ambigüedad para un estudiante universitario? | Confuso | Requiere ajustes de redacción | Claro y preciso |
| **Coherencia** | ¿El ítem corresponde a la obligación del artículo de la LOPDP citado? | No corresponde | Corresponde en parte | Corresponde plenamente |

Los valores 2 y 4 son intermedios. Si califica con 3 o menos, anote la redacción que sugiere.

## 4. Hoja de calificación

| Código | Ítem (texto en `cuestionario.md`) | Indicador | Artículo LOPDP | Pertinencia | Claridad | Coherencia | Observaciones |
|---|---|---|---|---|---|---|---|
| P00–P02 | Consentimiento y filtros | — | Arts. 7 y 8 | | | | |
| A1–A4 | Datos generales | — | Art. 10, lit. e | | | | |
| H1 | Datos solicitados | IE01 | Arts. 10, lit. e, y 25 | | | | |
| H2–H3 | Consentimiento pedido y forma | IE07 | Art. 8 | | | | |
| H4 | Finalidad | IE03 | Art. 12, num. 1 | | | | |
| H5 | Responsable | IE04 | Art. 12, num. 8 | | | | |
| H6 | Conservación | IE05 | Art. 12, num. 4 | | | | |
| H7 | Terceros | IE06 | Art. 12, num. 10 | | | | |
| H8 | Consentimiento por finalidad | IE08 | Art. 8 | | | | |
| H9 | Explicación de datos sensibles | IE02 | Arts. 12, num. 1, y 26, lit. a | | | | |
| H10 | Perfiles automatizados | IE15 | Arts. 12, num. 17, y 20 | | | | |
| H11, H16 | Ejercicio y canal de derechos | IE11 | Arts. 12, num. 14, y 13 | | | | |
| H12–H14 | Incidentes y exposiciones | IE14 | Arts. 10, lit. g, 43 y 46 | | | | |
| H15 | Información o capacitación | IE12 | Art. 24 | | | | |
| INF1–INF5 | Información recibida (INF4 inverso) | IE03–IE06 | Arts. 10, lit. c, y 12 | | | | |
| CON1–CON5 | Consentimiento (CON3 inverso) | IE07–IE09 | Art. 8 | | | | |
| DER1–DER7 | Conocimiento de derechos (DER6 inverso) | IE10–IE12 | Arts. 12, nums. 14–16, y 13–17 | | | | |
| CNF1–CNF6 | Confianza y seguridad (CNF3 y CNF6 inversos) | IE13 | Arts. 10, lit. j, 37 y 46 | | | | |

> En la plantilla `.xlsx`, cada ítem se califica por separado (46 ítems × 3 criterios). La tabla anterior agrupa los bloques solo para presentarlos.

**Preguntas abiertas:** (1) ¿Falta algún aspecto de la LOPDP que el cuestionario debería medir? (2) ¿Algún ítem podría identificar a una persona o resultar invasivo? (3) ¿La extensión es adecuada?

## 5. Cálculo y decisión

- **V de Aiken** por ítem y criterio: V = Σ(xᵢ − 1) / [n · (5 − 1)], donde n es el número de jueces.
- **Se conserva** el ítem si V ≥ 0,80 en los tres criterios. Si no, **se corrige** (con las observaciones) o **se elimina**. Cada ajuste se registra en la tabla de ajustes del Cap. 4.
- Con 3 jueces, V ≥ 0,80 exige que la suma de (x − 1) sea al menos 10 de 12 posibles. Con 5 jueces, al menos 16 de 20.
- Los resultados se trasladan al Cap. 4 (Tabla de validez de contenido) solo desde `analisis/salida/aiken_decision.csv`.
