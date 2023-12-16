import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def f(y, t):
    y1, y2 = y
    return [y1 - y2 + 2 * np.sin(t), 2 * y1 - y2]


t = np.linspace(0, 4, 41)  # моменти часу
y0 = [-1, 2]
[y1, y2] = odeint(f, y0, t, full_output=False).T

fig = plt.figure(figsize=plt.figaspect(0.4))
ax1 = fig.add_subplot(121)
yy1, = ax1.plot(t, y1, 'b', linewidth=2)
yy2, = ax1.plot(t, y2, 'r', linewidth=2)
ax1.legend([yy1, yy2], ['x(t)', 'y(t)'], fontsize=12, loc='lower right')
ax1.grid(True)

ax2 = fig.add_subplot(122)
tr, = ax2.plot(y1, y2, 'k', linewidth=2)
ax2.legend([tr], ['Траєкторія'], fontsize=12, loc='lower right')
ax2.grid(True)
