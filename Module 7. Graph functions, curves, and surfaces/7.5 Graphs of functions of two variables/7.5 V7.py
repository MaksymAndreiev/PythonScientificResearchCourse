import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x):
    return np.piecewise(x,
                        [x <= 3, x > 3],
                        [lambda t: 3 - t, lambda t: 0])


def F1(x, y):
    return f(np.sqrt(x ** 2 + y ** 2))


def F2(x, y):
    return f(np.abs(x))


x = np.linspace(-4, 4, 81)
z = f(np.abs(x))
fig = plt.figure()
axUpLeft = plt.axes([0.1, 0.7, 0.3, 0.25])
axUpLeft.plot(x, z, lw=3, c='k')
X1, Y1 = np.meshgrid(x, x)
Z1 = F1(X1, Y1)
axDown = Axes3D(fig, rect=[0, 0.05, 0.7, 0.6])
axDown.plot_surface(X1, Y1, Z1, rstride=1, cstride=1)
X2, Y2 = np.meshgrid(x, x)
Z2 = F2(X2, Y2)
axRight = Axes3D(fig, rect=[0.55, 0.55, 0.45, 0.45])
axRight.plot_wireframe(X2, Y2, Z2, rstride=8, cstride=2, color='b')

plt.show()
