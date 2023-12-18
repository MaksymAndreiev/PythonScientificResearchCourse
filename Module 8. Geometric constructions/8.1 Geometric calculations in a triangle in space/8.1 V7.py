import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import warnings

A = np.array([-3, -7, -5])
B = np.array([0, -1, -2])
C = np.array([-2, 3, 0])
X, Y, Z = zip(A, B, C, A)
fig = plt.figure()
warnings.filterwarnings('ignore')  # не виводити попередження
ax = Axes3D(fig)
ax.plot(X, Y, Z, linewidth=4, c='k')
ax.azim, ax.elev = 45, 20  # азимут і кутова висота точки спостереження
AB = B - A
AC = C - A
BC = C - B
LAB, LAC, LBC = map(np.linalg.norm, [AB, AC, BC])
sL = 'Довжини сторін:\tAB={:.4f}\tAC={:.4f}\tBC={:.4f}'.format(LAB, LAC, LBC)
print(sL)
ax.set_xlim(-7, 3)
ax.set_ylim(-7, 3)
ax.set_zlim(-7, 3)


def anglegrad(a, b):  # кут між векторами a,b в градусах
    sp = np.dot(a, b)
    la = np.linalg.norm(a)
    lb = np.linalg.norm(b)
    alph = np.arccos(sp / la / lb) * 180 / np.pi
    return alph


aA, aB, aC = map(anglegrad, [AB, -AB, AC], [AC, BC, BC])
sA = 'Кути трикутника:\tAM={:.2f} \tB={:.2f} \tC={:.2f}'.format(aA, aB, aC)
print(sA)
S = np.linalg.norm(np.cross(AB, AC)) / 2
print('Площа трикутника \tS=%6.5f' % S)

x = np.dot(AB, AC) / (LAC ** 2)
AD = x * AC
D = A + AD
BD = D - B
LBD = np.linalg.norm(BD)
print('Висота BD = ', LBD)
xBD, yBD, zBD = zip(B, D)
ax.plot(xBD, yBD, zBD, linewidth=4, c='g')
ax.scatter([D[0]], [D[1]], [D[2]], s=100, c='r')
plt.show()
