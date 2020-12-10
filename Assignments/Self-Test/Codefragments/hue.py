import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import pi

xval = np.arange(0, 2*pi, 0.01)
yval = np.ones_like(xval)

colormap = plt.get_cmap('hsv')
norm = mpl.colors.Normalize(0.0, 2*pi)

ax = plt.subplot(1, 1, 1, polar=True)
ax.scatter(xval, yval, c=xval, s=300, cmap=colormap, norm=norm, linewidths=0)
ax.set_yticks([])
ax.set_xticks([0, pi/2, pi, 1.5*pi])

plt.savefig('hue.png')