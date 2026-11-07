// Análisis de la encuesta a estudiantes (OE3) y de la validación por expertos.
// Uso:
//   node analisis_encuesta.js encuesta <respuestas.csv>      → depuración, indicadores IE01–IE15, alfa de Cronbach, chi-cuadrado y V de Cramér
//   node analisis_encuesta.js aiken <jueces.csv>             → V de Aiken por ítem y criterio (columnas: item, criterio, J1, J2, …; escala 1–5)
//   node analisis_encuesta.js prueba                         → autoprueba con valores de referencia y datos sintéticos (no son resultados)
// El CSV de respuestas usa los códigos de variable y de opción de encuesta/cuestionario.md (separador , o ;).
// No requiere dependencias externas.
'use strict';
const fs = require('fs');

// ------------------------------------------------------------------ utilidades
function parseCSV(text) {
  const sep = (text.split('\n')[0].match(/;/g) || []).length > (text.split('\n')[0].match(/,/g) || []).length ? ';' : ',';
  const rows = []; let row = [], cur = '', q = false;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (q) { if (ch === '"' && text[i + 1] === '"') { cur += '"'; i++; } else if (ch === '"') q = false; else cur += ch; }
    else if (ch === '"') q = true;
    else if (ch === sep) { row.push(cur); cur = ''; }
    else if (ch === '\n' || ch === '\r') { if (ch === '\r' && text[i + 1] === '\n') i++; row.push(cur); rows.push(row); row = []; cur = ''; }
    else cur += ch;
  }
  if (cur !== '' || row.length) { row.push(cur); rows.push(row); }
  const head = rows.shift().map(h => h.trim());
  return rows.filter(r => r.some(v => v.trim() !== '')).map(r => Object.fromEntries(head.map((h, j) => [h, (r[j] ?? '').trim()])));
}
const num = v => (v === '' || v === undefined || v === null) ? null : Number(v);
const mean = a => a.reduce((s, x) => s + x, 0) / a.length;
const variance = a => { const m = mean(a); return a.reduce((s, x) => s + (x - m) ** 2, 0) / (a.length - 1); }; // muestral
const median = a => { const s = [...a].sort((x, y) => x - y); const n = s.length; return n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2; };
const quantile = (a, p) => { const s = [...a].sort((x, y) => x - y); const h = (s.length - 1) * p; const lo = Math.floor(h); return s[lo] + (h - lo) * ((s[lo + 1] ?? s[lo]) - s[lo]); };
const pct = (k, n) => n ? Math.round(1000 * k / n) / 10 : null;

// Función gamma incompleta regularizada (Numerical Recipes) para el valor p de chi-cuadrado
function gammaln(x) { const c = [76.18009172947146, -86.50532032941677, 24.01409824083091, -1.231739572450155, 0.1208650973866179e-2, -0.5395239384953e-5];
  let y = x, t = x + 5.5; t -= (x + 0.5) * Math.log(t); let s = 1.000000000190015; for (const k of c) s += k / ++y; return -t + Math.log(2.5066282746310005 * s / x); }
function gammq(a, x) { // Q(a, x) = 1 - P(a, x)
  if (x <= 0) return 1;
  if (x < a + 1) { let sum = 1 / a, del = sum, ap = a; for (let n = 0; n < 500; n++) { ap++; del *= x / ap; sum += del; if (Math.abs(del) < Math.abs(sum) * 1e-14) break; }
    return 1 - sum * Math.exp(-x + a * Math.log(x) - gammaln(a)); }
  let b = x + 1 - a, c = 1e300, d = 1 / b, h = d;
  for (let i = 1; i < 500; i++) { const an = -i * (i - a); b += 2; d = an * d + b; if (Math.abs(d) < 1e-300) d = 1e-300; c = b + an / c; if (Math.abs(c) < 1e-300) c = 1e-300; d = 1 / d; const del = d * c; h *= del; if (Math.abs(del - 1) < 1e-14) break; }
  return Math.exp(-x + a * Math.log(x) - gammaln(a)) * h;
}
const chiP = (x, df) => gammq(df / 2, x / 2);

// Chi-cuadrado de Pearson con V de Cramér y control de frecuencias esperadas
function chiSquare(table) {
  const r = table.length, c = table[0].length;
  const rs = table.map(row => row.reduce((s, x) => s + x, 0)), cs = table[0].map((_, j) => table.reduce((s, row) => s + row[j], 0));
  const n = rs.reduce((s, x) => s + x, 0);
  let chi = 0, low = 0;
  for (let i = 0; i < r; i++) for (let j = 0; j < c; j++) { const e = rs[i] * cs[j] / n; if (e < 5) low++; chi += e ? (table[i][j] - e) ** 2 / e : 0; }
  const df = (r - 1) * (c - 1);
  return { chi2: chi, df, p: chiP(chi, df), cramerV: Math.sqrt(chi / (n * Math.min(r - 1, c - 1))), n, celdas_esperado_menor_5_pct: pct(low, r * c) };
}
// Alfa de Cronbach (con correlación ítem-total corregida y alfa si se elimina el ítem)
function cronbach(matrix) { // filas = casos completos; columnas = ítems
  const k = matrix[0].length;
  const alpha = m => { const kk = m[0].length; const items = [...Array(kk).keys()].map(j => variance(m.map(r => r[j]))); const tot = variance(m.map(r => r.reduce((s, x) => s + x, 0))); return kk / (kk - 1) * (1 - items.reduce((s, x) => s + x, 0) / tot); };
  const corr = (x, y) => { const mx = mean(x), my = mean(y); let sxy = 0, sx = 0, sy = 0; x.forEach((v, i) => { sxy += (v - mx) * (y[i] - my); sx += (v - mx) ** 2; sy += (y[i] - my) ** 2; }); return sxy / Math.sqrt(sx * sy); };
  const items = [...Array(k).keys()].map(j => {
    const rest = matrix.map(r => r.reduce((s, x, jj) => s + (jj === j ? 0 : x), 0));
    return { item: j + 1, r_item_total_corregida: +corr(matrix.map(r => r[j]), rest).toFixed(3), alfa_si_se_elimina: +alpha(matrix.map(r => r.filter((_, jj) => jj !== j))).toFixed(3) };
  });
  return { k, n: matrix.length, alfa: +alpha(matrix).toFixed(3), items };
}
// V de Aiken
const aikenV = (ratings, l = 1, c = 5) => ratings.reduce((s, x) => s + (x - l), 0) / (ratings.length * (c - 1));

// ------------------------------------------------------------------ indicadores
const ANY = v => v !== null;
const IND = {
  IE02: { q: 'B2', yes: [1, 2], excl: [8] }, IE03: { q: 'C1', yes: [1, 2] }, IE04: { q: 'C2', yes: [1, 2] },
  IE05: { q: 'C3', yes: [1, 2] }, IE06: { q: 'C4', yes: [1, 2] }, IE07_expreso: { q: 'D1', yes: [1] }, IE07_implicito: { q: 'D1', yes: [2] },
  IE08: { q: 'D2', yes: [1], excl: [3] }, IE09: { q: 'D3', yes: [4, 5] }, IE11: { q: 'E2', yes: [1] },
  IE12_LOPDP: { q: 'E4', yes: [1, 2] }, IE12_SPDP: { q: 'E5', yes: [1] }, IE12_capacitacion: { q: 'E6', yes: [1] },
  IE14_phishing: { q: 'F6', yes: [3, 4], excl: [8] }, IE14_listados: { q: 'F7', yes: [1] }, IE14_vulneracion_comunicada: { q: 'F8', yes: [1] },
  IE15: { q: 'C6', yes: [1], excl: [8] },
};
const B1 = ['B1_01', 'B1_02', 'B1_03', 'B1_04', 'B1_05', 'B1_06', 'B1_07', 'B1_08', 'B1_09', 'B1_10', 'B1_11'];
const E1 = ['E1_a', 'E1_b', 'E1_c', 'E1_d', 'E1_e'];
const F = ['F1', 'F2', 'F3', 'F4', 'F5'];
const grupo = row => { const a = num(row.A1); return a === 1 ? 'Pública' : (a === 2 || a === 3) ? 'Particular' : null; };

function prop(rows, def) {
  const vals = rows.map(r => num(r[def.q])).filter(v => ANY(v) && !(def.excl || []).includes(v));
  const k = vals.filter(v => def.yes.includes(v)).length;
  return { n: vals.length, si: k, pct: pct(k, vals.length) };
}
function cross(rows, isYes) { // tabla 2×2: grupo × (sí/no)
  const t = [[0, 0], [0, 0]]; const G = { 'Pública': 0, 'Particular': 1 };
  rows.forEach(r => { const g = grupo(r); const y = isYes(r); if (g === null || y === null) return; t[G[g]][y ? 0 : 1]++; });
  return t;
}

function analizarEncuesta(rows) {
  const total = rows.length;
  const validas = rows.filter(r => num(r.P00) === 1 && num(r.P01) === 1 && num(r.P02) === 1);
  const out = { depuracion: { recibidas: total, excluidas_por_filtro: total - validas.length, validas: validas.length } };
  out.muestra_por_sostenimiento = Object.fromEntries([1, 2, 3, 9].map(c => [c, validas.filter(r => num(r.A1) === c).length]));
  const b1Valid = validas.filter(r => num(r.B1_99) !== 1);
  out.IE01 = Object.fromEntries(B1.map(q => { const k = b1Valid.filter(r => num(r[q]) === 1).length; return [q, { n: b1Valid.length, si: k, pct: pct(k, b1Valid.length) }]; }));
  for (const [id, def] of Object.entries(IND)) out[id] = prop(validas, def);
  out.IE10 = Object.fromEntries(E1.map(q => [q, prop(validas, { q, yes: [1] })]));
  const e1c = validas.map(r => E1.map(q => num(r[q]))).filter(a => a.every(ANY));
  out.IE10.indice_medio_pct = e1c.length ? Math.round(1000 * mean(e1c.map(a => mean(a)))) / 10 : null;
  const fc = validas.map(r => F.map(q => num(r[q]))).filter(a => a.every(ANY));
  const fm = fc.map(a => mean(a));
  out.IE13 = fc.length ? { n: fc.length, media_ge_4_pct: pct(fm.filter(x => x >= 4).length, fc.length), mediana: median(fm), ric: +(quantile(fm, 0.75) - quantile(fm, 0.25)).toFixed(2) } : null;
  out.confiabilidad = {
    E1_derechos_KR20: e1c.length > 2 ? cronbach(e1c) : null,
    F_confianza: fc.length > 2 ? cronbach(fc) : null,
  };
  const yesOf = (q, yes, excl = []) => r => { const v = num(r[q]); if (!ANY(v) || excl.includes(v)) return null; return yes.includes(v); };
  const tests = {
    'IE03 fines × sostenimiento': yesOf('C1', [1, 2]),
    'IE07 consentimiento expreso × sostenimiento': yesOf('D1', [1]),
    'IE11 canal de derechos × sostenimiento': yesOf('E2', [1]),
    'IE13 confianza (media ≥ 4) × sostenimiento': r => { const a = F.map(q => num(r[q])); return a.every(ANY) ? mean(a) >= 4 : null; },
  };
  out.asociacion = Object.fromEntries(Object.entries(tests).map(([k, f]) => {
    const t = cross(validas, f); const res = chiSquare(t);
    return [k, { tabla_publica_si_no__particular_si_no: t, chi2: +res.chi2.toFixed(3), gl: res.df, p: +res.p.toFixed(4), V_Cramer: +res.cramerV.toFixed(3), celdas_esperado_menor_5_pct: res.celdas_esperado_menor_5_pct,
      nota: res.celdas_esperado_menor_5_pct > 20 ? 'Más del 20 % de celdas con esperado < 5: usar la prueba exacta de Fisher' : '' }];
  }));
  return out;
}

function analizarAiken(rows) {
  const judges = Object.keys(rows[0]).filter(k => /^J\d+$/i.test(k));
  return rows.map(r => { const x = judges.map(j => num(r[j])).filter(ANY); const v = aikenV(x);
    return { item: r.item, criterio: r.criterio, jueces: x.length, mediana: median(x), V: +v.toFixed(3), decision: v >= 0.70 ? 'Se conserva' : 'Reformular o eliminar' }; });
}

// ------------------------------------------------------------------ autoprueba
function prueba() {
  const ok = (name, got, exp, tol = 1e-3) => { const pass = Math.abs(got - exp) <= tol; console.log(`${pass ? 'OK ' : 'ERR'} ${name}: obtenido ${got}, esperado ${exp}`); return pass; };
  let all = true;
  all &= ok('p de chi2 = 3,841 con 1 gl', chiP(3.841, 1), 0.05, 5e-4);
  all &= ok('p de chi2 = 5,991 con 2 gl', chiP(5.991, 2), 0.05, 5e-4);
  all &= ok('p de chi2 = 11,345 con 3 gl', chiP(11.345, 3), 0.01, 5e-4);
  // Tabla 2×2 de referencia: [[10, 20], [20, 10]] → chi2 = 6,667; V = 0,333
  const t = chiSquare([[10, 20], [20, 10]]);
  all &= ok('chi2 de [[10,20],[20,10]]', t.chi2, 6.6667); all &= ok('V de Cramér', t.cramerV, 0.3333);
  // Alfa: ítems idénticos → 1; matriz de referencia calculada a mano → 0,9
  all &= ok('alfa con ítems idénticos', cronbach([[1, 1], [2, 2], [3, 3], [4, 4]]).alfa, 1);
  // [[1,2,1],[2,3,2],[3,3,3],[4,5,3],[5,5,5]]: var ítems 2,5; 1,8; 2,2; var total 18,3 → α = 1,5·(1 − 6,5/18,3) = 0,967
  all &= ok('alfa de matriz de referencia', cronbach([[1, 2, 1], [2, 3, 2], [3, 3, 3], [4, 5, 3], [5, 5, 5]]).alfa, 0.967);
  all &= ok('V de Aiken [5,5,5,5,5]', aikenV([5, 5, 5, 5, 5]), 1);
  all &= ok('V de Aiken [4,4,5,5,3]', aikenV([4, 4, 5, 5, 3]), 0.8);
  all &= ok('Tamaño de muestra N = 841 404', (() => { const N = 841404, z = 1.96, p = 0.5, e = 0.05; return N * z * z * p * p / (e * e * (N - 1) + z * z * p * p); })(), 383.98, 0.01);
  // Datos sintéticos: solo para comprobar que el flujo completo corre (NO son resultados)
  let s = 11; const rnd = () => (s = (s * 16807) % 2147483647) / 2147483647; const pick = a => a[Math.floor(rnd() * a.length)];
  const rows = [...Array(120)].map((_, i) => {
    const r = { P00: i === 0 ? 0 : 1, P01: 1, P02: 1, A1: pick([1, 1, 2, 3, 9]), B1_99: 0, B2: pick([1, 2, 3, 4, 8]), C1: pick([1, 2, 3, 4]), C2: pick([1, 3, 4]), C3: pick([2, 3, 4]), C4: pick([1, 2, 3]), C6: pick([1, 2, 3, 8]),
      D1: pick([1, 2, 3, 4]), D2: pick([1, 2, 3, 4]), D3: pick([1, 2, 3, 4, 5]), E2: pick([1, 2, 3]), E4: pick([1, 2, 3]), E5: pick([0, 1]), E6: pick([1, 2, 3]), F6: pick([1, 2, 3, 4, 8]), F7: pick([1, 2, 3]), F8: pick([1, 2, 3]) };
    B1.forEach(q => r[q] = pick([0, 1])); const base = pick([0, 1]); E1.forEach(q => r[q] = rnd() < 0.8 ? base : 1 - base);
    const lv = pick([1, 2, 3, 4, 5]); F.forEach(q => r[q] = Math.min(5, Math.max(1, lv + pick([-1, 0, 0, 1])))); return r; });
  const res = analizarEncuesta(rows);
  all &= ok('casos excluidos por filtro (sintético)', res.depuracion.excluidas_por_filtro, 1);
  console.log('Flujo completo con datos sintéticos: alfa F =', res.confiabilidad.F_confianza.alfa, '| KR-20 E1 =', res.confiabilidad.E1_derechos_KR20.alfa);
  console.log(all ? 'AUTOPRUEBA SUPERADA' : 'AUTOPRUEBA CON ERRORES');
  process.exitCode = all ? 0 : 1;
}

// ------------------------------------------------------------------ principal
const [mode, file] = process.argv.slice(2);
if (mode === 'encuesta') console.log(JSON.stringify(analizarEncuesta(parseCSV(fs.readFileSync(file, 'utf8'))), null, 1));
else if (mode === 'aiken') console.table(analizarAiken(parseCSV(fs.readFileSync(file, 'utf8'))));
else if (mode === 'prueba') prueba();
else console.log('Uso: node analisis_encuesta.js encuesta <respuestas.csv> | aiken <jueces.csv> | prueba');
