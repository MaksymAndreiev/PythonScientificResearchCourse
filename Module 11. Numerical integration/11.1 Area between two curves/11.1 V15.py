import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.integrate import quad

f1 = lambda x: x ** 2 - 2 * x - 3
f2 = lambda x: 3 * x ** 2 + x - 8
x = np.linspace(-3, 2, 31)
y1 = f1(x)
y2 = f2(x)
fig = plt.figure(facecolor='white')
plt.plot(x, y1, 'k-', x, y2, 'b-', linewidth=4)

f = lambda x: f2(x) - f1(x)
x1 = fsolve(f, -2.5)[0]
x2 = fsolve(f, 1.0)[0]
print('Точки перетину: {:6.3f} {:6.3f}'.format(x1, x2))

xf = np.linspace(x1, x2, 41)
yu = f2(xf)
yd = f1(xf)
plt.fill_between(xf, yu, yd, color='c')

s = quad(f, x2, x1)[0]
print('Площа між кривими={:6.4f}'.format(s))
print('Очікуваний результат={:6.4f}'.format(343/24))
plt.show()
