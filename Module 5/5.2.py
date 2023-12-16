import numpy as np

N = 5  # розмір квадратної матриці
A = np.random.randint(-N, N + 1, (N, N))  # матриця розміром 5х5 з елементами між -5 та 5 включно
print(A)
mul = np.prod(A, axis=0)  # додаток по стовпцям
print(mul)

pos = np.array(np.where((A > 0).all(axis=0))).flatten()  # масив індексів стовпців де всі елементи додатні

if len(pos):  # якщо є стовпці з додатніх чисел
    print(pos)
    A = np.insert(A, pos[0], 1, axis=1)  # вставити перед першим додатнім стовпцем стовпець з 1
    print(A)


def diag(i, j):  # повертає логічний масив елементів побічної діагоналі та тих, що нижче
    return np.greater_equal(i, N - 1 - j)


C = np.fromfunction(diag, np.shape(A))
print(C)
A[C] = 0  # обнульовуємо
print(A)
