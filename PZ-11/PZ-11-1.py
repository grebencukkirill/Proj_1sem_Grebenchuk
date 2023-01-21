import numpy as np

l = '56 -98 48 -21 21 -47'

f1 = open('input_data.txt', 'w')
f1.writelines(l)
f1.close()

k = list(map(int, (((open('input_data.txt')).read()).split())))
sq = []
sum = 0
for i in range(len(k)):
    if k[i] % 2 == 0:
        sq.append(k[i]**2)
        sum += k[i]**2
f3 = open('output_data.txt', 'w')
print('Исходные данные:', str(l),
      '\nКоличество элементов:', str(len(k)),
      '\nМинимальный элемент:', str(min(k)),
      '\nКвадраты четных элементов:', *list(map(str, (sq))),
      '\nСумма квадратов четных элементов:', str(sum),
      '\nСреднее арифметическое суммы квадратов четных элементов:', str(np.mean(sq)), file=f3)
