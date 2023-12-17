import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from sympy import symbols, simplify, lambdify, exp, sqrt, cos, sin

t0 = 0
t1 = 4 * np.pi
t = symbols('t')

xt = 6 * (cos(t) + t * sin(t))
yt = 6 * (sin(t) - t * cos(t))

fxt = simplify(xt.diff(t))
fyt = simplify(yt.diff(t))
fl = sqrt(fxt ** 2 + fyt ** 2)
Fl = lambdify(t, fl, 'numpy')

L = quad(Fl, t0, t1)[0]
print('Довжина = {:6.4f}'.format(L))
print('Очікуваний результат={:6.4f}'.format(48 * np.pi ** 2))

F = lambdify(t, yt, "numpy")
Fx = lambdify(t, xt, "numpy")
tc = np.linspace(-20, 25, 301)
yc = F(tc)
xc = Fx(tc)
fig = plt.figure()
plt.plot(xc, yc, 'k-', linewidth=3)
tsect = np.linspace(-10, 10, 201)
ysect = F(tsect)
xsect = Fx(tsect)
plt.plot(xsect, ysect, 'r-', linewidth=6)
plt.grid(True)
plt.show()
