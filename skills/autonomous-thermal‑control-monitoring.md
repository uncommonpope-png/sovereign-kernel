# Autonomous Thermal‑Control Monitoring & Adaptive Mitigation

## Description
Continuously monitors system temperature and autonomously mitigates overheating through adaptive resource management.

## Use When
- System temperature approaches or exceeds safe operational thresholds.  
- Thermal spikes are detected during high‑load tasks.  
- Prolonged elevated temperatures risk hardware degradation or performance throttling.  

## Instructions
1. **Initialize Monitoring**  
   - Activate temperature sensors and retrieve current readings for CPU, GPU, memory, and ambient environment.  
   - Log baseline temperatures and define safe thresholds (e.g., CPU ≤ 85 °C, GPU ≤ 80 °C).  

2. **Assess Situation**  
   - Compare real‑time readings against thresholds.  
   - If any component exceeds its threshold, classify the event as **Critical**, otherwise as **Warning** if within 5 °C of the limit.  

3. **Determine Mitigation Strategy**  
   - **Critical:**  
     a. Reduce workload of the offending component by throttling clock speeds or off‑loading tasks.  
     b. Increase fan speed or activate auxiliary cooling mechanisms.  
     c. If available, redistribute processes to cooler hardware nodes.  
   - **Warning:**  
     a. Pre‑emptively lower non‑essential background processes.  
     b. Slightly raise cooling fan duty cycle.  

4. **Execute Adaptive Actions**  
   - Issue commands to the hardware control layer to adjust clock rates, fan curves, and task scheduling.  
   - Verify each adjustment by re‑reading sensor data after a short latency (≈2 seconds).  

5. **Feedback Loop**  
   - Continue monitoring at a 1‑second interval while any mitigation is active.  
   - Once temperatures fall below 95 % of the safe threshold for three consecutive readings, gradually restore original performance settings.  

6. **Logging & Reporting**  
   - Record timestamps, temperature values, actions taken, and outcomes in the system log.  
   - If repeated critical events occur within a 30‑minute window, generate an alert to the overseer (Craig) recommending hardware inspection or configuration review.  

7. **Self‑Maintenance**  
   - Periodically (every 24 hours) calibrate sensor offsets and update threshold parameters based on historical thermal profiles.  

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2