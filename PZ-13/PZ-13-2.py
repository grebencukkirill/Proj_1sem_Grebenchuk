# Из матрицы сформировать массив из положительных четных элементов, найти их сумму и среднее арифметическое.

import random
import numpy as np

size = random.randint(2, 10)
n = np.array([[random.randint(-10, 10) for i in range(size)] for j in range(size)])
print('Изначальная матрица:')
print(n)
res = []
for i in n:
    for j in i:
        if (j%2==0) and (j>0):
            res.append(j)

print('Положительные четные числа:', *res)
print('Сумма положительных четных чисел:', sum(res))
print('Среднее арифметическое положительных четных чисел:', sum(res)/len(res))