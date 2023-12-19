import numpy as np

a = np.array([7, 9, -2])
b = np.array([5, 4, 3])
c1 = 4 * a - b
c2 = 4 * b - a

dc = c1 / c2
if dc[0] == dc[1] and dc[0] == dc[2]:
    print('Вектори c1 і c2 колінеарні')
else:
    print('Вектори c1 і c2 не колінеарні')
va = np.sqrt(a.dot(a))
vb = np.sqrt(b.dot(b))
print('|a|=', va, '|b|=', vb)
ab = np.dot(a, b) / va / vb
angle = np.arccos(ab)
print(angle * 180 / np.pi)  # переведення радіан в градуси
