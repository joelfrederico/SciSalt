#!/usr/bin/env python3
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

# Create data to plot
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a grid
gs = gridspec.GridSpec(1, 2)

# Create a figure
fig = plt.figure(figsize=(16, 6))

# Create axes
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])

# Plot data
ax1.plot(x, y1)
ax2.plot(x, y2)

# Rearrange figure to use all space
fig.tight_layout()

# Show figure
plt.show()
