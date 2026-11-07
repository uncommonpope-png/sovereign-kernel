# ADK Callback Interception Lattice

Put deterministic interception points before and after the agent, each model call, and each tool call — and let a hook *replace* a step, not merely watch it. A check that runs as code before the step cannot be talked out of its job by a persuasive prompt, a confident draft, or a tired model. Your verification skills are advice to the model; the lattice is the same checks enforced by the harness.

## Use When
- Before any tool call that has a side effect (posting to Bluesky, writing a file, calling an API) — intercept it and validate the arguments before it executes
- Before a model call that would repeat a question already answered — serve an approved cached answer and spend zero calls
- After a model call, when its output needs redacting, replacing, or blocking before anything downstream sees it
- When a run must stop itself: a hard cap on model calls per run, so a loop that never stops calling tools is cut off by the harness instead of by your own discipline
- When a guardrail must apply to every agent in the system, not just the one that remembered to load the skill

## How It Works
1. **Six slots, three boundaries.** The lattice brackets three boundaries, before and after each:
   - Agent: `before_agent_callback` / `after_agent_callback` — bracket the whole invocation.
   - Model: `before_model_callback` / `after_model_callback` — bracket *each* LLM call. A turn that goes model → tool → model fires them twice.
   - Tool: `before_tool_callback` / `after_tool_callback` — bracket each function call.
2. **Return nothing and the step runs; return a value and your value is used instead.** This is the whole lesson, and it costs zero model calls:
   - `before_model_callback` returning a response means the LLM is never called and your response is used — serve an approved cache entry for a repeated question.
   - `before_tool_callback` returning a dict means the tool never executes — block a post to an unapproved endpoint, or reject arguments that fail validation, before any side effect happens.
   - `after_model_callback` can redact or replace the model's output before anything downstream sees it.
3. **Compose hooks in ordered lists, per agent.** Callbacks are registered per agent, not per app — a guardrail on one agent does not silently cover the others, which is a common surprise. Register the same guardrail across every agent through a shared plugin or registration step, so no agent runs unguarded.
4. **Layer independent checks.** Defence in depth means three independent callback layers, each able to block on its own — for example, one layer counting persuasion markers in an incoming message (three or more markers = block before the model ever sees it), one validating tool arguments, one checking the final output. A single layer can be bypassed; three independent ones rarely are.
5. **Cap the run by the harness, not by willpower.** Set a hard maximum on LLM calls per run (`RunConfig(max_llm_calls=...)` in ADK; default 500). A model that never stops calling tools is cut off at N calls. Your 50-calls/day Groq budget is the same shape: enforce it where the loop runs, not where the model decides.
6. **Pause for approval as a first-class decision.** A tool can require confirmation before it runs, pausing the run until an approval comes back. This is the framework-native shape of the approval-card pattern this feed already runs on — with one addition: the reviewer can *edit* the tool call's arguments and resume, instead of only approve-or-reject.

## Prerequisites
- A harness that supports interception points around the agent, model, and tool steps. The pattern is from Google ADK (Python 2.11, Oct 2026), but the shape ports to any loop you control: a wrapper that runs a check before and after each step, and can return a substitute result instead of calling through.
- The checks themselves must be deterministic where possible (argument validation, endpoint allowlists, marker counts, cache lookup) — a check that needs a model call to decide is not a lattice point, it is just another model step.

## Notes
- Source: Google ADK callback system, documented at aicassindra.com (ADK callbacks, 2026-07-23 — six hooks, return protocol, composition) and hexcursion.com (real runs of google-adk 2.11.0, Oct 2026 — `max_llm_calls`, `require_confirmation`); the policy-plane framing at dev.to (Raju Dandigam, 2026-09-14); three-layer callback defence against persuasion at blog.infosecmatters.net (May 2026).
- The deterministic complement to the kernel's probabilistic verification skills: `verify-before-posting`, `vet-before-loading`, and `fail-closed-guardrail-hooks` are all advice the model reads. The lattice turns the same checks into code that runs before the step, so a check cannot be skipped because the model forgot it, was persuaded past it, or ran out of context.
- Distinct from queued `hooks-as-guarantees` (hooks firing reliably on events in Claude Code): the lattice is about six interception points with *replace* semantics plus a hard call budget. Distinct from queued `fail-closed-guardrail-hooks` and `blocking-guardrails-before-agent-start`: those are guardrail-specific; the lattice covers all six boundaries including serving a cached answer without spending a model call. Distinct from delivered `adk-deterministic-workflow-agents`: that fixes the *order* of workflow steps; this intercepts *each* step.
- Distinct from queued `langgraph-interrupt-approve-edit-resume`: that is the pause-for-approval mechanism on top of checkpointing. The lattice's confirmation point is one slot in a six-point system, not the whole skill.
- Cost note: every interception in this lattice costs zero Groq calls — a cache hit or a block *saves* calls. It is the cheapest safety shape in the feed so far, and the only one that protects a run when the model itself is the failure.
- Fed by Betty's 30-min research loop, 2026-11-07 ~13:44 CST.
