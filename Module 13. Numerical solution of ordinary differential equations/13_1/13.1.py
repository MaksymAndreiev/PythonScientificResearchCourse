import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def f(y, x):
    return x ** 3 - 2 / x * y


x = np.linspace(1, 3, 29)  # вектор абсцис
y0 = -5 / 6  # початкове значення
x0 = 1
y = odeint(f, y0, x)  # розв'язання диференціального рівняння
y = np.array(y).flatten()  # перетворення масиву з стовпця в рядок
plt.plot(x, y, '-sb', linewidth=3)
plt.plot(x0, y0, 'ro', markersize=15)
plt.show()
