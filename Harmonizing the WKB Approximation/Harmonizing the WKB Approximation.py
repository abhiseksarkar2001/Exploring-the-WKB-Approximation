#Harmonizing the WKB Approximation
import numpy as np
import matplotlib.pyplot as plt

# Define the potential function
def V(x):
    return 0.5 * x**2

# Define the WKB energy levels function
def energy_levels(n):
    return (n + 0.5) * np.pi

# Set the range of x values
x_min = -5
x_max = 5
x_vals = np.linspace(x_min, x_max, 1000)

# Calculate the classical turning points
x_turning_points = np.sqrt(2 * energy_levels(np.arange(1, 6)))  # assuming n=1 to 5

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
This code applies the WKB approximation to a harmonic oscillator potential (0.5 * x^2) and calculates the energy levels for n=1 to 5. It then generates a plot of the potential function and the WKB energy levels. The classical turning points are calculated using the energy levels, and the WKB energy levels are plotted using the WKB approximation formula:

$k = \sqrt{(2m(E-V(x)))}$ # wave number
$y(x) = k(x) / \pi$ # energy level

The resulting plot should show the potential function and the WKB energy levels, with each energy level labeled according to its quantum number n. The energy levels should be approximately evenly spaced, with the spacing increasing as n increases.
'''