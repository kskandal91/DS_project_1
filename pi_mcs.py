import pandas as pd
import numpy as np

# Estimate PI() using Monte Carlo
n_mcs = 10**6
x = np.random.uniform(low=0.0, high=1.0, size=(2,n_mcs))

euc_dist = (x[0]**2 + x[1]**2)**0.5

print(f"Pi estimate: {4*(euc_dist<1).sum()/n_mcs} using {n_mcs} point simulations")


