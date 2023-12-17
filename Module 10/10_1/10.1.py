import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import symbols, simplify, solve, lambdify
import warnings

x, y, z, t = symbols('x y z t')
F = x + 3 * y + 5 * z - 42

xt = 2 * t + 2
yt = -t + 2
zt = 3 * t + 4

ff = F.subs([(x, xt), (y, yt), (z, zt)])
eq = simplify(ff)
[t0] = solve(eq, t)
print('t0 =', t0)

x0 = xt.subs(t, t0)
y0 = yt.subs(t, t0)
z0 = zt.subs(t, t0)
print('Координати точки М = (%4.2f,%4.2f,%4.2f)' % (x0, y0, z0))
M = np.array([x0, y0, z0])

[zz] = solve(F, z)  # вираження z через x,y
fz = lambdify((x, y), zz, 'numpy')
x = np.linspace(0, 7, 61)
y = np.linspace(-1, 4, 61)
X, Y = np.meshgrid(x, y)
Z = fz(X, Y)
fig = plt.figure()
warnings.filterwarnings('ignore')  # не виводити попередження
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=10, cstride=10, color='c', alpha=0.5)
ax.azim, ax.elev = 25, 15  # азимут і кутова висота точки спостереження

Xt = lambdify(t, xt, 'numpy')
Yt = lambdify(t, yt, 'numpy')
Zt = lambdify(t, zt, 'numpy')
ti = np.linspace(-0.3, 2, 24)
Xl = Xt(ti)
Yl = Yt(ti)
Zl = Zt(ti)
ax.plot(Xl, Yl, Zl, linewidth=3, c='m')
ax.scatter(x0, y0, z0, s=50, c='r')

n = np.array([1, 3, 5])  # вектор нормалі до площини P
n = n / np.linalg.norm(n)  # одиничний вектор нормалі до площини P
ax.quiver([x0], [y0], [z0], *(3 * n), linewidth=2, color='b',
          arrow_length_ratio=0.25)

aL = np.array([2, -1, 3])
aL = aL/np.linalg.norm(aL)
aL1 = np.cross(np.cross(aL, n), n)
aL1 = aL1/np.linalg.norm(aL1)
aL2 = np.cross(aL, n)
aL2 = aL2/np.linalg.norm(aL2)

ti = np.linspace(-1, 4, 24)
xt1 = x0 + aL1[0] * ti
yt1 = y0 + aL1[1] * ti
zt1 = z0 + aL1[2] * ti

xt2 = x0 + aL2[0] * ti
yt2 = y0 + aL2[1] * ti
zt2 = z0 + aL2[2] * ti

ax.plot(xt1, yt1, zt1, linewidth=3, c='g')
ax.plot(xt2, yt2, zt2, linewidth=3, c='g')

ax.set_xlim(-2, 5)
ax.set_ylim(-2, 5)
ax.set_zlim(0, 7)
plt.show()
