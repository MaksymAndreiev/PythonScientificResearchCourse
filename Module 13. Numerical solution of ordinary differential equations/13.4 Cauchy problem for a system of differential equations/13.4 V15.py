import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def f(y, t):
    y1, y2, y3, y4 = y
    return [y2, y1 - 4 * y3, y4, -y1 + y3]


t = np.linspace(0, 1, 21)
y0 = [2, -np.sqrt(3), 0, np.sqrt(3)/2]
[y1, y2, y3, y4] = odeint(f, y0, t, full_output=False).T

fig = plt.figure()
ax1 = fig.add_subplot(111)
a1, = ax1.plot(t, y1, 'b', linewidth=2)
a2, = ax1.plot(t[0:26], y3[0:26], 'r', linewidth=2)
ax1.legend([a1, a2], ['x(t)', 'y(t)'])
ax1.grid(True)
