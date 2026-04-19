# xlsx

Create and edit Excel (.xlsx) spreadsheets with formulas, pivot tables, and charts.

## What this skill does
Generates and manipulates Excel workbooks — data entry, formulas, formatting, charts, and reading existing files — using openpyxl.

## Setup
```bash
pip install openpyxl
```

## Core Patterns

### Create workbook
```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Color
wb = Workbook()
ws = wb.active
ws.title = "PLT Ledger"
ws.append(["Cycle", "Profit", "Love", "Tax", "PLT Score"])
ws.append([1000, 0.85, 0.72, 0.43, 1.14])
ws["A1"].font = Font(bold=True, color="FFD700")
wb.save("plt_ledger.xlsx")
```

### Read workbook
```python
from openpyxl import load_workbook
wb = load_workbook("plt_ledger.xlsx")
ws = wb.active
for row in ws.iter_rows(values_only=True):
    print(row)
```

### Add formula
```python
ws["E2"] = "=B2+C2-D2"  # PLT score formula
```

### Add chart
```python
from openpyxl.chart import BarChart, Reference
chart = BarChart()
data = Reference(ws, min_col=2, max_col=4, min_row=1, max_row=ws.max_row)
chart.add_data(data, titles_from_data=True)
chart.title = "PLT Distribution"
ws.add_chart(chart, "G1")
wb.save("plt_ledger.xlsx")
```

## Example commands
```
ACTION: Create an xlsx ledger of the last 10 council deliberations with PLT scores
ACTION: Read plt_ledger.xlsx and summarize the trend in PLT scores
```
