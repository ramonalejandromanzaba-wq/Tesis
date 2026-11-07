# Cuestionario: Datos personales de estudiantes universitarios en Ecuador

> Versión 1.0 (07-11-2026), **antes del juicio de expertos y de la prueba piloto**. Texto listo para copiar en Google Forms o Microsoft Forms.
> Corresponde al Anexo "Cuestionario a estudiantes" de la tesis y a los indicadores IE01–IE15 (Cap. 3).
> Entre corchetes va el **código de la variable** para exportar a CSV y analizar con `scripts/analisis_encuesta.js`. Entre paréntesis van los **códigos numéricos** de cada opción. Los códigos no se muestran al participante.

## Configuración obligatoria del formulario (anonimato)

- **Google Forms:** Configuración → Respuestas → *Recopilar direcciones de correo electrónico* = **No recopilar**; *Limitar a 1 respuesta* = **desactivado** (exige iniciar sesión); *Permitir edición tras enviar* = desactivado. Sin preguntas de carga de archivos (también exigen iniciar sesión).
- **Microsoft Forms:** *Quién puede responder* = **Cualquier persona puede responder**; *Registrar nombre* = desactivado.
- Activar la **lógica de secciones**: si P00, P01 o P02 = "No", ir a la sección final ("Gracias") sin registrar más respuestas.
- Ninguna pregunta es obligatoria salvo P00–P02, para respetar el derecho a no responder.
- Al cerrar la recolección: exportar a CSV, cifrar el archivo, **eliminar las respuestas del servicio** y no subir la base al repositorio.

Tiempo estimado: 8–10 minutos.

---

## Sección 0. Consentimiento y filtros

*(Mostrar antes el texto de `encuesta/consentimiento_informado.md`.)*

**[P00] ¿Acepta participar voluntariamente en esta encuesta anónima?**
- Sí, acepto (1)
- No acepto (0) → fin

**[P01] ¿Tiene 18 años o más?**
- Sí (1)
- No (0) → fin

**[P02] ¿Está matriculado actualmente en una universidad o escuela politécnica del Ecuador?**
- Sí (1)
- No (0) → fin

## Sección A. Datos generales (no identificativos)

> No se pregunta el nombre de su universidad ni ningún dato que permita identificarle.

**[A1] Su universidad es:**
- Pública (1) · Particular cofinanciada (2) · Particular autofinanciada (3) · No lo sé (9)

**[A2] Región en la que se ubica la sede donde estudia:**
- Sierra (1) · Costa (2) · Amazonía (3) · Insular (4) · Estudio totalmente en línea (5)

**[A3] Área de su carrera:**
- Educación (1) · Artes y humanidades (2) · Ciencias sociales, periodismo e información (3) · Administración y derecho (4) · Ciencias naturales, matemáticas y estadística (5) · Tecnologías de la información y la comunicación (6) · Ingeniería, industria y construcción (7) · Agricultura, silvicultura, pesca y veterinaria (8) · Salud y bienestar (9) · Servicios (10)

**[A4] Nivel en el que se encuentra:**
- Nivelación o curso de admisión (0) · 1.º a 3.er nivel (1) · 4.º a 6.º nivel (2) · 7.º nivel o superior (3)

**[A5] Rango de edad:**
- 18 a 20 (1) · 21 a 24 (2) · 25 a 29 (3) · 30 o más (4)

**[A6] Modalidad de estudio:**
- Presencial (1) · Semipresencial o híbrida (2) · En línea o a distancia (3)

## Sección B. Datos que le pidió su universidad (IE01, IE02)

**[B1] Desde su postulación hasta hoy (admisión, matrícula, becas, bienestar, aula virtual u otros trámites), ¿cuáles de estos datos le pidió su universidad?** *(Marque todos los que correspondan.)*
- [B1_01] Identificación (cédula, nombres, fecha de nacimiento)
- [B1_02] Contacto (dirección, teléfono, correo personal)
- [B1_03] Fotografía
- [B1_04] Datos socioeconómicos del hogar (ingresos, vivienda, bienes)
- [B1_05] Datos de familiares o representantes
- [B1_06] Datos de salud (enfermedades, tratamientos, certificados médicos)
- [B1_07] Datos de discapacidad (carné o certificado)
- [B1_08] Autoidentificación étnica
- [B1_09] Datos biométricos (huella, reconocimiento facial)
- [B1_10] Ubicación o geolocalización
- [B1_11] Datos de navegación o actividad en plataformas virtuales
- [B1_99] No recuerdo

*(Cada casilla se exporta como 1 = marcada, 0 = no marcada.)*

**[B2] Cuando le pidieron datos de salud, discapacidad, socioeconómicos o biométricos, ¿le explicaron para qué se usarían?**
- Sí, claramente (1) · Sí, de forma general (2) · No (3) · No recuerdo (4) · No me pidieron esos datos (8)

**[B3] "Mi universidad me pidió solo los datos necesarios para los trámites que realicé."**
- Totalmente en desacuerdo (1) · En desacuerdo (2) · Ni de acuerdo ni en desacuerdo (3) · De acuerdo (4) · Totalmente de acuerdo (5)

## Sección C. Información que recibió (IE03–IE06, IE15)

Para C1 a C4: Sí, claramente (1) · Sí, de forma general (2) · No (3) · No recuerdo (4)

**[C1]** Al entregar sus datos, ¿le informaron **para qué** se usarían?
**[C2]** ¿Le informaron **quién es el responsable** de sus datos y **cómo contactarlo**?
**[C3]** ¿Le informaron **durante cuánto tiempo** se conservarán sus datos?
**[C4]** ¿Le informaron si sus datos se **compartirían con terceros** (otras instituciones, proveedores, plataformas en la nube)?

**[C5] Sobre la política de privacidad o de protección de datos de su universidad:**
- La leí completa (1) · La leí parcialmente (2) · Sé que existe, pero no la leí (3) · No sé si existe (4) · Sé que no existe (5)

**[C6] ¿Le informaron si alguna plataforma de su universidad (aula virtual, supervisión de exámenes en línea, analítica) analiza automáticamente su comportamiento o elabora perfiles?**
- Sí (1) · No (2) · No sé (3) · No uso esas plataformas (8)

## Sección D. Consentimiento (IE07–IE09)

**[D1] ¿Le pidieron su consentimiento para tratar sus datos personales?**
- Sí, de forma expresa (marcando una casilla o firmando) (1) · Sí, de forma implícita ("al continuar, acepta…") (2) · No (3) · No recuerdo (4)

**[D2] ¿Pudo aceptar o rechazar por separado los usos no necesarios para su matrícula (por ejemplo, publicidad o difusión de su imagen)?**
- Sí (1) · No, todo se aceptaba en un solo paso (2) · No me ofrecieron esos usos (3) · No recuerdo (4)

**[D3] "Sentí que podía negarme a entregar datos no indispensables sin perder la matrícula o un servicio."**
- Escala de 1 (totalmente en desacuerdo) a 5 (totalmente de acuerdo)

**[D4] ¿Ha recibido publicidad o mensajes de terceros que usaban datos que solo había entregado a su universidad?**
- Sí (1) · No (2) · No sé (3)

## Sección E. Conocimiento de sus derechos (IE10–IE12)

**[E1] Antes de esta encuesta, ¿sabía que la ley le reconoce estos derechos sobre sus datos?** Sí (1) · No (0)
- [E1_a] **Acceso:** conocer y obtener gratuitamente los datos que la universidad tiene de usted.
- [E1_b] **Rectificación y actualización:** corregir datos inexactos o incompletos.
- [E1_c] **Eliminación:** pedir que se borren sus datos cuando proceda.
- [E1_d] **Oposición:** negarse a ciertos tratamientos de sus datos.
- [E1_e] **Portabilidad:** recibir sus datos en un formato que pueda llevar a otro responsable.

**[E2] ¿Sabe cómo o ante quién ejercer esos derechos en su universidad?**
- Sí, conozco el canal (correo, formulario u oficina) (1) · Sé que existe un canal, pero no cuál es (2) · No (3)

**[E3] ¿Ha solicitado alguna vez a su universidad acceder, corregir o eliminar sus datos?**
- Sí, y me respondieron en un plazo razonable (1) · Sí, pero no me respondieron o tardaron mucho (2) · No (3)

**[E4] ¿Conoce la Ley Orgánica de Protección de Datos Personales (LOPDP)?**
- La he leído total o parcialmente (1) · He oído hablar de ella (2) · No (3)

**[E5] ¿Sabe que existe la Superintendencia de Protección de Datos Personales y que puede presentar reclamos ante ella?**
- Sí (1) · No (0)

**[E6] ¿Su universidad le ha dado información o capacitación sobre protección de datos personales?**
- Sí (1) · No (2) · No recuerdo (3)

## Sección F. Seguridad, confianza e incidentes (IE13, IE14)

Para F1 a F5: escala de 1 (totalmente en desacuerdo) a 5 (totalmente de acuerdo).

- **[F1]** Confío en que mi universidad protege adecuadamente mis datos personales.
- **[F2]** Creo que el personal de mi universidad accede solo a los datos que necesita para su función.
- **[F3]** Me sentiría seguro(a) entregando datos de salud o discapacidad a mi universidad.
- **[F4]** Si mis datos fueran expuestos o robados, mi universidad me lo comunicaría.
- **[F5]** Mi universidad me trata como dueño(a) de mis datos personales.

**[F6] ¿Con qué frecuencia recibe en su cuenta institucional correos sospechosos (que piden contraseñas, pagos o datos)?**
- Nunca (1) · Rara vez (2) · Algunas veces al semestre (3) · Con frecuencia (4) · No tengo cuenta institucional (8)

**[F7] ¿Ha visto publicados por su universidad listados con su número de cédula junto a su nombre, calificaciones o resultados?**
- Sí (1) · No (2) · No sé (3)

**[F8] ¿Su universidad le ha comunicado alguna vez que sus datos se vieron afectados por un incidente de seguridad?**
- Sí (1) · No (2) · No sé (3)

**[F9] (Opcional) ¿Desea añadir algún comentario sobre el tratamiento de sus datos en su universidad?** *Por favor, no escriba nombres, números de cédula, correos ni otros datos que le identifiquen a usted o a otras personas.*
*(Respuesta abierta. En el piloto se añade: "¿Alguna pregunta le resultó confusa? ¿Cuál y por qué?")*

---

### Sección final

Gracias por su participación. Sus respuestas son anónimas y se usarán solo de forma agregada en un trabajo de titulación. Si tiene preguntas: ramonalejandromanzaba@gmail.com

---

## Regla de "respuesta afirmativa" por indicador (para el análisis)

| Indicador | Pregunta(s) | Se cuenta como afirmativo | Se excluye del denominador |
|---|---|---|---|
| IE01 | B1_01 … B1_11 | casilla = 1 (una proporción por categoría) | B1_99 = 1 |
| IE02 | B2 | 1 o 2 | 8 |
| IE03 | C1 | 1 o 2 | — |
| IE04 | C2 | 1 o 2 | — |
| IE05 | C3 | 1 o 2 | — |
| IE06 | C4 | 1 o 2 | — |
| IE07 | D1 | 1 (expreso); se informa aparte el 2 (implícito) | — |
| IE08 | D2 | 1 | 3 |
| IE09 | D3 | 4 o 5 | — |
| IE10 | E1_a … E1_e | 1 (una proporción por derecho; índice = media de los 5) | — |
| IE11 | E2 | 1 | — |
| IE12 | E4, E5, E6 | E4 = 1 o 2; E5 = 1; E6 = 1 | — |
| IE13 | F1 … F5 | media de la escala ≥ 4 (se informan también mediana y RIC) | — |
| IE14 | F6, F7, F8 | F6 = 3 o 4; F7 = 1; F8 = 1 | F6 = 8 |
| IE15 | C6 | 1 | 8 |

Variable de cruce principal: **A1** recodificada como Pública (1) / Particular (2 o 3); se excluye 9 en los cruces.
