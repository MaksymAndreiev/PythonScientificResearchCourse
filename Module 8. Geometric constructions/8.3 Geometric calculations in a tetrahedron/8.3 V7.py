import warnings

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = np.array([5, 2, 0])
B = np.array([2, 5, 0])
C = np.array([1, 2, 4])
D = np.array([-1, 1, 1])
X, Y, Z = zip(A, B, C, A, D, B, C, D)

fig = plt.figure()
warnings.filterwarnings('ignore')  # не виводити попередження
ax = Axes3D(fig)
ax.plot(X, Y, Z, linewidth=4, c='k')
AB = B - A
AC = C - A
AD = D - A
BC = C - B
mp = np.array([AB, AC, AD])
V = np.abs(np.linalg.det(mp)) / 6

print('Об’єм тетраедра \tV=%8.5f' % V)
Nrm = np.cross(AB, AC)
S = np.linalg.norm(Nrm) / 2
print('Площа трикутника ABC\tS=%8.5f' % S)
h = 3 * V / S
print('Висота тетраедра \th=%8.5f' % h)

ax.azim, ax.elev = 80, 10  # азимут і кутова висота точки спостереження

M = A + AB + BC / 2
xAM, yAM, zAM = zip(A, M)
AM = M - A
E = A + AM * 2 / 3
AE = E - A
ax.scatter([E[0]], [E[1]], [E[2]], s=100, c='r')
xAE, yAE, zAE = zip(A, E)
ax.plot(xAE, yAE, zAE, linewidth=4, c='g')
DE = E - D
xDE, yDE, zDE = zip(D, E)
ax.plot(xDE, yDE, zDE, linewidth=4, c='g')
print(f'Координати точки перетину медіан: ', E)
plt.show()
