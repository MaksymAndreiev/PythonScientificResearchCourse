import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify, diff, lambdify, solve

x, y = symbols('x y')
F = x ** 2 - 6 * x * y - 7 * y ** 2 + 10 * x - 30 * y + 23
Fx = simplify(diff(F, x))
Fy = simplify(diff(F, y))
Fim = lambdify((x, y), F, 'numpy')

xl = np.linspace(-10, 10, 71)
yl = np.linspace(-10, 5, 71)
X, Y = np.meshgrid(xl, yl)
Z = Fim(X, Y)
fig, ax = plt.subplots(1, 1)
ax.contourf(X, Y, Z, [Fim(1, 1), 0], colors='c', extend='min')
ax.contour(X, Y, Z, [0], colors='k', linewidths=4)

ax.axis('equal')
x0 = 2
yr = solve(F.subs(x, x0), y)
y0 = yr[0]  # вібір першої точки, якщо розв’язків кілька
print('y0=', y0)

ax.scatter(x0, y0, s=100, c='r')
Fx0 = Fx.subs([(x, x0), (y, y0)])
Fy0 = Fy.subs([(x, x0), (y, y0)])
eqt = Fx0 * (x - x0) + Fy0 * (y - y0)
eqn = Fx0 * (y - y0) - Fy0 * (x - x0)

Eqt = lambdify((x, y), eqt, 'numpy')
Eqn = lambdify((x, y), eqn, 'numpy')
Zt = Eqt(X, Y)
Zn = Eqn(X, Y)
ax.contour(X, Y, Zt, [0], colors='r',
           linewidths=2, linestyles='dashed')
ax.contour(X, Y, Zn, [0], colors='b',
           linewidths=2, linestyles='dashdot')

ax.axis('equal')
x0 = -4
yr = solve(F.subs(x, x0), y)
y0 = yr[0]  # вібір першої точки, якщо розв’язків кілька
print('y0=', y0)

ax.scatter(x0, y0, s=100, c='r')
Fx0 = Fx.subs([(x, x0), (y, y0)])
Fy0 = Fy.subs([(x, x0), (y, y0)])
eqt = Fx0 * (x - x0) + Fy0 * (y - y0)
eqn = Fx0 * (y - y0) - Fy0 * (x - x0)

Eqt = lambdify((x, y), eqt, 'numpy')
Eqn = lambdify((x, y), eqn, 'numpy')
Zt = Eqt(X, Y)
Zn = Eqn(X, Y)
ax.contour(X, Y, Zt, [0], colors='r',
           linewidths=2, linestyles='dashed')
ax.contour(X, Y, Zn, [0], colors='b',
           linewidths=2, linestyles='dashdot')

ax.axis('equal')
x0 = 2
yr = solve(F.subs(x, x0), y)
y0 = yr[1]  # вібір першої точки, якщо розв’язків кілька
print('y0=', y0)

ax.scatter(x0, y0, s=100, c='r')
Fx0 = Fx.subs([(x, x0), (y, y0)])
Fy0 = Fy.subs([(x, x0), (y, y0)])
eqt = Fx0 * (x - x0) + Fy0 * (y - y0)
eqn = Fx0 * (y - y0) - Fy0 * (x - x0)

Eqt = lambdify((x, y), eqt, 'numpy')
Eqn = lambdify((x, y), eqn, 'numpy')
Zt = Eqt(X, Y)
Zn = Eqn(X, Y)
ax.contour(X, Y, Zt, [0], colors='r',
           linewidths=2, linestyles='dashed')
ax.contour(X, Y, Zn, [0], colors='b',
           linewidths=2, linestyles='dashdot')

ax.axis('equal')
x0 = 5
yr = solve(F.subs(x, x0), y)
y0 = yr[0]  # вібір першої точки, якщо розв’язків кілька
print('y0=', y0)

ax.scatter(x0, y0, s=100, c='r')
Fx0 = Fx.subs([(x, x0), (y, y0)])
Fy0 = Fy.subs([(x, x0), (y, y0)])
eqt = Fx0 * (x - x0) + Fy0 * (y - y0)
eqn = Fx0 * (y - y0) - Fy0 * (x - x0)

Eqt = lambdify((x, y), eqt, 'numpy')
Eqn = lambdify((x, y), eqn, 'numpy')
Zt = Eqt(X, Y)
Zn = Eqn(X, Y)
ax.contour(X, Y, Zt, [0], colors='r',
           linewidths=2, linestyles='dashed')
ax.contour(X, Y, Zn, [0], colors='b',
           linewidths=2, linestyles='dashdot')

ax.axis('equal')
x0 = 5
yr = solve(F.subs(x, x0), y)
y0 = yr[1]  # вібір першої точки, якщо розв’язків кілька
print('y0=', y0)

ax.scatter(x0, y0, s=100, c='r')
Fx0 = Fx.subs([(x, x0), (y, y0)])
Fy0 = Fy.subs([(x, x0), (y, y0)])
eqt = Fx0 * (x - x0) + Fy0 * (y - y0)
eqn = Fx0 * (y - y0) - Fy0 * (x - x0)

Eqt = lambdify((x, y), eqt, 'numpy')
Eqn = lambdify((x, y), eqn, 'numpy')
Zt = Eqt(X, Y)
Zn = Eqn(X, Y)
ax.contour(X, Y, Zt, [0], colors='r',
           linewidths=2, linestyles='dashed')
ax.contour(X, Y, Zn, [0], colors='b',
           linewidths=2, linestyles='dashdot')
# plt.vlines(2, -10, 5, linestyle='--', color='r')
plt.show()
