import random

l = '56 -98 48 -21 21 -47'

f1 = open('input_data.txt', 'w')
f1.writelines(l)
f1.close()


f2 = open('input_data.txt')
k = f2.read()
k.split()
sq = []
sum = 0
for i in range(len(k)):
    if k[i] == 0:
        sq.append(k[i]**2)
        sum += k[i]**2
print(k)
print('Исходные данные: ', l,'Количество элементов: ', len(k),'Минимальный элемент', min(k),'Квадраты четных элементов', *sq ,'Сумма квадратов четных элементов', sum ,'Среднее арифметическое суммы квадратов четных элементов')