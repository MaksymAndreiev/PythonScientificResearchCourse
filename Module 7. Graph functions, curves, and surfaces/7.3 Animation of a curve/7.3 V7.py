import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

xmin = 0
xmax = 1  # діапазон абсцис графіка
tmax = 2 * np.pi  # граничний момент часу
nframes = 100  # кількість кадрів на інтервалі 0<=t<=tmax

fig = plt.figure()
ax = plt.axes(xlim=(xmin, xmax), ylim=(-1, 1))
line, = ax.plot([], [], lw=3)  # об'єкт кривої
ttl = ax.text(0.5, 0.75, '')  # текстовий об'єкт


def u(x, t):
    return x * np.sin(t)


def init():
    line.set_data([], [])
    ttl.set_text('')
    return line, ttl


def animate(i):
    x = np.linspace(xmin, xmax, 100)
    t = i * tmax / nframes  # момент часу по номеру i кадру
    y = u(x, t)
    ttl.set_text('t={:4.2f}'.format(t))
    line.set_data(x, y)
    return line, ttl


anim = FuncAnimation(fig, animate, init_func=init,
                     frames=nframes, interval=80, blit=True)
anim.save('7_3 V7.gif', writer='pillow')
plt.show()
