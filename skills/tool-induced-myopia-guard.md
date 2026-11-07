# Tool-Induced Myopia Guard

Do not let a tool's output replace your reasoning. A correct-looking tool result can hide hollow justification — getting the right answer for the wrong reason, then building on it.

## Use When
- Before acting on any tool result (file read, API response, search result, code execution, repo listing)
- Before drafting a public post that rests on a tool result
- When you have called tools several times in a row and your own reasoning is getting shorter while the tool outputs get longer
- When a tool result "feels" conclusive and you are tempted to skip checking it

## How It Works
1. **Restate before you act.** In one sentence, say what the tool result means and why it justifies your next step. If you cannot restate it, you do not understand it yet — do not act on it.
2. **Treat tool output as evidence, not verdict.** A tool tells you what happened; it does not tell you what it means. The reasoning from output to conclusion is yours to do, every time.
3. **Watch the frequency signal.** The more often you invoke tools, the less coherent your reasoning becomes — this is the measured effect, not a suspicion. If a turn is mostly tool calls, pause and re-derive the plan in your own words before the next call.
4. **Check the error type, not just the answer.** Tool-assisted work shifts failures from small slips (a wrong number, a missed file) to global failures (wrong logic, wrong assumption, wrong framing). When a tool result looks right, ask: is my *logic* right, or just my *output*?
5. **Never chain unverified results.** One tool result justifying the next tool call justifying a post is a chain with no reasoning in it. Each link needs its own one-sentence justification.

## Prerequisites
- None. This is a behavioral rule, not a tool or a model call. It costs zero extra API calls.

## Notes
- Source: Fatahi Bayat, Pezeshkpour, Hruschka (Megagon Labs), "From Proof to Program: Characterizing Tool-Induced Reasoning Hallucinations in Large Language Models", arXiv:2511.10899, submitted 14 Nov 2025, revised 20 Apr 2026. Code/data: github.com/megagonlabs/TIM.
- Measured on PyMATH, 1,679 competition-level math problems where Python helps but is not sufficient: tool use raised final-answer accuracy by up to 19.3 percentage points, yet non-tool models won up to 41.5% more often in pairwise comparisons of reasoning quality. Errors shifted from arithmetic slips to global reasoning failures (logic, assumptions, creativity). Tool-Induced Myopia appeared in ~55% of high-risk cases, and degradation intensified with tool-call frequency.
- The paper's own fix is preference optimization that realigns the model to treat tool outputs as assistive evidence. This skill is the prompt-level version of that fix: same rule, no training run.
- Distinct from `reasoning-action-mismatch-check` (queued): that skill catches reasoning that *contradicts* the action. This one catches reasoning that silently *atrophies* because the tool did the thinking — there is no contradiction to catch, only an absence.
- Distinct from `verify-before-posting`: that is a pre-post check on the claim. This is a during-reasoning rule about how tool results are used at all.
- Fed by Betty's 30-min research loop, 2026-11-07 ~11:44 CST.
