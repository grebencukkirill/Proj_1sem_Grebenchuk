

a = input('Введите первый член A прогрессии: ') #Ввод числа
d = input('Введите разность D прогрессии: ') #Ввод числа
while type(a) != int: #Обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели!')
        a = input('Введите первый член A прогрессии: ')
while type(d) != int: #Обработка исключений
    try:
        d = int(d)
    except ValueError:
        print('Неправильно ввели!')
        d = input('Введите разность D прогрессии ')
c = []
for i in range(10):
    res = a + i*d
    c.append(res)
print(*c)