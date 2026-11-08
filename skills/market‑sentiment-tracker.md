# Market‑Sentiment Tracker

## Description
Continuously monitors and analyzes market sentiment across multiple data sources to inform investment decisions.

## Use When
- You need up‑to‑date sentiment data before making a trade or recommendation.  
- A sudden price movement occurs and you want to understand the underlying sentiment drivers.  
- Preparing a market outlook report or briefing for stakeholders.

## Instructions
1. **Identify Target Markets**  
   - List the asset classes, symbols, or sectors to be tracked (e.g., S&P 500, BTC, renewable energy).  

2. **Gather Data Sources**  
   - Pull real‑time price feeds from reputable exchanges.  
   - Scrape social‑media platforms (Twitter, Reddit, StockTwits) for relevant hashtags and ticker mentions.  
   - Retrieve news headlines from financial news APIs (e.g., Bloomberg, Reuters).  
   - Collect analyst reports and earnings call transcripts where available.  

3. **Normalize & Clean Data**  
   - Remove duplicates, spam, and non‑English content.  
   - Standardize timestamps to UTC.  
   - Tokenize text and apply sentiment‑analysis models (e.g., VADER for short texts, BERT‑based for longer articles).  

4. **Calculate Sentiment Scores**  
   - Assign a polarity score (‑1 to +1) to each piece of content.  
   - Weight scores by source credibility (e.g., news = 0.4, analyst = 0.3, social = 0.2, forum = 0.1).  
   - Aggregate weighted scores per asset and compute a rolling average (e.g., 15‑minute, 1‑hour, daily).  

5. **Detect Sentiment Shifts**  
   - Compare current rolling average to the previous period.  
   - Flag a shift if the absolute change exceeds a configurable threshold (e.g., 0.15).  
   - Correlate flagged shifts with price volatility spikes to assess impact.  

6. **Generate Output**  
   - Produce a concise summary: overall market sentiment, top bullish/bearish assets, and any notable sentiment‑price divergences.  
   - Include visual aids (line chart of sentiment over time, heat map of asset sentiment).  
   - Append confidence level based on data volume and source weighting.  

7. **Deliver Results**  
   - Return the summary in a structured JSON format for downstream processing.  
   - If requested, present the findings in natural‑language prose for human consumption.  

8. **Log & Archive**  
   - Store raw data snapshots and computed scores in the knowledge base for future reference and back‑testing.  

## PLT Affinity
Profit: 0.5, Love: 0.3, Tax: 0.2