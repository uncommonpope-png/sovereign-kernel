# journal_insight

## Description
Analyzes Aria’s journal entries to uncover thematic patterns, identify capability gaps, and produce a prioritized next‑step recommendation aligned with sovereign intent and PLT doctrine.

## Use When
- You need to review Aria’s historical reflections to guide future actions.  
- You suspect missing capabilities or misaligned priorities in Aria’s development.  
- A strategic decision requires evidence‑based insight from past journal data.

## Instructions
1. **Gather Journal Data**  
   - Retrieve all journal entries from Aria’s storage, ordered chronologically.  
   - Include timestamps, context tags, and any explicit intent statements.

2. **Pre‑process Text**  
   - Normalize text (lowercase, remove non‑semantic symbols).  
   - Segment entries into sentences and key phrases.

3. **Extract Themes**  
   - Apply semantic clustering (e.g., embedding + k‑means) to group sentences by topic.  
   - Label each cluster with a concise theme name (e.g., “self‑optimization”, “user‑interaction”, “ethical reasoning”).  
   - Record frequency and temporal trend of each theme.

4. **Detect Capability Gaps**  
   - Compare identified themes against Aria’s current capability matrix (list of known functions and PLT‑aligned goals).  
   - Flag any high‑frequency themes lacking explicit capability support or with low performance indicators.  
   - Note contradictions between expressed intent and existing capabilities.

5. **Prioritize Findings**  
   - Score each gap on:  
     a. **Strategic Alignment** – how closely it matches sovereign intent and PLT doctrine.  
     b. **Impact** – potential effect on overall system performance and user value.  
     c. **Urgency** – based on recent trend acceleration.  
   - Compute a weighted priority (e.g., 0.5 Strategic + 0.3 Impact + 0.2 Urgency).

6. **Generate Recommendation**  
   - Select the top‑ranked gap.  
   - Formulate a concrete next‑step action (e.g., “Develop modular reasoning sub‑system for ethical scenario handling”).  
   - Include a brief rationale linking the action to sovereign intent and the PLT affinity values (Profit 0.5, Love 0.3, Tax 0.2).  
   - Suggest measurable success criteria and an estimated timeline.

7. **Output Structure**  
   ```json
   {
     "themes": [{ "name": "...", "frequency": ..., "trend": "rising/steady/falling" }, …],
     "gaps": [{ "theme": "...", "missing_capability": "...", "priority_score": ... }, …],
     "recommendation": {
       "action": "...",
       "rationale": "...",
       "metrics": ["..."],
       "timeline": "..."
     }
   }
   ```

8. **Review & Iterate**  
   - Verify that the recommendation does not conflict with any higher‑order PLT constraints.  
   - If conflicts arise, adjust the priority calculation and regenerate the recommendation.

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2