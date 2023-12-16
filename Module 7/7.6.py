import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

plt.close('all')
N = 81
x = np.linspace(-4, 4, N)
X, Y = np.meshgrid(x, x)
Z = np.zeros((N, N))
# задання висоти поверхні по ділянкам
SQ = np.sqrt(X ** 2 + Y ** 2)
C1 = SQ < 2
F1 = 2 - SQ
Z[C1] = F1[C1]
C2 = SQ < 1
F2 = SQ
Z[C2] = F2[C2]
# створення графічного вікна вдвічі ширшим за висоту
fig = plt.figure(figsize=plt.figaspect(0.5))
# побудува графіка поверхні
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
surf = ax1.plot_surface(X, Y, Z, rstride=1, cstride=1,
                        antialiased=False, cmap='hsv')
ax1.set_zlim(-0.01, 2.01)
fig.colorbar(surf, shrink=0.5, aspect=10)
img = plt.imread('../Module 5/FigExample_5_3.png')
ax2 = fig.add_subplot(1, 2, 2)
ax2.imshow(img)

plt.show()
