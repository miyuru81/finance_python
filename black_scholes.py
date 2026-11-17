import numpy as np
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

stock_price = 230   
strike_price = 240   
time_to_expiry = 0.5 
risk_free_rate = 0.04 
volatility = 0.25   

price = black_scholes_call(stock_price, strike_price, time_to_expiry, risk_free_rate, volatility)

print(f"--- Black-Scholes Option Pricing ---")
print(f"Theoretical Call Option Price: ${price:.2f}")
