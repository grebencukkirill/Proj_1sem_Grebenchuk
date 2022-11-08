

a = input('Введите число: ') #Ввод числа

while type(a) != int: #Обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели!')
        a = input('Введите число: ')
arr = []
for i in range()
