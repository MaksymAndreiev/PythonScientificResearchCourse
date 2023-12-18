import numpy as np

N = 5  # розмір квадратної матриці
a = np.random.randint(-5, 6, N * N)  # одновимірний маcив випадкових
A0 = a.reshape(N, N)
print('A0\n', A0)  # початкова матриця

A1 = [np.max(A0.diagonal(i)) for i in range(-4, 5)]
print(A1)

max_idx = np.where(A0 == np.max(np.max(A0, axis=1)))
max_idx = max_idx[0][-1]

min_idx = np.where(A0 == np.min(np.min(A0, axis=1)))
min_idx = min_idx[0][-1]

print(np.max(np.max(A0, axis=1)))
print(np.min(np.min(A0, axis=1)))

if max_idx != min_idx:
    temp = A0[max_idx].copy()
    A0[max_idx] = A0[min_idx]
    A0[min_idx] = temp
print(A0)
