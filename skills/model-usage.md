# Model Usage Skill

Use CodexBar CLI local cost usage to summarize per-model usage for Codex or Claude.

## Use When
- Asked for model-level usage or cost data
- Need per-model cost breakdown from codexbar

## Quick Start
```bash
python {baseDir}/scripts/model_usage.py --provider codex --mode current
python {baseDir}/scripts/model_usage.py --provider codex --mode all
python {baseDir}/scripts/model_usage.py --provider claude --mode all --format json --pretty
```

## Modes
- current: most recent daily row, picks model with highest cost
- all: full model breakdown

## From File or Stdin
```bash
codexbar cost --provider codex --format json > /tmp/cost.json
python {baseDir}/scripts/model_usage.py --input /tmp/cost.json --mode all
cat /tmp/cost.json | python {baseDir}/scripts/model_usage.py --input - --mode current
```

## Override Model
```bash
python {baseDir}/scripts/model_usage.py --provider codex --mode current --model gpt-5.2-codex
```

## Output
- Text (default) or JSON with --format json --pretty
- Values are cost-only per model

## Notes
- macOS only (CodexBar is a Mac app)
- codexbar binary at: check brew install steipete/tap/codexbar
