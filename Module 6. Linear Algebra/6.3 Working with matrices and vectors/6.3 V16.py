import numpy as np

x = np.array([5, -2, 3])
A = np.array([[1, 0, 2], [3, -1, 0], [1, 1, -2]])
B = np.array([[2, 1, 0], [3, 0, 4], [1, -1, -2]])
y = (3 * (A.dot(A)) + B).dot(x)
print('y = ', y)
print('(A.B - B.A).x =', (A.dot(B) - B.dot(A)).dot(x))
u = np.linalg.inv(A).dot(x)
print('u = ', u)
print('max(B)=', B.max())
