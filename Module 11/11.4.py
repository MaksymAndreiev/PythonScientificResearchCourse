import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad, nquad
from sympy import symbols, integrate, pprint

# Використання функції dblquad
f = lambda y, x: 4 / 5 * x * y + 9 / 11 * x ** 2 * y ** 2
g = lambda x: -np.sqrt(x)
h = lambda x: x ** 3
I1 = dblquad(f, 0, 1, g, h)
print("I1 ={:5.3}".format(I1[0]))

# Використання функції nquad
xbnd = lambda: [0, 1]
ybnd = lambda x: [g(x), h(x)]
I2 = nquad(f, [ybnd, xbnd])
print("I2 ={:5.3}".format(I2[0]))
xh = np.linspace(-1, 2, num=61)
xg = np.linspace(0, 2, num=41)
yg = g(xg)
yh = h(xh)

x, y = symbols('x y')
F = 4 / 5 * x * y + 9 / 11 * x ** 2 * y ** 2
f1 = integrate(F, x, y)

fig = plt.figure(facecolor='white')
plt.plot(xg, yg, 'k-', xh, yh, 'b-', linewidth=4)
xr = np.linspace(0, 1, num=21)
yrg = g(xr)
yrh = h(xr)
plt.fill_between(xr, yrg, yrh, color='c')
plt.grid(True)
plt.show()
