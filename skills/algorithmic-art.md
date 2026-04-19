# algorithmic-art

Generate algorithmic and generative art using code execution.

## What this skill does
Creates visual art through mathematical algorithms, fractals, L-systems, cellular automata, and generative patterns. Outputs SVG, PNG, or HTML canvas.

## Tools
- Python with matplotlib, PIL, numpy, cairo
- p5.js / Processing for interactive sketches
- SVG generation via plain text

## Patterns

### Fractal (Mandelbrot)
```python
import numpy as np
import matplotlib.pyplot as plt
w, h = 800, 600
x = np.linspace(-2.5, 1.0, w)
y = np.linspace(-1.25, 1.25, h)
C = x[np.newaxis,:] + 1j*y[:,np.newaxis]
Z = np.zeros_like(C)
M = np.zeros(C.shape, dtype=int)
for i in range(100):
    mask = np.abs(Z) <= 2
    Z[mask] = Z[mask]**2 + C[mask]
    M[mask] += 1
plt.imsave("fractal.png", M, cmap="inferno")
```

### L-System Tree
```python
def lsystem(axiom, rules, n):
    s = axiom
    for _ in range(n):
        s = "".join(rules.get(c,c) for c in s)
    return s
tree = lsystem("F", {"F":"FF+[+F-F-F]-[-F+F+F]"}, 4)
```

### PLT Art
- Profit art: sharp geometric expansion, gold palette
- Love art: flowing curves, warm rose tones
- Tax art: rigid grids, cool grey balance

## Example commands
```
ACTION: Generate a Mandelbrot fractal and save to art/fractal.png
ACTION: Create an L-system tree with depth 5 in SVG format
```
