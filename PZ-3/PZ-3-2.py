#Составить программу определяющую размер скидки в зависимости от потраченной суммы

a = input('Введите число: ') #Ввод числа

while type(a) != int: #Обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели!')
        a = input('Введите число: ')

if a < 500: #Проверка
    print('Скидка составит 2%') #Вывод если введенное число меньше 500
elif 500 <= a < 1000:
    print('Скидка составит 3%') #Вывод если введенное число больше или равно 500 и меньше 1000
elif 1000 <= a < 1500:
    print('Скидка составит 4%') #Вывод если введенное число больше или равно 1000 и меньше 1500
elif 1500 <= a < 2000:
    print('Скидка составит 5%') #Вывод если введенное число больше или равно 1500 и меньше 2000
else:
    print('Цена не соответствует условию') #Вывод если не соответствует ни одному из условий