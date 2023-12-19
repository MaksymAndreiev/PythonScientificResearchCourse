import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def f(y, t):
    y1, y2 = y
    return [y2, 4 * y2 - 29 * y1]


t = np.linspace(0, 1, 41)  # моменти часу
y0 = [4, 1]  # початкові значення
w = odeint(f, y0, t)  # розв’язуємо систему
y1 = w[:, 0]
y2 = w[:, 1]
fig = plt.figure(figsize=plt.figaspect(0.4))
ax1 = fig.add_subplot(121)
ax1.plot(t, y1, '-o', linewidth=2)
ax1.grid(True)
x = np.linspace(0, 0.2, 41)
x0 = t[0]
Yt = y0[0] + y0[1] * (x - x0)
plt.plot(x, Yt, 'r', linewidth=3)
ax2 = fig.add_subplot(122)
ax2.plot(y1, y2, '-o', linewidth=2)
ax2.grid(True)
