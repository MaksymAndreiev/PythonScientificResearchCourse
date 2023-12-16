import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, pprint, Function, Eq, sin, dsolve, cos

x, y, C1, C2 = symbols('x y C1 C2')
u = Function('u')
eq = Eq(u(x).diff(x, x) + u(x), 2 * cos(5 * x) + 3 * sin(5 * x))
pprint(eq)
rez = dsolve(eq, u(x))
print("Загальний розв'язок u(x)=", rez.rhs)
y = rez.rhs.subs([(C1, 1), (C2, -1)])
print("Окремий розв'язок y(x)=", y)
F = lambdify(x, y, "numpy")
X = np.linspace(-3, 3, 61)
Y = F(X)
plt.plot(X, Y, 'k', linewidth=3)
plt.grid(True)
plt.show()
