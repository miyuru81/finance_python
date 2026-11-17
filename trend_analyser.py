import yfinance as yf
import matplotlib.pyplot as plt

ticker = "AAPL"
data = yf.download(ticker, period="2y")['Close']

data_50 = data.rolling(window=50).mean()
data_200 = data.rolling(window=200).mean()

plt.figure(figsize=(14, 7))
plt.plot(data, label='Actual Price', color='black', alpha=0.3) 
plt.plot(data_50, label='50-Day (Short Term)', color='blue', linewidth=2)
plt.plot(data_200, label='200-Day (Long Term)', color='red', linewidth=2)

plt.title(f"{ticker} Trend Analysis: The Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True, alpha=0.2)

plt.show()
