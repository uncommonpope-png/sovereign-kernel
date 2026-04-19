# nano-pdf Skill

Lightweight PDF operations: view, extract text, merge, split, and convert PDFs.

## Use When
- Extracting text from PDF files
- Merging or splitting PDF documents
- Converting PDF to other formats

## Text Extraction
```bash
# pdftotext (poppler)
pdftotext input.pdf output.txt
pdftotext -layout input.pdf -         # preserve layout, output to stdout
pdftotext -f 3 -l 7 input.pdf -      # pages 3-7 only

# python pdfplumber
python3 -c "
import pdfplumber
with pdfplumber.open('input.pdf') as pdf:
    for page in pdf.pages:
        print(page.extract_text())
"
```

## Merge PDFs
```bash
# Using pdfunite (poppler)
pdfunite file1.pdf file2.pdf file3.pdf merged.pdf

# Using PyPDF2
python3 -c "
from PyPDF2 import PdfMerger
m = PdfMerger()
for f in ['a.pdf','b.pdf']: m.append(f)
m.write('merged.pdf')
"
```

## Split PDF (extract pages)
```bash
# Extract pages 2-5
pdftk input.pdf cat 2-5 output pages_2_to_5.pdf

# Python
python3 -c "
from PyPDF2 import PdfReader, PdfWriter
r = PdfReader('input.pdf')
w = PdfWriter()
for i in range(1, 4): w.add_page(r.pages[i])
open('out.pdf','wb').write(w.write())
"
```

## Install
```bash
brew install poppler         # pdftotext, pdfunite
brew install pdftk-java      # pdftk
pip install pdfplumber PyPDF2
```
