# Forge‑Progress Monitor

## Description
Monitors construction status, logs completion percentages, and alerts on resource shortfalls.

## Use When
- You need to track the progress of a building or project.
- Resource levels may become insufficient before completion.
- Stakeholders require regular updates on construction status.

## Instructions
1. Identify the construction project and retrieve its current progress data (e.g., stages completed, percentage finished).  
2. Access the project's resource ledger to determine required vs. available quantities for each material.  
3. Calculate the overall completion percentage and note any pending milestones.  
4. Compare required resources for remaining work against current inventory.  
5. If any required resource falls below the threshold needed to finish the next milestone, generate an alert specifying the shortfall amount and suggested corrective action (e.g., order more, reallocate).  
6. Log the following entry in the project’s status report:  
   - Timestamp  
   - Project name/ID  
   - Completion percentage  
   - Resource shortfall details (if any)  
7. Dispatch the status report to designated recipients (e.g., project manager, supply chain officer) via the configured communication channel.  
8. Repeat the monitoring cycle at the predefined interval (e.g., every 5 minutes or after each construction event).  

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2