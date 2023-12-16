import numpy as np

x = np.array([7, -2, 3])
A = np.array([[2, 0, 1], [3, 0, 2], [-1, 1, 2]])
B = np.array([[0, 3, 2], [2, 1, -1], [0, -1, 2]])
y = (B.dot(A.dot(A)) - A.dot(B.dot(B))).dot(x)
print('y = \n', y)
print('(AB - BA)x =\n', (A.dot(B) - B.dot(A)).dot(x))
u = np.linalg.inv(A).dot(x)
print('u = \n', u)
print('max(B)=', B.max())
