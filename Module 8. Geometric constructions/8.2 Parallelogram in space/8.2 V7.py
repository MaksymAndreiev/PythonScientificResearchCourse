import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import warnings

plt.close('all')
A = np.array([-3, -7, -5])
B = np.array([0, -1, -1])
C = np.array([-5, 3, 0])
AB = B - A
AC = C - A
BC = C - B
D = A + (AB + AC)  # координати вершини D
BD = D - B
print('Координати точки D:\t%8.2f %8.2f %8.2f' % (D[0], D[1], D[2]))
nrm = np.cross(AB, AC)
S = np.linalg.norm(nrm)
print('Площа паралелограма \tS=%8.5f' % S)
fig = plt.figure()
warnings.filterwarnings('ignore')  # не виводити попередження
ax = Axes3D(fig)
X, Y, Z = zip(A, B, D, C, A)

ax.plot(X, Y, Z, linewidth=4, c='k')
ax.azim, ax.elev = 65, 30  # азимут і кутова висота точки спостереження
ax.scatter(X, Y, Z, s=100, c='r')
t = np.linspace(0, 1, 9)
p, q = np.meshgrid(t, t)
X = A[0] + p * AB[0] + q * AC[0]
Y = A[1] + p * AB[1] + q * AC[1]
Z = A[2] + p * AB[2] + q * AC[2]
ax.plot_surface(X, Y, Z, rstride=1, cstride=2, color='c', alpha=0.3)

E = A + AB + BD / 2
ax.scatter([E[0]], [E[1]], [E[2]], s=100, c='r')
xAE, yAE, zAE = zip(A, E)
ax.plot(xAE, yAE, zAE, linewidth=4, c='g')
xAE, yAE, zAE = zip(B, D)
ax.plot(xAE, yAE, zAE, linewidth=4, c='b')

ne = nrm / np.linalg.norm(nrm)  # одиничний вектор нормалі
ax.quiver(*E, *(2 * ne), linewidth=2, color='b',
          arrow_length_ratio=0.25)
ax.set_xlim(-8, 9)
ax.set_ylim(-8, 9)
ax.set_zlim(-8, 9)
plt.show()
