# Genera planificacion/Planificacion_Gantt.xlsx a partir de planificacion/Planificacion_Jira.csv
# (hoja Tareas + hoja Gantt semanal con fórmulas y formato condicional). Requiere Microsoft Excel.
# Uso: powershell -ExecutionPolicy Bypass -File scripts/gantt_excel.ps1
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$csv  = Join-Path $root "planificacion\Planificacion_Jira.csv"
$xlsx = Join-Path $root "planificacion\Planificacion_Gantt.xlsx"

$filas = Import-Csv -Path $csv -Encoding UTF8
# Fecha como fórmula =DATE(a,m,d): evita conversiones de tipo y de configuración regional por COM
function FechaExcel([string]$iso) { $d = [datetime]::ParseExact($iso, "yyyy-MM-dd", $null); "=DATE($($d.Year),$($d.Month),$($d.Day))" }
$inicioProyecto = [datetime]"2026-10-13"
$semanas = 20

$xl = New-Object -ComObject Excel.Application
$xl.Visible = $false
$xl.DisplayAlerts = $false
try {
$wb = $xl.Workbooks.Add()
while ($wb.Worksheets.Count -gt 1) { $wb.Worksheets.Item($wb.Worksheets.Count).Delete() }

# ---------------- Hoja Tareas ----------------
$t = $wb.Worksheets.Item(1); $t.Name = "Tareas"
$enc = "ID","ID principal","Tipo","Resumen","Inicio","Fin","Duración (días)","Prioridad","Estado","Etiquetas","Descripción"
for ($c = 0; $c -lt $enc.Count; $c++) { $t.Cells.Item(1, $c + 1).Value2 = $enc[$c] }
$r = 2
foreach ($f in $filas) {
  $t.Cells.Item($r, 1).Value2 = [int]$f.'ID'
  if ($f.'ID principal') { $t.Cells.Item($r, 2).Value2 = [int]$f.'ID principal' }
  $t.Cells.Item($r, 3).Value2 = $f.'Tipo de incidencia'
  $t.Cells.Item($r, 4).Value2 = $f.'Resumen'
  $t.Cells.Item($r, 5).Formula = (FechaExcel $f.'Fecha de inicio')
  $t.Cells.Item($r, 6).Formula = (FechaExcel $f.'Fecha de vencimiento')
  $t.Cells.Item($r, 7).Formula = "=F$r-E$r+1"
  $t.Cells.Item($r, 8).Value2 = $f.'Prioridad'
  $t.Cells.Item($r, 9).Value2 = $f.'Estado'
  $t.Cells.Item($r, 10).Value2 = $f.'Etiquetas'
  $t.Cells.Item($r, 11).Value2 = $f.'Descripción'
  $r++
}
$ultima = $r - 1
$t.Range("E2:F$ultima").NumberFormat = "dd/mm/yyyy"
$t.Range("A1:K1").Font.Bold = $true
$t.Range("A1:K1").Interior.Color = 0x5C3A1F   # azul oscuro (BGR)
$t.Range("A1:K1").Font.Color = 0xFFFFFF
$t.Columns("A:J").AutoFit() | Out-Null
$t.Columns("D").ColumnWidth = 60; $t.Columns("K").ColumnWidth = 70
$t.Range("D:D,K:K").WrapText = $true
$t.Range("A1:K$ultima").Borders.LineStyle = 1
# Épicas en negrita
for ($i = 2; $i -le $ultima; $i++) { if ($t.Cells.Item($i, 3).Value2 -eq "Épica") { $t.Range("A$($i):K$($i)").Font.Bold = $true; $t.Range("A$($i):K$($i)").Interior.Color = 0xF2E6DA } }
$t.Activate(); $xl.ActiveWindow.SplitRow = 1; $xl.ActiveWindow.FreezePanes = $true
$lo = $t.ListObjects  # sin tabla formal para no alterar las fórmulas de la hoja Gantt

# ---------------- Hoja Gantt ----------------
$g = $wb.Worksheets.Add([Type]::Missing, $t); $g.Name = "Gantt"
$g.Cells.Item(1, 1).Value2 = "Planificación del proyecto ITI-TFG-B26-0021 — 13 de octubre de 2026 a 26 de febrero de 2027"
$g.Cells.Item(1, 1).Font.Bold = $true; $g.Cells.Item(1, 1).Font.Size = 14
$g.Cells.Item(2, 1).Value2 = "Leyenda: azul oscuro = épica · azul = tarea · verde = tarea lista · naranja = hito · «Hoy» en rojo = semana actual. Las barras se calculan con las fechas de la hoja Tareas."
$g.Cells.Item(2, 1).Font.Italic = $true

$cab = "ID","Actividad","Inicio","Fin","Estado"
for ($c = 0; $c -lt $cab.Count; $c++) { $g.Cells.Item(4, $c + 1).Value2 = $cab[$c] }
$col0 = 6   # primera columna de semanas (F)
for ($k = 0; $k -lt $semanas; $k++) {
  $fecha = $inicioProyecto.AddDays(7 * $k)
  # Encabezado de semana; muestra "Hoy" en la semana actual
  $g.Cells.Item(3, $col0 + $k).Formula = "=IF(AND(TODAY()>=R4C,TODAY()<R4C+7),""Hoy"",""S$($k + 1)"")" -replace "R4C", ($g.Cells.Item(4, $col0 + $k).Address($true, $false))
  $g.Cells.Item(4, $col0 + $k).Formula = (FechaExcel $fecha.ToString("yyyy-MM-dd"))
}
$colFin = $col0 + $semanas - 1
$letraFin = ($g.Cells.Item(4, $colFin).Address($false, $false)) -replace '\d', ''
$g.Range("F4:$($letraFin)4").NumberFormat = "dd-mmm"
$g.Range("F3:$($letraFin)4").HorizontalAlignment = -4108
$g.Range("F4:$($letraFin)4").Orientation = 90

for ($i = 2; $i -le $ultima; $i++) {
  $fila = $i + 3   # fila 5 en adelante
  $g.Cells.Item($fila, 1).Formula = "=Tareas!A$i"
  $g.Cells.Item($fila, 2).Formula = "=IF(Tareas!C$i=""Épica"",Tareas!D$i,""    ""&Tareas!D$i)"
  $g.Cells.Item($fila, 3).Formula = "=Tareas!E$i"
  $g.Cells.Item($fila, 4).Formula = "=Tareas!F$i"
  $g.Cells.Item($fila, 5).Formula = "=Tareas!I$i"
  # Clase de la actividad: H = hito, E = épica, L = lista, T = tarea (columna auxiliar oculta)
  $g.Cells.Item($fila, $colFin + 1).Formula = "=IF(ISNUMBER(SEARCH(""hito"",Tareas!J$i)),""H"",IF(Tareas!C$i=""Épica"",""E"",IF(Tareas!I$i=""Listo"",""L"",""T"")))"
  $aux = $g.Cells.Item($fila, $colFin + 1).Address($false, $true)
  $g.Range($g.Cells.Item($fila, $col0), $g.Cells.Item($fila, $colFin)).Formula = "=IF(AND(`$C$fila<=F`$4+6,`$D$fila>=F`$4),$aux,"""")"
}
$filaFin = $ultima + 3
$g.Range("C5:D$filaFin").NumberFormat = "dd/mm/yyyy"
$barras = $g.Range("F5:$($letraFin)$filaFin")
$barras.NumberFormat = ";;;"           # oculta el 1; solo se ve el color
$barras.ColumnWidth = 3.2

# Formato condicional por valor de celda (sin funciones, independiente del idioma de Excel)
$fc = $barras.FormatConditions
$c1 = $fc.Add(1, 3, "=""T"""); $c1.Interior.Color = 0xD69B5B   # tarea: azul
$c2 = $fc.Add(1, 3, "=""L"""); $c2.Interior.Color = 0x50B000   # lista: verde
$c3 = $fc.Add(1, 3, "=""E"""); $c3.Interior.Color = 0x5C3A1F   # épica: azul oscuro
$c4 = $fc.Add(1, 3, "=""H"""); $c4.Interior.Color = 0x2E8CF4   # hito: naranja
$hoy = $g.Range("F3:$($letraFin)3").FormatConditions.Add(1, 3, "=""Hoy""")
$hoy.Interior.Color = 0x0000FF; $hoy.Font.Color = 0xFFFFFF; $hoy.Font.Bold = $true
$g.Columns($colFin + 1).Hidden = $true

# Formato general
$g.Range("A4:$($letraFin)4").Font.Bold = $true
$g.Range("A3:$($letraFin)4").Interior.Color = 0xF2E6DA
$g.Range("A4:$($letraFin)$filaFin").Borders.LineStyle = 1
$g.Range("A4:$($letraFin)$filaFin").Borders.Color = 0xD9D9D9
$g.Columns("A").ColumnWidth = 5; $g.Columns("B").ColumnWidth = 62
$g.Columns("C:D").ColumnWidth = 11; $g.Columns("E").ColumnWidth = 10
for ($i = 5; $i -le $filaFin; $i++) { if ($t.Cells.Item($i - 3, 3).Value2 -eq "Épica") { $g.Range("A$($i):E$($i)").Font.Bold = $true } }
$g.Activate(); $xl.ActiveWindow.SplitRow = 4; $xl.ActiveWindow.SplitColumn = 5; $xl.ActiveWindow.FreezePanes = $true
$xl.ActiveWindow.DisplayGridlines = $false

# Configuración de impresión: horizontal, una página de ancho
$g.PageSetup.Orientation = 2
$g.PageSetup.Zoom = $false
$g.PageSetup.FitToPagesWide = 1
$g.PageSetup.FitToPagesTall = $false

if (Test-Path $xlsx) { Remove-Item $xlsx }
$wb.SaveAs($xlsx, 51)   # 51 = xlOpenXMLWorkbook (.xlsx)
$wb.Close($false)
} finally {
  $xl.Quit()
  [void][Runtime.InteropServices.Marshal]::ReleaseComObject($xl)
}
"Guardado: $xlsx ($($ultima - 1) actividades, $semanas semanas)"
