// Genera la plantilla de registro del análisis documental (OE2) y verifica sus fórmulas con HyperFormula.
// Uso: node build_analisis_documental.js <ruta_salida.xlsx> [--prueba]
// Con --prueba llena el registro con calificaciones sintéticas (aleatorias, con semilla fija) para comprobar
// las fórmulas; ese archivo NO debe usarse como resultado ni incorporarse al repositorio.
const ExcelJS = require('exceljs');
const { HyperFormula } = require('hyperformula');

const OUT = process.argv[2];
const PRUEBA = process.argv.includes('--prueba');
const FONT = 'Arial';
const N_U = 64;          // universidades y escuelas politécnicas (CES, consulta del 07-11-2026)
const FIRST = 5;         // primera fila de datos en Registro
const LAST = FIRST + N_U - 1;
const N_REV = 13;        // reverificación del 20 %

const IND = [
  ['ID01', 'Política o aviso de privacidad publicado y accesible desde el sitio principal', 'LOPDP arts. 10 lit. c, 12 y 47 num. 4', 'Principal'],
  ['ID02', 'Identifica al responsable con dirección, teléfono y correo', 'LOPDP art. 12 num. 8', 'Principal'],
  ['ID03', 'Declara los fines del tratamiento de datos de estudiantes', 'LOPDP arts. 10 lit. d y 12 num. 1', 'Principal'],
  ['ID04', 'Declara la base legal de cada tratamiento', 'LOPDP arts. 7 y 12 num. 2', 'Principal'],
  ['ID05', 'Declara el tiempo de conservación', 'LOPDP arts. 10 lit. i y 12 num. 4', 'Principal'],
  ['ID06', 'Informa transferencias o comunicaciones, destinatarios y garantías', 'LOPDP arts. 12 num. 10, 33 y 55', 'Principal'],
  ['ID07', 'Enumera los derechos (acceso, rectificación, eliminación, oposición, portabilidad) y cómo ejercerlos', 'LOPDP arts. 12 nums. 14-15 y 13 a 17', 'Principal'],
  ['ID08', 'Canal específico y operativo para ejercer derechos', 'LOPDP arts. 8 y 13', 'Principal'],
  ['ID09', 'Dónde y cómo reclamar ante el responsable y la Autoridad', 'LOPDP art. 12 num. 16', 'Principal'],
  ['ID10', 'Posibilidad de revocar el consentimiento', 'LOPDP arts. 8 y 12 num. 13', 'Principal'],
  ['ID11', 'Designación del delegado de protección de datos con contacto', 'LOPDP arts. 12 num. 9 y 48', 'Principal'],
  ['ID12', 'Referencia expresa a la LOPDP y su Reglamento', 'LOPDP arts. 10 lit. a y 47 num. 1', 'Principal'],
  ['ID13', 'Declara categorías especiales tratadas y su base de legitimación', 'LOPDP arts. 25 y 26', 'Principal'],
  ['ID14', 'Formularios en línea con cláusula informativa y consentimiento por finalidad', 'LOPDP arts. 8 y 12', 'Principal'],
  ['ID15', 'Aviso de cookies con opción de aceptar o rechazar', 'LOPDP arts. 8 y 12 num. 3', 'Complementario'],
  ['ID16', 'Fecha de vigencia o última actualización de la política', 'LOPDP art. 10 lit. c', 'Complementario'],
];
const N_PRIN = 14;
const SOST = ['Pública', 'Particular cofinanciada', 'Particular autofinanciada'];
const CAL = ['S', 'P', 'N'];

const INPUT_FILL = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFFFF2CC' } };
const FORMULA_FILL = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFEDEDED' } };
const HEAD_FILL = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FF1F3864' } };
const thin = { style: 'thin', color: { argb: 'FFBFBFBF' } };
const BORDER = { top: thin, left: thin, bottom: thin, right: thin };

const wb = new ExcelJS.Workbook();
wb.creator = 'Ramón Alejandro Manzaba Castro';
wb.title = 'Análisis documental LOPDP — universidades ecuatorianas';
wb.calcProperties.fullCalcOnLoad = true;
const I = wb.addWorksheet('Instrucciones');
const K = wb.addWorksheet('Indicadores');
const R = wb.addWorksheet('Registro', { views: [{ state: 'frozen', xSplit: 3, ySplit: 4 }] });
const S = wb.addWorksheet('Resumen');
const V = wb.addWorksheet('Reverificación');
const L = wb.addWorksheet('Listas');

const colL = n => { let s = ''; while (n > 0) { const m = (n - 1) % 26; s = String.fromCharCode(65 + m) + s; n = Math.floor((n - 1) / 26); } return s; };
function header(ws, row, vals, start = 1) {
  vals.forEach((v, i) => { const c = ws.getCell(row, start + i); c.value = v; c.fill = HEAD_FILL; c.border = BORDER;
    c.font = { name: FONT, bold: true, color: { argb: 'FFFFFFFF' }, size: 10 }; c.alignment = { wrapText: true, vertical: 'middle', horizontal: 'center' }; });
}
function title(ws, t, sub) {
  ws.getCell('A1').value = t; ws.getCell('A1').font = { name: FONT, bold: true, size: 14, color: { argb: 'FF1F3864' } };
  if (sub) { ws.getCell('A2').value = sub; ws.getCell('A2').font = { name: FONT, italic: true, size: 9 }; }
}
function box(c, fill) { c.border = BORDER; if (fill) c.fill = fill; c.alignment = { wrapText: true, vertical: 'top' }; }

// ---------------------------------------------------------------- Listas
title(L, 'Listas de validación');
header(L, 3, ['Calificación', 'Sostenimiento']);
CAL.forEach((v, i) => { L.getCell(4 + i, 1).value = v; });
SOST.forEach((v, i) => { L.getCell(4 + i, 2).value = v; });
const LIST_CAL = `Listas!$A$4:$A$${3 + CAL.length}`;
const LIST_SOST = `Listas!$B$4:$B$${3 + SOST.length}`;

// ---------------------------------------------------------------- Indicadores
title(K, 'Indicadores documentales derivados de la LOPDP (Cap. 3, Tabla de indicadores documentales)', 'S = sí, completo; P = parcial o ambiguo; N = no se encontró en la fecha de consulta.');
header(K, 4, ['ID', 'Indicador', 'Base legal', 'Tipo']);
IND.forEach((r, i) => r.forEach((v, j) => { const c = K.getCell(5 + i, j + 1); c.value = v; box(c); }));
[8, 70, 32, 16].forEach((w, i) => K.getColumn(i + 1).width = w);

// ---------------------------------------------------------------- Registro
title(R, 'Registro del análisis documental (una fila por universidad)', 'Celdas amarillas: ingresar. Celdas grises: fórmula. Para cada indicador: calificación (S/P/N), URL exacta de la evidencia y fecha de consulta (dd/mm/aaaa). Guardar copia en PDF de cada evidencia.');
const fixed = ['N.º', 'Universidad o escuela politécnica', 'Sostenimiento', 'Sitio web oficial'];
header(R, 4, fixed);
let c0 = fixed.length + 1;
const calCol = {}; // ID -> columna de calificación
IND.forEach(([id]) => {
  calCol[id] = c0;
  header(R, 4, [`${id} calif.`, `${id} URL de evidencia`, `${id} fecha`], c0);
  R.getCell(3, c0).value = id; R.getCell(3, c0).font = { name: FONT, bold: true };
  c0 += 3;
});
const scoreStart = c0;
IND.slice(0, N_PRIN).forEach(([id], i) => header(R, 4, [`Puntaje ${id}`], scoreStart + i));
const cITD = scoreStart + N_PRIN;
const cComp = cITD + 1;
header(R, 4, ['ITD (0-100)', 'Indicadores principales calificados'], cITD);
for (let r = FIRST; r <= LAST; r++) {
  R.getCell(r, 1).value = r - FIRST + 1; box(R.getCell(r, 1));
  [2, 3, 4].forEach(k => box(R.getCell(r, k), INPUT_FILL));
  R.getCell(r, 3).dataValidation = { type: 'list', allowBlank: true, formulae: [LIST_SOST] };
  IND.forEach(([id]) => {
    const cc = calCol[id];
    [0, 1, 2].forEach(k => box(R.getCell(r, cc + k), INPUT_FILL));
    R.getCell(r, cc).dataValidation = { type: 'list', allowBlank: true, formulae: [LIST_CAL] };
  });
  IND.slice(0, N_PRIN).forEach(([id], i) => {
    const a = `${colL(calCol[id])}${r}`;
    const c = R.getCell(r, scoreStart + i);
    c.value = { formula: `IF(${a}="S",1,IF(${a}="P",0.5,IF(${a}="N",0,"")))` }; box(c, FORMULA_FILL);
  });
  const sc = `${colL(scoreStart)}${r}:${colL(scoreStart + N_PRIN - 1)}${r}`;
  R.getCell(r, cComp).value = { formula: `COUNT(${sc})` }; box(R.getCell(r, cComp), FORMULA_FILL);
  R.getCell(r, cITD).value = { formula: `IF(${colL(cComp)}${r}<${N_PRIN},"",ROUND(100/${N_PRIN}*SUM(${sc}),1))` }; box(R.getCell(r, cITD), FORMULA_FILL);
}
R.getColumn(1).width = 5; R.getColumn(2).width = 38; R.getColumn(3).width = 22; R.getColumn(4).width = 30;
for (let k = fixed.length + 1; k < scoreStart; k++) R.getColumn(k).width = ((k - fixed.length - 1) % 3 === 1) ? 34 : 10;
for (let k = scoreStart; k <= cComp; k++) R.getColumn(k).width = 10;

// ---------------------------------------------------------------- Resumen
title(S, 'Resumen del análisis documental', 'Todo se calcula a partir de Registro. C_D = cumplimiento documental del indicador (S = 1; P = 0,5; N = 0), en %. B_N = 100 - C_D.');
header(S, 4, ['ID', 'Indicador', 'S', 'P', 'N', 'Calificadas', '% S', '% P', '% N', 'C_D (%)', 'B_N (%)']);
IND.forEach(([id, txt], i) => {
  const r = 5 + i; const col = colL(calCol[id]); const rg = `Registro!$${col}$${FIRST}:$${col}$${LAST}`;
  S.getCell(r, 1).value = id; S.getCell(r, 2).value = txt;
  S.getCell(r, 3).value = { formula: `COUNTIF(${rg},"S")` };
  S.getCell(r, 4).value = { formula: `COUNTIF(${rg},"P")` };
  S.getCell(r, 5).value = { formula: `COUNTIF(${rg},"N")` };
  S.getCell(r, 6).value = { formula: `SUM(C${r}:E${r})` };
  S.getCell(r, 7).value = { formula: `IF(F${r}=0,"",ROUND(100*C${r}/F${r},1))` };
  S.getCell(r, 8).value = { formula: `IF(F${r}=0,"",ROUND(100*D${r}/F${r},1))` };
  S.getCell(r, 9).value = { formula: `IF(F${r}=0,"",ROUND(100*E${r}/F${r},1))` };
  S.getCell(r, 10).value = { formula: `IF(F${r}=0,"",ROUND(100*(C${r}+0.5*D${r})/F${r},1))` };
  S.getCell(r, 11).value = { formula: `IF(J${r}="","",ROUND(100-J${r},1))` };
  for (let k = 1; k <= 11; k++) box(S.getCell(r, k), k > 2 ? FORMULA_FILL : null);
});
const r0 = 5 + IND.length + 2;
header(S, r0, ['Sostenimiento', 'Universidades registradas', 'Con ITD calculado', 'ITD medio', 'ITD mínimo', 'ITD máximo']);
const sostR = `Registro!$C$${FIRST}:$C$${LAST}`, itdR = `Registro!$${colL(cITD)}$${FIRST}:$${colL(cITD)}$${LAST}`;
[...SOST, 'Total'].forEach((s, i) => {
  const r = r0 + 1 + i;
  S.getCell(r, 1).value = s;
  if (s !== 'Total') {
    S.getCell(r, 2).value = { formula: `COUNTIF(${sostR},A${r})` };
    S.getCell(r, 3).value = { formula: `COUNTIFS(${sostR},A${r},${itdR},">=0")` };
    S.getCell(r, 4).value = { formula: `IF(C${r}=0,"",ROUND(AVERAGEIF(${sostR},A${r},${itdR}),1))` };
    S.getCell(r, 5).value = { formula: `IF(C${r}=0,"",MINIFS(${itdR},${sostR},A${r}))` };
    S.getCell(r, 6).value = { formula: `IF(C${r}=0,"",MAXIFS(${itdR},${sostR},A${r}))` };
  } else {
    S.getCell(r, 2).value = { formula: `COUNTA(Registro!$B$${FIRST}:$B$${LAST})` };
    S.getCell(r, 3).value = { formula: `COUNT(${itdR})` };
    S.getCell(r, 4).value = { formula: `IF(C${r}=0,"",ROUND(AVERAGE(${itdR}),1))` };
    S.getCell(r, 5).value = { formula: `IF(C${r}=0,"",MIN(${itdR}))` };
    S.getCell(r, 6).value = { formula: `IF(C${r}=0,"",MAX(${itdR}))` };
  }
  for (let k = 1; k <= 6; k++) box(S.getCell(r, k), k > 1 ? FORMULA_FILL : null);
});
[8, 60, 8, 8, 8, 11, 8, 8, 8, 10, 10].forEach((w, i) => S.getColumn(i + 1).width = w);

// ---------------------------------------------------------------- Reverificación
title(V, 'Reverificación del 20 % de las universidades (confiabilidad del registro)', 'Repetir la verificación completa de 13 universidades elegidas al azar, al menos dos semanas después. Registrar la segunda calificación de cada indicador principal; el acuerdo se calcula solo.');
header(V, 4, ['N.º en Registro', 'Universidad', 'Fecha de la 2.ª verificación', ...IND.slice(0, N_PRIN).map(([id]) => `${id} 2.ª`), ...IND.slice(0, N_PRIN).map(([id]) => `${id} acuerdo`), 'Acuerdos', 'Comparados']);
const aStart = 4 + N_PRIN;
for (let i = 0; i < N_REV; i++) {
  const r = 5 + i;
  [1, 2, 3].forEach(k => box(V.getCell(r, k), INPUT_FILL));
  V.getCell(r, 2).value = { formula: `IF(A${r}="","",INDEX(Registro!$B$${FIRST}:$B$${LAST},A${r}))` }; box(V.getCell(r, 2), FORMULA_FILL);
  IND.slice(0, N_PRIN).forEach(([id], j) => {
    const second = V.getCell(r, 4 + j); box(second, INPUT_FILL);
    second.dataValidation = { type: 'list', allowBlank: true, formulae: [LIST_CAL] };
    const first = `INDEX(Registro!$${colL(calCol[id])}$${FIRST}:$${colL(calCol[id])}$${LAST},$A${r})`;
    const c = V.getCell(r, aStart + j);
    c.value = { formula: `IF(OR($A${r}="",${colL(4 + j)}${r}=""),"",IF(${first}=${colL(4 + j)}${r},1,0))` }; box(c, FORMULA_FILL);
  });
  const ag = `${colL(aStart)}${r}:${colL(aStart + N_PRIN - 1)}${r}`;
  V.getCell(r, aStart + N_PRIN).value = { formula: `SUM(${ag})` }; box(V.getCell(r, aStart + N_PRIN), FORMULA_FILL);
  V.getCell(r, aStart + N_PRIN + 1).value = { formula: `COUNT(${ag})` }; box(V.getCell(r, aStart + N_PRIN + 1), FORMULA_FILL);
}
const rt = 5 + N_REV + 1;
V.getCell(rt, 2).value = 'Porcentaje de acuerdo'; V.getCell(rt, 2).font = { name: FONT, bold: true };
const cA = colL(aStart + N_PRIN), cB = colL(aStart + N_PRIN + 1);
V.getCell(rt, 3).value = { formula: `IF(SUM(${cB}5:${cB}${4 + N_REV})=0,"",ROUND(100*SUM(${cA}5:${cA}${4 + N_REV})/SUM(${cB}5:${cB}${4 + N_REV}),1))` }; box(V.getCell(rt, 3), FORMULA_FILL);
V.getColumn(2).width = 36; V.getColumn(3).width = 14;

// ---------------------------------------------------------------- Instrucciones
title(I, 'Análisis documental de la información pública sobre protección de datos personales', 'Trabajo de integración curricular — Ramón Alejandro Manzaba Castro — UTI, 2026-2027 (OE2)');
[
  ['Propósito', 'Registrar, para cada universidad y escuela politécnica registrada en el CES, si su información pública cumple los 16 indicadores derivados de la LOPDP (hoja Indicadores), con evidencia verificable.'],
  ['Población', '64 universidades y escuelas politécnicas (CES, consulta del 07-11-2026; el portal no indica fecha de corte). Copiar el listado nominal del archivo descargable del CES en la columna B de Registro el día de inicio y anotar cualquier diferencia.'],
  ['Procedimiento', '1) Revisar pie de página, menús de transparencia y normativa, páginas de admisión. 2) Buscar en el sitio y con un buscador restringido al dominio: privacidad, protección de datos, LOPDP, delegado, cookies. 3) Calificar S/P/N, pegar la URL exacta y la fecha. 4) Guardar copia en PDF de la evidencia. 5) En formularios, revisar solo la cláusula informativa; no enviar datos personales.'],
  ['Índice', 'ITD = 100/14 × suma de puntajes de ID01 a ID14 (S = 1; P = 0,5; N = 0). Se calcula solo cuando los 14 indicadores principales están calificados. ID15 e ID16 son complementarios y se reportan aparte en Resumen.'],
  ['Confiabilidad', 'Repetir 13 universidades (20 %) al azar al menos dos semanas después en la hoja Reverificación e informar el porcentaje de acuerdo.'],
  ['Ética', 'Solo información de acceso público. Los resultados se publican agregados por sostenimiento.'],
].forEach(([k, v], i) => {
  const r = 4 + i; I.getCell(r, 1).value = k; I.getCell(r, 1).font = { name: FONT, bold: true }; I.getCell(r, 1).alignment = { vertical: 'top' };
  I.getCell(r, 2).value = v; I.getCell(r, 2).alignment = { wrapText: true, vertical: 'top' }; I.getRow(r).height = 54;
});
I.getColumn(1).width = 18; I.getColumn(2).width = 110;

// ---------------------------------------------------------------- Datos sintéticos (solo --prueba)
let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
if (PRUEBA) {
  for (let r = FIRST; r <= LAST; r++) {
    R.getCell(r, 2).value = `Universidad sintética ${r - FIRST + 1}`;
    R.getCell(r, 3).value = SOST[r - FIRST < 36 ? 0 : (r - FIRST < 44 ? 1 : 2)];
    IND.forEach(([id]) => { if (!(r === LAST && id === 'ID14')) R.getCell(r, calCol[id]).value = CAL[Math.floor(rnd() * 3)]; });
  }
  for (let i = 0; i < N_REV; i++) {
    V.getCell(5 + i, 1).value = 1 + i * 4;
    IND.slice(0, N_PRIN).forEach(([id], j) => {
      const orig = R.getCell(FIRST + i * 4, calCol[id]).value;
      V.getCell(5 + i, 4 + j).value = (j === 0 && i < 3) ? (orig === 'S' ? 'N' : 'S') : orig; // 3 desacuerdos deliberados
    });
  }
}

[I, K, R, S, V, L].forEach(ws => ws.eachRow({ includeEmpty: true }, row => row.eachCell({ includeEmpty: true }, c => {
  c.font = Object.assign({ name: FONT, size: 10 }, c.font || {}, { name: FONT });
})));

// ---------------------------------------------------------------- Verificación con HyperFormula
function toArr(ws) {
  const out = [];
  ws.eachRow({ includeEmpty: true }, (row, r) => { out[r - 1] = []; row.eachCell({ includeEmpty: true }, (c, k) => {
    let v = c.value; if (v && typeof v === 'object' && v.formula) v = '=' + v.formula;
    out[r - 1][k - 1] = v === undefined ? null : v; }); });
  for (let i = 0; i < out.length; i++) if (!out[i]) out[i] = [];
  return out;
}
const sheets = {}; wb.worksheets.forEach(ws => { sheets[ws.name] = toArr(ws); });
const hf = HyperFormula.buildFromSheets(sheets, { licenseKey: 'gpl-v3' });
let nF = 0; const errs = [];
wb.worksheets.forEach(ws => { const sid = hf.getSheetId(ws.name);
  ws.eachRow({ includeEmpty: true }, (row, r) => row.eachCell({ includeEmpty: true }, (c, k) => {
    if (c.value && typeof c.value === 'object' && c.value.formula) { nF++;
      let res = hf.getCellValue({ sheet: sid, row: r - 1, col: k - 1 });
      if (res && typeof res === 'object' && res.type) { errs.push(`${ws.name}!${c.address}: ${res.type} ${res.message || ''}`); res = undefined; }
      c.value = { formula: c.value.formula, result: res === null ? '' : res }; } })); });
const out = { total_formulas: nF, total_errors: errs.length, errors: errs.slice(0, 10) };
if (PRUEBA) {
  // Comprobación independiente en JS del ITD de la primera fila, del C_D de ID01 y del acuerdo
  const sc = v => v === 'S' ? 1 : v === 'P' ? 0.5 : v === 'N' ? 0 : null;
  const itd1 = Math.round(100 / N_PRIN * IND.slice(0, N_PRIN).reduce((a, [id]) => a + sc(R.getCell(FIRST, calCol[id]).value), 0) * 10) / 10;
  let s = 0, p = 0, n = 0; for (let r = FIRST; r <= LAST; r++) { const v = R.getCell(r, calCol.ID01).value; if (v === 'S') s++; else if (v === 'P') p++; else if (v === 'N') n++; }
  out.prueba = {
    itd_fila1_excel: R.getCell(FIRST, cITD).value.result, itd_fila1_js: itd1,
    itd_ultima_fila_incompleta: JSON.stringify(R.getCell(LAST, cITD).value.result),
    cd_id01_excel: S.getCell(5, 10).value.result, cd_id01_js: Math.round(1000 * (s + 0.5 * p) / (s + p + n)) / 10,
    itd_medio_total: S.getCell(r0 + 4, 4).value.result,
    acuerdo_excel: V.getCell(rt, 3).value.result, acuerdo_esperado: Math.round(1000 * (N_REV * N_PRIN - 3) / (N_REV * N_PRIN)) / 10,
  };
}
console.log(JSON.stringify(out, null, 1));
wb.xlsx.writeFile(OUT).then(() => console.log('Escrito: ' + OUT));
