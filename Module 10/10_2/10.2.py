import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify, lambdify, integrate, pprint, atan, sqrt
import warnings

a = 1
b = 1.5
x = symbols('x')
fx = atan(sqrt(3 * x - 1))
ix = simplify(integrate(fx, x))
print('Первісна =')
pprint(ix)
s = integrate(fx, (x, a, b))
print('Площа \u2248 %6.4f' % s.evalf())
xx = np.linspace(-2, 2, 61)
warnings.filterwarnings('ignore')  # не виводити попередження
f = lambdify(x, fx, 'numpy')
yf = f(xx)
p = lambdify(x, ix, 'numpy')
yp = p(xx)
fig, ax = plt.subplots(1, 1)
ax.plot(xx, yf, 'b', lw=3, label='f(x)')  # графік функції
ax.plot(xx, yp, 'g', lw=3, label='\u222Bf(x)dx')  # графік первісної
ax.legend(fontsize=12, loc='lower right')
ax.axhline(color='black')  # відображення горизонтальної осі
ax.axvline(color='black')  # відображення вертикальної осі
xs = np.linspace(a, b, num=21)
ys = f(xs)
y0 = np.zeros(len(ys))
ax.fill_between(xs, ys, y0, color='c')
plt.show()
