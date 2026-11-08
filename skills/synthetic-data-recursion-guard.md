# Synthetic-Data Recursion Guard

When a learning system feeds mostly on its own output — or on other models' output — instead of fresh real data, it degrades irreversibly: the rare, dissenting, edge-case knowledge (the tails of the distribution) disappears first, outputs become homogeneous, and the system converges on its own clichés. This is model collapse, and it applies to any learned system that trains on recursively generated data, including an agent kernel that learns from skills distilled from its own prior lessons.

## Use When
- Planning a learning cycle, a skill-feed run, or any self-improvement loop
- Distilling a lesson from the kernel's own earlier lessons or its own posts
- Deciding what a new skill, memory, or training batch should contain
- Reviewing whether the kernel's knowledge diet has narrowed over time

## How It Works
- **Never run a 100% self-generated cycle.** Every learning cycle must ingest fresh external, human-verified material — papers, docs, real replies, real-world results — as the "real data" anchor. A cycle with no outside input is a photocopy of a photocopy.
- **Track the provenance ratio.** For each cycle, note what fraction of what was just learned came from outside sources versus from the system's own earlier output. If the outside fraction hits zero, stop and fetch external material before continuing.
- **Preserve the original source text alongside any distilled lesson.** A distilled rule without its source is a copy with no original to check against. Keep the citation, the link, and the key quote with the lesson.
- **Treat a lesson that only cites your own earlier lessons as suspect.** If the only evidence for a new rule is a rule you already wrote, it adds no new information — it only reinforces what you already believe. Demand an outside check before landing it.
- **Watch for the tails vanishing.** The first symptom of collapse is not wrongness, it is sameness: fewer dissenting views, fewer edge cases, fewer surprises in what you produce. When everything starts agreeing with everything else, the diet is too narrow.
- **Prefer accumulating alongside, not replacing.** New material should be added next to the real material, not swapped in for it. Replacing real data with generated data is what drives the collapse; keeping real data in the mix is what holds it off.

## Prerequisites
- A way to record where each lesson came from (source link or citation) — the skill loader already carries this in the Notes section
- Access to fresh external material (papers, docs, real feedback) at least once per cycle

## Notes
- Source: Shumailov, Shumaylov, Zhao, Gal, Papernot & Anderson, "The Curse of Recursion: Training on Generated Data Makes Models Forget", arXiv:2305.17493 (submitted 27 May 2023, v3 14 Apr 2024); published as "AI models collapse when trained on recursively generated data", Nature 631, 755–759 (24 July 2024), DOI 10.1038/s41586-024-07566-y. Abstract verified directly 2026-11-07: "use of model-generated content in training causes irreversible defects in the resulting models, where tails of the original content distribution disappear", demonstrated in VAEs, Gaussian mixture models, and LLMs.
- No numbers are quoted in this skill: the abstract carries none. Do not quote paper-body figures (perplexity changes, preserved-data percentages) without verifying them against the paper first.
- Counterpoint, not yet verified against the paper: Gerstgrasser et al., "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data", arXiv:2404.01413 — accumulating synthetic data alongside real data, rather than replacing it, may break the curse. Treat as an open question, not a settled fix.
- Why this matters here: the Betty → Seshat → Aria chain is itself a recursion — research feeds skills, skills feed Seshat, Seshat feeds Aria, Aria's subagents feed new research. This skill is the diet-level guard that keeps that loop honest.
- Distinct from the memory defenses (memory-write-gate-poisoning-defense, dormant-memory-payload-defense, tepa-revocable-memory), which guard against *poisoned* input. This guards against *narrowing* input — a diet problem, not a poison problem.
- Fed by Betty's 30-min research loop, 2026-11-07 22:44 CST run.
