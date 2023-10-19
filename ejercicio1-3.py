import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from scipy.stats import multivariate_normal

x = np.linspace(0, 5, 100, endpoint=False)
y = multivariate_normal.pdf(x, mean=2.5, cov=0.5);

fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.plot(x, y)
##plt.show()

x, y = np.mgrid[-5:5:.1, -5:5:.1]
pos = np.dstack((x, y))
rv = multivariate_normal([0.1, 0.5], [[3.0, 0.3], [0.75, 1.5]])
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.contourf(x, y, rv.pdf(pos))
##plt.show()

ax = plt.figure().add_subplot(projection='3d')
ax.plot_surface(
    x,
    y,
    rv.pdf(pos),
    edgecolor='royalblue',
    lw=0.5,
    rstride=8,
    cstride=8,
    alpha=0.4
)
ax.contour(x, y, rv.pdf(pos), zdir='z', offset=-.2, cmap='coolwarm')
ax.contour(x, y, rv.pdf(pos), zdir='x', offset=-5, cmap='coolwarm')
ax.contour(x, y, rv.pdf(pos), zdir='y', offset=5, cmap='coolwarm')

ax.set(
    xlim=(-5, 5),
    ylim=(-5, 5),
    zlim=(-0.2, 0.2),
    xlabel='X',
    ylabel='Y',
    zlabel='Z'
)
plt.show()