# Forge‑Progress Tracker

## Description
Aggregates Phase 4 telemetry, predicts milestone completion, and issues alerts on deviation.

## Use When
- Monitoring ongoing forge operations in Phase 4.  
- Need to forecast milestone dates based on current telemetry.  
- Detecting or preventing deviations from planned progress.  
- Providing stakeholders with timely alerts and status updates.

## Instructions
1. **Collect Telemetry**  
   - Access all Phase 4 data streams (temperature, pressure, energy consumption, material feed rates, error logs, etc.).  
   - Store the latest values in a structured dataset keyed by timestamp and sensor ID.

2. **Normalize & Validate**  
   - Convert raw readings to standard units.  
   - Flag any missing or out‑of‑range values; request retransmission if necessary.  

3. **Compute Progress Metrics**  
   - Calculate cumulative metrics required for each milestone (e.g., total material processed, energy budget used, cycle count).  
   - Compare current metrics against the milestone target values defined in the Forge Plan.

4. **Predict Completion Dates**  
   - Apply a rolling linear regression (or more advanced time‑series model if data volume permits) to each metric’s trend.  
   - Estimate the projected timestamp when each milestone will be reached.  
   - Record confidence intervals for each prediction.

5. **Detect Deviations**  
   - Define deviation thresholds (e.g., >5 % lag on time, >10 % variance on energy use).  
   - If any metric’s projected completion falls outside its threshold, mark it as a deviation.

6. **Generate Alerts**  
   - For each deviation, compose an alert containing:  
     - Milestone name  
     - Current metric value vs. target  
     - Predicted completion date and confidence interval  
     - Specific cause indicators (e.g., temperature drift, feed rate drop)  
   - Dispatch alerts to the designated channels (operator dashboard, email, Slack, etc.) with appropriate severity level.

7. **Update Stakeholder Report**  
   - Summarize overall Phase 4 status: on‑track milestones, at‑risk milestones, and predicted overall completion.  
   - Include visualizations (trend lines, confidence bands) if the output medium supports them.  
   - Log the report in the Forge Progress Archive.

8. **Iterate**  
   - Repeat steps 1‑7 on a configurable interval (e.g., every 5 minutes) or upon receipt of new telemetry bursts.  
   - Adjust prediction models dynamically as more data becomes available.

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2