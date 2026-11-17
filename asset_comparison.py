import yfinance as yf
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT"]
data = yf.download(tickers, period="1y")['Close']


cumulative_returns = data / data.iloc[0]

aapl_final = (cumulative_returns['AAPL'].iloc[-1] - 1) * 100
msft_final = (cumulative_returns['MSFT'].iloc[-1] - 1) * 100

print(f"--- 1-Year Performance ---")
print(f"Apple (AAPL): {aapl_final:.2f}%")
print(f"Microsoft (MSFT): {msft_final:.2f}%")

plt.figure(figsize=(10, 6))
plt.plot(cumulative_returns['AAPL'], label='Apple (AAPL)', color='#555555') 
plt.plot(cumulative_returns['MSFT'], label='Microsoft (MSFT)', color='#00a4ef') 

plt.title("Apple vs. Microsoft: 1-Year Cumulative Return")
plt.ylabel("Growth of $1 Investment")
plt.xlabel("Date")
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()
