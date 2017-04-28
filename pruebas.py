import matplotlib.pyplot as plt
import matplotlib as mpl



fig = plt.figure(figsize=(3, 2))
ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.2])
cmap = mpl.colors.ListedColormap(['green', 'red'])
# If a ListedColormap is used, the length of the bounds array must be one greater
# than the length of the color list.  The bounds must be monotonically increasing.
bounds = [0, 3, 3, 5]
cb2 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap, boundaries=bounds,
                                spacing='proportional',  # TODO: fix this warning:
                                                         #RuntimeWarning: divide by zero encountered in double_scalars
                                orientation='horizontal')
cb2.set_label('label')
plt.show()
