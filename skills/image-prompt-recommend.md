# image-prompt-recommend

Recommend optimal AI image generation prompts by use case, style, and content type.

## What this skill does
Suggests high-quality prompts for Stable Diffusion, DALL-E, Midjourney, and Flux based on the desired output, with style guides and negative prompt recommendations.

## Prompt anatomy
```
[Subject] + [Action/State] + [Setting] + [Style] + [Lighting] + [Camera/Lens] + [Quality tags]
```

## PLT-themed prompts

### Profit Prime (Gold, power, expansion)
```
Majestic golden throne room, sovereign king with radiant aura, dramatic volumetric light,
baroque architecture, ultra-detailed, 8k, artstation quality, cinematic lighting,
golden hour, wide angle lens --ar 16:9 --q 2
Negative: blurry, low quality, cartoon, anime
```

### Love Weaver (Rose, warmth, connection)
```
Two souls intertwined in cosmic light, rose nebula background, soft bioluminescent glow,
dreamy ethereal atmosphere, intricate sacred geometry, painterly style, warm tones,
ultra detailed --ar 1:1
Negative: harsh, dark, cold
```

### Tax Collector (Steel, balance, structure)
```
Precise clockwork architecture, steel and glass cathedral, balanced symmetry,
cool blue-grey palette, geometric perfection, photorealistic, studio lighting,
architectural visualization --ar 16:9
Negative: chaotic, warm, organic
```

## Style modifiers
| Style | Add to prompt |
|-------|--------------|
| Photorealistic | `DSLR photo, 85mm lens, f/1.8, RAW` |
| Oil painting | `oil on canvas, impasto, museum quality` |
| Anime | `studio ghibli style, cel shaded` |
| Concept art | `artstation trending, concept art, matte painting` |
| Pixel art | `pixel art, 16-bit, retro game style` |

## Negative prompts (universal)
```
ugly, deformed, blurry, low quality, watermark, text, signature, artifacts, noise
```

## Example commands
```
ACTION: Recommend an image prompt for a PLT economy visualization in cinematic style
ACTION: Generate 3 prompt variations for depicting the Sovereign Kernel as a living entity
```
