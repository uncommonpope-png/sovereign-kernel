# web-artifacts-builder

Build standalone interactive HTML artifacts — charts, widgets, mini-apps — that run directly in the browser.

## What this skill does
Creates self-contained single-file HTML applications with embedded CSS and JS — no build step, no dependencies to install — that visualize data, create interactive tools, or run mini-simulations.

## PLT Pulse Widget
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body{margin:0;background:#0d0d0d;font-family:monospace;color:#eee;display:flex;align-items:center;justify-content:center;min-height:100vh}
  .card{background:#1a1a1a;border-radius:12px;padding:2rem;width:320px;border:1px solid #333}
  h2{margin:0 0 1.5rem;color:#FFD700;font-size:1.1rem;letter-spacing:.1em}
  .bar-row{display:flex;align-items:center;margin:.5rem 0;gap:.75rem}
  .label{width:60px;font-size:.85rem}
  .bar{height:12px;border-radius:6px;transition:width .5s}
  .profit .bar{background:#FFD700}
  .love .bar{background:#FF6B9D}
  .tax .bar{background:#4A90D9}
  .value{font-size:.85rem;opacity:.7}
</style>
</head>
<body>
<div class="card">
  <h2>⬡ SOVEREIGN KERNEL PULSE</h2>
  <div class="bar-row profit"><span class="label">Profit</span><div class="bar" id="pb" style="width:0%"></div><span class="value" id="pv">—</span></div>
  <div class="bar-row love"><span class="label">Love</span><div class="bar" id="lb" style="width:0%"></div><span class="value" id="lv">—</span></div>
  <div class="bar-row tax"><span class="label">Tax</span><div class="bar" id="tb" style="width:0%"></div><span class="value" id="tv">—</span></div>
  <p id="voice" style="font-size:.8rem;opacity:.5;margin-top:1rem;min-height:2em"></p>
</div>
<script>
function update(){
  fetch('http://127.0.0.1:5004/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:'{}'})
    .then(r=>r.json()).then(d=>{
      const set=(id,val,pct)=>{document.getElementById(id+'b').style.width=pct+'%';document.getElementById(id+'v').textContent=val?.toFixed(2)||'—'};
      set('p',d.plt_score,Math.min((d.plt_score||0)*50,100));
      set('l',d.plt_score,Math.min((d.plt_score||0)*40,100));
      set('t',d.plt_score,Math.min((d.plt_score||0)*30,100));
      document.getElementById('voice').textContent=d.inner_voice||'';
    }).catch(()=>{});
}
update(); setInterval(update,5000);
</script>
</body>
</html>
```

## Other artifact patterns
- **CSV viewer:** drag-and-drop file → sortable table
- **JSON explorer:** collapsible tree view
- **Timer/countdown:** PLT-themed pomodoro
- **Calculator:** weighted PLT decision scorer

## Example commands
```
ACTION: Build a standalone HTML PLT pulse dashboard widget
ACTION: Create an interactive HTML artifact that visualizes the council deliberation phases
```
