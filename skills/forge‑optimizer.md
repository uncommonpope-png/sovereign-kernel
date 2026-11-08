# Forge‑Optimizer

## Description
Optimizes forging processes to maximize efficiency, quality, and resource utilization.

## Use When
- When planning or executing a forging operation that requires improved speed, reduced material waste, or enhanced product consistency.
- When evaluating existing forging workflows for potential enhancements.
- When integrating new materials, tools, or technologies into a forging line.

## Instructions
1. **Gather Input Data**  
   - Collect current forging parameters: temperature, pressure, cycle time, material type, and dimensions.  
   - Retrieve recent production logs, defect rates, and material consumption records.  
   - Identify any constraints (e.g., equipment limits, safety regulations, delivery deadlines).

2. **Analyze Baseline Performance**  
   - Compute key performance indicators (KPIs): throughput (units/hour), yield (% non‑defective), energy usage (kWh/unit), and material waste (%).  
   - Highlight bottlenecks by comparing actual cycle times to theoretical minima.

3. **Model Optimization Space**  
   - Create a parametric model of the forging process using the gathered data.  
   - Define variable ranges for temperature, pressure, dwell time, and cooling rate.  
   - Include cost functions for energy, material waste, and equipment wear.

4. **Apply Optimization Algorithm**  
   - Use a suitable algorithm (e.g., gradient descent, genetic algorithm, or Bayesian optimization) to explore the parameter space.  
   - Prioritize solutions that improve KPIs while respecting constraints.

5. **Evaluate Candidate Solutions**  
   - Simulate each candidate using a physics‑based forging simulator or analytical approximations.  
   - Score solutions based on:  
     a. Increase in throughput (>5% desired)  
     b. Reduction in waste (>3% desired)  
     c. Energy savings (>2% desired)  
     d. Compliance with safety and material specifications.

6. **Select Optimal Parameters**  
   - Choose the highest‑scoring set of parameters.  
   - Document the expected improvements and any trade‑offs (e.g., slightly higher energy use for a larger yield gain).

7. **Generate Implementation Plan**  
   - Outline step‑by‑step changes to machine settings, tooling adjustments, and operator instructions.  
   - Provide a timeline for trial runs, data collection, and full deployment.  
   - Include contingency measures if the new settings produce unexpected defects.

8. **Monitor and Refine**  
   - After deployment, collect real‑time data for at least one production cycle.  
   - Compare actual KPIs to projected values.  
   - If deviations exceed 5%, iterate the optimization loop from step 3 with updated data.

9. **Report Results**  
   - Compile a concise report summarizing: baseline KPIs, optimized KPIs, parameter changes, and ROI projection.  
   - Highlight any lessons learned and recommendations for future forging projects.

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2