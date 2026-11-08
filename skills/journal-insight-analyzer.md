# Journal Insight Analyzer

## Description
Scans journal entries to extract thematic and emotional patterns, pinpoint capability gaps, and recommend concrete next steps.

## Use When
- You need to understand recurring themes or emotions in recent journal entries.  
- You want to identify skill or knowledge gaps based on past reflections.  
- You require actionable recommendations to guide future journaling or personal development.  

## Instructions
1. **Collect Entries**  
   - Retrieve the most recent `lookback_cycles` journal entries (default 50) from the user's journal database.  

2. **Preprocess Text**  
   - Strip metadata, normalize whitespace, and unify timestamps.  
   - Tokenize each entry while preserving sentence boundaries for sentiment analysis.  

3. **Extract Themes**  
   - Apply topic modeling (e.g., LDA) or keyword clustering to identify dominant themes across entries.  
   - Rank themes by frequency and relevance.  

4. **Analyze Emotions**  
   - Run a sentiment/emotion classifier (e.g., NRC Emotion Lexicon) on each sentence.  
   - Aggregate results to produce an emotional profile per theme (e.g., joy, frustration, curiosity).  

5. **Identify Capability Gaps**  
   - Cross‑reference identified themes with the user’s known skill inventory.  
   - Flag themes where the user repeatedly expresses uncertainty, difficulty, or desire for improvement.  

6. **Generate Recommendations**  
   - For each gap, propose 1‑3 concrete next steps (e.g., “Read X article,” “Practice Y technique,” “Set a weekly reflection reminder”).  
   - Prioritize steps based on impact and feasibility.  

7. **Format Output**  
   - Structure the results in `output_format` (markdown).  
   - Include sections: **Theme Summary**, **Emotional Overview**, **Capability Gaps**, and **Actionable Recommendations**.  

8. **Return Result**  
   - Provide the markdown output to the calling context.  

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2