from matplotlib.colors import BoundaryNorm
import matplotlib.pyplot as plt
import matplotlib as mpl
fig = plt.figure(figsize=(3, 2))
ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.2])
cmap = mpl.colors.ListedColormap(['green', 'red'])
bounds = [0, 0.0001, 5]
norm = BoundaryNorm(boundaries=bounds, ncolors=2)
cb2 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap, norm=norm,
                                spacing='proportional',
                                orientation='horizontal')
cb2.set_label('0 of 5')
plt.show()
