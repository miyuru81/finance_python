import yfinance as yf

ticker_symbol = "AAPL"
company = yf.Ticker(ticker_symbol)

print(f"--- Fetching Financials for {ticker_symbol} ---")


balance_sheet = company.balance_sheet


metrics = ["Total Debt", "Cash and Cash Equivalents", "Total Assets"]

summary = balance_sheet.reindex(metrics).dropna(how="all")

print(summary)

if "Total Debt" in summary.index:
    latest_debt = summary.loc["Total Debt"].iloc[0]
    print(f"\nLatest Total Debt: ${latest_debt/ 1e9:.2f} Billion")


