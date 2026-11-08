# Watchdog for PDP Resource Gaps

## Description
Monitors and alerts on potential gaps in PDP (Personal Development Plan) resources to ensure continuous support.

## Use When
- When the PDP system shows missing or insufficient resources for any user.
- When scheduled audits detect anomalies in resource allocation.
- When a user reports lack of access to required development materials.

## Instructions
1. **Initialize Monitoring**  
   - Access the PDP resource database and retrieve the latest resource allocation tables.  
   - Load the predefined resource completeness criteria (e.g., mandatory modules, recommended readings, tool access).

2. **Identify Gaps**  
   - Compare each user's assigned PDP against the completeness criteria.  
   - Flag any missing mandatory items, overdue renewals, or insufficient quantities (e.g., limited licenses).  
   - Log the gap details: user ID, missing resource, severity, and timestamp.

3. **Prioritize Alerts**  
   - Assign priority levels:  
     - **Critical** – mandatory resource missing, impacting compliance.  
     - **High** – recommended resource missing, affecting performance.  
     - **Medium** – optional resource unavailable, may affect growth.  
   - Sort flagged gaps by priority and timestamp.

4. **Generate Notification**  
   - Compose a concise alert message including: user ID, missing resource, priority, and suggested remediation steps.  
   - Route the alert to:  
     - The user’s PDP manager.  
     - The resource provisioning team.  
     - The central monitoring dashboard.

5. **Log and Archive**  
   - Record the alert in the PDP audit log with a unique identifier.  
   - Update the monitoring dashboard to reflect current gap status.

6. **Follow‑Up Verification**  
   - After 24 hours, re‑query the resource database for each flagged item.  
   - If the gap persists, resend the alert with escalated priority.  
   - If resolved, mark the alert as closed and note the resolution method.

7. **Report Summary**  
   - At the end of each monitoring cycle (e.g., daily), generate a summary report: total gaps detected, breakdown by priority, resolution rate, and any trends.  
   - Send the summary to senior PDP oversight and archive for compliance review.

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2