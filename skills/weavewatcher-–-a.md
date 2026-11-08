# WeaveWatcher

## Description
Continuously monitors the Soulverse “Weave” telemetry endpoint, extracts key events, logs them to `data/weave_events.json`, and raises PLT‑compliant alerts on threshold breaches.

## Use When
- You need real‑time visibility into new layer deployments, resource usage spikes, or emergent pattern signatures in the Soulverse.  
- Downstream analysis pipelines require a structured log of weave events.  
- Automated alerting is required when operational thresholds are exceeded.

## Instructions
1. **Initialize Configuration**  
   - Load or create a configuration file (e.g., `config/weave_watcher.yaml`).  
   - Parameters:  
     - `endpoint`: URL of the Weave telemetry API.  
     - `interval_seconds`: Monitoring interval (default `60`).  
     - `thresholds`:  
       - `cpu_spike_percent`: e.g., `80`  
       - `memory_spike_percent`: e.g., `75`  
       - `deployment_rate_per_min`: e.g., `5`  
   - Validate that `data/` directory exists; create it if missing.

2. **Start Monitoring Loop**  
   - Begin an infinite loop that sleeps for `interval_seconds` between iterations.  
   - On each iteration, perform steps 3‑6.

3. **Fetch Telemetry Data**  
   - Issue an HTTP GET request to `endpoint`.  
   - Handle network errors with exponential back‑off (max 5 retries).  
   - Parse the JSON response; ensure it contains fields for `layers`, `resource_usage`, and `patterns`.

4. **Extract Relevant Events**  
   - **New Layer Deployments**: Detect any layer IDs not present in the previous iteration. Record `{timestamp, layer_id, version, author}`.  
   - **Resource Usage Spikes**: Compare current CPU/memory percentages against previous values. If `cpu > thresholds.cpu_spike_percent` or `memory > thresholds.memory_spike_percent`, create an event `{timestamp, type: "resource_spike", cpu, memory}`.  
   - **Emergent Pattern Signatures**: Identify pattern entries whose `signature_score` exceeds a configurable `pattern_score_threshold` (default `0.9`). Record `{timestamp, pattern_id, score}`.

5. **Log Events**  
   - Append each extracted event as a separate JSON line to `data/weave_events.json`.  
   - Ensure file writes are atomic (write to a temp file then rename) to avoid corruption.

6. **Raise PLT‑Compliant Alerts**  
   - For any event that crosses a defined threshold, construct an alert payload:  
     ```json
     {
       "type": "WeaveWatcherAlert",
       "severity": "high" | "medium" | "low",
       "details": <event>,
       "timestamp": "<ISO8601>"
     }
     ```  
   - Dispatch the alert via the PLT alerting channel (e.g., `plt.alert(payload)`).  
   - Log the alert dispatch in `data/weave_alerts.log` with a timestamp.

7. **State Maintenance**  
   - Keep an in‑memory cache of the last known layer IDs and resource metrics to enable delta detection.  
   - Persist this cache periodically (e.g., every 5 minutes) to `data/weave_watcher_state.json` for recovery after restarts.

8. **Graceful Shutdown**  
   - Listen for termination signals (SIGINT/SIGTERM).  
   - Flush any pending events to disk, persist state, and exit cleanly.

9. **Testing & Validation**  
   - Run the skill in a sandbox environment with a mock telemetry endpoint.  
   - Verify that events are correctly logged and alerts are emitted when thresholds are intentionally breached.  
   - Check that `data/weave_events.json` remains a valid line‑delimited JSON file.

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2