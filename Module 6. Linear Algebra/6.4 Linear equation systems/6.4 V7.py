import numpy as np

A = np.array([[1, 2, 5], [1, -1, 3], [3, -6, -1]])
B = np.array([-9, 2, 25])

x = np.linalg.solve(A, B)
print("Розв'язок за допомогою solve=", x)

Ainv = np.linalg.inv(A)
x = Ainv.dot(B)
print("Розв'язок за допомогою оберненої матриці=", x)

d = np.linalg.det(A)
B = np.array(B, dtype=A.dtype)
b = B[:None]  # вектор правої частини
b = np.reshape(B, (-1, 1))
A1 = np.hstack((b, A[:, 1:]))
d1 = np.linalg.det(A1)
A2 = np.hstack((A[:, 0:1], b, A[:, 2:3]))
d2 = np.linalg.det(A2)
A3 = np.hstack((A[:, 0:2], b))
d3 = np.linalg.det(A3)
print("Допоміжні матриці")
print('A1=\n', A1, '\nA2=\n', A2, '\nA3=\n', A3)
x = np.array([d1, d2, d3]) / d
print("Розв'язок методом Крамера=", x)
