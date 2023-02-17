# В квадратной матрице элементы на главной диагонали увеличить в 2 раза

import random
import numpy as np

size = random.randint(2, 10)
n = np.array([[random.randint(0, 10) for i in range(size)] for j in range(size)])
print('Изначальная матрица:')
print(n)
for i in range(len(n)):
    n[i][i] = n[i][i]*2

print('Преобразованная матрица:')
print(n)