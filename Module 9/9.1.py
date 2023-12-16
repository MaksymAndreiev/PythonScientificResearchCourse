import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, solve, limit, oo
import warnings

x, y = symbols('x y')
f = (x ** 3 + 3 * x ** 2 - 2 * x - 2) / (2 - 3 * x ** 2)
# f = (x ** 3 + 3 * x ** 2 - 2 * x - 2) / (x ** 2 - 5 * x - 6)
a = limit(f / x, x, oo)
b = limit(f - a * x, x, oo)
fasm = a * x + b
print('Рівняння асимптоти: y=', fasm)

sols = solve(2 - 3 * x ** 2, x)
# sols = solve(x ** 2 - 5 * x - 6, x)
print('Корені знаменника:', sols)
print('Границя 1 =', limit(f, x, sols[0]))
print('Границя 2 =', limit(f, x, sols[1]))
sols[0] = float(sols[0])
sols[1] = float(sols[1])

F = lambdify(x, f, "numpy")
X = np.linspace(-2, 2, 101)
# print(F(-np.sqrt(6) / 3))
# warnings.filterwarnings('ignore')  # не виводити попередження
Y = F(X)
plt.plot(X, Y, 'b', linewidth=3)
Fasm = lambdify(x, fasm, "numpy")
Yasm = Fasm(X)
plt.plot(X, Yasm, linestyle='--', color='r')
x1 = -np.sqrt(6) / 3
plt.vlines(x1, -15, 15, linestyle='-', color='w', linewidth=5)
x2 = np.sqrt(6) / 3
plt.vlines(x2, -15, 15, linestyle='-', color='w', linewidth=5)
# kl = np.where(Y == np.inf)
# plt.vlines(X[kl], -6, 6, linestyle='--', color='r')
plt.vlines(sols[0], -10, 10, linestyle='--', color='r')
plt.vlines(sols[1], -10, 10, linestyle='--', color='r')
plt.axhline(color='k')  # відображення горизонтальної осі
plt.axvline(color='k')  # відображення вертикальної осі
plt.grid(True)
plt.show()
