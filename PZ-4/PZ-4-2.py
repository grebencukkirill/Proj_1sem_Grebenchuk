# Дано целое число N (>0).
# С помощью операций деления нацело и взятия отсатка от деления определить, имеются ли в записи числа цифра "2".
# Если имеется, то вывести TRUE, если нет - FALSE.
a = input('Введите число: ')

while type(a) != int: #Обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели!')
        a = input('Введите число: ')

while a > 0:
    b = a % 10
    a = a // 10
    if b == 2:
        print('TRUE')
        break
else:
    print('FALSE')