// Genera la plantilla de matriz de riesgos (OE3) y verifica sus fórmulas con HyperFormula.
// Uso: node build_matriz.js <ruta_salida.xlsx> [escenarios.json]
// Sin JSON genera la plantilla con una fila de ejemplo; con JSON genera la matriz aplicada
// (un objeto por escenario, con claves iguales a los encabezados de la hoja Matriz).
const ExcelJS = require('exceljs');
const { HyperFormula } = require('hyperformula');

const OUT = process.argv[2];
const DATA = process.argv[3] ? JSON.parse(require('fs').readFileSync(process.argv[3], 'utf8')) : null;
const FONT = 'Arial';
const N_ROWS = 100;            // filas de escenarios
const FIRST = 5;               // primera fila de datos en Matriz
const LAST = FIRST + N_ROWS - 1;

const PROB = ['Muy baja', 'Baja', 'Media', 'Alta', 'Muy alta'];
const IMP = ['Muy bajo', 'Bajo', 'Medio', 'Alto', 'Muy alto'];
const NIVEL_COLOR = { 'Muy bajo': 'FFC6E0B4', 'Bajo': 'FFE2EFDA', 'Medio': 'FFFFEB9C', 'Alto': 'FFF8CBAD', 'Muy alto': 'FFFF7C80' };
// Tabla de decisión (Cap. 2, Tabla 15). Filas de arriba abajo: Muy alta ... Muy baja.
const DECISION = {
  'Muy alta': ['Medio', 'Alto', 'Alto', 'Muy alto', 'Muy alto'],
  'Alta':     ['Bajo', 'Medio', 'Alto', 'Muy alto', 'Muy alto'],
  'Media':    ['Bajo', 'Medio', 'Medio', 'Alto', 'Muy alto'],
  'Baja':     ['Muy bajo', 'Bajo', 'Medio', 'Alto', 'Alto'],
  'Muy baja': ['Muy bajo', 'Muy bajo', 'Bajo', 'Medio', 'Alto'],
};
const PROB_DESC = [...PROB].reverse(); // Muy alta → Muy baja

const INPUT_FILL = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFFFF2CC' } };
const FORMULA_FILL = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFEDEDED' } };
const HEAD_FILL = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FF1F3864' } };
const GROUP_FILL = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFD9E1F2' } };
const thin = { style: 'thin', color: { argb: 'FFBFBFBF' } };
const BORDER = { top: thin, left: thin, bottom: thin, right: thin };

const wb = new ExcelJS.Workbook();
wb.creator = 'Ramón Alejandro Manzaba Castro';
wb.title = 'Matriz de riesgos LOPDP — plantilla';
wb.calcProperties.fullCalcOnLoad = true;

// Hojas en el orden de presentación
const I = wb.addWorksheet('Instrucciones');
const M = wb.addWorksheet('Matriz', { views: [{ state: 'frozen', xSplit: 1, ySplit: 4 }] });
const D = wb.addWorksheet('Decisión');
const E = wb.addWorksheet('Escalas');
const A = wb.addWorksheet('Amenazas');
const C = wb.addWorksheet('Controles');
const P = wb.addWorksheet('Delphi');
const B = wb.addWorksheet('Brier');
const H = wb.addWorksheet('Mapa de calor');
const L = wb.addWorksheet('Listas');

// Hojas en el orden de presentación

function styleAll(ws) {
  ws.eachRow({ includeEmpty: true }, row => row.eachCell({ includeEmpty: true }, c => {
    c.font = Object.assign({ name: FONT, size: 10 }, c.font || {}, { name: FONT });
  }));
}
function header(ws, rowIdx, values, startCol = 1) {
  values.forEach((v, i) => {
    const c = ws.getCell(rowIdx, startCol + i);
    c.value = v;
    c.font = { name: FONT, bold: true, color: { argb: 'FFFFFFFF' }, size: 10 };
    c.fill = HEAD_FILL;
    c.alignment = { wrapText: true, vertical: 'middle', horizontal: 'center' };
    c.border = BORDER;
  });
}
function title(ws, text, sub) {
  ws.getCell('A1').value = text;
  ws.getCell('A1').font = { name: FONT, bold: true, size: 14, color: { argb: 'FF1F3864' } };
  if (sub) { ws.getCell('A2').value = sub; ws.getCell('A2').font = { name: FONT, italic: true, size: 9 }; }
}
function table(ws, startRow, rows, opts = {}) {
  rows.forEach((r, i) => r.forEach((v, j) => {
    const c = ws.getCell(startRow + i, (opts.startCol || 1) + j);
    c.value = v;
    c.alignment = { wrapText: true, vertical: 'top' };
    c.border = BORDER;
  }));
}
const q = s => `'${s}'`; // nombre de hoja entre comillas

// ---------------------------------------------------------------- Listas
const SUBPROC = ['SP1. Registro y postulación', 'SP2. Admisión y nivelación', 'SP3. Becas y aranceles diferenciados',
  'SP4. Pago de matrícula', 'SP5. Legalización de la matrícula', 'SP6. Reportes y archivo'];
const LISTAS = [
  ['Probabilidad', PROB],
  ['Impacto', IMP],
  ['Sí/No', ['Sí', 'No']],
  ['Dimensión', ['Confidencialidad', 'Integridad', 'Disponibilidad', 'Licitud']],
  ['Tipo de vulnerabilidad', ['Jurídica', 'Organizacional', 'Técnica', 'Grupos vulnerables de titulares']],
  ['Tratamiento', ['Mitigar', 'Transferir', 'Evitar', 'Aceptar']],
  ['Estado', ['Identificado', 'En tratamiento', 'Tratado', 'Aceptado', 'Cerrado']],
  ['Agravantes', [0, 1, 2, 3]],
  ['Subproceso', SUBPROC],
  ['Nivel de riesgo', IMP],
];
const listRef = {};
LISTAS.forEach(([name, vals], j) => {
  const col = j + 1;
  header(L, 1, [name], col);
  vals.forEach((v, i) => { L.getCell(i + 2, col).value = v; L.getCell(i + 2, col).border = BORDER; });
  const letter = L.getColumn(col).letter;
  listRef[name] = `Listas!$${letter}$2:$${letter}$${vals.length + 1}`;
  L.getColumn(col).width = 26;
});
L.getCell('A10').value = 'Hoja de soporte: valores de las listas desplegables. Modificar solo si cambian los criterios aprobados.';
L.getCell('A10').font = { name: FONT, italic: true, size: 9 };

// ---------------------------------------------------------------- Decisión
title(D, 'Tabla de decisión del nivel de riesgo', 'El nivel se asigna por tabla, no por multiplicación (guía SPDP V.2). Impacto muy alto ⇒ nivel mínimo alto.');
D.getCell('A3').value = 'Probabilidad / Impacto';
header(D, 3, ['Probabilidad / Impacto', ...IMP]);
PROB_DESC.forEach((p, i) => {
  const r = 4 + i;
  const c0 = D.getCell(r, 1); c0.value = p; c0.font = { name: FONT, bold: true }; c0.border = BORDER;
  DECISION[p].forEach((lv, j) => {
    const c = D.getCell(r, 2 + j);
    c.value = lv; c.border = BORDER; c.alignment = { horizontal: 'center' };
    c.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: NIVEL_COLOR[lv] } };
  });
});
D.getCell('A10').value = 'Criterios de aceptación del riesgo';
D.getCell('A10').font = { name: FONT, bold: true, size: 12 };
header(D, 11, ['Nivel', 'Criterio']);
D.mergeCells('B11:F11');
const ACEPT = [
  ['Muy bajo', 'Aceptable. Registrar la decisión y monitorear periódicamente.'],
  ['Bajo', 'Aceptable. Registrar la decisión y monitorear periódicamente.'],
  ['Medio', 'Tratar dentro del plan anual, salvo aceptación formal y justificada de la dirección.'],
  ['Alto', 'Tratamiento prioritario. Si afecta categorías especiales o tratamiento a gran escala, activar EIPD (art. 42 LOPDP).'],
  ['Muy alto', 'Tratamiento prioritario y EIPD. Con impacto muy alto sobre el titular, no puede aceptarse sin observaciones del DPD y del área jurídica y aprobación de la máxima autoridad.'],
];
ACEPT.forEach(([n, t], i) => {
  const r = 12 + i;
  D.getCell(r, 1).value = n; D.getCell(r, 1).border = BORDER;
  D.getCell(r, 1).fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: NIVEL_COLOR[n] } };
  D.mergeCells(`B${r}:F${r}`);
  D.getCell(r, 2).value = t; D.getCell(r, 2).alignment = { wrapText: true, vertical: 'top' }; D.getCell(r, 2).border = BORDER;
  D.getRow(r).height = 30;
});
D.getCell('A18').value = 'Fuente: Capítulo 2, Tablas de decisión y criterios de aceptación; Guía SPDP V.2 (Res. SPDP-SPD-2026-0012-R).';
D.getCell('A18').font = { name: FONT, italic: true, size: 9 };
D.getColumn(1).width = 24; for (let c = 2; c <= 6; c++) D.getColumn(c).width = 14;

const DEC_ROWS = `${q('Decisión')}!$A$4:$A$8`;
const DEC_COLS = `${q('Decisión')}!$B$3:$F$3`;
const DEC_BODY = `${q('Decisión')}!$B$4:$F$8`;

// ---------------------------------------------------------------- Escalas
title(E, 'Escalas de probabilidad e impacto', 'Versión inicial propuesta en el Capítulo 2; se calibra con el panel Delphi antes de aplicarla.');
E.getCell('A4').value = 'Probabilidad (lapso anual)'; E.getCell('A4').font = { name: FONT, bold: true, size: 12 };
header(E, 5, ['Nivel', 'Valor ordinal', 'Frecuencia anual esperada', 'Descripción orientativa']);
table(E, 6, [
  ['Muy baja', 1, 'Menos de una vez cada 10 años', 'Sin antecedentes en la institución ni en el sector; la amenaza requiere capacidades poco comunes.'],
  ['Baja', 2, 'Una vez cada 2 a 10 años', 'Antecedentes en el sector, pero los controles existentes dificultan su materialización.'],
  ['Media', 3, 'Aproximadamente una vez cada 1 a 2 años', 'Antecedentes en IES similares y controles parciales.'],
  ['Alta', 4, 'Entre 1 y 5 veces por año', 'El evento ha ocurrido en la institución o la vulnerabilidad es conocida y explotable.'],
  ['Muy alta', 5, 'Más de 5 veces por año', 'El evento es recurrente o la vulnerabilidad se explota con facilidad.'],
]);
E.getCell('A12').value = 'Impacto sobre el titular (adaptado de ENISA, 2013)'; E.getCell('A12').font = { name: FONT, bold: true, size: 12 };
header(E, 13, ['Nivel', 'Valor ordinal', 'Consecuencias para el titular']);
E.mergeCells('C13:D13');
const IMP_T = [
  'Molestias menores que el titular supera sin dificultad (por ejemplo, reingresar información).',
  'Inconvenientes que el titular supera con algún esfuerzo (costos menores, tiempo, molestias).',
  'Consecuencias significativas que puede superar con dificultad (pérdida de oportunidades académicas, cargos indebidos reversibles, temor o estrés).',
  'Consecuencias graves, difíciles de superar (fraude o suplantación de identidad, discriminación, exclusión de beneficios, daño reputacional).',
  'Consecuencias irreversibles o que afectan derechos fundamentales, la salud o la integridad (exposición de datos de salud o discapacidad, afectación a menores de edad).',
];
IMP.forEach((n, i) => { const r = 14 + i; table(E, r, [[n, i + 1, IMP_T[i]]]); E.mergeCells(`C${r}:D${r}`); E.getRow(r).height = 30; });
E.getCell('A20').value = 'Impacto sobre el responsable (perspectiva secundaria)'; E.getCell('A20').font = { name: FONT, bold: true, size: 12 };
header(E, 21, ['Nivel', 'Valor ordinal', 'Consecuencias para la institución']);
E.mergeCells('C21:D21');
const IMP_R = [
  'Sin consecuencias legales ni económicas relevantes.',
  'Requerimiento u observación de la autoridad sin sanción; costos de respuesta menores.',
  'Medidas correctivas ordenadas por la SPDP; costos de respuesta moderados; cobertura mediática local.',
  'Sanción administrativa; costos de respuesta significativos; afectación reputacional nacional.',
  'Sanción por infracción grave (art. 72 LOPDP); interrupción del servicio académico; pérdida de confianza masiva.',
];
IMP.forEach((n, i) => { const r = 22 + i; table(E, r, [[n, i + 1, IMP_R[i]]]); E.mergeCells(`C${r}:D${r}`); E.getRow(r).height = 28; });
E.getCell('A28').value = 'Criterios agravantes del impacto (cada uno suma un nivel; máximo: Muy alto)'; E.getCell('A28').font = { name: FONT, bold: true, size: 12 };
header(E, 29, ['Criterio', 'Fundamento', 'Ejemplo en matrícula']);
E.mergeCells('C29:D29');
[
  ['Categorías especiales de datos o grupos vulnerables (incluidos adolescentes)', 'LOPDP art. 25; guía SPDP', 'Certificados de discapacidad; aspirantes menores de edad'],
  ['Número de titulares afectados superior al umbral masivo definido por la institución', 'Guía SPDP', 'Base completa de aspirantes del periodo'],
  ['Vulneración intencional o datos combinables que facilitan la identificación', 'Guía SPDP; ENISA (2013)', 'Exfiltración por atacante con cédula + datos socioeconómicos'],
].forEach((r, i) => { table(E, 30 + i, [r]); E.mergeCells(`C${30 + i}:D${30 + i}`); E.getRow(30 + i).height = 30; });
E.getColumn(1).width = 30; E.getColumn(2).width = 22; E.getColumn(3).width = 40; E.getColumn(4).width = 60;

// ---------------------------------------------------------------- Amenazas
title(A, 'Catálogo de amenazas (proceso de admisión y matrícula)', 'Punto de partida; ampliar en la fase de identificación.');
header(A, 4, ['ID', 'Amenaza', 'Comunidad de amenaza', 'Vector típico', 'Dimensiones', 'Subprocesos']);
table(A, 5, [
  ['AM-01', 'Phishing y robo de credenciales institucionales', 'Ciberdelincuencia organizada', 'Correo fraudulento dirigido al personal de admisiones', 'C, I', 'SP1–SP5'],
  ['AM-02', 'Ransomware', 'Ciberdelincuencia organizada', 'Credenciales comprometidas; vulnerabilidades sin parche', 'C, I, D', 'Todos'],
  ['AM-03', 'Acceso indebido por privilegios excesivos', 'Personal interno o temporal', 'Perfiles por unidad y no por función en el SGA', 'C', 'SP2, SP3, SP5'],
  ['AM-04', 'Exposición por enlaces o carpetas compartidas', 'Personal interno (error humano)', 'Enlace "cualquiera con el enlace" en la nube', 'C', 'SP3, SP6'],
  ['AM-05', 'Publicación de listados con datos personales', 'Personal interno (error humano)', 'Listas de admitidos con cédula y calificaciones en canales públicos', 'C, Licitud', 'SP2'],
  ['AM-06', 'Tratamiento por proveedor sin garantías contractuales', 'Encargados (proveedores SaaS)', 'Contrato sin cláusulas de protección de datos', 'C, Licitud', 'SP1, SP4, SP5'],
  ['AM-07', 'Conservación indefinida de expedientes', 'Responsable (falla organizacional)', 'Ausencia de política de conservación y eliminación', 'Licitud, C', 'SP6'],
  ['AM-08', 'Uso de datos para finalidades no informadas', 'Responsable (falla organizacional)', 'Consentimiento genérico usado para marketing', 'Licitud', 'SP1'],
  ['AM-09', 'Fraude en pagos o suplantación del pagador', 'Ciberdelincuencia', 'Manipulación de comprobantes; compromiso de la pasarela', 'C, I', 'SP4'],
  ['AM-10', 'Alteración de calificaciones o resultados de admisión', 'Interno malicioso o atacante externo', 'Cuenta privilegiada comprometida', 'I', 'SP2'],
  ['AM-11', 'Indisponibilidad del portal en el periodo de postulación', 'Fallas técnicas o ataque de denegación de servicio', 'Saturación; fallo del proveedor', 'D', 'SP1, SP4'],
  ['AM-12', 'Pérdida de documentación por falta de respaldo', 'Fallas técnicas o error humano', 'Borrado accidental sin copia de seguridad', 'D, I', 'SP3, SP5'],
]);
[8, 42, 30, 46, 14, 14].forEach((w, i) => A.getColumn(i + 1).width = w);

// ---------------------------------------------------------------- Controles
title(C, 'Catálogo de controles (referencia ISO/IEC 27002:2022)', 'Controles candidatos para el tratamiento de riesgos del proceso de matrícula.');
header(C, 4, ['Ref. ISO/IEC 27002:2022', 'Control', 'Tipo', 'Aplicación en el proceso de matrícula']);
table(C, 5, [
  ['5.1', 'Políticas de seguridad de la información', 'Organizacional', 'Política de protección de datos del proceso de admisión'],
  ['5.9', 'Inventario de información y otros activos asociados', 'Organizacional', 'RAT y registro de repositorios con datos de aspirantes'],
  ['5.12', 'Clasificación de la información', 'Organizacional', 'Etiquetar como restringidos los certificados de discapacidad y fichas socioeconómicas'],
  ['5.15', 'Control de acceso', 'Técnico', 'Acceso por función a carpetas y módulos del SGA'],
  ['5.18', 'Derechos de acceso', 'Organizacional', 'Revisión de accesos al cierre de cada periodo de admisión'],
  ['5.19 / 5.20', 'Seguridad en relaciones y acuerdos con proveedores', 'Jurídico', 'Cláusulas de protección de datos con pasarela, CRM, nube y LMS'],
  ['5.24 / 5.26', 'Planificación y respuesta a incidentes', 'Organizacional', 'Procedimiento de notificación en el término del art. 43 LOPDP'],
  ['5.31', 'Requisitos legales, regulatorios y contractuales', 'Jurídico', 'Matriz de requisitos LOPDP, RLOPDP y resoluciones SPDP'],
  ['5.34', 'Privacidad y protección de la información personal', 'Jurídico', 'Consentimiento por finalidad; aviso de privacidad del formulario'],
  ['6.3', 'Concienciación, educación y formación', 'Organizacional', 'Capacitación al personal de admisiones y temporal'],
  ['8.2', 'Derechos de acceso privilegiado', 'Técnico', 'Cuentas administrativas separadas y registradas'],
  ['8.5', 'Autenticación segura', 'Técnico', 'Autenticación multifactor para personal con acceso a datos de aspirantes'],
  ['8.6', 'Gestión de la capacidad', 'Técnico', 'Dimensionar el portal para los cierres de postulación'],
  ['8.7', 'Protección contra malware', 'Técnico', 'Protección de puestos de trabajo y servidores del proceso'],
  ['8.8', 'Gestión de vulnerabilidades técnicas', 'Técnico', 'Parcheo del SGA, portal y servidores en plazos definidos'],
  ['8.10', 'Eliminación de la información', 'Técnico', 'Eliminación de expedientes de no admitidos al vencer el plazo'],
  ['8.11', 'Enmascaramiento de datos', 'Técnico', 'Seudonimizar reportes y listados de admitidos'],
  ['8.12', 'Prevención de fuga de datos', 'Técnico', 'Bloquear enlaces públicos en carpetas restringidas'],
  ['8.13', 'Copias de seguridad de la información', 'Técnico', 'Respaldo cifrado de expedientes'],
  ['8.15 / 8.16', 'Registro y monitoreo de actividades', 'Técnico', 'Registro de accesos a fichas socioeconómicas'],
  ['8.24', 'Uso de criptografía', 'Técnico', 'Cifrado en tránsito y en reposo de documentos sensibles'],
]);
[20, 44, 16, 60].forEach((w, i) => C.getColumn(i + 1).width = w);

// ---------------------------------------------------------------- Matriz
M.getCell('A1').value = 'Matriz de riesgos del tratamiento de datos personales — LOPDP';
M.getCell('A1').font = { name: FONT, bold: true, size: 14, color: { argb: 'FF1F3864' } };
M.getCell('A2').value = DATA
  ? 'Matriz preliminar — UTI, proceso de admisión y matrícula (sede Quito). Escenarios candidatos derivados de la literatura: las vulnerabilidades, los controles existentes, la probabilidad y el impacto se completan con el diagnóstico autorizado y el panel Delphi.'
  : 'Leyenda: celdas amarillas = ingresar datos; celdas grises = fórmula (no editar). Una fila por escenario y dimensión. La fila 5 es un EJEMPLO ficticio: reemplazar o borrar.';
M.getCell('A2').font = { name: FONT, italic: true, size: 9 };
const COLS = [
  // [encabezado, ancho, tipo: 'in' | 'f', lista?]
  ['ID', 9, 'in'],
  ['Proceso / subproceso', 24, 'in', 'Subproceso'],
  ['Actividad de tratamiento', 30, 'in'],
  ['Categorías de datos', 26, 'in'],
  ['¿Categoría especial?', 11, 'in', 'Sí/No'],
  ['Titulares (tipo y n.º estimado)', 22, 'in'],
  ['¿Grupo vulnerable?', 11, 'in', 'Sí/No'],
  ['Activo / sistema', 22, 'in'],
  ['Dimensión (C/I/D/Licitud)', 16, 'in', 'Dimensión'],
  ['Comunidad de amenaza', 24, 'in'],
  ['Vector', 26, 'in'],
  ['Vulnerabilidad', 30, 'in'],
  ['Tipo de vulnerabilidad', 18, 'in', 'Tipo de vulnerabilidad'],
  ['Art. LOPDP / norma SPDP', 18, 'in'],
  ['Control existente', 24, 'in'],
  ['Probabilidad inherente (lapso anual)', 14, 'in', 'Probabilidad'],
  ['Rationale probabilidad', 34, 'in'],
  ['Impacto inherente (titular)', 13, 'in', 'Impacto'],
  ['Impacto (responsable)', 13, 'in', 'Impacto'],
  ['Rationale impacto', 34, 'in'],
  ['Agravantes (n.º)', 11, 'in', 'Agravantes'],
  ['Impacto ajustado (titular)', 13, 'f'],
  ['Nivel inherente', 13, 'f'],
  ['Tratamiento', 13, 'in', 'Tratamiento'],
  ['Control propuesto (ref. ISO/IEC 27002)', 32, 'in'],
  ['Responsable', 20, 'in'],
  ['Plazo', 12, 'in'],
  ['Probabilidad residual', 13, 'in', 'Probabilidad'],
  ['Impacto residual (ajustado)', 13, 'in', 'Impacto'],
  ['Nivel residual', 13, 'f'],
  ['¿Requiere EIPD?', 16, 'f'],
  ['Aceptación del riesgo residual', 30, 'f'],
  ['Indicador de monitoreo', 30, 'in'],
  ['Estado', 14, 'in', 'Estado'],
];
const col = name => M.getColumn(COLS.findIndex(c => c[0] === name) + 1).letter;
// Bloques (fila 3)
const BLOQUES = [
  ['Identificación del tratamiento', 1, 8], ['Escenario de riesgo', 9, 15], ['Riesgo inherente', 16, 23],
  ['Tratamiento', 24, 27], ['Riesgo residual', 28, 32], ['Monitoreo', 33, 34],
];
BLOQUES.forEach(([t, a, b]) => {
  M.mergeCells(3, a, 3, b);
  const c = M.getCell(3, a);
  c.value = t; c.fill = GROUP_FILL; c.font = { name: FONT, bold: true }; c.alignment = { horizontal: 'center' }; c.border = BORDER;
});
header(M, 4, COLS.map(c => c[0]));
M.getRow(4).height = 54;
COLS.forEach((c, i) => { M.getColumn(i + 1).width = c[1]; });

const cP = col('Probabilidad inherente (lapso anual)'), cI = col('Impacto inherente (titular)'), cAg = col('Agravantes (n.º)');
const cIA = col('Impacto ajustado (titular)'), cNI = col('Nivel inherente'), cPR = col('Probabilidad residual');
const cIR = col('Impacto residual (ajustado)'), cNR = col('Nivel residual'), cE = col('¿Categoría especial?');
const cGV = col('¿Grupo vulnerable?'), cEIPD = col('¿Requiere EIPD?'), cAc = col('Aceptación del riesgo residual');
const IMPL = listRef['Impacto'];
const F = {
  [cIA]: r => `IF(${cI}${r}="","",INDEX(${IMPL},MIN(5,MATCH(${cI}${r},${IMPL},0)+IF(${cAg}${r}="",0,${cAg}${r}))))`,
  [cNI]: r => `IF(OR(${cP}${r}="",${cIA}${r}=""),"",INDEX(${DEC_BODY},MATCH(${cP}${r},${DEC_ROWS},0),MATCH(${cIA}${r},${DEC_COLS},0)))`,
  [cNR]: r => `IF(OR(${cPR}${r}="",${cIR}${r}=""),"",INDEX(${DEC_BODY},MATCH(${cPR}${r},${DEC_ROWS},0),MATCH(${cIR}${r},${DEC_COLS},0)))`,
  [cEIPD]: r => `IF(${cNI}${r}="","",IF(OR(${cNI}${r}="Alto",${cNI}${r}="Muy alto"),IF(OR(${cE}${r}="Sí",${cGV}${r}="Sí"),"Sí (obligatoria)","Valorar"),"Recomendada por defecto"))`,
  [cAc]: r => `IF(${cNR}${r}="","",IF(${cIR}${r}="Muy alto","Requiere observaciones DPD/jurídico y aprobación de la máxima autoridad",IF(OR(${cNR}${r}="Muy bajo",${cNR}${r}="Bajo"),"Aceptable (registrar y monitorear)",IF(${cNR}${r}="Medio","Tratar en plan anual o aceptación formal","No aceptable: tratamiento prioritario"))))`,
};

const EJEMPLO = [
  'R-001', 'SP3. Becas y aranceles diferenciados',
  'Recepción y almacenamiento de certificados de discapacidad y fichas socioeconómicas',
  'Discapacidad y salud; socioeconómicos; identificación', 'Sí', 'Aspirantes y núcleo familiar (≈300 por periodo)', 'Sí',
  'Carpeta compartida en la nube (Bienestar Estudiantil)', 'Confidencialidad',
  'Ciberdelincuencia (credenciales robadas); personal interno con acceso excesivo',
  'Enlace de carpeta compartido como público o cuenta comprometida por phishing',
  'Carpeta sin clasificación ni restricción de acceso; documentos recibidos por correo', 'Organizacional',
  'LOPDP arts. 25, 37 y 40', 'Contraseña institucional sin MFA',
  'Media', 'EJEMPLO: mediana Delphi ronda 2 = 3 (RIC = 1); exposición por enlaces compartidos es frecuente en el sector (Ulven y Wangen, 2021).',
  'Alto', 'Alto', 'EJEMPLO: datos de discapacidad y socioeconómicos de ≈300 titulares; riesgo de discriminación y exclusión de beneficios.',
  1, null, null, 'Mitigar',
  '5.12 Clasificación; 5.15 Control de acceso; 8.5 Autenticación segura (MFA); 8.12 Prevención de fuga; minimización (guardar solo la verificación)',
  'Dirección de TI y Bienestar Estudiantil', '3 meses', 'Baja', 'Medio', null, null, null,
  'N.º de enlaces públicos detectados por mes; % de carpetas sensibles con acceso restringido', 'Identificado',
];

for (let r = FIRST; r <= LAST; r++) {
  COLS.forEach((c, i) => {
    const cell = M.getCell(r, i + 1);
    const letter = M.getColumn(i + 1).letter;
    cell.border = BORDER;
    cell.alignment = { wrapText: true, vertical: 'top' };
    if (c[2] === 'f') {
      cell.value = { formula: F[letter](r) };
      cell.fill = FORMULA_FILL;
    } else {
      cell.fill = INPUT_FILL;
      if (DATA) { const row = DATA[r - FIRST]; if (row && row[c[0]] !== undefined) cell.value = row[c[0]]; }
      else if (r === FIRST && EJEMPLO[i] !== null) cell.value = EJEMPLO[i];
      if (c[3]) cell.dataValidation = { type: 'list', allowBlank: true, formulae: [listRef[c[3]]], showErrorMessage: true, errorTitle: 'Valor no válido', error: 'Seleccione un valor de la lista.' };
    }
  });
}
if (DATA) DATA.forEach((_, i) => { M.getRow(FIRST + i).height = 75; }); else M.getRow(FIRST).height = 75;
// Formato condicional de niveles
[cIA, cNI, cNR].forEach(letter => {
  M.addConditionalFormatting({
    ref: `${letter}${FIRST}:${letter}${LAST}`,
    rules: Object.entries(NIVEL_COLOR).map(([lv, color], k) => ({
      type: 'cellIs', operator: 'equal', formulae: [`"${lv}"`], priority: k + 1,
      style: { fill: { type: 'pattern', pattern: 'solid', bgColor: { argb: color } }, font: { bold: true } },
    })),
  });
});
M.autoFilter = { from: { row: 4, column: 1 }, to: { row: 4, column: COLS.length } };

// ---------------------------------------------------------------- Mapa de calor
title(H, 'Mapa de calor (representación, no calibración)', 'Número de escenarios por celda, calculado desde la hoja Matriz.');
function heat(startRow, label, probCol, impCol) {
  H.getCell(startRow, 1).value = label; H.getCell(startRow, 1).font = { name: FONT, bold: true, size: 12 };
  header(H, startRow + 1, ['Probabilidad / Impacto', ...IMP]);
  PROB_DESC.forEach((p, i) => {
    const r = startRow + 2 + i;
    const c0 = H.getCell(r, 1); c0.value = p; c0.font = { name: FONT, bold: true }; c0.border = BORDER;
    IMP.forEach((imp, j) => {
      const c = H.getCell(r, 2 + j);
      const hc = H.getColumn(2 + j).letter;
      c.value = { formula: `COUNTIFS(Matriz!$${probCol}$${FIRST}:$${probCol}$${LAST},$A${r},Matriz!$${impCol}$${FIRST}:$${impCol}$${LAST},${hc}$${startRow + 1})` };
      c.alignment = { horizontal: 'center' }; c.border = BORDER;
      c.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: NIVEL_COLOR[DECISION[p][j]] } };
    });
  });
}
heat(4, 'Riesgo inherente', cP, cIA);
heat(12, 'Riesgo residual', cPR, cIR);
H.getCell('A20').value = 'Resumen por nivel'; H.getCell('A20').font = { name: FONT, bold: true, size: 12 };
header(H, 21, ['Nivel', 'Inherente', 'Residual']);
IMP.forEach((lv, i) => {
  const r = 22 + i;
  table(H, r, [[lv]]);
  H.getCell(r, 2).value = { formula: `COUNTIF(Matriz!$${cNI}$${FIRST}:$${cNI}$${LAST},$A${r})` };
  H.getCell(r, 3).value = { formula: `COUNTIF(Matriz!$${cNR}$${FIRST}:$${cNR}$${LAST},$A${r})` };
  [2, 3].forEach(k => { H.getCell(r, k).border = BORDER; H.getCell(r, k).alignment = { horizontal: 'center' }; });
  H.getCell(r, 1).fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: NIVEL_COLOR[lv] } };
});
H.getCell('A27').value = 'Total'; H.getCell('A27').font = { name: FONT, bold: true };
H.getCell('B27').value = { formula: 'SUM(B22:B26)' }; H.getCell('C27').value = { formula: 'SUM(C22:C26)' };
H.getColumn(1).width = 24; for (let c = 2; c <= 6; c++) H.getColumn(c).width = 13;

// ---------------------------------------------------------------- Brier
title(B, 'Calibración de expertos — puntaje de Brier', 'Cada experto indica la probabilidad (0 a 1) de que la afirmación sea verdadera. BS = (1/N)·Σ(f − o)². Umbral: BS ≤ 0,25.');
header(B, 4, ['ID', 'Afirmación de calibración', 'E01', 'E02', 'E03', 'E04', 'E05', 'Resultado real (1 = verdadera, 0 = falsa)', 'Fuente de verificación']);
const CALIB = [
  ['La LOPDP se publicó en el Registro Oficial en 2021.', 1, 'R.O. Quinto Supl. 459, 26-05-2021'],
  ['El art. 43 de la LOPDP fija un término de cinco días para notificar vulneraciones a la autoridad.', 1, 'LOPDP art. 43'],
  ['ISO/IEC 27005:2022 es una norma certificable.', 0, 'ISO/IEC 27005:2022 (norma de orientación)'],
  ['El Reglamento General a la LOPDP se expidió mediante Decreto Ejecutivo N.º 904.', 1, 'R.O. Tercer Supl. 435, 13-11-2023'],
  ['Según Sophos (2024), más del 60 % de las IES encuestadas sufrió ransomware en el último año.', 1, 'Sophos, State of Ransomware in Education 2024 (66 %)'],
  ['ISO/IEC 27002:2022 agrupa sus controles en cuatro temas.', 1, 'ISO/IEC 27002:2022'],
  ['ISO/IEC 27002:2022 contiene más de 100 controles.', 0, 'ISO/IEC 27002:2022 (93 controles)'],
  ['El RGPD europeo es aplicable desde mayo de 2018.', 1, 'Reglamento (UE) 2016/679, art. 99'],
  ['LINDDUN incluye la categoría de amenaza "Spoofing".', 0, 'Deng et al. (2011)'],
  ['La Res. SPDP-SPD-2026-0005-R regula el tratamiento de datos personales a gran escala.', 1, 'R.O. Supl. 231, 25-02-2026'],
];
const EJ_E01 = [0.9, 0.7, 0.4, 0.6, 0.8, 0.6, 0.3, 0.9, 0.2, 0.8]; // ejemplo ficticio
CALIB.forEach(([t, o, src], i) => {
  const r = 5 + i;
  table(B, r, [[`C${String(i + 1).padStart(2, '0')}`, t]]);
  for (let k = 3; k <= 7; k++) {
    const c = B.getCell(r, k); c.border = BORDER; c.fill = INPUT_FILL; c.numFmt = '0.00';
    c.dataValidation = { type: 'decimal', operator: 'between', allowBlank: true, formulae: [0, 1], showErrorMessage: true, error: 'Ingrese una probabilidad entre 0 y 1.' };
  }
  if (!DATA) B.getCell(r, 3).value = EJ_E01[i];
  B.getCell(r, 8).value = o; B.getCell(r, 8).border = BORDER; B.getCell(r, 8).alignment = { horizontal: 'center' };
  B.getCell(r, 9).value = src; B.getCell(r, 9).border = BORDER; B.getCell(r, 9).font = { name: FONT, size: 8, italic: true };
  B.getRow(r).height = 28;
});
const labels = [['Puntaje de Brier (BS)', 16], ['Peso para ponderación (1 − BS si calibrado; 0 si no)', 17], ['Calibración', 18]];
labels.forEach(([t, r]) => { B.getCell(r, 2).value = t; B.getCell(r, 2).font = { name: FONT, bold: true }; });
for (let k = 3; k <= 7; k++) {
  const L_ = B.getColumn(k).letter;
  const rng = `${L_}5:${L_}14`;
  B.getCell(16, k).value = { formula: `IF(COUNT(${rng})<10,"",(SUMSQ(${rng})-2*SUMPRODUCT(${rng},$H$5:$H$14)+SUMSQ($H$5:$H$14))/COUNT(${rng}))` };
  B.getCell(16, k).numFmt = '0.000';
  B.getCell(17, k).value = { formula: `IF(${L_}16="","",IF(${L_}16<=0.25,1-${L_}16,0))` };
  B.getCell(17, k).numFmt = '0.000';
  B.getCell(18, k).value = { formula: `IF(${L_}16="","",IF(${L_}16<=0.25,"Calibrado","No calibrado"))` };
  [16, 17, 18].forEach(r => { B.getCell(r, k).fill = FORMULA_FILL; B.getCell(r, k).border = BORDER; B.getCell(r, k).alignment = { horizontal: 'center' }; });
}
B.getCell('B20').value = 'La columna E01 contiene valores de EJEMPLO; borrarlos antes de aplicar el instrumento. El BS se calcula solo cuando el experto responde las 10 afirmaciones.';
B.getCell('B20').font = { name: FONT, italic: true, size: 9 };
[7, 62, 9, 9, 9, 9, 9, 18, 34].forEach((w, i) => B.getColumn(i + 1).width = w);

// ---------------------------------------------------------------- Delphi
title(P, 'Registro de estimaciones Delphi', 'Valores ordinales 1–5 (1 = Muy baja/Muy bajo … 5 = Muy alta/Muy alto). Consenso: RIC ≤ 1. Máximo tres rondas.');
header(P, 4, ['ID escenario', 'Variable', 'Ronda', 'E01', 'E02', 'E03', 'E04', 'E05', 'Mediana', 'Q1', 'Q3', 'RIC', '¿Consenso?', 'Nivel (mediana)', 'Media ponderada (Brier)', 'Nivel (ponderado)']);
const N_DEL = 60;
for (let i = 0; i < N_DEL; i++) {
  const r = 5 + i;
  const rng = `D${r}:H${r}`;
  for (let k = 1; k <= 8; k++) {
    const c = P.getCell(r, k); c.border = BORDER; c.fill = INPUT_FILL;
    if (k === 2) c.dataValidation = { type: 'list', allowBlank: true, formulae: ['"Probabilidad,Impacto"'] };
    if (k === 3) c.dataValidation = { type: 'whole', operator: 'between', allowBlank: true, formulae: [1, 3] };
    if (k >= 4) c.dataValidation = { type: 'whole', operator: 'between', allowBlank: true, formulae: [1, 5], showErrorMessage: true, error: 'Ingrese un valor entero de 1 a 5.' };
  }
  const lvl = x => `IF(B${r}="Probabilidad",INDEX(${listRef['Probabilidad']},ROUND(${x},0)),INDEX(${listRef['Impacto']},ROUND(${x},0)))`;
  const fs = [
    `IF(COUNT(${rng})=0,"",MEDIAN(${rng}))`,
    `IF(COUNT(${rng})=0,"",QUARTILE(${rng},1))`,
    `IF(COUNT(${rng})=0,"",QUARTILE(${rng},3))`,
    `IF(COUNT(${rng})=0,"",K${r}-J${r})`,
    `IF(L${r}="","",IF(L${r}<=1,"Sí","No"))`,
    `IF(OR(I${r}="",B${r}=""),"",${lvl(`I${r}`)})`,
    `IF(COUNT(${rng})<5,"",IFERROR(SUMPRODUCT(${rng},Brier!$C$17:$G$17)/SUM(Brier!$C$17:$G$17),""))`,
    `IF(OR(O${r}="",B${r}=""),"",${lvl(`O${r}`)})`,
  ];
  fs.forEach((f, j) => {
    const c = P.getCell(r, 9 + j);
    c.value = { formula: f }; c.fill = FORMULA_FILL; c.border = BORDER; c.alignment = { horizontal: 'center' };
    if (j < 4 || j === 6) c.numFmt = '0.00';
  });
}
if (!DATA) ['R-001', 'Probabilidad', 1, 3, 4, 3, 3, 2].forEach((v, k) => { P.getCell(5, k + 1).value = v; });
P.getCell(`A${6 + N_DEL}`).value = 'La fila 5 es un EJEMPLO ficticio; borrarla antes de aplicar el instrumento. La media ponderada usa los pesos de la hoja Brier y requiere las cinco respuestas.';
P.getCell(`A${6 + N_DEL}`).font = { name: FONT, italic: true, size: 9 };
[12, 14, 7, 6, 6, 6, 6, 6, 9, 7, 7, 7, 11, 14, 14, 14].forEach((w, i) => P.getColumn(i + 1).width = w);
P.views = [{ state: 'frozen', ySplit: 4 }];

// ---------------------------------------------------------------- Instrucciones (primera hoja)
title(I, 'Plantilla de matriz de riesgos del tratamiento de datos personales (LOPDP)', 'Trabajo de integración curricular — Ramón Alejandro Manzaba Castro — UTI, 2026');
const INSTR = [
  ['Propósito', 'Registrar, evaluar y monitorear los escenarios de riesgo del tratamiento de datos personales conforme a la metodología del Capítulo 2 (fases 0 a 4), la LOPDP, su Reglamento General y la guía de gestión de riesgos de la SPDP (V.2, 2026).'],
  ['Leyenda', 'Celdas amarillas: datos que ingresa el usuario. Celdas grises: fórmulas (no editar). Las listas desplegables provienen de la hoja Listas.'],
  ['Paso 1', 'Fase 1 (identificación): completar en Matriz los bloques "Identificación del tratamiento" y "Escenario de riesgo". Una fila por escenario y por dimensión (confidencialidad, integridad, disponibilidad o licitud). Usar los catálogos de Amenazas y Controles como punto de partida.'],
  ['Paso 2', 'Fase 2 (evaluación): calibrar a los expertos en la hoja Brier, registrar las rondas en Delphi y trasladar a Matriz la probabilidad anual y el impacto sobre el titular con su rationale. Indicar el número de agravantes (hoja Escalas). El impacto ajustado y el nivel inherente se calculan solos.'],
  ['Paso 3', 'Fase 3 (mitigación): elegir el tratamiento, proponer controles (ref. ISO/IEC 27002:2022), responsable y plazo, y estimar la probabilidad y el impacto residuales. El nivel residual, la necesidad de EIPD y el criterio de aceptación se calculan solos.'],
  ['Paso 4', 'Fase 4 (monitoreo): definir el indicador, actualizar el estado y revisar la matriz periódicamente o ante incidentes. La hoja Mapa de calor resume los resultados.'],
  ['Reglas de la guía SPDP', 'Toda estimación lleva su rationale; la probabilidad se refiere a un año; C, I, D y licitud se modelan por separado; el nivel se asigna por tabla (hoja Decisión), no multiplicando etiquetas; un impacto muy alto sobre el titular nunca queda por debajo de nivel alto.'],
  ['Confidencialidad', 'No registrar datos personales reales. Describir procesos, sistemas y categorías de datos; usar códigos para personas (E01, E02…).'],
  DATA
    ? ['Caso UTI', 'Este archivo contiene los escenarios candidatos del proceso de admisión y matrícula de la UTI (Capítulo 3). Las vulnerabilidades marcadas "A verificar" se confirman o descartan en el diagnóstico; la probabilidad y el impacto se registran tras el panel Delphi (hojas Delphi y Brier).']
    : ['Ejemplo', 'La fila 5 de Matriz, la fila 5 de Delphi y la columna E01 de Brier contienen valores ficticios de ejemplo. Borrarlos antes de usar la plantilla.'],
];
INSTR.forEach(([k, v], i) => {
  const r = 4 + i;
  I.getCell(r, 1).value = k; I.getCell(r, 1).font = { name: FONT, bold: true }; I.getCell(r, 1).alignment = { vertical: 'top' };
  I.getCell(r, 2).value = v; I.getCell(r, 2).alignment = { wrapText: true, vertical: 'top' };
  I.getRow(r).height = 48;
});
I.getCell('B5').fill = INPUT_FILL;
I.getColumn(1).width = 22; I.getColumn(2).width = 110;
wb.views = [{ activeTab: 0 }];

[I, M, D, E, A, C, P, B, H, L].forEach(styleAll);

// ---------------------------------------------------------------- Verificación con HyperFormula
function toSheetArray(ws) {
  const out = [];
  ws.eachRow({ includeEmpty: true }, (row, r) => {
    out[r - 1] = [];
    row.eachCell({ includeEmpty: true }, (c, k) => {
      let v = c.value;
      if (v && typeof v === 'object' && v.formula) v = '=' + v.formula;
      else if (v && typeof v === 'object' && v.richText) v = v.richText.map(t => t.text).join('');
      out[r - 1][k - 1] = v === undefined ? null : v;
    });
  });
  for (let i = 0; i < out.length; i++) if (!out[i]) out[i] = [];
  return out;
}
const sheets = {};
wb.worksheets.forEach(ws => { sheets[ws.name] = toSheetArray(ws); });
const hf = HyperFormula.buildFromSheets(sheets, { licenseKey: 'gpl-v3' });
let nFormulas = 0, nErrors = 0;
const errors = [];
wb.worksheets.forEach(ws => {
  const sid = hf.getSheetId(ws.name);
  ws.eachRow({ includeEmpty: true }, (row, r) => row.eachCell({ includeEmpty: true }, (c, k) => {
    if (c.value && typeof c.value === 'object' && c.value.formula) {
      nFormulas++;
      let res = hf.getCellValue({ sheet: sid, row: r - 1, col: k - 1 });
      if (res && typeof res === 'object' && res.type) { nErrors++; errors.push(`${ws.name}!${c.address}: ${res.type} ${res.message || ''}`); res = undefined; }
      c.value = { formula: c.value.formula, result: res === null ? '' : res };
    }
  }));
});
// HyperFormula no implementa QUARTILE (sí Excel y LibreOffice): se verifica en JS con el método inclusivo de Excel.
const quartileInc = (arr, k) => { const s = [...arr].sort((a, b) => a - b); const h = (s.length - 1) * k / 4; const lo = Math.floor(h); return s[lo] + (h - lo) * ((s[lo + 1] ?? s[lo]) - s[lo]); };
const realErrors = errors.filter(e => !/QUARTILE/.test(e));
const quartErrors = errors.length - realErrors.length;
for (let r = 5; r < 5 + N_DEL; r++) {
  const vals = [4, 5, 6, 7, 8].map(k => P.getCell(r, k).value).filter(v => typeof v === 'number');
  const q1 = vals.length ? quartileInc(vals, 1) : '', q3 = vals.length ? quartileInc(vals, 3) : '';
  const ric = vals.length ? q3 - q1 : '';
  const set = (k, v) => { P.getCell(r, k).value = { formula: P.getCell(r, k).value.formula, result: v }; };
  set(10, q1); set(11, q3); set(12, ric); set(13, ric === '' ? '' : (ric <= 1 ? 'Sí' : 'No'));
}
console.log(JSON.stringify({ total_formulas: nFormulas, total_errors: realErrors.length, quartile_cells_checked_in_js: quartErrors, errors: realErrors.slice(0, 20) }, null, 1));
const show = (s, a) => { const ws = wb.getWorksheet(s); return `${s}!${a} = ${JSON.stringify(ws.getCell(a).value.result)}`; };
if (DATA) {
  // Resumen de resultados calculados (TSV) para trasladarlos al documento.
  const v = (a) => { const x = M.getCell(a).value; return x && typeof x === 'object' && 'formula' in x ? (x.result ?? '') : (x ?? ''); };
  console.log(['ID', 'Dim', 'P', 'I', 'Ag', 'IA', 'NI', 'Trat', 'PR', 'IR', 'NR', 'EIPD', 'Aceptación'].join('\t'));
  DATA.forEach((_, i) => {
    const r = FIRST + i;
    console.log([`A${r}`, `${col('Dimensión (C/I/D/Licitud)')}${r}`, `${cP}${r}`, `${cI}${r}`, `${cAg}${r}`, `${cIA}${r}`, `${cNI}${r}`,
      `${col('Tratamiento')}${r}`, `${cPR}${r}`, `${cIR}${r}`, `${cNR}${r}`, `${cEIPD}${r}`, `${cAc}${r}`].map(v).join('\t'));
  });
  const Hs = wb.getWorksheet('Mapa de calor');
  console.log('Resumen por nivel (inherente/residual): ' + IMP.map((lv, i) => `${lv}: ${Hs.getCell(22 + i, 2).value.result ?? 0}/${Hs.getCell(22 + i, 3).value.result ?? 0}`).join('; '));
} else console.log([
  show('Matriz', `${cIA}5`), show('Matriz', `${cNI}5`), show('Matriz', `${cNR}5`), show('Matriz', `${cEIPD}5`), show('Matriz', `${cAc}5`),
  show('Matriz', `${cNI}6`), show('Mapa de calor', 'E8'), show('Mapa de calor', 'D16'), show('Mapa de calor', 'B27'),
  show('Brier', 'C16'), show('Brier', 'C17'), show('Brier', 'C18'), show('Brier', 'D16'),
  show('Delphi', 'I5'), show('Delphi', 'J5'), show('Delphi', 'K5'), show('Delphi', 'L5'), show('Delphi', 'M5'), show('Delphi', 'N5'), show('Delphi', 'O5'),
].join('\n'));

wb.xlsx.writeFile(OUT).then(() => console.log('Escrito: ' + OUT));
