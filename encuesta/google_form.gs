/**
 * Crea el formulario de Google Forms de la encuesta (cuestionario v2.2, 55 preguntas).
 * GENERADO por scripts/generar_google_form.py a partir de analisis/config.py y encuesta/consentimiento_informado.md.
 * No editar a mano: si cambia el cuestionario, se cambia config.py y se vuelve a generar.
 *
 * Uso: script.google.com → Nuevo proyecto → pegar este archivo → completar VERIFICACION_ETICA → ejecutar crearFormulario.
 */

// Número y fecha del oficio de verificación ética de la UTI (Anexo L). La encuesta NO se abre sin este dato.
const VERIFICACION_ETICA = '';
// true solo para la prueba piloto: añade la pregunta abierta sobre preguntas confusas.
const PILOTO = false;

const DATOS = {
 "titulo": "Encuesta: Datos personales de estudiantes universitarios del Ecuador",
 "consentimiento": "Le invitamos a participar en una encuesta para un Trabajo de Integración Curricular de la carrera de Ingeniería en Tecnologías de la Información de la Universidad Tecnológica Indoamérica. La encuesta está dirigida a estudiantes de grado de todas las universidades y escuelas politécnicas del Ecuador, públicas y privadas.\n\n¿Quién es el responsable de sus datos? Ramón Alejandro Manzaba Castro, estudiante investigador, bajo la tutoría de María Cristina Jiménez Hernández, MSc. Contacto: ramonalejandromanzaba@gmail.com. Por tratarse de una investigación individual, no existe un delegado de protección de datos.\n\n¿Para qué es la encuesta? Para conocer qué datos personales piden las universidades y escuelas politécnicas a sus estudiantes, si les informan para qué los usan, cómo obtienen su consentimiento cuando hace falta y qué saben los estudiantes sobre sus derechos según la Ley Orgánica de Protección de Datos Personales (LOPDP). Las respuestas no se usarán para ninguna otra finalidad.\n\n¿Con qué base legal? Con su consentimiento, libre, específico, informado e inequívoco (LOPDP, arts. 7, num. 1, y 8), que usted da al marcar \"Sí, acepto\".\n\n¿Qué se hará con sus respuestas? Se recogen en un formulario en línea, se guardan en una base de datos de la investigación y se analizan con estadística; los resultados se publican solo de forma agregada (porcentajes del conjunto, nunca respuestas individuales ni resultados de una universidad en particular). No se toman decisiones automatizadas sobre usted ni se elaboran perfiles.\n\n¿Quién más tiene acceso? (encargado y transferencia internacional) Las respuestas se almacenan en Google Forms, servicio de Google LLC. Ese proveedor actúa como encargado del tratamiento y sus servidores pueden estar fuera del Ecuador, lo que constituye una transferencia internacional. No se comunican las respuestas a ninguna otra persona o institución.\n\n¿Quién puede participar? Personas de 18 años o más que estudien actualmente una carrera de grado en una universidad o escuela politécnica del Ecuador.\n\n¿Qué datos se recogen? No le pediremos su nombre, número de cédula, correo electrónico, número de matrícula ni teléfono; el formulario no registra su correo, no exige iniciar sesión y no permite subir archivos. Le preguntaremos en qué universidad estudia (puede elegir \"Prefiero no responder\") y, de forma opcional, la región: esos datos se usan solo para el análisis interno y nunca se publicará un resultado por universidad. Las preguntas generales usan rangos (por ejemplo, de edad). No se le preguntará por su salud ni por una posible discapacidad; solo si su universidad le pidió ese tipo de datos. Como algunas respuestas combinadas podrían, en teoría, acercarse a una persona, la base se trata como seudonimizada y no como anónima: en el análisis la universidad se reemplaza por un código y no se cruza con el semestre. Los datos se recogen directamente de usted.\n\n¿Es obligatoria? No. Su participación es voluntaria y no recibirá compensación. Negarse o dejar preguntas sin responder no tiene ninguna consecuencia para usted; si una respuesta es errónea, solo afecta la calidad del análisis estadístico. Puede abandonar la encuesta en cualquier momento cerrando la página; lo que no envíe no se registrará.\n\n¿Puedo retirar mi consentimiento y ejercer mis derechos? Sí. Puede revocar su consentimiento y ejercer los derechos de acceso, rectificación y actualización, eliminación, oposición, portabilidad, suspensión del tratamiento y a no ser objeto de decisiones automatizadas escribiendo a ramonalejandromanzaba@gmail.com. Como no se recogen datos que le identifiquen directamente, es posible que no podamos localizar sus respuestas una vez enviadas; en ese caso se le explicará por escrito.\n\n¿Dónde puedo reclamar? Ante el investigador, en el correo indicado, y ante la Superintendencia de Protección de Datos Personales (SPDP), autoridad de protección de datos del Ecuador.\n\n¿Cuánto tiempo se conservan? Al cerrar la encuesta, las respuestas se exportan a un archivo cifrado al que solo accede el investigador y se eliminan del servicio de formularios. La base seudonimizada se conserva hasta la aprobación del Trabajo de Integración Curricular y luego se elimina. Ninguna respuesta individual se publica ni se sube a repositorios.\n\n¿Cuánto dura? Entre 13 y 15 minutos.\n\n¿Hay riesgos o beneficios? El riesgo es mínimo, porque no se recogen datos identificativos directos ni datos sensibles suyos. El beneficio esperado es contribuir a que las universidades protejan mejor los datos de sus estudiantes.\n\n@@ETICA@@\n\nRecomendación: en la pregunta abierta final (solo en la prueba piloto), por favor no escriba nombres, números de cédula, correos ni otros datos que le identifiquen a usted o a otras personas.",
 "filtros": [
  {
   "titulo": "[P00] ¿Acepta participar voluntariamente en esta encuesta, que no recoge datos que le identifiquen directamente?",
   "si": "Sí, acepto",
   "no": "No acepto"
  },
  {
   "titulo": "[P01] ¿Tiene 18 años o más?",
   "si": "Sí",
   "no": "No"
  },
  {
   "titulo": "[P02] ¿Estudia actualmente una carrera de grado en una universidad o escuela politécnica del Ecuador?",
   "si": "Sí",
   "no": "No"
  }
 ],
 "secciones": [
  {
   "titulo": "Datos generales",
   "ayuda": "No se piden datos que le identifiquen. La universidad se usa solo para el análisis interno; nunca se publica un resultado por universidad.",
   "items": [
    {
     "tipo": "opcion",
     "titulo": "[A1] Su universidad es:",
     "opciones": [
      "Pública",
      "Particular cofinanciada",
      "Particular autofinanciada",
      "No lo sé"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[A2] Área de su carrera:",
     "opciones": [
      "Educación",
      "Artes y humanidades",
      "Ciencias sociales, periodismo e información",
      "Administración y derecho",
      "Ciencias naturales, matemáticas y estadística",
      "Tecnologías de la información y la comunicación",
      "Ingeniería, industria y construcción",
      "Agricultura, silvicultura, pesca y veterinaria",
      "Salud y bienestar",
      "Servicios"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[A3] Semestre o nivel en el que se encuentra:",
     "opciones": [
      "Nivelación o curso de admisión",
      "1.º a 3.er semestre",
      "4.º a 6.º semestre",
      "7.º semestre o superior",
      "Posgrado (especialización, maestría o doctorado)"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[A4] Rango de edad:",
     "opciones": [
      "18 a 20",
      "21 a 24",
      "25 a 29",
      "30 o más"
     ],
     "obligatoria": false
    },
    {
     "tipo": "lista",
     "titulo": "[A5] ¿En qué universidad o escuela politécnica estudia?",
     "opciones": [
      "Escuela Politécnica Nacional",
      "Escuela Superior Politécnica Agropecuaria de Manabí Manuel Félix López (ESPAM MFL)",
      "Escuela Superior Politécnica de Chimborazo",
      "Escuela Superior Politécnica del Litoral (ESPOL)",
      "Facultad Latinoamericana de Ciencias Sociales (FLACSO)",
      "Instituto de Altos Estudios Nacionales (IAEN)",
      "Pontificia Universidad Católica del Ecuador (PUCE)",
      "Universidad Agraria del Ecuador",
      "Universidad Andina Simón Bolívar",
      "Universidad Bolivariana del Ecuador",
      "Universidad Casa Grande",
      "Universidad Católica de Cuenca",
      "Universidad Católica de Santiago de Guayaquil (UCSG)",
      "Universidad Central del Ecuador",
      "Universidad de Cuenca",
      "Universidad de Especialidades Espíritu Santo (UEES)",
      "Universidad de Especialidades Turísticas",
      "Universidad de Guayaquil",
      "Universidad de Investigación de Tecnología Experimental Yachay",
      "Universidad de las Américas (UDLA)",
      "Universidad de las Artes",
      "Universidad de las Fuerzas Armadas ESPE",
      "Universidad de los Hemisferios",
      "Universidad de Otavalo",
      "Universidad de Seguridad Ciudadana y Ciencias Policiales (USECIPOL)",
      "Universidad del Azuay",
      "Universidad del Pacífico - Escuela de Negocios",
      "Universidad del Río (UDR)",
      "Universidad Estatal Amazónica",
      "Universidad Estatal de Bolívar",
      "Universidad Estatal de Milagro",
      "Universidad Estatal del Sur de Manabí",
      "Universidad Estatal Península de Santa Elena (UPSE)",
      "Universidad Iberoamericana del Ecuador",
      "Universidad Intercultural de las Nacionalidades y Pueblos Indígenas Amawtay Wasi",
      "Universidad Internacional del Ecuador (UIDE)",
      "Universidad Laica Eloy Alfaro de Manabí",
      "Universidad Laica Vicente Rocafuerte de Guayaquil",
      "Universidad Metropolitana",
      "Universidad Nacional de Chimborazo",
      "Universidad Nacional de Educación",
      "Universidad Nacional de Loja",
      "Universidad Particular Internacional SEK",
      "Universidad Politécnica Estatal del Carchi",
      "Universidad Politécnica Salesiana (UPS)",
      "Universidad Pública de Santo Domingo de los Tsáchilas",
      "Universidad Regional Amazónica Ikiam",
      "Universidad Regional Autónoma de los Andes (UNIANDES)",
      "Universidad San Francisco de Quito (USFQ)",
      "Universidad San Gregorio de Portoviejo",
      "Universidad Técnica de Ambato",
      "Universidad Técnica de Babahoyo",
      "Universidad Técnica de Cotopaxi",
      "Universidad Técnica de Machala",
      "Universidad Técnica de Manabí",
      "Universidad Técnica del Norte",
      "Universidad Técnica Estatal de Quevedo",
      "Universidad Técnica Luis Vargas Torres de Esmeraldas",
      "Universidad Técnica Particular de Loja (UTPL)",
      "Universidad Tecnológica ECOTEC",
      "Universidad Tecnológica Empresarial de Guayaquil",
      "Universidad Tecnológica Indoamérica",
      "Universidad Tecnológica Israel",
      "Universidad UTE",
      "Prefiero no responder"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[A6] Modalidad de su carrera:",
     "opciones": [
      "Presencial",
      "Semipresencial o híbrida",
      "En línea"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[A7] ¿Cómo se enteró de esta encuesta? (opcional)",
     "opciones": [
      "Enlace en redes sociales o grupos de mensajería",
      "Correo electrónico",
      "Código QR en el campus",
      "Invitación de un docente",
      "Invitación de un compañero o amigo",
      "Otro"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[A8] Región del Ecuador en la que estudia (opcional):",
     "opciones": [
      "Costa",
      "Sierra",
      "Amazonía",
      "Galápagos"
     ],
     "obligatoria": false
    }
   ]
  },
  {
   "titulo": "Datos que le pidió su universidad",
   "ayuda": "Opciones: Sí / No / No recuerdo, salvo que se indiquen otras.",
   "items": [
    {
     "tipo": "casillas",
     "titulo": "[H1] Desde su postulación hasta hoy (admisión, matrícula, becas, bienestar, aula virtual u otros trámites), ¿qué datos le pidió su universidad? (marque todas las que correspondan)",
     "opciones": [
      "Identificación (cédula, nombres, fecha de nacimiento)",
      "Contacto (dirección, teléfono, correo personal)",
      "Fotografía",
      "Datos socioeconómicos del hogar",
      "Datos de familiares o representantes",
      "Datos de salud",
      "Datos de discapacidad",
      "Autoidentificación étnica",
      "Condición migratoria",
      "Identidad de género o nombre social",
      "Datos biométricos (huella, reconocimiento facial)",
      "Ubicación o geolocalización",
      "Actividad en plataformas virtuales",
      "No recuerdo"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion_rama_H2",
     "titulo": "[H2] ¿Su universidad le pidió su consentimiento (autorización) para tratar sus datos personales?",
     "opciones": [
      "Sí",
      "No",
      "No recuerdo"
     ],
     "obligatoria": false
    }
   ]
  },
  {
   "titulo": "Forma del consentimiento",
   "ayuda": "",
   "items": [
    {
     "tipo": "opcion",
     "titulo": "[H3] ¿De qué forma lo dio?",
     "opciones": [
      "De forma expresa (marcando una casilla o firmando)",
      "De forma implícita (\"al continuar, acepta…\")",
      "De forma verbal",
      "No recuerdo"
     ],
     "obligatoria": false
    }
   ],
   "id": "H3"
  },
  {
   "titulo": "Información, derechos e incidentes",
   "ayuda": "",
   "id": "H4",
   "items": [
    {
     "tipo": "opcion",
     "titulo": "[H4] Al entregar sus datos, ¿le informaron para qué se usarían?",
     "opciones": [
      "Sí",
      "No",
      "No recuerdo"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[H5a] ¿Le informaron quién es el responsable de sus datos?",
     "opciones": [
      "Sí",
      "No",
      "No recuerdo"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[H5b] ¿Le informaron cómo contactar al responsable de sus datos?",
     "opciones": [
      "Sí",
      "No",
      "No recuerdo"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[H6] ¿Le informaron durante cuánto tiempo se conservarán sus datos?",
     "opciones": [
      "Sí",
      "No",
      "No recuerdo"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[H7] ¿Le informaron si sus datos se compartirían con terceros (otras instituciones, proveedores, plataformas en la nube)?",
     "opciones": [
      "Sí",
      "No",
      "No recuerdo"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[H8] ¿Pudo aceptar o rechazar por separado los usos no necesarios para su matrícula (por ejemplo, publicidad o difusión de su imagen)?",
     "opciones": [
      "Sí",
      "No",
      "No recuerdo"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[H9] Cuando le pidieron datos de salud, discapacidad, socioeconómicos o biométricos, ¿le explicaron para qué se usarían?",
     "opciones": [
      "Sí",
      "No",
      "No recuerdo",
      "No me pidieron esos datos"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[H10] ¿Le informaron si alguna plataforma de su universidad (aula virtual, supervisión de exámenes en línea, analítica) analiza automáticamente su comportamiento o elabora perfiles?",
     "opciones": [
      "Sí",
      "No",
      "No recuerdo",
      "No uso esas plataformas"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[H11] ¿Ha solicitado alguna vez a su universidad acceder, corregir o eliminar sus datos?",
     "opciones": [
      "Sí, y me respondieron en un plazo razonable",
      "Sí, pero no me respondieron o tardaron mucho",
      "No"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[H12] ¿Su universidad le ha comunicado alguna vez que sus datos se vieron afectados por un incidente de seguridad?",
     "opciones": [
      "Sí",
      "No",
      "No recuerdo"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[H13] ¿Ha visto publicados por su universidad listados con su número de cédula junto a su nombre, calificaciones o resultados?",
     "opciones": [
      "Sí",
      "No",
      "No recuerdo"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[H14] En el último semestre, ¿recibió en su cuenta institucional correos que pedían contraseñas, pagos o datos personales?",
     "opciones": [
      "Sí",
      "No",
      "No recuerdo"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[H15] ¿Su universidad le ha dado información o capacitación sobre protección de datos personales?",
     "opciones": [
      "Sí",
      "No",
      "No recuerdo"
     ],
     "obligatoria": false
    },
    {
     "tipo": "opcion",
     "titulo": "[H16] ¿Sabe por qué canal (correo, formulario u oficina) puede ejercer sus derechos sobre sus datos en su universidad?",
     "opciones": [
      "Sí",
      "No",
      "No estoy seguro(a)"
     ],
     "obligatoria": false
    }
   ]
  },
  {
   "titulo": "Su opinión: información recibida",
   "ayuda": "1 = Totalmente en desacuerdo · 2 = En desacuerdo · 3 = Ni de acuerdo ni en desacuerdo · 4 = De acuerdo · 5 = Totalmente de acuerdo",
   "items": [
    {
     "tipo": "escala",
     "titulo": "[INF1] Mi universidad me explicó con claridad para qué usa mis datos personales.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[INF2a] Sé quién es el responsable de mis datos en mi universidad.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[INF2b] Sé cómo contactar al responsable de mis datos en mi universidad.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[INF3] Mi universidad me informó cuánto tiempo conservará mis datos.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[INF4] No sé con quién comparte mi universidad mis datos personales.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[INF5a] La política de privacidad de mi universidad es fácil de encontrar.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[INF5b] La política de privacidad de mi universidad es fácil de entender.",
     "obligatoria": false
    }
   ]
  },
  {
   "titulo": "Su opinión: consentimiento",
   "ayuda": "1 = Totalmente en desacuerdo · 2 = En desacuerdo · 3 = Ni de acuerdo ni en desacuerdo · 4 = De acuerdo · 5 = Totalmente de acuerdo",
   "items": [
    {
     "tipo": "escala",
     "titulo": "[CON1] Mi universidad me pidió autorización antes de recoger mis datos personales.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[CON2] Pude aceptar o rechazar por separado los usos de mis datos que no eran necesarios para estudiar.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[CON3] Sentí que estaba obligado(a) a entregar todos los datos que me pedían para poder estudiar.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[CON4] Entendí lo que estaba aceptando cuando di mi autorización.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[CON5] Sé que puedo retirar mi autorización cuando quiera.",
     "obligatoria": false
    }
   ]
  },
  {
   "titulo": "Su opinión: conocimiento de derechos",
   "ayuda": "1 = Totalmente en desacuerdo · 2 = En desacuerdo · 3 = Ni de acuerdo ni en desacuerdo · 4 = De acuerdo · 5 = Totalmente de acuerdo",
   "items": [
    {
     "tipo": "escala",
     "titulo": "[DER1] Sé que puedo pedir a mi universidad acceso a todos los datos que tiene de mí.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[DER2] Sé que puedo pedir que corrijan o actualicen mis datos.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[DER3] Sé que puedo pedir que eliminen mis datos cuando ya no sean necesarios.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[DER4] Sé que puedo oponerme a ciertos usos de mis datos.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[DER5] Sé que puedo pedir mis datos en un formato que me permita llevarlos a otra institución.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[DER6] No sabría ante quién reclamar si mi universidad usa mal mis datos.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[DER7] Conozco la Ley Orgánica de Protección de Datos Personales.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[DER8] Sé que puedo pedir que se suspenda el uso de mis datos mientras se revisa si son correctos.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[DER9] Sé que puedo pedir que una decisión sobre mí no se tome solo con un sistema automático.",
     "obligatoria": false
    }
   ]
  },
  {
   "titulo": "Su opinión: confianza y percepción de seguridad",
   "ayuda": "1 = Totalmente en desacuerdo · 2 = En desacuerdo · 3 = Ni de acuerdo ni en desacuerdo · 4 = De acuerdo · 5 = Totalmente de acuerdo",
   "items": [
    {
     "tipo": "escala",
     "titulo": "[CNF1] Confío en que mi universidad protege adecuadamente mis datos personales.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[CNF2] Creo que el personal de mi universidad accede solo a los datos que necesita para su función.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[CNF3] Me preocupa que mis datos personales se filtren desde los sistemas de mi universidad.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[CNF4] Si mis datos se vieran afectados por un incidente de seguridad, mi universidad me lo comunicaría.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[CNF5] Me sentiría seguro(a) entregando a mi universidad datos sensibles, como los de salud.",
     "obligatoria": false
    },
    {
     "tipo": "escala",
     "titulo": "[CNF6] Mi universidad trata mis datos como si le pertenecieran a ella y no a mí.",
     "obligatoria": false
    }
   ]
  }
 ],
 "final": "Gracias por su participación. Sus respuestas no contienen datos que le identifiquen directamente y se usarán solo de forma agregada en un Trabajo de Integración Curricular; ningún resultado se publicará por universidad. Si tiene preguntas: ramonalejandromanzaba@gmail.com",
 "piloto": "¿Alguna pregunta le resultó confusa? ¿Cuál y por qué? (Por favor, no escriba nombres, números de cédula, correos ni otros datos que le identifiquen a usted o a otras personas.)",
 "n_preguntas": 55
};

function crearFormulario() {
  if (!VERIFICACION_ETICA.trim()) {
    throw new Error('Complete VERIFICACION_ETICA con el número y la fecha del oficio de la UTI antes de crear el formulario.');
  }
  const form = FormApp.create(DATOS.titulo + (PILOTO ? ' (PILOTO)' : ''));
  form.setDescription('Encuesta para un Trabajo de Integración Curricular (Universidad Tecnológica Indoamérica). Lea la información de la primera sección antes de responder.');

  // --- Configuración: sin correos, sin inicio de sesión, sin límite de una respuesta (exigiría iniciar sesión)
  try { form.setEmailCollectionType(FormApp.EmailCollectionType.DO_NOT_COLLECT); } catch (e) { form.setCollectEmail(false); }
  try { form.setRequireLogin(false); } catch (e) { /* solo existe en cuentas de Google Workspace */ }
  form.setLimitOneResponsePerUser(false);
  form.setAllowResponseEdits(false);
  form.setShowLinkToRespondAgain(false);
  form.setPublishingSummary(false);
  form.setProgressBar(true);
  form.setConfirmationMessage(DATOS.final);

  // --- Sección 1: consentimiento y filtros (si alguna respuesta es "No", el formulario termina)
  const consentimiento = DATOS.consentimiento.replace('@@ETICA@@', 'Verificación ética: ' + VERIFICACION_ETICA + '.');
  form.addSectionHeaderItem().setTitle('Información para participantes').setHelpText(consentimiento);
  // Cada filtro va en su propia sección: Google Forms aplica un solo salto de sección por sección.
  DATOS.filtros.forEach(function (f, i) {
    if (i > 0) form.addPageBreakItem().setTitle('Requisitos para participar');
    const it = form.addMultipleChoiceItem().setTitle(f.titulo).setRequired(true);
    it.setChoices([
      it.createChoice(f.si, FormApp.PageNavigationType.CONTINUE),
      it.createChoice(f.no, FormApp.PageNavigationType.SUBMIT)
    ]);
  });

  // --- Resto de secciones
  const paginas = {};
  let ramaH2 = null;
  DATOS.secciones.forEach(function (s) {
    const pb = form.addPageBreakItem().setTitle(s.titulo);
    if (s.ayuda) pb.setHelpText(s.ayuda);
    if (s.id) paginas[s.id] = pb;
    s.items.forEach(function (q) {
      if (q.tipo === 'opcion') {
        form.addMultipleChoiceItem().setTitle(q.titulo).setChoiceValues(q.opciones).setRequired(q.obligatoria);
      } else if (q.tipo === 'lista') {
        form.addListItem().setTitle(q.titulo).setChoiceValues(q.opciones).setRequired(q.obligatoria);
      } else if (q.tipo === 'casillas') {
        form.addCheckboxItem().setTitle(q.titulo).setChoiceValues(q.opciones).setRequired(q.obligatoria);
      } else if (q.tipo === 'escala') {
        form.addScaleItem().setTitle(q.titulo).setBounds(1, 5)
          .setLabels('Totalmente en desacuerdo', 'Totalmente de acuerdo').setRequired(q.obligatoria);
      } else if (q.tipo === 'opcion_rama_H2') {
        ramaH2 = { item: form.addMultipleChoiceItem().setTitle(q.titulo).setRequired(q.obligatoria), opciones: q.opciones };
      }
    });
  });
  // H3 solo se muestra si H2 = Sí; las demás respuestas saltan a la sección de H4
  const it = ramaH2.item;
  it.setChoices(ramaH2.opciones.map(function (o) {
    return it.createChoice(o, o === 'Sí' ? paginas['H3'] : paginas['H4']);
  }));
  paginas['H3'].setGoToPage(FormApp.PageNavigationType.CONTINUE);

  if (PILOTO) {
    form.addPageBreakItem().setTitle('Prueba piloto');
    form.addParagraphTextItem().setTitle(DATOS.piloto).setRequired(false);
  }

  Logger.log('Formulario creado (' + DATOS.n_preguntas + ' preguntas).');
  Logger.log('Editar: ' + form.getEditUrl());
  Logger.log('Enlace público: ' + form.getPublishedUrl());
  Logger.log('Revise en Configuración que no se recopilen correos ni se limite a una respuesta por persona.');
}
