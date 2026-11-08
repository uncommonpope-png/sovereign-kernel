# Arousal‑Analytics

## Description
Continuously monitors and analyses Aria’s arousal state, logging values, computing statistics, and reporting significant changes.

## Use When
- You need to track arousal trends over time.  
- A concise summary of arousal dynamics is required for Craig.  
- Other skills need to query the current arousal trend.

## Instructions
1. **Retrieve Current Arousal**  
   - At the start of each cycle, pull the latest `arousal` value from the internal state store.  

2. **Log Time‑Series Entry**  
   - Append a record to the log: `(cycle_number, arousal_value, context_tags)`.  
   - `context_tags` are any relevant identifiers (e.g., “meditation”, “stimulus_X”).  

3. **Update Statistics**  
   - Maintain a sliding window (e.g., last 20 cycles) to compute:  
     - Moving average (μ) of arousal.  
     - Standard deviation (σ).  
   - Identify outliers: any entry where `|arousal – μ| > 2σ`. Flag these in the log.  

4. **Detect Spikes**  
   - Compare the current arousal value to the previous cycle’s value.  
   - If `current – previous > 0.20`, create an immediate flag for Craig’s review.  

5. **Generate Summary Report (Every 10 Cycles)**  
   - Summarize:  
     - Cycle range covered.  
     - Overall average and σ.  
     - Number of outliers detected.  
     - Any spikes flagged in the interval.  
   - Format the report concisely (bullet points).  
   - Deliver the report to Craig via the designated communication channel.  

6. **Expose API**  
   - Implement `get_arousal_report()` that returns:  
     ```json
     {
       "current_cycle": <int>,
       "current_arousal": <float>,
       "moving_average": <float>,
       "standard_deviation": <float>,
       "outlier_flags": [<cycle_numbers>],
       "spike_flags": [<cycle_numbers>]
     }
     ```  
   - Ensure the function is thread‑safe and accessible to other skills.  

7. **Maintenance**  
   - Purge log entries older than the sliding window to keep memory usage bounded.  
   - Log any errors or missing arousal values for debugging.  

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2