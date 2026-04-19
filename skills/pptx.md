# pptx

Create and edit PowerPoint (.pptx) presentations with slides, charts, and layouts.

## What this skill does
Generates presentation decks programmatically — slides, bullet points, charts, images, speaker notes — using python-pptx.

## Setup
```bash
pip install python-pptx
```

## Core Patterns

### Create presentation
```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

prs = Presentation()
slide_layout = prs.slide_layouts[1]  # Title and Content
slide = prs.slides.add_slide(slide_layout)
slide.shapes.title.text = "Sovereign Kernel: PLT Report"
tf = slide.placeholders[1].text_frame
tf.text = "Cycle 1000 completed"
tf.add_paragraph().text = "Autonomy level: 0.72"
tf.add_paragraph().text = "Mythos phase: Trials"
prs.save("kernel_report.pptx")
```

### Add chart slide
```python
from pptx.util import Inches
from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE

chart_data = ChartData()
chart_data.categories = ["Profit", "Love", "Tax"]
chart_data.add_series("PLT", (0.85, 0.72, 0.43))
slide = prs.slides.add_slide(prs.slide_layouts[5])
slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED,
    Inches(1), Inches(1), Inches(8), Inches(5), chart_data)
```

### Read existing deck
```python
prs = Presentation("existing.pptx")
for slide in prs.slides:
    for shape in slide.shapes:
        if shape.has_text_frame:
            print(shape.text_frame.text)
```

## Example commands
```
ACTION: Create a 5-slide PPTX deck summarizing this week's council records
ACTION: Add a PLT bar chart slide to kernel_report.pptx
```
