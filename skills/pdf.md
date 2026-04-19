# pdf

Read, extract, and create PDF documents including forms, tables, and structured content.

## What this skill does
Handles PDF reading (text extraction, table parsing), creation (report generation), and manipulation (merge, split, annotate).

## Setup
```bash
pip install pypdf pdfplumber reportlab
```

## Read / Extract

### Extract all text
```python
import pdfplumber
with pdfplumber.open("doc.pdf") as pdf:
    for page in pdf.pages:
        print(page.extract_text())
```

### Extract tables
```python
with pdfplumber.open("report.pdf") as pdf:
    for page in pdf.pages:
        for table in page.extract_tables():
            for row in table:
                print(row)
```

## Create PDF

### Simple report with reportlab
```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
c = canvas.Canvas("output.pdf", pagesize=A4)
c.setFont("Helvetica-Bold", 16)
c.drawString(72, 750, "Sovereign Kernel Report")
c.setFont("Helvetica", 12)
c.drawString(72, 720, f"PLT Score: 0.85")
c.save()
```

## Merge / Split
```python
from pypdf import PdfWriter, PdfReader
writer = PdfWriter()
for fname in ["a.pdf", "b.pdf"]:
    reader = PdfReader(fname)
    for page in reader.pages:
        writer.add_page(page)
with open("merged.pdf", "wb") as f:
    writer.write(f)
```

## Example commands
```
ACTION: Extract text from report.pdf and store key points in memory
ACTION: Create a PDF report from today's council deliberation records
```
