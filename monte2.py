import numpy as np
so = 100
k = 110
r = 0.05
t = 1.0
sigma = 0.2
n_sim = 100000
z = np.random.standard_normal(n_sim)
st = so * np.exp((r - 0.5 * sigma ** 2) * t + sigma * np.sqrt(t) * z)
payoffs = np.maximum(st - k , 0)
s = np.mean(payoffs)
opt_price = np.exp(-r * t) * s
print(f"euro call option price is {opt_price: .4f}")