// Genera encuesta/plantilla_juicio_expertos.xlsx (V de Aiken por ítem y criterio) y verifica sus fórmulas con HyperFormula.
// Uso: node build_plantilla_aiken.js <salida.xlsx> [--prueba]
// La hoja Calificaciones (primera hoja) tiene el formato que lee analisis/validacion.py: item | criterio | J1 … J7.
// Con --prueba llena calificaciones de referencia para comprobar las fórmulas (ese archivo no se versiona).
const ExcelJS = require('exceljs');
const { HyperFormula } = require('hyperformula');

const OUT = process.argv[2];
const PRUEBA = process.argv.includes('--prueba');
const FONT = 'Arial';
const N_J = 7;               // hasta 7 jueces (mínimo 3)
const V_MIN = 0.80;          // criterio de conservación del ítem
const CRITERIOS = ['pertinencia', 'claridad', 'coherencia'];
// Ítems del cuestionario v2.0 (encuesta/cuestionario.md)
const ITEMS = [
  ['P00', 'Acceso', 'Consentimiento para participar'], ['P01', 'Acceso', 'Mayoría de edad'], ['P02', 'Acceso', 'Condición de estudiante'],
  ['A1', 'Demográfico', 'Tipo de universidad'], ['A2', 'Demográfico', 'Área de la carrera'], ['A3', 'Demográfico', 'Semestre'], ['A4', 'Demográfico', 'Rango de edad'],
  ['H1', 'Hechos', 'Datos solicitados'], ['H2', 'Hechos', 'Se pidió consentimiento'], ['H3', 'Hechos', 'Forma del consentimiento'],
  ['H4', 'Hechos', 'Informado de la finalidad'], ['H5', 'Hechos', 'Informado del responsable'], ['H6', 'Hechos', 'Informado de la conservación'],
  ['H7', 'Hechos', 'Informado de terceros'], ['H8', 'Hechos', 'Consentimiento separado por finalidad'], ['H9', 'Hechos', 'Explicación de datos sensibles'],
  ['H10', 'Hechos', 'Plataformas que elaboran perfiles'], ['H11', 'Hechos', 'Ejercicio de derechos'], ['H12', 'Hechos', 'Comunicación de vulneración'],
  ['H13', 'Hechos', 'Listados con cédula'], ['H14', 'Hechos', 'Correos sospechosos'], ['H15', 'Hechos', 'Información o capacitación recibida'],
  ['H16', 'Hechos', 'Canal para ejercer derechos'],
  ...['INF1', 'INF2', 'INF3', 'INF4', 'INF5'].map(c => [c, 'Likert: información recibida', c === 'INF4' ? 'Ítem inverso' : '']),
  ...['CON1', 'CON2', 'CON3', 'CON4', 'CON5'].map(c => [c, 'Likert: consentimiento', c === 'CON3' ? 'Ítem inverso' : '']),
  ...['DER1', 'DER2', 'DER3', 'DER4', 'DER5', 'DER6', 'DER7'].map(c => [c, 'Likert: conocimiento de derechos', c === 'DER6' ? 'Ítem inverso' : '']),
  ...['CNF1', 'CNF2', 'CNF3', 'CNF4', 'CNF5', 'CNF6'].map(c => [c, 'Likert: confianza y seguridad', ['CNF3', 'CNF6'].includes(c) ? 'Ítem inverso' : '']),
];

const INPUT_FILL = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFFFF2CC' } };
const FORMULA_FILL = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFEDEDED' } };
const HEAD_FILL = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FF1F3864' } };
const thin = { style: 'thin', color: { argb: 'FFBFBFBF' } };
const BORDER = { top: thin, left: thin, bottom: thin, right: thin };
const col = n => { let s = ''; while (n > 0) { const m = (n - 1) % 26; s = String.fromCharCode(65 + m) + s; n = Math.floor((n - 1) / 26); } return s; };
const box = (c, fill) => { c.border = BORDER; if (fill) c.fill = fill; c.alignment = { vertical: 'top', wrapText: true }; };
const head = (ws, r, vals) => vals.forEach((v, i) => { const c = ws.getCell(r, i + 1); c.value = v; c.fill = HEAD_FILL; c.border = BORDER;
  c.font = { name: FONT, bold: true, color: { argb: 'FFFFFFFF' } }; c.alignment = { horizontal: 'center', vertical: 'middle', wrapText: true }; });

const wb = new ExcelJS.Workbook();
wb.creator = 'Ramón Alejandro Manzaba Castro';
wb.calcProperties.fullCalcOnLoad = true;
const K = wb.addWorksheet('Calificaciones', { views: [{ state: 'frozen', xSplit: 2, ySplit: 1 }] });
const R = wb.addWorksheet('Resumen por ítem', { views: [{ state: 'frozen', ySplit: 1 }] });
const I = wb.addWorksheet('Instrucciones');

// ---------------- Calificaciones (una fila por ítem y criterio)
const jCols = [...Array(N_J)].map((_, j) => `J${j + 1}`);
const cN = 3 + N_J, cS = cN + 1, cV = cS + 1, cD = cV + 1;
head(K, 1, ['item', 'criterio', ...jCols, 'n_jueces', 'suma_x_menos_l', 'V_Aiken', 'cumple']);
let r = 2;
const filaDe = {};
for (const [cod] of ITEMS) for (const cr of CRITERIOS) {
  K.getCell(r, 1).value = cod; K.getCell(r, 2).value = cr; box(K.getCell(r, 1)); box(K.getCell(r, 2));
  for (let j = 0; j < N_J; j++) {
    const c = K.getCell(r, 3 + j); box(c, INPUT_FILL);
    c.dataValidation = { type: 'whole', operator: 'between', allowBlank: true, formulae: [1, 5], showErrorMessage: true, error: 'Calificación de 1 a 5' };
  }
  const rg = `C${r}:${col(2 + N_J)}${r}`;
  K.getCell(r, cN).value = { formula: `COUNT(${rg})` };
  K.getCell(r, cS).value = { formula: `IF(${col(cN)}${r}=0,"",SUM(${rg})-${col(cN)}${r}*1)` };            // S = Σ(x − l), l = 1
  K.getCell(r, cV).value = { formula: `IF(${col(cN)}${r}<3,"",ROUND(${col(cS)}${r}/(${col(cN)}${r}*4),3))` }; // V = S / (n(c − 1)), c = 5
  K.getCell(r, cD).value = { formula: `IF(${col(cV)}${r}="","",IF(${col(cV)}${r}>=${V_MIN},"Sí","No"))` };
  [cN, cS, cV, cD].forEach(k => box(K.getCell(r, k), FORMULA_FILL));
  (filaDe[cod] = filaDe[cod] || {})[cr] = r;
  r++;
}
const ultima = r - 1;
[8, 13, ...jCols.map(() => 5), 9, 10, 9, 8].forEach((w, i) => K.getColumn(i + 1).width = w);

// ---------------- Resumen por ítem
head(R, 1, ['Ítem', 'Bloque', 'Nota', 'V pertinencia', 'V claridad', 'V coherencia', 'V mínima', 'Decisión']);
ITEMS.forEach(([cod, bloque, nota], i) => {
  const rr = 2 + i;
  [cod, bloque, nota].forEach((v, k) => { R.getCell(rr, k + 1).value = v; box(R.getCell(rr, k + 1)); });
  CRITERIOS.forEach((cr, k) => { R.getCell(rr, 4 + k).value = { formula: `Calificaciones!${col(cV)}${filaDe[cod][cr]}` }; box(R.getCell(rr, 4 + k), FORMULA_FILL); });
  R.getCell(rr, 7).value = { formula: `IF(COUNT(D${rr}:F${rr})<3,"",MIN(D${rr}:F${rr}))` };
  R.getCell(rr, 8).value = { formula: `IF(G${rr}="","",IF(G${rr}>=${V_MIN},"Se conserva","Corregir o eliminar"))` };
  [7, 8].forEach(k => box(R.getCell(rr, k), FORMULA_FILL));
});
const rt = ITEMS.length + 3;
R.getCell(rt, 1).value = 'Ítems que se conservan'; R.getCell(rt, 1).font = { name: FONT, bold: true };
R.getCell(rt, 7).value = { formula: `COUNTIF(H2:H${ITEMS.length + 1},"Se conserva")` };
R.getCell(rt + 1, 1).value = 'Ítems evaluados'; R.getCell(rt + 1, 1).font = { name: FONT, bold: true };
R.getCell(rt + 1, 7).value = { formula: `COUNT(G2:G${ITEMS.length + 1})` };
[8, 30, 14, 12, 12, 12, 11, 20].forEach((w, i) => R.getColumn(i + 1).width = w);

// ---------------- Instrucciones
I.getCell('A1').value = 'Juicio de expertos sobre el cuestionario (V de Aiken)';
I.getCell('A1').font = { name: FONT, bold: true, size: 14, color: { argb: 'FF1F3864' } };
[
  ['Jueces', 'De 3 a 5 expertos (hasta 7 columnas) en protección de datos, seguridad de la información o metodología. Cada juez se identifica con J1, J2, … (sin nombres).'],
  ['Criterios', 'Pertinencia (el ítem mide su indicador), claridad (se entiende sin ambigüedad) y coherencia (corresponde al artículo de la LOPDP citado). Escala de 1 a 5; ver encuesta/formato_juicio_expertos.md.'],
  ['Cálculo', 'V = Σ(x − 1) / (n · 4), con l = 1, c = 5 y n = número de jueces (mínimo 3 para calcular). Se conserva el ítem si V ≥ 0,80 en los tres criterios; si no, se corrige o se elimina.'],
  ['Uso con Python', 'La hoja Calificaciones puede guardarse como analisis/datos/expertos.xlsx: validacion.py usa las columnas item, criterio y J1…J7 e ignora las de fórmula.'],
].forEach(([k, v], i) => { const c1 = I.getCell(3 + i, 1), c2 = I.getCell(3 + i, 2); c1.value = k; c1.font = { name: FONT, bold: true };
  c2.value = v; c2.alignment = { wrapText: true, vertical: 'top' }; I.getRow(3 + i).height = 45; });
I.getColumn(1).width = 16; I.getColumn(2).width = 110;

// ---------------- datos de prueba
if (PRUEBA) {
  for (let rr = 2; rr <= ultima; rr++) for (let j = 0; j < 5; j++) K.getCell(rr, 3 + j).value = (rr === 2) ? [4, 4, 5, 5, 3][j] : (rr === 3 ? [5, 5, 5, 5, 5][j] : (rr === 4 ? [3, 3, 4, 2, 3][j] : 5));
}
[K, R, I].forEach(ws => ws.eachRow({ includeEmpty: true }, row => row.eachCell({ includeEmpty: true }, c => { c.font = Object.assign({ name: FONT, size: 10 }, c.font || {}, { name: FONT }); })));

// ---------------- verificación con HyperFormula
const toArr = ws => { const out = []; ws.eachRow({ includeEmpty: true }, (row, rr) => { out[rr - 1] = []; row.eachCell({ includeEmpty: true }, (c, k) => {
  let v = c.value; if (v && typeof v === 'object' && v.formula) v = '=' + v.formula; out[rr - 1][k - 1] = v === undefined ? null : v; }); });
  for (let i = 0; i < out.length; i++) if (!out[i]) out[i] = []; return out; };
const sheets = {}; wb.worksheets.forEach(ws => { sheets[ws.name] = toArr(ws); });
const hf = HyperFormula.buildFromSheets(sheets, { licenseKey: 'gpl-v3' });
let nF = 0; const errs = [];
wb.worksheets.forEach(ws => { const sid = hf.getSheetId(ws.name); ws.eachRow({ includeEmpty: true }, (row, rr) => row.eachCell({ includeEmpty: true }, (c, k) => {
  if (c.value && typeof c.value === 'object' && c.value.formula) { nF++; let res = hf.getCellValue({ sheet: sid, row: rr - 1, col: k - 1 });
    if (res && typeof res === 'object' && res.type) { errs.push(`${ws.name}!${c.address}: ${res.type}`); res = undefined; }
    c.value = { formula: c.value.formula, result: res === null ? '' : res }; } })); });
const out = { total_formulas: nF, total_errors: errs.length, errors: errs.slice(0, 5) };
if (PRUEBA) out.prueba = {
  V_fila2_excel: K.getCell(2, cV).value.result, V_fila2_esperado: 0.8,
  V_fila3_excel: K.getCell(3, cV).value.result, V_fila3_esperado: 1,
  V_fila4_excel: K.getCell(4, cV).value.result, V_fila4_esperado: 0.5,
  P00_Vmin_excel: R.getCell(2, 7).value.result, P00_decision: R.getCell(2, 8).value.result,
  conservados_excel: R.getCell(rt, 7).value.result, conservados_esperado: ITEMS.length - 1,
};
console.log(JSON.stringify(out, null, 1));
wb.xlsx.writeFile(OUT).then(() => console.log('Escrito: ' + OUT));
