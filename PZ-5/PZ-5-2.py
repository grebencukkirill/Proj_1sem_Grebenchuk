

def TrianglePS(a):


for i in range(3):
    a = input('Введите число: ')

    while type(a) != int:  # Обработка исключений
        try:
            a = int(a)
        except ValueError:
            print('Неправильно ввели!')
            a = input('Введите число: ')

    print('Периметр: ', TrianglePS())