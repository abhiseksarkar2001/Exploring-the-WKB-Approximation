#WKB Approximation: Breaking the Quartic Code
import numpy as np
import matplotlib.pyplot as plt

# Define the potential function
def V(x):
    return 0.5 * x**4 - 0.25 * x**2

# Define the WKB energy levels function
def energy_levels(n):
    return 0.5 + n + np.sqrt(np.abs(0.25 + 2 * n - 4 * np.sqrt((n**2 - n + 0.0625))))

# Set the range of x values
x_min = -2
x_max = 2
x_vals = np.linspace(x_min, x_max, 1000)

# Calculate the classical turning points
x_turning_points = np.sqrt((2 * energy_levels(np.arange(1, 6)) - 0.5) / 2)  # assuming n=1 to 5

# Initialize the energy level plot
fig, ax = plt.subplots()

# Plot the potential function
ax.plot(x_vals, V(x_vals), color='black', label='Potential')

# Plot the WKB energy levels
for n in range(1, 6):
    x_start = -x_turning_points[n-1]
    x_end = x_turning_points[n-1]
    x_wkb = np.linspace(x_start, x_end, 100)
    E_wkb = energy_levels(n)
    k_wkb = np.sqrt(2 * (E_wkb - V(x_wkb)))
    #k_wkb = np.sqrt(np.maximum(2 * (E_wkb - V(x_wkb)), 0))
    y_wkb = k_wkb / np.pi
    ax.plot(x_wkb, y_wkb, label=f'n={n}')

# Set the axis labels and title
ax.set_xlabel('x')
ax.set_ylabel('Energy (WKB approximation)')
ax.set_title('WKB Energy Levels')

# Set the legend and show the plot
ax.legend()
plt.show()

'''
This code applies the WKB approximation to a quartic potential (0.5 * x^4 - 0.25 * x^2) and calculates the energy levels for n=1 to 5. It then generates a plot of the potential function and the WKB energy levels. The classical turning points are calculated using the energy levels, and the WKB energy levels are plotted using a formula that is specific to this potential:

E_n = 0.5 + n + sqrt(0.25 + 2n - 4sqrt(n^2 - n + 1/16))

The resulting plot should show the potential function and the WKB energy levels, with each energy level labeled according to its quantum number n. The energy levels should be approximately evenly spaced, with the spacing increasing as n increases. Note that the exact formula for the energy levels in this potential can be found using the supersymmetric quantum mechanics (SUSY QM) technique, which is related to the WKB approximation.
'''