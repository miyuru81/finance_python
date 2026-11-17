import yfinance as yf

tickers = ["AAPL", "SPY"]
data = yf.download(tickers, period="2y")['Close']
returns = data.pct_change().dropna()


covariance = returns.cov().iloc[0, 1]
market_variance = returns['SPY'].var()

beta = covariance / market_variance

print(f"--- Apple (AAPL) Risk Profile ---")
print(f"Beta vs S&P 500: {beta:.2f}")

if beta > 1:
    print("Interpretation: AAPL is more volatile than the market (Aggressive).")
else:
    print("Interpretation: AAPL is less volatile than the market (Defensive).")
