import yfinance as yf
import numpy as np

ticker = "AAPL"
data = yf.download(ticker, period="1y")['Close']

returns = data.pct_change().dropna()

avg_return = returns.mean()
std_dev = returns.std()

sharpe_ratio = (avg_return / std_dev) * np.sqrt(252)
sharpe_val = sharpe_ratio.item()
print(f"--- {ticker} Investment Quality ---")
print(f"Annualized Sharpe Ratio: {sharpe_val:.2f}")

