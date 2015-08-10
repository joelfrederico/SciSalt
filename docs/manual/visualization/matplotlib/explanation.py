#!/usr/bin/env python3
import scisalt.matplotlib as sm
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
mesh = np.meshgrid(x, y)
img = np.sin(mesh[0]) * np.cos(mesh[1])

fig, ax, im = sm.imshow(img)

fig.set_figwidth(10)

print('Width: {}'.format(fig.get_figwidth()))

plt.show()
