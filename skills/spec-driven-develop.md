# spec-driven-develop

Automate the pre-development specification workflow — requirements, architecture, and task decomposition — before writing any code.

## What this skill does
Generates a full SPEC.md document from a natural language goal, covering: problem statement, constraints, architecture decisions, API contracts, and decomposed implementation tasks.

## Spec file format
```markdown
# SPEC: [Feature Name]
Date: 2026-04-18
Author: Sovereign Kernel (Aria)
PLT Justification: P=0.8 L=0.3 T=0.2 — PROCEED

## Problem Statement
[What problem does this solve?]

## Constraints
- Must compile cleanly (cargo check passes)
- No breaking changes to existing API
- Max 200 lines of new Rust code

## Architecture Decision
[ADR: why this approach over alternatives]

## API / Interface Contract
\`\`\`rust
// Public API
pub fn new_feature(input: &str) -> Result<String>
\`\`\`

## Implementation Tasks
1. [ ] Add struct definition
2. [ ] Implement core logic
3. [ ] Wire into main loop
4. [ ] Write test
5. [ ] Update README

## Acceptance Criteria
- [ ] Passes cargo check with 0 errors
- [ ] Feature behaves as described in problem statement
- [ ] Memory usage unchanged
```

## Generate spec with Ollama
```python
prompt = f"""You are a senior architect. Generate a SPEC.md for:
Goal: {goal}
Existing codebase: Rust, tokio async, single main.rs
Format: Problem Statement, Constraints, Architecture, Tasks, Acceptance Criteria.
Max 400 words."""
```

## Example commands
```
ACTION: Generate a SPEC.md for adding a REST API endpoint to the sovereign kernel
ACTION: Create a spec for integrating the news-monitor skill with automatic daily digest storage
```
