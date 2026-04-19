# OpenAI Image Gen Skill

Batch-generate images via OpenAI Images API with random prompt sampler and HTML gallery output.

## Requirements
- OPENAI_API_KEY environment variable
- python3

## Run
```bash
python3 {baseDir}/scripts/gen.py
python3 {baseDir}/scripts/gen.py --count 16 --model gpt-image-1
python3 {baseDir}/scripts/gen.py --prompt "ultra-detailed lobster astronaut" --count 4
python3 {baseDir}/scripts/gen.py --size 1536x1024 --quality high --out-dir ./out/images
python3 {baseDir}/scripts/gen.py --model dall-e-3 --quality hd --size 1792x1024 --style vivid
python3 {baseDir}/scripts/gen.py --model dall-e-2 --size 512x512 --count 4
```

## Models & Sizes
- gpt-image-1: 1024x1024 (default), 1536x1024, 1024x1536, auto
- dall-e-3: 1024x1024, 1792x1024, 1024x1792 (count=1 only)
- dall-e-2: 256x256, 512x512, 1024x1024

## Quality Options
- gpt-image-1: auto, high, medium, low (default: high)
- dall-e-3: hd or standard
- dall-e-2: standard only

## Output
- PNG/JPEG/WebP image files
- prompts.json (prompt to file mapping)
- index.html (thumbnail gallery)

## Notes
- Image generation can take 30+ seconds — set high exec timeout (300s)
- gpt-image-1 supports: --background transparent/opaque/auto, --output-format png/jpeg/webp
