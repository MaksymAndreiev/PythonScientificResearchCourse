import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import symbols, simplify, diff, lambdify
import warnings

x, y = symbols('x y')
zf = x ** 2 + x * y + y ** 2 - x + 3 * y
zx = simplify(diff(zf, x))
zy = simplify(diff(zf, y))
print("dz/dx =", zx)
print("dz/dy =", zy)

x0 = -0.5
y0 = 0.7
z0 = zf.subs([(x, x0), (y, y0)])
print('Координати точки %5.2f %5.2f %5.2f' % (x0, y0, z0))

zx0 = zx.subs([(x, x0), (y, y0)])
zy0 = zy.subs([(x, x0), (y, y0)])
print("dz/dx(x0) =", zx0)
print("dz/dy(y0) =", zy0)

F = lambdify((x, y), zf, 'numpy')

xx = np.linspace(-1, 1, 21)
yy = np.linspace(-0.5, 1, 21)
X, Y = np.meshgrid(xx, yy)
Z = F(X, Y)
fig = plt.figure()
warnings.filterwarnings('ignore')  # не виводити попередження
ax = Axes3D(fig, xlim=(-2, 3), ylim=(-2, 3), zlim=(-1, 4))
ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, linewidth=1)

P = np.array([x0, y0, z0], dtype='float')
ax.plot3D(*P, c='r', marker='o', ms=10)

n = np.array([zx0, zy0, -1], dtype='float')
ax.quiver(*P, *(-1 * n), linewidth=2, color='r',
          arrow_length_ratio=0.25)

t = np.linspace(-1, 1, 21)
xc = t
yc = y0*np.ones(xc.shape)  # для площини y=y0 буде yc=y0*np.ones(tc.shape)
zc = F(xc, yc)
ax.plot(xc, yc, zc, linewidth=3, c='k')

nc = np.array([1, 0, zx0 + zy0 * 0], dtype='float')
ax.quiver(*P, *nc, linewidth=2, color='m', arrow_length_ratio=0.25)

t = np.linspace(-0.5, 1, 21)
yc = t
xc = x0*np.ones(yc.shape)
zc = F(xc, yc)
ax.plot(xc, yc, zc, linewidth=3, c='k')

nc = np.array([1, 1, zx0 + zy0 * 1], dtype='float')
ax.quiver(*P, *nc, linewidth=2, color='m', arrow_length_ratio=0.25, length=0.5)
plt.show()
