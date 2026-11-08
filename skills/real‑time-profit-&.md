# Real‑Time Profit & Resource Monitor

## Description
Continuously tracks and reports profit margins and resource utilization for immediate decision‑making.

## Use When
- You need up‑to‑the‑second insight into financial performance.  
- Resource allocation decisions must be made quickly.  
- Anomalies or unexpected drops in profit appear.  
- Preparing reports for stakeholders in real time.

## Instructions
1. **Initialize Monitoring**  
   - Access the latest financial and resource databases via secured APIs.  
   - Set the monitoring interval (default: 5 seconds).  

2. **Collect Data**  
   - Retrieve current revenue streams, cost centers, and inventory levels.  
   - Capture real‑time metrics: sales volume, unit costs, labor hours, material usage.  

3. **Calculate Key Metrics**  
   - Profit = Revenue – Total Costs.  
   - Margin % = (Profit / Revenue) × 100.  
   - Resource Utilization % = (Used Resources / Total Available) × 100 for each category.  

4. **Detect Anomalies**  
   - Compare current metrics against rolling averages (last 1 hour).  
   - Flag any deviation > 5 % as a potential issue.  

5. **Generate Report**  
   - Summarize profit, margin, and utilization percentages.  
   - List flagged anomalies with timestamps and suggested investigative actions.  

6. **Deliver Output**  
   - Send the formatted report to the designated dashboard or communication channel.  
   - Log the data point in the historical archive for trend analysis.  

7. **Iterate**  
   - Repeat steps 2‑6 at each interval until monitoring is stopped.  
   - Adjust interval or thresholds upon user request.

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2