

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