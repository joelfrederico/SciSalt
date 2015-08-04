#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

# Create data to plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot data
plt.plot(x, y)

# Show figure
plt.show()
