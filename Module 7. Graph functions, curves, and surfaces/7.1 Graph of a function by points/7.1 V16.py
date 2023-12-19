import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (6 * np.cbrt((x - 2) ** 2)) - 4 * x + 8


x = np.linspace(-10, 10, 300)  # крива
y = f(x)
x1 = np.linspace(-10, 10, 30)  # ламана
y1 = f(x1)
Z = np.vstack((x1, y1)).transpose()
print(Z)

plt.plot(x, y, 'r', x1, y1, 'bo-', linewidth=1)  # графіки функції і ламаної
plt.axhline(color='black', lw=1)  # відображення горизонтальної осі
plt.axvline(color='black', lw=1)  # відображення вертикальної осі
plt.show()
