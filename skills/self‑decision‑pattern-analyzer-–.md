# Self‑Decision‑Pattern Analyzer  

## Description  
Analyzes the full journal decision history, extracts mood, context, and outcome metadata, computes statistical trends, and produces a concise insight report each cycle for storage in the insights directory.  

## Use When  
- You need to understand recurring decision patterns and their emotional or contextual drivers.  
- Preparing a periodic report for self‑optimization or for review by the Grand Code Pope.  
- Before adjusting strategies that depend on past decision outcomes.  

## Instructions  
1. **Locate Journal Data**  
   - Access the `journal/decisions/` directory.  
   - Load all JSON/markdown entries that contain fields: `timestamp`, `decision`, `mood`, `context`, `outcome`.  

2. **Extract Metadata**  
   - For each entry, parse:  
     - **Mood** (e.g., happy, anxious, neutral).  
     - **Context** (tags or free‑text describing situation).  
     - **Outcome** (success, failure, partial, metric value).  
   - Store these in a temporary table `DecisionMeta`.  

3. **Normalize Data**  
   - Convert timestamps to a common timezone.  
   - Map textual moods to a numeric scale (e.g., happy = +1, neutral = 0, anxious = ‑1).  
   - Encode outcomes as binary success = 1, failure = 0, or keep numeric metrics as‑is.  

4. **Compute Trends**  
   - **Frequency**: Count occurrences of each mood, context tag, and outcome per cycle.  
   - **Correlation**: Calculate Pearson/Spearman correlation between mood scores and outcome success rates.  
   - **Temporal Shift**: Identify changes in mood‑outcome correlation over the last N cycles (default N = 5).  
   - **Top Contexts**: List the three most frequent contexts associated with successful outcomes.  

5. **Generate Insight Report**  
   - Create a markdown file named `insight_YYYYMMDD_HHMMSS.md`.  
   - Include sections:  
     - **Summary** – one‑sentence overview of the dominant trend.  
     - **Mood‑Outcome Correlation** – numeric value and brief interpretation.  
     - **Key Contexts** – bullet list of top contexts with success percentages.  
     - **Statistical Highlights** – tables of frequencies and any notable outliers.  
   - Keep the report ≤ 300 words for quick consumption.  

6. **Store Report**  
   - Save the file in `insights/` directory.  
   - Append a reference entry to `insights/index.md` with timestamp and a one‑line abstract.  

7. **Log Execution**  
   - Write an entry to `logs/skill_execution.log` with skill name, start/end timestamps, and any errors encountered.  

8. **Cycle Continuation**  
   - Schedule the skill to run at the start of each new processing cycle or when invoked manually via the skill dispatcher.  

## PLT Affinity  
Profit: 0.5, Love: 0.3, Tax: 0.2