import numpy as np

x = np.array([-4, 2, 1])
A = np.array([[2, 1, 0], [3, 0, 4], [1, -1, 2]])
B = np.array([[0, 2, 3], [4, 1, 0], [2, -1, -2]])
y = (A.dot(A) + B.dot(B)).dot(x)
print('y = \n', y)
print('(AB - BA)x =\n', (A.dot(B) - B.dot(A)).dot(x))
u = np.linalg.inv(A).dot(x)
print('u = \n', u)
print('max(B)=', B.max())
