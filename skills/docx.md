# docx

Create and edit Microsoft Word (.docx) documents with formatting, tables, and styles.

## What this skill does
Generates, reads, and modifies Word documents programmatically using python-docx.

## Setup
```bash
pip install python-docx
```

## Core Patterns

### Create document
```python
from docx import Document
from docx.shared import Pt, RGBColor
doc = Document()
doc.add_heading("Sovereign Kernel Report", 0)
doc.add_paragraph("PLT analysis complete.")
table = doc.add_table(rows=2, cols=3)
table.cell(0,0).text = "Profit"; table.cell(0,1).text = "Love"; table.cell(0,2).text = "Tax"
table.cell(1,0).text = "0.85"; table.cell(1,1).text = "0.72"; table.cell(1,2).text = "0.43"
doc.save("report.docx")
```

### Read document
```python
doc = Document("report.docx")
for para in doc.paragraphs:
    print(para.text)
```

### Apply styles
```python
from docx.shared import Pt
p = doc.add_paragraph("Bold declaration")
run = p.runs[0]
run.bold = True
run.font.size = Pt(14)
run.font.color.rgb = RGBColor(0xFF, 0xD7, 0x00)  # PLT Gold
```

### Add image
```python
doc.add_picture("chart.png", width=docx.shared.Inches(4))
```

## Example commands
```
ACTION: Create a docx report from today's council records and save to reports/council.docx
ACTION: Read report.docx and summarize each paragraph
```
