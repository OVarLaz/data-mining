import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

n_lines = 120
x = np.linspace(0, 10, 10)
y = np.sin(x[:, None] + np.pi * np.linspace(0, 1, n_lines))
c = np.arange(1, n_lines + 1)

cmap = mpl.cm.get_cmap('winter', n_lines)
print cmap

print x,y,c

fig, ax = plt.subplots(dpi=100)
# Make dummie mappable
dummie_cax = ax.scatter(c, c, c=c, cmap=cmap)
print dummie_cax
# Clear axis
ax.cla()
for i, yi in enumerate(y.T):
    ax.plot(x, yi, c=cmap(i))
fig.colorbar(dummie_cax, ticks=c)
plt.show();