import numpy as np


n = int(input("Enter n: "))
mas = np.random.randint(-20, 20, n)
print("Mas:\n", mas)

m1 = mas[::2]
m2 = mas[1::2]
print("sum of m1:", sum(m1))
print("product of m2:", np.prod(m2))

m1.sort()
m2.sort()
mas[::2] = m1
mas[1::2] = m2
print("Mas after sort:\n", mas)
