// Convierte Capítulos/01_Introducción.tex en el borrador tesis/cap1.md.
// Usa main.aux (numeración de citas, tablas y secciones) y main.bbl (referencias IEEE),
// por lo que debe ejecutarse después de compilar main.tex.
// Uso: node scripts/tex2md_cap1.js
const fs = require("fs");

const tex = fs.readFileSync("Capítulos/01_Introducción.tex", "utf8");
const aux = fs.readFileSync("main.aux", "utf8");
const bbl = fs.readFileSync("main.bbl", "utf8");

// --- Numeración de citas y etiquetas -------------------------------------
const citeNum = {};
for (const m of aux.matchAll(/\\bibcite\{([^}]+)\}\{(\d+)\}/g)) citeNum[m[1]] = +m[2];
const labelNum = {};
for (const m of aux.matchAll(/\\newlabel\{([^}]+)\}\{\{([^}]*)\}/g)) labelNum[m[1]] = m[2];

// --- Utilidades de análisis ----------------------------------------------
function argAt(s, i) { // s[i] === "{": devuelve [contenido, índice tras "}"]
  let d = 0;
  for (let j = i; j < s.length; j++) {
    if (s[j] === "{" && s[j - 1] !== "\\") d++;
    else if (s[j] === "}" && s[j - 1] !== "\\") { d--; if (d === 0) return [s.slice(i + 1, j), j + 1]; }
  }
  throw new Error("Llave sin cerrar cerca de: " + s.slice(i, i + 60));
}
function replaceCmd(s, name, nargs, fn) {
  let out = "", i = 0; const key = "\\" + name;
  while (true) {
    const k = s.indexOf(key, i);
    if (k < 0) { out += s.slice(i); return out; }
    const next = s[k + key.length];
    if (next && /[A-Za-z]/.test(next)) { out += s.slice(i, k + key.length); i = k + key.length; continue; }
    out += s.slice(i, k);
    let j = k + key.length, opt = null;
    while (s[j] === " ") j++;
    if (s[j] === "[") { const e = s.indexOf("]", j); opt = s.slice(j + 1, e); j = e + 1; }
    const args = [];
    for (let a = 0; a < nargs; a++) { while (s[j] === " ") j++; const [c, e] = argAt(s, j); args.push(c); j = e; }
    out += fn(args, opt); i = j;
  }
}

// --- Conversión de texto en línea ----------------------------------------
function inline(s) {
  s = replaceCmd(s, "cite", 1, ([keys], opt) => {
    const ns = keys.split(",").map(k => { const n = citeNum[k.trim()]; if (!n) throw new Error("Cita sin número: " + k); return n; });
    return opt ? `[${ns.join(", ")}, ${inline(opt)}]` : ns.map(n => `[${n}]`).join(", ");
  });
  s = replaceCmd(s, "ref", 1, ([k]) => labelNum[k] ?? "??");
  s = replaceCmd(s, "label", 1, () => "");
  s = replaceCmd(s, "shortstack", 1, ([t]) => t.replace(/\\\\/g, " "));
  s = replaceCmd(s, "parbox", 2, ([, t]) => t);
  s = replaceCmd(s, "multirow", 3, ([, , t]) => t);
  s = replaceCmd(s, "multicolumn", 3, ([, , t]) => t);
  s = replaceCmd(s, "rule", 2, () => "");
  s = replaceCmd(s, "vspace", 1, () => "");
  s = replaceCmd(s, "mbox", 1, ([t]) => t);
  s = replaceCmd(s, "textit", 1, ([t]) => `*${inline(t).trim()}*`);
  s = replaceCmd(s, "emph", 1, ([t]) => `*${inline(t).trim()}*`);
  s = replaceCmd(s, "textbf", 1, ([t]) => `**${inline(t).trim()}**`);
  s = replaceCmd(s, "texttt", 1, ([t]) => "`" + t.replace(/\\_/g, "_") + "`");
  s = replaceCmd(s, "path", 1, ([t]) => "`" + t + "`");
  s = replaceCmd(s, "url", 1, ([t]) => t);
  s = s.replace(/\\(centering|raggedright|footnotesize|scriptsize|small|normalsize|hline|noindent|par)\b/g, "");
  s = replaceCmd(s, "cline", 1, () => "");
  s = s.replace(/---/g, "—").replace(/--/g, "–").replace(/``/g, "“").replace(/''/g, "”")
       .replace(/\\,/g, "\u202F").replace(/~/g, "\u00A0").replace(/\\%/g, "%").replace(/\\&/g, "&")
       .replace(/\\ldots/g, "…").replace(/\\_/g, "_").replace(/\\ /g, " ").replace(/\$([^$]*)\$/g, "$1");
  return s;
}

// --- Tablas --------------------------------------------------------------
function table(block) {
  const cap = (block.match(/\\caption\{/) ? argAt(block, block.indexOf("\\caption{") + 8)[0] : "");
  const lab = (block.match(/\\label\{([^}]+)\}/) || [])[1];
  const num = labelNum[lab] ?? "";
  const ini = block.search(/\\begin\{tabularx?\}/);
  const fin = block.search(/\\end\{tabularx?\}/);
  let body = block.slice(ini, fin);
  body = body.replace(/^\\begin\{tabularx\}\{[^}]*\}/, "").replace(/^\\begin\{tabular\}/, "");
  const [, afterSpec] = argAt(body, body.indexOf("{")); // especificación de columnas
  body = body.slice(afterSpec);
  // Separar filas por "\\" solo fuera de llaves (p. ej., \shortstack{a\\b} no corta la fila)
  const rawRows = []; { let d = 0, cur = "";
    for (let i = 0; i < body.length; i++) {
      const ch = body[i];
      if (ch === "{" && body[i - 1] !== "\\") d++; else if (ch === "}" && body[i - 1] !== "\\") d--;
      if (d === 0 && ch === "\\" && body[i + 1] === "\\") {
        rawRows.push(cur); cur = ""; i++;
        if (body[i + 1] === "[") i = body.indexOf("]", i);
      } else cur += ch;
    }
    rawRows.push(cur); }
  const rows = rawRows.map(r => r.replace(/\\hline|\\cline\{[^}]*\}/g, "").trim()).filter(r => r.length);
  const cells = rows.map(r => {
    const parts = []; let d = 0, cur = "";
    for (let i = 0; i < r.length; i++) {
      const ch = r[i];
      if (ch === "{" && r[i - 1] !== "\\") d++; else if (ch === "}" && r[i - 1] !== "\\") d--;
      if (ch === "&" && r[i - 1] !== "\\" && d === 0) { parts.push(cur); cur = ""; } else cur += ch;
    }
    parts.push(cur);
    return parts.map(c => inline(c).replace(/\s+/g, " ").replace(/\|/g, "\\|").trim());
  });
  const ncol = Math.max(...cells.map(c => c.length));
  const fill = c => { while (c.length < ncol) c.push(""); return c; };
  const lines = [`**Tabla ${num}**`, `*${inline(cap).trim()}*`, ""];
  lines.push("| " + fill(cells[0]).join(" | ") + " |");
  lines.push("|" + " --- |".repeat(ncol));
  for (const c of cells.slice(1)) lines.push("| " + fill(c).join(" | ") + " |");
  const fuente = block.match(/\\fuente\{/) ? argAt(block, block.indexOf("\\fuente{") + 7)[0] : null;
  lines.push("");
  lines.push(`*Elaborado por:* Ramón Alejandro Manzaba Castro. *Fuente:* ${fuente ? inline(fuente).trim() : "elaboración propia"}.`);
  return lines.join("\n");
}

// --- Documento -----------------------------------------------------------
let s = tex.split(/\r?\n/).filter(l => !/^\s*%/.test(l) && !/^\\newcolumntype/.test(l)).join("\n");
s = s.replace(/\\begin\{landscape\}|\\end\{landscape\}/g, "");

const out = [];
const chunks = s.split(/(\\begin\{table\}[\s\S]*?\\end\{table\}|\\begin\{figure\}[\s\S]*?\\end\{figure\})/);
for (const ch of chunks) {
  if (ch.startsWith("\\begin{table}")) { out.push(table(ch)); continue; }
  if (ch.startsWith("\\begin{figure}")) {
    const lab = (ch.match(/\\label\{([^}]+)\}/) || [])[1];
    const cap = argAt(ch, ch.indexOf("\\caption{") + 8)[0];
    out.push(`**Figura ${labelNum[lab] ?? ""}**\n*${inline(cap).trim()}*\n\n> Diagrama elaborado en TikZ; véase el PDF. Su contenido coincide con la tabla del árbol de problemas.`);
    continue;
  }
  let t = ch;
  t = replaceCmd(t, "chapter", 1, ([x]) => `# CAPÍTULO I. ${inline(x).toUpperCase()}`);
  // Encabezados numerados según main.aux
  let sec = 0, sub = 0;
  t = t.replace(/\\(section|subsection)\{([^}]*)\}(\s*\\label\{([^}]+)\})?/g, (m, kind, title, _l, lab) => {
    const n = lab && labelNum[lab] ? labelNum[lab] : null;
    return (kind === "section" ? "## " : "### ") + (n ? n + " " : "") + inline(title);
  });
  // Listas
  t = t.replace(/\\begin\{enumerate\}([\s\S]*?)\\end\{enumerate\}/g, (m, body) => {
    let k = 0; return body.split(/\\item\s+/).slice(1).map(it => `${++k}. ${it.trim()}`).join("\n\n");
  });
  t = t.replace(/\\begin\{itemize\}([\s\S]*?)\\end\{itemize\}/g, (m, body) =>
    body.split(/\\item\s+/).slice(1).map(it => `- ${it.trim()}`).join("\n"));
  out.push(inline(t));
}
let md = out.join("\n\n").replace(/\n{3,}/g, "\n\n").trim();

// Numerar secciones sin etiqueta a partir del orden de aparición
{ let sec = 0, sub = 0;
  md = md.split("\n").map(l => {
    if (/^## (?!\d)/.test(l)) { sec++; sub = 0; return l.replace(/^## /, `## 1.${sec} `); }
    if (/^## \d/.test(l)) { sec = +l.match(/^## 1\.(\d+)/)[1]; sub = 0; return l; }
    if (/^### (?!\d)/.test(l)) { sub++; return l.replace(/^### /, `### 1.${sec}.${sub} `); }
    if (/^### \d/.test(l)) { sub = +l.match(/^### 1\.\d+\.(\d+)/)[1]; return l; }
    return l;
  }).join("\n"); }

// --- Referencias del capítulo (formato IEEE, desde main.bbl) -------------
const usados = [...new Set([...tex.matchAll(/\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g)].flatMap(m => m[1].split(",").map(k => k.trim())))]
  .sort((a, b) => citeNum[a] - citeNum[b]);
const items = {};
for (const m of bbl.matchAll(/\\bibitem\{([^}]+)\}([\s\S]*?)(?=\\bibitem\{|\\end\{thebibliography\})/g)) items[m[1]] = m[2];
function bibText(t) {
  t = t.replace(/\\BIBentryALTinterwordspacing|\\BIBentrySTDinterwordspacing|\\newblock|\\BIBforeignlanguage\{[^}]*\}/g, " ");
  t = replaceCmd(t, "emph", 1, ([x]) => `*${x}*`);
  t = replaceCmd(t, "url", 1, ([x]) => x);
  t = replaceCmd(t, "path", 1, ([x]) => x);
  t = t.replace(/\\'\{?([aeiouAEIOU])\}?/g, (m, v) => ({a:"á",e:"é",i:"í",o:"ó",u:"ú",A:"Á",E:"É",I:"Í",O:"Ó",U:"Ú"})[v])
       .replace(/\\'\{\\i\}/g, "í").replace(/\\~\{?n\}?/g, "ñ").replace(/\\~\{?a\}?/g, "ã").replace(/\\c\{c\}/g, "ç")
       .replace(/\\\^\{?e\}?/g, "ê").replace(/\\textordmasculine/g, "º").replace(/\\&/g, "&").replace(/\\%/g, "%")
       .replace(/``/g, "“").replace(/''/g, "”").replace(/--/g, "–").replace(/~/g, " ").replace(/\\,/g, " ")
       .replace(/[{}]/g, "").replace(/\\[A-Za-z]+/g, "").replace(/\s+/g, " ").trim();
  return t;
}
md += "\n\n## Referencias del capítulo\n\nNumeración IEEE idéntica a la del PDF (`main.pdf`).\n\n" +
  usados.map(k => `[${citeNum[k]}] ${bibText(items[k] || k)}`).join("\n\n");

md = `<!-- Generado automáticamente desde Capítulos/01_Introducción.tex con scripts/tex2md_cap1.js.
     El .tex es la fuente vigente; para actualizar este borrador, compilar main.tex y volver a ejecutar el script. -->\n\n` + md + "\n";
fs.writeFileSync("tesis/cap1.md", md);
const palabras = md.replace(/<!--[\s\S]*?-->/, "").split(/\s+/).filter(Boolean).length;
console.log("tesis/cap1.md:", md.split("\n").length, "líneas,", palabras, "palabras,", usados.length, "referencias");
