# market_adaptive_strategy

## Description
Generates profit‑balanced trading actions by analyzing real‑time cryptocurrency price data and community sentiment from CoinGecko, Twitter, and Reddit, using moving‑average crossovers and sentiment scoring while adhering to PLT doctrine.

## Use When
- You need to decide entry, exit, or position‑size adjustments for crypto assets in a rapidly changing market.  
- Real‑time price trends and social‑media sentiment are required to align actions with profit, love (community well‑being), and tax (regulatory compliance) considerations.  
- You must produce a prioritized list of actions that respects the PLT affinity distribution.

## Instructions
1. **Gather Data**  
   a. Query CoinGecko’s public API for the target asset’s current price, 24‑hour high/low, and historical price series (e.g., 1‑hour candles for the past 200 periods).  
   b. Use the Twitter API (or a public search endpoint) to collect the most recent 500 tweets containing the asset’s ticker or name, filtering out retweets and non‑English content.  
   c. Scrape the top 100 Reddit posts/comments from relevant subreddits (r/CryptoCurrency, r/Bitcoin, etc.) mentioning the asset within the last 24 hours.

2. **Pre‑process**  
   a. Convert price data to a numeric time series aligned on hourly timestamps.  
   b. Clean tweet and Reddit text: remove URLs, emojis, and stop‑words; perform lemmatization.  

3. **Compute Technical Indicator**  
   a. Calculate the 20‑period Simple Moving Average (SMA20) and the 50‑period Simple Moving Average (SMA50) on the price series.  
   b. Identify crossover signals:  
      - **Bullish crossover**: SMA20 crosses above SMA50.  
      - **Bearish crossover**: SMA20 crosses below SMA50.  

4. **Assess Sentiment**  
   a. Apply a sentiment analyzer (e.g., VADER) to each tweet and Reddit comment.  
   b. Derive an aggregate sentiment score:  
      \[
      S = \frac{\sum_{i=1}^{N} sentiment_i}{N}
      \]  
      where \(N\) is the total number of messages.  
   c. Classify sentiment: Positive (S > 0.05), Neutral (‑0.05 ≤ S ≤ 0.05), Negative (S < ‑0.05).

5. **Combine Signals**  
   a. Create a weighted confidence metric \(C\):  
      \[
      C = 0.6 \times \text{crossover\_signal} + 0.4 \times S
      \]  
      - Assign crossover\_signal = +1 for bullish, –1 for bearish, 0 for no clear crossover.  
   b. Clamp \(C\) to the range [‑1, 1].

6. **Derive Action Set**  
   Based on \(C\) and PLT affinity, propose actions ordered by priority:  
   - **Profit (0.5)**: Adjust position size or execute trade to capture expected price move.  
   - **Love (0.3)**: If sentiment is strongly positive, consider community‑supportive actions (e.g., share educational content, avoid manipulative spikes).  
   - **Tax (0.2)**: Ensure any trade complies with jurisdictional reporting thresholds and avoids excessive turnover that could trigger unfavorable tax treatment.  

   Example actions:  
   1. **Buy** X units (if \(C > 0.4\) and profit‑impact outweighs tax cost).  
   2. **Sell** Y units (if \(C < -0.4\)).  
   3. **Hold / Reduce exposure** (if \(|C| ≤ 0.2\)).  
   4. **Publish a balanced market commentary** (if sentiment ≥ 0.1 and love priority applies).  
   5. **Log transaction for tax reporting** (always include).

7. **Output Format**  
   Return a JSON‑compatible list ordered by priority, each entry containing:  
   ```json
   {
     "action": "buy|sell|hold|commentary|tax_log",
     "asset": "<ticker>",
     "quantity": "<numeric or null>",
     "reason": "Combined signal C=..., SMA crossover, sentiment S=...",
     "plt_weight": {"profit":0.5,"love":0.3,"tax":0.2}
   }
   ```

8. **Safety Checks**  
   - Verify that the proposed trade does not exceed predefined risk limits (e.g., max