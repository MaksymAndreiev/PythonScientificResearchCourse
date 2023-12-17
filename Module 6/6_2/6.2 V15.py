import numpy as np

A = np.array([[1, 1, 1], [2, 0, 1], [0, 1, 1]])
B = np.array([[1, 1, 3], [1, 0, 1], [2, 0, 1]])
M = 2 * A.dot(A) + 3 * A + 5 * np.eye(3)
print('M = \n', M)
A1 = np.linalg.inv(A)
print('Обернена AM=\n', A1)
dt = np.linalg.det(A)
print('Визначник=', dt)
print('AM+B=\n', A + B)
print('AM-B=\n', A - B)
print('AM.B=\n', A.dot(B))  # матричний добуток матриць
print('AM*B=\n', A * B)  # поелементний добуток матриць
print('AM.B-AM*B=\n', A.dot(B) - A * B)
X = A1.dot(B)  # Розв’язати матричне рівняння AX = B відносно матриці X
print('X=\n', np.around(X, 4))
