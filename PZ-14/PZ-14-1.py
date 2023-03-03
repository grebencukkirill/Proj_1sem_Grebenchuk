# Из исходного текстового файла (hotline.txt) перенести в первый файл строки с корректными номерами телефонов (т. е. в номере должно быть 11 цифр, например, 86532547891),
# а во второй с некорректными номерами телефонов. Посчитать полученные строки в каждом файле.

import re

with open('hotline.txt') as file1:
    a = file1.readlines()
p = re.compile(r'[0-9]{11}')
incorrect = []
sum1 = 0
sum2 = 0
with open('correct.txt', 'w') as file1:
    for i in a:
        if p.search(i):
            file1.write(i)
            sum1 += 1
        else:
            incorrect.append(i)
            sum2 += 1
with open('incorrect.txt', 'w') as file1:
    for i in incorrect:
        file1.write(i)
print('Корректных номеров:', sum1)
print('Некорректных номеров:', sum2)