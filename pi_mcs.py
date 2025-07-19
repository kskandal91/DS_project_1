import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def estimate_pi(n_points=10**4, seed=None, plot=True):
    """
    Estimate the value of Pi using the Monte Carlo method.
    Optionally visualize the simulation.
    Args:
        n_points (int): Number of random points to generate.
        seed (int or None): Random seed for reproducibility.
        plot (bool): Whether to show a plot of the simulation.
    Returns:
        float: Estimated value of Pi.
    """
    if seed is not None:
        np.random.seed(seed)
    # Generate random points in the unit square [-1, 1] x [-1, 1]
    x = np.random.uniform(-1, 1, n_points)
    y = np.random.uniform(-1, 1, n_points)
    # Points inside the unit circle
    inside = x**2 + y**2 < 1
    pi_estimate = 4 * np.sum(inside) / n_points
    print(f"Pi estimate: {pi_estimate} using {n_points} point simulations")
    if plot:
        plt.figure(figsize=(6,6))
        # Plot a random subset if too many points
        max_points = 20000
        if n_points > max_points:
            idx = np.random.choice(n_points, max_points, replace=False)
            x_plot, y_plot, inside_plot = x[idx], y[idx], inside[idx]
        else:
            x_plot, y_plot, inside_plot = x, y, inside
        plt.scatter(x_plot[inside_plot], y_plot[inside_plot], color='blue', s=0.5, label='Inside Circle')
        plt.scatter(x_plot[~inside_plot], y_plot[~inside_plot], color='red', s=0.5, label='Outside Circle')
        # Draw unit circle
        circle = Circle((0, 0), 1, color='green', fill=False, linewidth=2, label='Unit Circle')
        plt.gca().add_patch(circle)
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.legend(markerscale=6)
        plt.title('Monte Carlo Estimation of Pi')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
    return pi_estimate

if __name__ == "__main__":
    estimate_pi(n_points=10**5, seed=42, plot=True)



