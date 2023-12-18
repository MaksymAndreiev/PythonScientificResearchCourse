import numpy as np

N = 5
a = np.random.randint(-10, 10, N * N)
A0 = a.reshape(N, N)
print("A0=\n", A0)
A1 = A0.astype(float)
A2 = A1[1::2, ::]
print("A2=\n", A2)
means = np.mean(A2, 1)
print("average=\n", means)
A3 = A2[::, 0]
A3 = means
A2[::, 0] = A3
print("A2 after changes=\n", A2)
A1[1::2, ::] = A2
print("A1 after changes=\n", A1)

pos = np.array(np.where((A1 < 0).all(axis=0))).flatten()

if len(pos):
    print("pos:", pos)
    A1 = np.insert(A1, pos[0], 0, axis=1)
    print("A1 after insert column=\n", A1)


def uldiag(i, j):
    return np.logical_and(i < j, i < N - j - 1)


B = np.fromfunction(uldiag, np.shape(A1))
print(B)

A1[B] = 0
print("\nA1=\n", A1)
