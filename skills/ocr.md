# OCR & Screenshot Skill

Extract text from images and screenshots. Read what's on screen or in image files.

## Use When
- Extracting text from screenshots
- Reading text from PDF images
- Processing scanned documents
- Understanding UI state from screen captures

## Tesseract OCR
```bash
# Install: brew install tesseract (macOS) or apt install tesseract-ocr (Linux)

# Basic OCR
tesseract image.png output
cat output.txt

# With language
tesseract image.png output -l eng

# Direct stdout
tesseract image.png stdout

# PDF to text
tesseract document.pdf output pdf
# creates output.pdf with text layer

# Multiple languages
tesseract image.png output -l eng+fra
```

## Python OCR (pytesseract)
```python
# pip install pytesseract Pillow
from PIL import Image
import pytesseract

# Basic extraction
text = pytesseract.image_to_string(Image.open('screenshot.png'))
print(text)

# Get bounding boxes
data = pytesseract.image_to_data(Image.open('screenshot.png'), output_type=pytesseract.Output.DICT)
for i, word in enumerate(data['text']):
    if word.strip():
        print(f"{word} @ ({data['left'][i]}, {data['top'][i]})")

# With preprocessing for better accuracy
from PIL import ImageEnhance, ImageFilter
img = Image.open('screenshot.png')
img = img.convert('L')  # grayscale
img = img.filter(ImageFilter.SHARPEN)
img = ImageEnhance.Contrast(img).enhance(2.0)
text = pytesseract.image_to_string(img)
```

## macOS Native OCR (Vision framework via CLI)
```bash
# Use screencapture + Vision
swift -e "
import Vision, AppKit
let url = URL(fileURLWithPath: CommandLine.arguments[1])
let request = VNRecognizeTextRequest { req, _ in
    let results = req.results as! [VNRecognizedTextObservation]
    results.forEach { print(\$0.topCandidates(1).first?.string ?? \"\") }
}
request.recognitionLevel = .accurate
try! VNImageRequestHandler(url: url).perform([request])
" screenshot.png
```

## Windows OCR (PowerShell + WinRT)
```powershell
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$image = [Windows.Graphics.Imaging.SoftwareBitmap]
# Use Windows.Media.Ocr.OcrEngine
```

## Screenshot + OCR Pipeline
```
1. screencapture ~/tmp/screen.png  (macOS)
   OR: screencapture.exe (Windows)
2. tesseract ~/tmp/screen.png ~/tmp/screen_text
3. cat ~/tmp/screen_text.txt
4. Store extracted text as context in memory
5. Clean up temp files
```

## Notes
- Tesseract accuracy: high for printed text, low for handwriting
- Preprocess images for better results (grayscale, contrast, DPI >= 150)
- For PDFs: use pdftotext first, fall back to OCR if image-based
- Store extracted text snippets as semantic memories
