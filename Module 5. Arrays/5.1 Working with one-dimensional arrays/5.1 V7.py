import numpy as np

N = 12
A = np.round(20 * (0.5 - np.random.random(N)), 2)
print(A)
min1 = min(A)
max1 = max(A)
print('Мінімальний елемент = %5.2f\nМаксимальний елемент = %f' % (min1, max1))
A1 = A[::2]
print(A1)
A2 = A[1::2]
print(A2)
A1 = np.append(A1, A2, axis=0)
print(A1)
