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
i = 0
for num in nums:
    if i == len(nums)-1 and len(nums) != 1:
        if (num < nums[i - 1]) and (num < nums[0]):
            print('Первый локальный минимум: ', num)
            break
        print('Локальный минимум отсутствует')
        break
    else:
        print('Первый локальный минимум: ', nums[0])
        break
    if (num < nums[i-1]) and (num < nums[i+1]):
        print('Первый локальный минимум: ', num)
        break
    i += 1
else:
    print('Локальный минимум отсутствует')

