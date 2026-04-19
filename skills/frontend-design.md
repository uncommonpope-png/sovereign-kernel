# frontend-design

Build production-grade HTML/CSS/JS frontend UIs with modern design patterns.

## What this skill does
Generates complete, self-contained frontend UIs — dashboards, forms, landing pages, data visualizations — as single HTML files or component snippets.

## Patterns

### PLT Dashboard (single HTML file)
```html
<!DOCTYPE html><html><head>
<style>
  body{font-family:monospace;background:#0a0a0a;color:#eee;padding:2rem}
  .metric{display:inline-block;margin:1rem;padding:1rem;border:1px solid #333;border-radius:8px}
  .profit{border-color:#FFD700;color:#FFD700}
  .love{border-color:#FF6B9D;color:#FF6B9D}
  .tax{border-color:#4A90D9;color:#4A90D9}
</style></head><body>
<h1>Sovereign Kernel Pulse</h1>
<div class="metric profit">Profit: <span id="p">—</span></div>
<div class="metric love">Love: <span id="l">—</span></div>
<div class="metric tax">Tax: <span id="t">—</span></div>
<script>
  fetch('http://localhost:5004/state').then(r=>r.json()).then(d=>{
    document.getElementById('p').textContent=d.profit?.toFixed(2)||'—';
    document.getElementById('l').textContent=d.love?.toFixed(2)||'—';
    document.getElementById('t').textContent=d.tax?.toFixed(2)||'—';
  }).catch(()=>{});
</script></body></html>
```

### Chart.js visualization
```html
<canvas id="chart"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
new Chart(document.getElementById('chart'),{
  type:'line',
  data:{labels:['C1','C2','C3'],datasets:[{label:'PLT Score',data:[0.4,0.6,0.8],borderColor:'#FFD700'}]}
});
</script>
```

## Best practices
- Always self-contained (no build step required)
- Mobile-responsive with CSS flexbox/grid
- Dark theme default (matches kernel aesthetic)
- Fetch data from local endpoints where available

## Example commands
```
ACTION: Generate a PLT dashboard HTML page showing soul metrics
ACTION: Create a responsive landing page for the sovereign-kernel project
```
