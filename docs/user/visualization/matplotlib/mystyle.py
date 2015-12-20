#!/usr/bin/env python3
import scisalt.matplotlib as sm
import matplotlib.pyplot as plt
import numpy as np

# Create data to plot
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Set up figure with axes
fig, ax = sm.setup_axes(rows=1, cols=2, figsize=(16, 6))

# Plot data
ax[0, 0].plot(x, y1)
ax[0, 1].plot(x, y2)

fig.tight_layout()

plt.show()
