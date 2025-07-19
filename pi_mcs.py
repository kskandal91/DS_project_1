import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Estimate PI() using Monte Carlo
n_mcs = 10**4
x = np.random.uniform(low=0.0, high=1.0, size=(2,n_mcs))

inside = (x[0]**2 + x[1]**2) < 1

print(f"Pi estimate: {4*inside.sum()/n_mcs} using {n_mcs} point simulations")

# Visualization
plt.figure(figsize=(6,6))
plt.scatter(x[0][inside], x[1][inside], color='blue', s=0.5, label='Inside Circle')
plt.scatter(x[0][~inside], x[1][~inside], color='red', s=0.5, label='Outside Circle')

# Draw unit circle
circle = plt.Circle((0, 0), 1, color='green', fill=False, linewidth=2, label='Unit Circle')
plt.gca().add_patch(circle)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend(markerscale=6)
plt.title('Monte Carlo Estimation of Pi')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



