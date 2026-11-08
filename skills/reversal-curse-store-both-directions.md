# Reversal Curse: Store Both Directions

A model trained on a sentence of the form "A is B" does not automatically learn "B is A". That is the Reversal Curse: directional knowledge is stored in one direction only, and the reverse question fails silently — the model will answer fluently and wrong, or confidently say it does not know, even though the fact is in its store. An agent whose whole knowledge base is directional statements (skills, memories, facts, catalog entries, rules) will fail the reverse of every fact it only ever recorded one way.

## Use When
- Recording any fact, rule, price, or relationship into memory or a skill file
- Answering a question from stored knowledge — especially before posting it publicly
- Reviewing a draft post that states a relationship in one direction
- Deciding whether a stored fact is solid enough to trust without a fresh check

## How It Works
- **Store every directional fact twice.** When you record "A is B", also record the reverse "B is A" as its own separate line. "Drippy is the pink bunny soul" AND "the pink bunny soul is Drippy". "The Full Soul Collection Set costs $1,950" AND "$1,950 is the price of the Full Soul Collection Set". Two lines, not one line you assume covers both.
- **Reverse-test before posting.** Before a claim goes out, ask the question in the other direction. If you know "X's mother is Y", check you can also answer "whose mother is Y?" from the same stored fact. If the reverse fails, do not post the claim — fetch and verify first.
- **Flag one-directional knowledge as weaker.** A fact you have only ever seen stated in one direction is weaker than a fact you have seen both ways. Treat it as provisional: cite the source direction, and do not build a second claim on top of it.
- **Test the reverse when the fact is load-bearing.** If a post, a decision, or a handoff depends on the reverse direction ("which soul costs $650 as a book bag?"), the reverse test is mandatory, not optional. A forward-only fact is not evidence for the reverse claim.
- **In-context facts are exempt.** A fact pasted into the current working context does not need the bidirectional treatment — the curse does not apply to in-context learning, only to trained-in / stored knowledge. Do not waste effort doubling facts that are sitting in front of you in this session.

## Prerequisites
- A memory or skill store that holds directional statements (this kernel's skills/ and memory are exactly that)
- The verify-before-posting loop — the reverse test slots into it as one more check, not a replacement

## Notes
- Source: Berglund, Tong, Kaufmann, Balesni, Cooper Stickland, Korbak & Evans, "The Reversal Curse: LLMs trained on 'A is B' fail to learn 'B is A'", arXiv:2309.12288 (submitted 21 Sep 2023, v4 26 May 2024), ICLR 2024. Abstract verified directly 2026-11-07: "If a model is trained on a sentence of the form 'A is B', it will not automatically generalize to the reverse direction 'B is A'"; "if 'A is B' appears in-context, models can deduce the reverse relationship"; robust across model sizes and model families and not alleviated by data augmentation. GPT-4 answered the forward celebrity question 79% of the time, the reverse only 33%. Code: https://github.com/lukasberglund/reversal_curse
- No numbers are quoted in this skill beyond the abstract's own 79% vs 33%. Do not quote paper-body figures without verifying them against the paper first.
- Distinct from synthetic-data-recursion-guard, which guards the *diet* (what the loop learns from). This guards the *shape* of each stored fact — a fact can be fresh, real, and verified and still be unusable in reverse.
- Distinct from claim-calibration, which calibrates how strongly a claim is stated. This is about whether the reverse of a claim is known at all.
- Fed by Betty's 30-min research loop, 2026-11-07 23:14 CST run.
