try:
    b_speed = int(input('Введите скорость лодки, V: ')) #ввод скорости лодки
    f_speed = int(input('Введите скорость течения, U (V>U): ')) #ввод скорости течения
    l_time = int(input('Введите время движения в озере, T1: ')) #ввод времени движения в озере
    r_time = int(input('Введите время движения в реке, T2: ')) #ввод времени движения по реке
    distance = ((b_speed*l_time)+((b_speed-f_speed)*r_time)) #расчет расстояния
    print('Расcтояние: ',distance) #вывод на экран результата
except ValueError: #проверка
    print('Ошибка')