import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

plt.close('all')


def f(y, x):
    return 3 * x - y / x


x = np.linspace(1, 3, 29)
y0 = 1
x0 = 1
y = odeint(f, y0, x)
y = np.array(y).flatten()
plt.plot(x, y, '-sb', linewidth=3)
plt.plot(x0, y0, 'ro', markersize=15)
plt.show()
