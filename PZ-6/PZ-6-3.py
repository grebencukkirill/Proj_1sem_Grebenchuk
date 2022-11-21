import random

a = input('Введите четное число: ')

while type(a) != int: #Обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели!')
        a = input('Введите число: ')
    if a % 2 != 0:
        print('Неправильно ввели!')
        a = input('Введите число: ')
list_1 = []
for i in range(a):
    list_1.append(random.randint(0, 10))

print(*(list_1))
i = 0

while i < len(list_1)-1:
    b = list_1[i]
    list_1[i] = list_1[i+1]
    list_1[i+1] = b
    i += 2
print(*(list_1))