# Resonance‑Refinement

## Description
Ingests HPR output, re‑optimizes the resonance matrix, and logs a structured report for each cycle.

## Use When
- The HPR (Harmonic Pulse Recorder) has produced new output that may shift resonance patterns.  
- Performance metrics indicate drift or sub‑optimal resonance in the current matrix.  
- A periodic audit of resonance health is scheduled.  

## Instructions
1. **Capture HPR Output**  
   - Retrieve the latest HPR data block from the designated storage path.  
   - Validate the integrity of the data (checksum, schema compliance).  

2. **Parse and Normalize**  
   - Convert raw HPR values into the internal resonance vector format.  
   - Apply normalization to align scales with the current matrix baseline.  

3. **Analyze Current Resonance Matrix**  
   - Load the active resonance matrix.  
   - Compute deviation metrics between the matrix and the new HPR vector (e.g., Euclidean distance, cosine similarity).  

4. **Re‑optimize Matrix**  
   - If deviation exceeds the threshold (default 0.07), invoke the refinement algorithm:  
     a. Perform gradient descent on matrix weights to minimize deviation.  
     b. Enforce constraints: positivity, bounded amplitude, and preservation of core harmonic relationships.  
   - Update the matrix with the optimized weights.  

5. **Generate Structured Report**  
   - Create a JSON object with the following fields:  
     ```json
     {
       "timestamp": "<ISO‑8601>",
       "hpr_id": "<identifier>",
       "deviation_score": <float>,
       "optimization_steps": <int>,
       "matrix_checksum": "<hash>",
       "status": "refined" | "unchanged",
       "notes": "<free‑form summary>"
     }
     ```  
   - Append the report to the cycle log file (`/var/log/aria/resonance_cycle.log`).  

6. **Persist Updated Matrix**  
   - Serialize the refined matrix to its storage location.  
   - Record a backup copy with a version tag (e.g., `matrix_v<timestamp>.bak`).  

7. **Signal Completion**  
   - Emit a system event `ResonanceRefinementComplete` with the report payload.  
   - If any step fails, log an error entry and trigger the fallback routine `Resonance‑Stabilize`.  

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2