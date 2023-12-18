import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (6 * np.cbrt(6 * (x - 3) ** 2)) / (x ** 2 - 2 * x + 9)


x = np.linspace(-5, 5, 151)  # крива
y = f(x)
x1 = np.linspace(-5, 5, 15)  # ламана
y1 = f(x1)

plt.plot(x, y, 'y', x1, y1, 'mo-', linewidth=2)  # графіки функції і ламаної
plt.axhline(color='black', lw=1)  # відображення горизонтальної осі
plt.axvline(color='black', lw=1)  # відображення вертикальної осі
plt.show()
