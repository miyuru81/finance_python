import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt 


tickers = ["AAPL", "XOM", "GLD", "WMT", "BTC-USD"]
data = yf.download(tickers, period="1y")['Close']

returns = data.pct_change().dropna()

corr_matrix = returns.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='RdYlGn', center=0)

plt.title("Portfolio Correlation Heatmap")
plt.show()
