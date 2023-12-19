import matplotlib.pyplot as plt
import numpy as np

N = 100
x = np.linspace(-4, 4, N+1)
y = np.linspace(-4, 4, N+1)
[X, Y] = np.meshgrid(x, y)

x0 = -3.5; y0 = -1.7
x1 = -1.3; y1 = 2.0
x2 = 1.4; y2 = 1.9
x3 = -0.8; y3 = -1.8

Q1 = Y > y0 + (y3 - y0) / (x3 - x0) * (X - x0)
Q2 = Y < y0 + (y1 - y0) / (x1 - x0) * (X - x0)
Q3 = Y < y1 + (y2 - y1) / (x2 - x1) * (X - x1)
Q4 = Y > y3 + (y3 - y2) / (x3 - x2) * (X - x2)

Q = Q1 & Q2 & Q3 & Q4

B = np.zeros([N + 1, N + 1])
B[np.flipud(Q)] = 255

cc = 172
n = 3
B[0:n, :] = cc
B[-n:, :] = cc
B[:, :n] = cc
B[:, -n:] = cc

ext = [-5, 5, -5, 5]
plt.imshow(B, cmap='gray', extent=ext)
plt.show()