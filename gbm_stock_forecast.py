import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

ticker = "AAPL"
data = yf.download(ticker, period="1y")['Close']

log_returns = np.log(data / data.shift(1)).dropna()

days_to_forecast = 252  
num_simulations = 10000
last_price = data.iloc[-1].item()

mu = log_returns.mean().item()
sigma = log_returns.std().item()

Z = np.random.standard_normal((days_to_forecast, num_simulations))
daily_multipliers = np.exp((mu - 0.5 * sigma**2) + sigma * Z)
price_paths = last_price * daily_multipliers.cumprod(axis=0)

plt.figure(figsize=(12, 6))
plt.plot(price_paths[:, :100], color='blue', alpha=0.05)  # Plot first 100 paths
plt.axhline(last_price, color='red', linestyle='--', label=f'Current Price: ${last_price:.2f}')
plt.title(f"Geometric Brownian Motion: 10,000 Possible Futures for {ticker}")
plt.xlabel("Days into Future")
plt.ylabel("Price (USD)")
plt.legend()
plt.savefig("gbm_forecast.png" , dpi=300, bbox_inches="tight")
plt.show()

ending_prices = price_paths[-1, :]
print(f"--- {ticker} 1-Year Forecast (GBM) ---")
print(f"Average Expected Price: ${np.mean(ending_prices):.2f}")
print(f"95% Confidence Floor (Worst Case): ${np.percentile(ending_prices, 5):.2f}")
print(f"5% Upside Potential (Best Case): ${np.percentile(ending_prices, 95):.2f}")
