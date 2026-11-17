import numpy as np
from math import log, sqrt, exp, erf
so = 100
k = 110
t = 1.0
r = 0.05
sigma = 0.2
def N(x):
    return 0.5 * (1 + erf(x/ sqrt(2)))
d1 = (log(so/k) + (r + 0.5 * sigma ** 2) * t) / (sigma * sqrt(t))
d2 = d1 - sigma * sqrt(t)
bsprice = so * N(d1) - k * exp(-r * t) * N(d2)
print(f"black sholes price : {bsprice: .6f}\n")
sim_counts = [1000, 10000, 100000, 1000000]
for n in sim_counts:
    z = np.random.standard_normal(n)
    st = so * np.exp((r - 0.5 * sigma ** 2) * t + sigma * np.sqrt(t) * z)
    payoffs = np.maximum(st - k, 0)
    mcprice = np.exp(-r * t) * np.mean(payoffs)
    error = abs(mcprice - bsprice)
    print(f" N={n: ,d} | " f"monte price={mcprice: .6f} | " f"error value= {error: .6f}")

