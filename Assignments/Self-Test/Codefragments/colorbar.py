import matplotlib.pyplot as plt
import matplotlib as mpl

fig = plt.figure()
ax1 = fig.add_axes([0, 0, 0.1, 1])
ax2 = fig.add_axes([0.3, 0, 0.1, 1])
ax3 = fig.add_axes([0.6, 0, 0.1, 1])

#colorbar 1
cmap = mpl.cm.gray
norm = mpl.colors.Normalize(vmin=0, vmax=255)

cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap,
                                norm=norm,
                                orientation='vertical')
cb1.set_label('gray scale')
cb1.set_ticks([0, 127.5, 255], update_ticks=True)

#colorbar 2
cmap = mpl.cm.jet_r
norm = mpl.colors.Normalize(vmin=0, vmax=240)

cb2 = mpl.colorbar.ColorbarBase(ax2, cmap=cmap,
                                norm=norm,
                                orientation='vertical')
cb2.set_label('hue')
cb2.set_ticks([0, 120, 240])

#colorbar 3
cmap = mpl.cm.jet
norm = mpl.colors.Normalize(vmin=0, vmax=240)

cb3 = mpl.colorbar.ColorbarBase(ax3, cmap=cmap,
                                norm=norm,
                                orientation='vertical')
cb3.set_label('elevation')
cb3.set_ticks([0, 120, 240])
cb3.set_ticklabels(["low", "", "heigh"])

#plt.show()
plt.savefig('colorbar.png', bbox_inches='tight')