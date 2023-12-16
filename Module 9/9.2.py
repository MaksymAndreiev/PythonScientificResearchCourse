import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify, sqrt, diff, lambdify
import warnings

x, y = symbols('x y')
fx = (sqrt((1 + x ** 2) ** 3)) / (3 * x ** 3)
f1x = simplify(diff(fx, x))
f2x = simplify(diff(fx, x, x))
print("f'(x)=", f1x, '\nf"(x)=', f2x)
warnings.filterwarnings('ignore')  # не виводити попередження
F0 = lambdify(x, fx, "numpy")
F1 = lambdify(x, f1x, "numpy")
F2 = lambdify(x, f2x, "numpy")
X = np.linspace(0.5, 1, 41)
Y = F0(X)
X1 = np.linspace(0.5, 1, 41)
Y1 = F1(X1)
X2 = np.linspace(0.5, 1, 41)
Y2 = F2(X2)
fig, ax = plt.subplots(1, 1)
ax.plot(X, Y, 'b', linewidth=3, label='f(x)')
ax.plot(X1, Y1, 'r', linewidth=3, label="f'(x)")
ax.plot(X2, Y2, 'g', linewidth=3, label='f"(x)')
ax.legend(fontsize=12, loc='lower right')  # loc='upper center'
ax.grid(True)
x0 = 0.8
y0 = F0(x0)
ax.scatter(x0, y0, s=50, c='k')
k = F1(x0)
Xt = np.linspace(x0 - 1, x0 + 1, 21)
Yt = y0 + k * (Xt - x0)
ax.plot(Xt, Yt, '--k', linewidth=2)
plt.show()
