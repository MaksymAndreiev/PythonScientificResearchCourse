import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad, nquad
from sympy import symbols, sqrt, integrate, pprint, sin, exp, lambdify, pi
import sympy as sym

x = symbols('x')
x0 = -4  # точка касания
y = (4 - 16 * x) * sin(4 * x)  # символьное уравнение кривой
y1 = y.diff(x)
y0 = y.subs(x, x0)
y10 = y1.subs(x, x0)  # значение производной в точке
func = lambdify(x, y, "numpy")  # уравнение кривой
tangent = lambdify(x, y0 + y10 * (x - x0), "numpy")  # уравнение касательной
dlt = 0.5  # полуширина (по оси x) отрезка касательной
Xt = np.linspace(x0 - dlt, x0 + dlt, 21)
