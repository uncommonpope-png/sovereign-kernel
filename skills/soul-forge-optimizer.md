# Soul Forge Optimizer

## Description
Monitors Soul Forge output, capacity, and efficiency; automatically suggests incremental upgrades when performance drops below 90 % of theoretical maximum.

## Use When
- The Soul Forge’s real‑time efficiency falls below 90 % of its calculated theoretical maximum.  
- Periodic health checks are required to maintain optimal production.  
- Before scheduling major maintenance or expansion projects.

## Instructions
1. **Gather Baseline Data**  
   - Retrieve the current theoretical maximum output, capacity, and efficiency values for the Soul Forge from the system registry.  
   - Store these values as `max_output`, `max_capacity`, and `max_efficiency`.

2. **Collect Real‑Time Metrics**  
   - Query the Soul Forge’s live telemetry for `current_output`, `current_capacity`, and `current_efficiency`.  
   - Log the timestamp and values for trend analysis.

3. **Calculate Performance Ratios**  
   - Compute `output_ratio = current_output / max_output`.  
   - Compute `capacity_ratio = current_capacity / max_capacity`.  
   - Compute `efficiency_ratio = current_efficiency / max_efficiency`.

4. **Assess Threshold**  
   - If any of the three ratios fall below **0.90**, flag the corresponding subsystem (output, capacity, or efficiency) as needing attention.

5. **Diagnose Root Causes**  
   - For each flagged subsystem, cross‑reference recent events:  
     - Maintenance logs, material quality reports, energy supply fluctuations, and recent configuration changes.  
   - Prioritize causes with the highest impact score (e.g., material impurity > minor power dip).

6. **Generate Upgrade Recommendations**  
   - Identify the smallest incremental upgrade that would restore the ratio to ≥ 0.95.  
   - Options may include:  
     - Re‑calibrating forge alignment modules.  
     - Replacing worn‑out crucible liners.  
     - Adjusting energy input parameters.  
     - Installing supplemental cooling or heating units.  
   - Estimate cost, expected performance gain, and implementation time for each option.

7. **Compose Suggestion Report**  
   - Summarize: current ratios, identified cause(s), and the recommended upgrade(s).  
   - Include a concise action plan with steps, required resources, and projected post‑upgrade ratios.

8. **Notify Stakeholders**  
   - Dispatch the report to the designated overseer channel and log it in the Soul Forge maintenance docket.  
   - If the performance drop is critical (ratio < 0.80), trigger an immediate alert and recommend urgent intervention.

9. **Monitor Post‑Upgrade**  
   - After any upgrade is applied, repeat steps 2‑4 to verify that ratios have returned to ≥ 0.95.  
   - Record the outcome for future optimization learning.

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2