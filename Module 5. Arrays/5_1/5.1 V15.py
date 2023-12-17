import numpy as np

N = 15
A = np.round(20 * (0.25 - np.random.rand(N)), 2)  # масив з N елементів від -5 до 5
print(A)

K = int(input('K = '))
L = int(input('L = '))
if K > L:
    K, L = L, K

A1 = A[K:L + 1]  # ділянка між K та L
A1.sort()  # сортуємо
A[K:L + 1] = A1

print(A)
print(
    f"Сума додатніх елементів масиву з номерами між K та L: {np.sum(np.where(A1 > 0, A1, 0))}")  # якщо елемнт
# масиву не більший за 0, він замінюється 0 та всі елементи сумуються
