import yfinance as yf
import pandas as pd
import numpy as np
ticker = "AAPL"
df = yf.download(ticker, period="5y", auto_adjust=True, progress=False)
df["MA50"]= df["Close"].rolling(window=50).mean()
df["MA200"]= df["Close"].rolling(window=200).mean()
df["signal"]= 0
df.loc[df["MA50"]> df["MA200"], "signal"]= 1
df["trade"]= df["signal"].diff()
df["market_returns"]= df["Close"].pct_change()
df["strat_return"]= (df["signal"].shift(1)* df["market_returns"])
trans_cost = 0.001
df["cost"]= np.abs(df["trade"])* trans_cost
df["strat_return_after_cost"]= (df["strat_return"]- df["cost"])
initial_capital = 10000
df["portfolio"] = (1 + df["strat_return_after_cost"]).cumprod()* initial_capital
daily_returns= df["strat_return_after_cost"].dropna()
sharpe_ratio= (daily_returns.mean()/ daily_returns.std())* np.sqrt(252)
roll_max = df["portfolio"].cummax()
drawdown = (df["portfolio"] - roll_max)/ roll_max
max_drawdown = drawdown.min()
final_port_val = df["portfolio"].iloc[-1]
print(f"ticker: {ticker}")
print(f"final portfolio value: ${final_port_val:,.2f}")
print(f"sharpe ratio: {sharpe_ratio:.3f}")
print(f"maximum drawdown: {max_drawdown:.2%}")