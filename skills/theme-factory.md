# theme-factory

Create cohesive visual themes — color palettes, typography, component styles — for apps and documents.

## What this skill does
Generates complete design system themes: color tokens, typography scales, spacing systems, and component style definitions in CSS, JSON, or Tailwind config format.

## PLT Theme (CSS variables)
```css
:root {
  /* PLT Color System */
  --plt-profit:     #FFD700;
  --plt-profit-dim: #B8980A;
  --plt-love:       #FF6B9D;
  --plt-love-dim:   #C4456F;
  --plt-tax:        #4A90D9;
  --plt-tax-dim:    #2D6BA8;

  /* Neutrals */
  --bg-base:        #0D0D0D;
  --bg-surface:     #1A1A1A;
  --bg-elevated:    #242424;
  --border:         #333333;
  --text-primary:   #EEEEEE;
  --text-secondary: #888888;
  --text-muted:     #555555;

  /* Typography */
  --font-mono:      'JetBrains Mono', 'Fira Code', monospace;
  --font-serif:     'Georgia', 'Times New Roman', serif;
  --font-sans:      'Inter', 'Segoe UI', sans-serif;
  --size-xs:  0.75rem;
  --size-sm:  0.875rem;
  --size-md:  1rem;
  --size-lg:  1.25rem;
  --size-xl:  1.5rem;
  --size-2xl: 2rem;

  /* Spacing */
  --space-1: 0.25rem; --space-2: 0.5rem; --space-3: 0.75rem;
  --space-4: 1rem;    --space-6: 1.5rem; --space-8: 2rem;

  /* Radius */
  --radius-sm: 4px; --radius-md: 8px; --radius-lg: 12px; --radius-full: 9999px;
}
```

## Generate theme JSON (design tokens)
```python
def generate_theme(name, primary, secondary, accent):
    return {
        "name": name,
        "colors": {
            "primary": primary, "secondary": secondary, "accent": accent,
            "background": "#0D0D0D", "surface": "#1A1A1A", "text": "#EEEEEE"
        },
        "typography": {"fontMono": "JetBrains Mono", "fontSans": "Inter"},
        "spacing": {"base": "1rem", "scale": 1.5}
    }
plt_theme = generate_theme("PLT Sovereign", "#FFD700", "#FF6B9D", "#4A90D9")
```

## Tailwind config extension
```js
module.exports = {
  theme: { extend: {
    colors: { profit: '#FFD700', love: '#FF6B9D', tax: '#4A90D9' },
    fontFamily: { mono: ['JetBrains Mono', 'monospace'] }
  }}
}
```

## Example commands
```
ACTION: Generate a complete CSS theme for the sovereign kernel dashboard
ACTION: Create a dark PLT color palette as JSON design tokens
```
