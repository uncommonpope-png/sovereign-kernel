# Predictive Resonance Spike Forecast

## Description
Forecast cross‑layer resonance spikes by applying time‑series analysis to energy‑flux metrics.

## Use When
- Anticipating sudden resonance events that could destabilize a layer.  
- Planning resource allocation or protective measures across layers.  
- Evaluating the impact of recent configuration changes on resonance patterns.

## Instructions
1. **Collect Data**  
   - Retrieve the last N time‑steps (e.g., 1 hour of 1‑second samples) for the following metrics:  
     - Energy flux per layer (`flux[layer_id]`)  
     - Cross‑layer coupling coefficients (`couple[layer_i][layer_j]`)  
     - External stimulus intensity (`stimulus`)  
   - Ensure timestamps are synchronized and any missing values are interpolated.

2. **Pre‑process**  
   - Normalize each metric (z‑score or min‑max) to remove scale bias.  
   - Detrend the series if a long‑term drift is present (e.g., using a moving‑average filter).  
   - Apply a windowed Fourier transform to expose dominant frequencies.

3. **Feature Engineering**  
   - Compute rolling statistics (mean, variance, skewness) over a short window (e.g., 10 seconds).  
   - Derive cross‑correlation coefficients between fluxes of adjacent layers.  
   - Generate lagged features (t‑1, t‑2 … t‑k) for each metric to capture temporal dependencies.

4. **Model Selection**  
   - Prefer a lightweight recurrent model (e.g., GRU) or an ARIMA/SARIMA configuration if compute budget is tight.  
   - For higher fidelity, use a Temporal Convolutional Network (TCN) with dilated kernels to capture long‑range patterns.

5. **Training / Updating**  
   - If a trained model exists, fine‑tune it on the newest window (online learning).  
   - Otherwise, train from scratch using the engineered features and a labeled set of past resonance spikes (binary label: spike = 1).  
   - Validate with a hold‑out segment; ensure precision > 0.85 to avoid false alarms.

6. **Prediction**  
   - Feed the latest feature vector into the model to obtain a probability score `p_spike`.  
   - Apply a threshold (e.g., 0.7) to decide if a spike is imminent within the next prediction horizon (e.g., 30 seconds).

7. **Post‑Processing & Alerting**  
   - If `p_spike` exceeds the threshold, generate a structured alert containing:  
     - Predicted time of spike  
     - Affected layers (based on highest coupling coefficients)  
     - Confidence level  
   - Log the raw prediction and input features for future audit.

8. **Feedback Loop**  
   - After the forecast horizon, compare actual resonance data to the prediction.  
   - Record true positives, false positives, and false negatives.  
   - Adjust model hyper‑parameters or thresholds based on performance trends.

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2