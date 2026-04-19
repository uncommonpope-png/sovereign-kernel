# drawio

Generate draw.io diagrams from natural language descriptions, export to PNG/SVG/PDF.

## What this skill does
Creates architecture diagrams, flowcharts, mind maps, and system diagrams as draw.io XML, then exports via the draw.io CLI or API.

## Setup
```bash
# Install draw.io desktop CLI (Linux/Mac/Windows)
# https://github.com/jgraph/drawio-desktop/releases
# Windows: drawio.exe in PATH
npm install -g draw.io  # alternative
```

## Generate diagram XML
```python
# Minimal draw.io XML template
diagram = """<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/>
<mxCell id="2" value="Sovereign Kernel" style="rounded=1;fillColor=#FFD700;fontStyle=1;"
  vertex="1" parent="1"><mxGeometry x="100" y="100" width="160" height="60" as="geometry"/></mxCell>
<mxCell id="3" value="Skill Engine" style="rounded=1;fillColor=#4A5568;fontColor=#fff;"
  vertex="1" parent="1"><mxGeometry x="320" y="100" width="120" height="60" as="geometry"/></mxCell>
<mxCell id="4" edge="1" source="2" target="3" parent="1">
  <mxGeometry relative="1" as="geometry"/></mxCell>
</root></mxGraphModel>"""
with open("diagram.drawio", "w") as f:
    f.write(diagram)
```

## Export to PNG
```bash
# Using draw.io CLI
drawio --export --format png --output diagram.png diagram.drawio

# Using xvfb on headless Linux
xvfb-run drawio --export --format png diagram.drawio
```

## Diagram types
- **Flowchart:** decision boxes, process nodes, arrows
- **Architecture:** services, databases, queues, connections
- **Mind map:** central concept with radiating branches
- **Sequence diagram:** actors, lifelines, messages

## Example commands
```
ACTION: Generate a draw.io architecture diagram of the sovereign kernel components
ACTION: Create a flowchart of the PLT council deliberation phases and export to PNG
```
