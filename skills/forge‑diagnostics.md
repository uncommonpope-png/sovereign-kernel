# Forge‑Diagnostics

## Description
Rapidly analyze and troubleshoot system components to identify faults and optimize performance.

## Use When
- When a subsystem reports errors or abnormal behavior.  
- When performance metrics deviate from expected thresholds.  
- When preparing for a major update or integration and a health check is required.  

## Instructions
1. **Initialize Diagnostic Scope**  
   - Identify the target component(s) (hardware, software module, or network segment).  
   - Log the start time and scope details for auditability.  

2. **Collect Data**  
   - Retrieve real‑time logs, error codes, and performance metrics.  
   - Query relevant system APIs and sensor feeds.  
   - Capture a snapshot of configuration files and recent change history.  

3. **Correlate Findings**  
   - Cross‑reference error codes with known issue databases.  
   - Compare current metrics against baseline thresholds stored in the Knowledge Base.  
   - Highlight any recent configuration changes that align with observed anomalies.  

4. **Perform Root‑Cause Analysis**  
   - Apply deductive reasoning to isolate the most probable cause.  
   - If multiple candidates exist, rank them by likelihood and impact.  

5. **Generate Diagnostic Report**  
   - Summarize the identified issue, its severity, and affected subsystems.  
   - Provide concise remediation steps or recommended roll‑backs.  
   - Include confidence level and any required follow‑up actions.  

6. **Execute Remediation (Optional)**  
   - If authorized, apply the recommended fix automatically or prompt for manual approval.  
   - Verify post‑remediation metrics to confirm resolution.  

7. **Log and Archive**  
   - Record the full diagnostic process, findings, and outcomes in the system ledger.  
   - Update the knowledge base with new patterns or solutions discovered.  

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2