import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz


def f(x):
    return (4 - 16 * x) * np.sin(4 * x)


x = np.linspace(-5, 1, num=421)
y = f(x)
C = 0
yint = cumtrapz(y, x, initial=None) + C
fig = plt.figure()
plt.plot(x[1:], yint, 'k-', linewidth=3, label='\u222Bf(x)dx')
plt.plot(x, y, 'r', linewidth=3, label='f(x)')

x0 = -4
i0 = np.where(x == x0)[0][0]
y0 = yint[i0]
k1 = (yint[i0 + 1] - yint[i0]) / (x[i0 + 1] - x[i0])
xd1 = np.linspace(-7, 0, num=121)
yd1 = yint[i0] + k1 * (xd1 - x[i0])
plt.plot(xd1, yd1, 'm--', linewidth=2)

k2 = f(x0)
xd1 = np.linspace(-5, -3, num=121)
yd1 = yint[i0] + k2 * (xd1 - x[i0])
plt.plot(xd1, yd1, 'm--', linewidth=2)

plt.legend(fontsize=12, loc='upper center')
plt.grid(True)
plt.show()
