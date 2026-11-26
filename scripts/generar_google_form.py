"""Genera encuesta/google_form.gs: un Google Apps Script que crea el formulario de la encuesta (cuestionario v2.2).

Uso: python scripts/generar_google_form.py
Todo el texto sale de analisis/config.py (preguntas y opciones) y de encuesta/consentimiento_informado.md (primera
pantalla), de modo que el formulario coincide literalmente con lo que reconoce analisis/limpieza.py: cada pregunta
empieza con su código entre corchetes y las opciones se copian tal cual.

Cómo usar el .gs (lo hace el autor, con su cuenta de Google):
1. Abrir https://script.google.com → Nuevo proyecto → pegar el contenido de encuesta/google_form.gs.
2. Completar la constante VERIFICACION_ETICA con el número y la fecha del oficio de la UTI (sin ella el script se
   detiene: la encuesta no se abre sin la respuesta ética documentada).
3. Ejecutar crearFormulario y autorizar. El registro muestra el enlace de edición y el enlace público.
4. Revisar en Configuración: no recopilar correos, sin "Limitar a 1 respuesta", sin carga de archivos.
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "analisis"))
import config as C  # noqa: E402

SALIDA = RAIZ / "encuesta" / "google_form.gs"


def texto_plano(md):
    md = re.sub(r"\s*\[(nums?\.[^\]]*)\]", "", md)
    md = re.sub(r"\*\*(.+?)\*\*", r"\1", md)
    md = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"\1", md)
    return md.strip()


def consentimiento():
    t = (RAIZ / "encuesta" / "consentimiento_informado.md").read_text(encoding="utf-8")
    cuerpo = t.split("\n---\n")[1]  # entre el primer y el segundo separador
    lineas = [l for l in cuerpo.strip().splitlines() if l.strip()]
    titulo = texto_plano(lineas[0])
    parrafos = []
    for l in lineas[1:]:
        if l.startswith("**Verificación ética:**"):
            parrafos.append("@@ETICA@@")
        else:
            parrafos.append(texto_plano(l))
    return titulo, "\n\n".join(parrafos)


def opciones(cod):
    if cod in C.DEMOGRAFICOS:
        return list(C.DEMOGRAFICOS[cod])
    if cod in C.HECHOS:
        return list(C.HECHOS[cod])
    raise KeyError(cod)


def main():
    titulo, consent = consentimiento()
    T = C.TEXTO
    preg = lambda c: f"[{c}] {T[c]}"
    secciones = [
        {"titulo": "Datos generales", "ayuda": "No se piden datos que le identifiquen. La universidad se usa solo para el análisis interno; nunca se publica un resultado por universidad.",
         "items": [{"tipo": "lista" if c == "A5" else "opcion", "titulo": preg(c), "opciones": opciones(c),
                    "obligatoria": False} for c in [f"A{i}" for i in range(1, 9)]]},
        {"titulo": "Datos que le pidió su universidad", "ayuda": "Opciones: Sí / No / No recuerdo, salvo que se indiquen otras.",
         "items": [{"tipo": "casillas", "titulo": preg("H1"), "opciones": list(C.H1_OPCIONES.values()), "obligatoria": False},
                   {"tipo": "opcion_rama_H2", "titulo": preg("H2"), "opciones": opciones("H2"), "obligatoria": False}]},
        {"titulo": "Forma del consentimiento", "ayuda": "",
         "items": [{"tipo": "opcion", "titulo": preg("H3").replace("(Solo si H2 = Sí) ", ""), "opciones": opciones("H3"), "obligatoria": False}],
         "id": "H3"},
        {"titulo": "Información, derechos e incidentes", "ayuda": "", "id": "H4",
         "items": [{"tipo": "opcion", "titulo": preg(c), "opciones": opciones(c), "obligatoria": False}
                   for c in ["H4", "H5a", "H5b"] + [f"H{i}" for i in range(6, 17)]]},
    ]
    escalas = []
    for d, info in C.DIMENSIONES.items():
        escalas.append({"titulo": f"Su opinión: {info['nombre'].lower()}",
                        "ayuda": "1 = Totalmente en desacuerdo · 2 = En desacuerdo · 3 = Ni de acuerdo ni en desacuerdo · 4 = De acuerdo · 5 = Totalmente de acuerdo",
                        "items": [{"tipo": "escala", "titulo": preg(i), "obligatoria": False} for i in info["items"]]})
    datos = {
        "titulo": titulo,
        "consentimiento": consent,
        "filtros": [{"titulo": preg("P00"), "si": "Sí, acepto", "no": "No acepto"},
                    {"titulo": preg("P01"), "si": "Sí", "no": "No"},
                    {"titulo": preg("P02"), "si": "Sí", "no": "No"}],
        "secciones": secciones + escalas,
        "final": "Gracias por su participación. Sus respuestas no contienen datos que le identifiquen directamente y se "
                 "usarán solo de forma agregada en un Trabajo de Integración Curricular; ningún resultado se publicará "
                 "por universidad. Si tiene preguntas: ramonalejandromanzaba@gmail.com",
        "piloto": "¿Alguna pregunta le resultó confusa? ¿Cuál y por qué? (Por favor, no escriba nombres, números de "
                  "cédula, correos ni otros datos que le identifiquen a usted o a otras personas.)",
        "n_preguntas": len(C.ITEMS_CUESTIONARIO),
    }
    js = GS.replace("@@DATOS@@", json.dumps(datos, ensure_ascii=False, indent=1))
    SALIDA.write_text(js, encoding="utf-8")
    n = 3 + sum(len(s["items"]) for s in datos["secciones"])
    print(f"Escrito {SALIDA}: {n} preguntas (config: {datos['n_preguntas']})")
    assert n == datos["n_preguntas"]


GS = r"""/**
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

const DATOS = @@DATOS@@;

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
"""

if __name__ == "__main__":
    main()
