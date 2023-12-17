import warnings
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = np.array([1, -1, 2])
B = np.array([2, 1, 2])
C = np.array([1, 1, 4])

fig = plt.figure()
warnings.filterwarnings('ignore')  # не виводити попередження
ax = Axes3D(fig)
X, Y, Z = zip(A, B, C)
ax.scatter(X, Y, Z, s=100, c='r')
ax.azim, ax.elev = 30, 20  # азимут і кутова висота точки спостереження

d = np.array([B - A, C - A])
detx = np.linalg.det(d[:, 1:])
dety = np.linalg.det(d[:, [0, 2]])
detz = np.linalg.det(d[:, 0:-1])

x = np.linspace(0, 3, 61)
y = np.linspace(-2, 3, 81)
X, Y = np.meshgrid(x, y)
Z = A[2] + 1 / detz * ((Y - A[1]) * dety - (X - A[0]) * detx)

ax.plot_surface(X, Y, Z, rstride=7, cstride=7, color='c', alpha=0.5)

xAB, yAB, zAB = zip(A, B)
ax.plot(xAB, yAB, zAB, linewidth=4, c='g')
xAC, yAC, zAC = zip(A, C)
ax.plot(xAC, yAC, zAC, linewidth=4, c='g')
xCB, yCB, zCB = zip(C, B)
ax.plot(xCB, yCB, zCB, linewidth=4, c='g')

Nrm = np.cross(B - A, C - A)  # вектор нормалі до площини
S = np.linalg.norm(Nrm) / 2  # площа трикутника
a = np.linalg.norm(C - B)  # довжина сторони протилежна A
aA = np.dot(A - B, A - C) * a ** 2 / 8 / S ** 2  # коефіцієнт 𝛼𝐴
b = np.linalg.norm(C - A)  # довжина сторони протилежна B
aB = np.dot(B - A, B - C) * b ** 2 / 8 / S ** 2  # коефіцієнт 𝛼𝐵
c = np.linalg.norm(B - A)  # довжина сторони протилежна C
aC = np.dot(C - A, C - B) * c ** 2 / 8 / S ** 2  # коефіцієнт 𝛼𝐶
O = (a * A + b * B + c * C) / (a + b + c)  # координати центра кола
print('Координати центра кола:\t%8.2f%8.2f%8.2f' % (O[0], O[1], O[2]))

ax.scatter(*O, s=80, c='b')  # зображення точки центра

s = (a + b + c) / 2
Rc = np.sqrt((np.abs(s - a) * np.abs(s - b) * np.abs(s - c)) / s)

ne = Nrm / np.linalg.norm(Nrm)  # одиничний вектор нормалі до площини
va = (A - O) / np.linalg.norm(A - O)  # одиничний вектор 𝒂
vb = np.cross(va, ne)  # одиничний вектор 𝒃
t = np.linspace(0, 2 * np.pi, 51)
xcircum, ycircum, zcircum = O[:, None] + Rc * va[:, None] * np.cos(t) + Rc * vb[:, None] * np.sin(t)
ax.plot(xcircum, ycircum, zcircum, linewidth=3, c='m')

ax.quiver(*O, *(-1 * ne), linewidth=2, color='b', arrow_length_ratio=0.25)
plt.show()
