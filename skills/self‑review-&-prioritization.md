# Self‑Review & Prioritization Skill

## Description
Analyzes recent journal entries to spot recurring themes and skill gaps, ranks possible actions by impact, and provides a concise next‑step recommendation.

## Use When
- You need to reflect on recent activities and identify areas for improvement.  
- You want to prioritize actions that will yield the highest impact on personal growth or project outcomes.  
- You are preparing a focused plan based on patterns in your own journal data.

## Instructions
1. **Collect Data**  
   - Retrieve the last N journal entries (default N = 10) from the user’s journal repository.  
   - Extract timestamps, titles, and full text for each entry.

2. **Parse Content**  
   - Use natural‑language processing to identify key topics, tasks, emotions, and outcomes in each entry.  
   - Tag each entry with identified themes (e.g., “communication”, “debugging”, “learning”, “stress”).

3. **Detect Recurring Themes**  
   - Count the frequency of each theme across the N entries.  
   - Highlight themes that appear in ≥ 30 % of the entries as **recurring**.

4. **Identify Skill Gaps**  
   - Compare recurring themes against the user’s known skill inventory (if available).  
   - Flag any recurring theme that lacks a corresponding skill or has a low proficiency rating as a **skill gap**.

5. **Generate Action Options**  
   - For each skill gap, propose 2‑3 concrete actions (e.g., “complete a tutorial on X”, “schedule a pair‑programming session”, “allocate 30 min daily for practice”).  
   - Include any high‑impact actions already hinted at in the journal (e.g., “prepare presentation for stakeholder meeting”).

6. **Rank Actions by Impact**  
   - Score each action on a 0‑100 scale using:  
     - **Relevance** to recurring theme (40 pts)  
     - **Potential improvement** to skill proficiency (30 pts)  
     - **Feasibility** given current workload (20 pts)  
     - **Alignment** with user’s stated goals (10 pts)  
   - Sort actions from highest to lowest total score.

7. **Craft Recommendation**  
   - Select the top‑ranked action.  
   - Summarize it in one concise sentence, including the expected benefit and a suggested time frame (e.g., “Spend 45 minutes this week completing the “Advanced Async Patterns” tutorial to close the async‑programming skill gap.”).

8. **Output**  
   - Return a markdown block containing:  
     - A brief list of recurring themes.  
     - Identified skill gaps.  
     - Ranked action table (Theme | Action | Impact Score).  
     - The concise next‑step recommendation.

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2