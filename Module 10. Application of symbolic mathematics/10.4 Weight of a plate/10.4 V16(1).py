import matplotlib.pyplot as plt
from sympy import symbols, integrate, And, solve, plot_implicit

plt.close('All')

x, y = symbols('x y')
Fun = (x ** 2) / 4 + (y ** 2) / 25
plot_implicit(And(Fun < 1), depth=2)
fig = plt.gcf()
ax = fig.gca()
ax.axis('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

x0 = -2; x1 = 2
sols = solve(Fun - 1, y)
print(sols)
y0 = sols[0]
y1 = sols[1]
mu = x ** 4
m = integrate(mu, (y, y0, y1), (x, x0, x1))
print("Маса платівки=", m)