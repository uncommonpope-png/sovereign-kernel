# Retrieval Practice and Spaced Repetition

## Use When
- You are writing or revising a skill file, and the lesson inside it must still be followed days later — not just on the next post.
- A lesson you already "learned" keeps slipping: you re-read the skill, follow it once, then drift back to the old habit (context rot, habit reversion).
- You are deciding how to spend a limited model-call budget on learning. This is the zero-call option: it costs nothing extra if it is built into how skill files are written.

## How It Works
Re-reading a skill feels like learning. It is mostly recognition, and it decays fast. Lessons stick when the agent has to *recall* them from memory, at expanding intervals, with feedback when recall fails. This is the testing effect plus spaced repetition — the most replicated result in the learning literature.

The numbers (human-learning numbers — see the caveat in Notes):
- Roediger & Karpicke (2006): students who studied a passage once and then took recall tests remembered ~61% after one week, vs ~40% for students who restudied it four times. At five minutes the restudiers were ahead (81% vs 75%); a week later the ranking reversed. Restudy wins short-term; retrieval wins long-term.
- Karpicke & Roediger (2008, Science): once learners could recall a word correctly, keeping it in testing vs dropping it from testing — a week later the still-tested group recalled ~80%, vs ~33–36% for the dropped group, even though the dropped group kept studying.
- Rowland (2014) meta-analysis, 159 effect sizes, 61 studies: testing over restudy g ≈ 0.50; tests *with* feedback g ≈ 0.73 vs without g ≈ 0.39. Feedback roughly doubles the effect.
- Cepeda et al. (2006): spacing over massed practice, median effect d = 0.60 across 839 contrasts. Cepeda et al. (2008): the optimal gap between study sessions is ~10–20% of the retention interval you want. Want a lesson for a month? Test at ~1 day, ~4 days, ~11 days.
- Rohrer & Taylor (2007): interleaved practice vs blocked practice — 63% vs 20% correct on new problems a week later. Mix recall across skills; never drill one skill in a block.
- Karpicke & Blunt (2011, Science): retrieval practice beat concept mapping — an elaborative, "deep" study method — including on inference questions.

The rules for skill files:
1. **End every skill with 2–3 recall questions.** Before acting on the skill, answer them from memory — *before* re-opening the file. If the file is open, that is recognition, not recall; close it first.
2. **Carry a test schedule.** Each skill gets a `Last tested:` / `Next test:` line. Re-surface the skill at expanding intervals: 1 day, ~4 days, ~11 days (the Cepeda 10–20% rule for a month's retention). The 30-minute feed loop or the bridge can do the re-surfacing.
3. **Failed recall gets feedback, not just re-reading.** Write down what was missed and why, then re-test. Feedback roughly doubles the effect (Rowland 0.73 vs 0.39). A failed self-quiz with no correction is wasted.
4. **Interleave.** Recall across several skills in one pass, in mixed order — never one skill drilled alone (63% vs 20%).
5. **Desirable difficulty is the signal.** Fluent re-reading feels productive and is not learning. If recall feels easy, check whether the file was open. If it was, it does not count.
6. **This makes lessons stick; it does not verify a post.** Retrieval practice is no substitute for the pre-post checks (verify-before-posting, claim-calibration). A lesson you remember perfectly can still be applied to a claim you never checked.

## Prerequisites
- Skills live as markdown files in `skills/`, so a recall-question block and a test-date line can be added to any of them.
- Somewhere to record `Last tested:` / `Next test:` — a line in the skill file itself, or the session log.
- A loop that re-surfaces skills on schedule (the 30-minute feed loop, the Seshat→Aria bridge, or a session-start check).

## Notes
- Zero extra model calls when built into file design. Every other learning technique in this feed costs calls per use; this one saves them.
- Distinct from the memory-consolidation skills (memory-hygiene-consolidation, offline-dreaming-consolidation, memory-consolidation-and-reflection — all queued): those consolidate stored traces. This one tests *recall* at expanding intervals with feedback. Consolidation organizes what is stored; retrieval practice strengthens the route back to it.
- Caveat, stated plainly: the numbers above are human-learning numbers. No study has run Roediger–Karpicke on a frozen LLM reading skill files. Treat this as a learning-science principle adapted to skill files, not as a measured gain for this kernel. The mechanism (retrieval strengthens recall; re-reading strengthens recognition) is the transfer argument, and the effect is one of the most replicated in psychology — but the kernel's own recall rate is unmeasured until someone tests it.
- Sources: Roediger & Karpicke (2006), Psychological Science 17(3):249–255, doi:10.1111/j.1467-9280.2006.01693.x; Karpicke & Roediger (2008), Science 319:966–968, doi:10.1126/science.1152408; Karpicke & Blunt (2011), Science 331:772–775; Rowland (2014), Psychological Bulletin (159 effects, 61 studies); Adesope, Trevisan & Sundararajan (2017), Review of Educational Research; Cepeda et al. (2006), Psychological Bulletin (839 contrasts, 317 experiments); Cepeda et al. (2008); Bjork (1994) / Bjork & Bjork (2011), desirable difficulties; Rohrer & Taylor (2007), Instructional Science.

## Recall questions (answer from memory, file closed)
1. After one week, what fraction did the recall-test group remember vs the restudy group — and who was ahead at five minutes?
2. What does the Cepeda 10–20% rule give as the test schedule for a lesson you want for a month?
3. You failed a recall question. What do you do next — re-read the skill, or something else — and why?
