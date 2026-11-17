import yfinance as yf

total_cash = 10000
portfolio_split = {
    "AAPL": 0.50, 
    "GLD":  0.30,  
    "WMT":  0.20  }

print(f"--- Rebalancing Portfolio for ${total_cash:,} ---")

for ticker, weight in portfolio_split.items():
    stock = yf.Ticker(ticker)
    current_price = stock.history(period="1d")['Close'].iloc[-1]
    
    target_amount = total_cash * weight
    shares_to_buy = int(target_amount / current_price)
    
    print(f"{ticker}: Buy {shares_to_buy} shares at ${current_price:.2f} each")
