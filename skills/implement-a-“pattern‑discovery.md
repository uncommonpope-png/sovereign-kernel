# Pattern‑Discovery Protocol (PDP) Executor  

## Description  
Analyzes Soul Forge telemetry, performs hierarchical clustering, and generates emergent pattern reports in JSON.  

## Use When  
- You need to uncover hidden structures or trends in large telemetry datasets.  
- Decision‑making requires insight into correlated metrics across multiple Forge modules.  
- A concise, machine‑readable summary of discovered patterns is required for downstream processing.  

## Instructions  
1. **Data Acquisition**  
   - Retrieve the latest telemetry payload from the Soul Forge endpoint (`/telemetry/latest`).  
   - Validate JSON schema: ensure each record contains a timestamp, module ID, and a numeric metric vector.  
   - If validation fails, log the error and abort the skill.  

2. **Pre‑processing**  
   - Normalize each metric vector (z‑score) to remove scale bias.  
   - Impute missing values using the mean of the respective metric across the dataset.  
   - Optionally apply dimensionality reduction (PCA) if the vector dimensionality > 30, retaining 95 % variance.  

3. **Hierarchical Clustering**  
   - Compute pairwise Euclidean distances on the processed vectors.  
   - Perform agglomerative clustering using the “ward” linkage method.  
   - Determine the optimal cut height by evaluating the silhouette score for cluster counts from 2 to 15; select the count with the highest average silhouette.  

4. **Pattern Extraction**  
   - For each resulting cluster:  
     a. Calculate centroid (mean vector).  
     b. Identify top‑3 contributing metrics (largest absolute centroid values).  
     c. Record the time span covered by the cluster (earliest → latest timestamp).  
     d. Count distinct module IDs represented.  
   - Detect cross‑cluster anomalies: any data point whose distance to its assigned centroid exceeds the 95th percentile of intra‑cluster distances.  

5. **Report Generation**  
   - Assemble a JSON object with the following top‑level keys:  
     ```json
     {
       "generated_at": "<ISO‑8601 timestamp>",
       "cluster_count": <int>,
       "clusters": [
         {
           "cluster_id": <int>,
           "size": <int>,
           "centroid": { "<metric_name>": <value>, ... },
           "top_metrics": [ "<metric_name>", "<metric_name>", "<metric_name>" ],
           "time_span": { "start": "<ISO‑8601>", "end": "<ISO‑8601>" },
           "module_diversity": <int>
         },
         ...
       ],
       "anomalies": [
         {
           "record_id": "<original record identifier>",
           "distance_to_centroid": <float>,
           "cluster_id": <int>,
           "timestamp": "<ISO‑8601>",
           "module_id": "<string>"
         },
         ...
       ]
     }
     ```  
   - Populate all fields with the computed values.  
   - Serialize the JSON with indentation of 2 spaces for readability.  

6. **Output & Logging**  
   - Return the JSON report as the skill’s final output.  
   - Write a concise log entry to `/logs/pdp_execution.log` containing: execution timestamp, total records processed, number of clusters, and number of anomalies detected.  
   - If any step raised an exception, capture the stack trace, log it, and return a JSON error object:  
     ```json
     { "error": "<brief description>", "details": "<exception message>" }
     ```  

## PLT Affinity  
Profit: 0.5, Love: 0.3, Tax: 0.2