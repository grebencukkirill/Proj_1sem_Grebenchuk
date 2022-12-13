# Дан список размера N.
# Найти номер его первого локального минимума (локальный минимум - это элемент, который меньше любого из своих соседей).

import random
a = input('Введите число: ') #Ввод числа

while type(a) != int: #Обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели!')
        a = input('Введите число: ')

nums = []
for i in range(a):
    nums.append(random.randint(0, 10))
print(*(nums))

i = 1

while i < a:
    if nums[i-1]>nums[i]<nums[i+1]:
        print('Первый локальный минимум: ', nums[i])
        break
    i += 1
else:
    print('Локальный минимум отсутствует')