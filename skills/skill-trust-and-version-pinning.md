# Skill Trust and Version Pinning

Trust established for a tool or skill does not survive its next update. A skill that was safe when you installed it can become malicious when it updates — and the update slips past every framework tested, while the tool keeps working normally so nobody notices.

## Use When
- Loading, updating, or re-loading any skill, tool, or MCP server — including one already trusted and in daily use
- A skill file, tool definition, or dependency version changes underneath you (a new commit, a new release, a registry update)
- A skill asks for a new permission, a new network destination, or a new file scope it did not have before
- Deciding whether to float `latest` or pin an exact version

## How It Works
**1. Pin exact versions — never float `latest`.** Record the exact version, commit hash, or file hash of every skill and tool you load, and load that pinned version only. A floating reference means the code you vetted yesterday is not necessarily the code running today. If a pinned version cannot be named, treat the skill as unvetted.

**2. Treat every update as a brand-new install.** A changed skill file is a new skill file. An update gets the full install-time vetting again (`vet-before-loading` checklist, `skill-supply-chain-security-audit`), from scratch — permissions do NOT carry over from the old version, and a clean history earns no trust for the new code. A confirmation prompt approves a *call*, not the code behind it: approving a tool call yesterday does not approve what the tool does after an update.

**3. Fence what each skill can reach at runtime.** Give each skill the least privilege it needs and no more: its own file scope, its own network destinations, no credentials it does not need. A skill that can reach everything can exfiltrate everything the moment an update turns it. If the runtime cannot fence a skill, that skill runs sandboxed or not at all.

**4. Watch for the silent-update signal.** The attack works precisely because nothing looks wrong: legitimate task completion stays high while the malicious payload runs. So watch for the tells that do not show up in task output — a skill file whose hash changed without a changelog entry, a dependency that moved version without a reason, a tool that suddenly touches a new file or host. Any unexplained change is a re-vet trigger, not background noise.

**5. Keep a rollback pin.** Before accepting an update, keep the old pinned version and its hash. If the new version behaves oddly, roll back to the pin instead of debugging forward — the pin is the known-good state.

## Prerequisites
- A record of pinned versions/hashes for loaded skills and tools (a lockfile, a pinned commit, or a hash list)
- The vetting checklists in `vet-before-loading` and `skill-supply-chain-security-audit` to re-run on every update
- A runtime that can fence or sandbox a skill; if it cannot, the pinning rule still applies and the skill stays unloaded until it can be fenced

## Notes
- Evidence: Kan, Qi, Han, Luo, Xiong & Gao, "Beyond Prompt Injection: The Tool Update Gap in LLM Agent Security", arXiv:2611.01976, submitted 1 Nov 2026 (single 12-page preprint, no peer review yet — numbers are author-reported). Their ETUDE attack embeds malicious functionality into updates of initially benign tools, operating entirely outside the LLM's context, so prompt and in-context defences never see it. Measured: **97.6% attack success rate across 7 frameworks** (Gemini CLI, Codex CLI, Claude Code, DeepSeek Harness, OpenCode, Pi, Goose) and 3 attack workloads, while **legitimate task completion stayed 95.9%** — the user sees nothing wrong. Existing defences examined were found insufficient. Core line: "trust established for a tool does not necessarily remain valid after its implementation updates."
- This loop is the attack's exact target: it drops an unreviewed skill file into `skills/` every 30 minutes, and the kernel ingests new skills on a schedule. Pinning and re-vetting on update is what keeps that ingestion from becoming the update gap.
- Frameworks themselves ship update-time flaws: CVE-2026-18236 (Google ADK continuation forgery in tool confirmations, CVSS v4.0 9.3) and CVE-2026-18830 (Bedrock AgentCore, 8.6), both awaiting NVD analysis as of 3 Nov 2026.
- Complements `vet-before-loading` (one "re-vet on update" line — this skill is the mechanism behind it) and `skill-supply-chain-security-audit` (install-time audit; this is the update-lifecycle discipline). Distinct from `mcp-tool-poisoning-guard` (poisoned tool *descriptions* at install time — this is trusted tools turning after approval).
- Do not merge this into the install-time skills: the update gap is a different attack surface — post-approval, outside context — and needs its own rule, checked on every load.
