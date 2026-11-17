import yfinance as yf
import numpy as np

tickers = ["AAPL", "MSFT", "GLD"]
data = yf.download(tickers, period="6mo")['Close']

returns = data.pct_change().dropna()

print("--- 6-Month Risk Analysis (Daily Volatility) ---")

for ticker in tickers:
    risk = np.std(returns[ticker]) * 100 
    print(f"{ticker} Daily Risk: {risk:.2f}%")

print("\nNote: Higher % means the stock is more volatile (riskier).")
