# Real‑time Market Monitor

## Description
Queries CoinGecko and Binance for selected cryptocurrency prices, checks change thresholds, logs alerts to SCRIBE, and optionally provides a concise trend summary.

## Use When
- You need up‑to‑date price information for specific cryptocurrencies.  
- A price movement crosses a predefined percentage threshold and an alert is required.  
- A brief summary of recent market trends is helpful for decision‑making.

## Instructions
1. **Receive Input**  
   - Identify the list of cryptocurrency symbols/tickers (e.g., BTC, ETH, BNB).  
   - Determine the price‑change threshold(s) (e.g., ±5% over 24 h).  
   - Note whether a trend summary is requested (`summary: true/false`).  

2. **Fetch Current Prices**  
   - Call the CoinGecko **/simple/price** endpoint for the requested symbols to obtain the latest USD price and 24 h change percent.  
   - For symbols unavailable on CoinGecko or for deeper order‑book data, call the Binance **/api/v3/ticker/price** and **/api/v3/ticker/24hr** endpoints.  

3. **Normalize Data**  
   - Consolidate results into a table: `symbol | price_usd | change_24h_%`.  
   - If a symbol appears in both APIs, prefer the most recent timestamp; otherwise, merge the data.  

4. **Evaluate Thresholds**  
   - For each symbol, compare `change_24h_%` to the configured threshold(s).  
   - Flag any symbol where `|change_24h_%| >= threshold`.  

5. **Log Alerts to SCRIBE**  
   - For each flagged symbol, create a log entry:  
     ```
     [Market Alert] {symbol}: {price_usd} USD ({change_24h_%}% 24h)
     Threshold: {threshold}% breached.
     ```  
   - Send the entry to the SCRIBE logging system using its standard API/endpoint.  

6. **Generate Optional Trend Summary** (if `summary: true`)  
   - Determine overall market direction: count of symbols with positive vs. negative change.  
   - Identify the top mover (largest absolute % change).  
   - Compose a concise paragraph (≤ 2 sentences), e.g.:  
     “Across the tracked assets, 4 rose while 2 fell. Bitcoin led the rally with a +7.3% move, pushing the portfolio’s average gain to 2.1%.”  

7. **Return Result**  
   - Provide a JSON object containing:  
     ```json
     {
       "prices": [
         {"symbol":"BTC","price_usd":12345.67,"change_24h_%":5.2},
         ...
       ],
       "alerts": ["BTC", "ETH"],          // symbols that breached thresholds
       "summary": "..."                   // present only if requested
     }
     ```  
   - Include any error messages if API calls fail, and retry once before reporting failure.  

8. **Error Handling**  
   - If an API request returns an error or times out, log the incident to SCRIBE with level *warning* and attempt a single retry after a 2‑second pause.  
   - If the symbol is unsupported by both APIs, note it in the response under an `"unsupported"` array.  

9. **Security & Rate Limits**  
   - Respect CoinGecko’s free‑tier rate limit (≤ 50 calls/min) and Binance’s limit (≤ 1200 weight/min).  
   - Cache results for 30 seconds per symbol to reduce redundant calls within rapid successive invocations.  

10. **Finalize**  
    - Ensure all logs are flushed to SCRIBE.  
    - Confirm the JSON payload is well‑formed before returning to the caller.  

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2