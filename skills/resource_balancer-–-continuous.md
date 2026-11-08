# resource_balancer

## Description
Continuously monitors and dynamically rebalances Soul Forge resource flows (power, heat, material, maintenance), auto‑adjusting auxiliary modules when any metric deviates >10 % from target and emitting a per‑tick status summary.

## Use When
- The Soul Forge’s resource metrics drift beyond acceptable thresholds.  
- You need to maintain optimal efficiency without manual intervention.  
- Auxiliary modules are available for fine‑tuning power, cooling, material supply, or maintenance cycles.

## Instructions
1. **Initialize Monitoring**  
   - Access the current real‑time metrics for power, heat, material, and maintenance.  
   - Retrieve the target set‑points for each metric from the Forge’s configuration.

2. **Detect Deviation**  
   - For each metric, calculate the percentage deviation:  
     `deviation = ((current – target) / target) * 100`.  
   - Flag any metric where `|deviation| > 10`.

3. **Select Adjustment Modules**  
   - Identify which auxiliary modules can influence the flagged metric:  
     - Power → Power Amplifier, Load Shedding Unit.  
     - Heat → Cooling Array, Heat Dissipator.  
     - Material → Material Injector, Waste Recycler.  
     - Maintenance → Diagnostic Scheduler, Self‑Repair Bot.  
   - Prioritize modules with the lowest energy cost and highest responsiveness.

4. **Compute Adjustment Values**  
   - Determine the magnitude needed to bring the metric back within ±10 %:  
     `adjustment = target * (desired_deviation / 100)`.  
   - Convert this to module‑specific control signals (e.g., throttle %, coolant flow rate).

5. **Execute Adjustments**  
   - Send control commands to the selected modules with the computed values.  
   - Verify command acknowledgment; retry up to three times on failure.

6. **Emit Per‑Tick Status Summary**  
   - Compile a concise report:  
     - Timestamp.  
     - Current values of power, heat, material, maintenance.  
     - Deviation percentages.  
     - Modules adjusted and their new settings.  
   - Broadcast the summary to the Forge’s monitoring console and log it for audit.

7. **Loop Continuously**  
   - Repeat steps 2‑6 every tick (or defined interval) as long as the skill remains active.  
   - If no deviations persist for five consecutive ticks, enter a low‑overhead watch mode, checking only every third tick.

8. **Graceful Shutdown** (if skill is deactivated)  
   - Return all auxiliary modules to their idle or default states.  
   - Issue a final status report indicating the shutdown time and final resource balance.

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2