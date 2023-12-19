import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, pprint, Function, Eq, exp, sin, dsolve

plt.close('all')
x, y, C1, C2 = symbols('x y C1 C2')
u = Function('u')
eq = Eq(u(x).diff(x, x) + 2 * u(x).diff(x) + 5 * u(x), -17 * sin(2 * x))
pprint(eq)

rez = dsolve(eq, u(x))
print("Загальний розв'язок u(x)=", rez.rhs)

y = rez.rhs.subs([(C1, 1), (C2, -1)])
print("Окремий розв'язок y(x)=", y)

F = lambdify(x, y, "numpy")
X = np.linspace(-3, 1.1, 61)
Y = F(X)
plt.plot(X, Y, 'k', linewidth=3)
plt.grid(True)
plt.show()