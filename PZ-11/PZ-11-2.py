# Из предложенного текстового файла (text18-3.txt) вывести на экран его
# содержимое, количество знаков пунктуации в первых четырех строках.
# Сформировать новый файл, в который поместить текст в стихотворной форме
# предварительно заменив символы третей строки их числовыми кодами.
f1 = open('text18-3.txt')
print(f1.read())
text = open('text18-3.txt').readlines()
f1.close()
sum = 0
digits = ''
stih = ''
for i in range(4):
    sum += text[i].count('.') + text[i].count(',') + text[i].count('!') + text[i].count('?') + text[i].count(':') + text[i].count(';')
for i in range(len(text[2])-2):
    digits += str(ord(text[2][i]))
    digits += ' '
f2 = open('stih.txt', 'w')
for i in range(len(text)):
    if i == 2:
        f2.write(digits + '\n')
        continue
    f2.write(text[i])
f2.close()
print('Количество знаков пунктуации в первых четырех строках: ', sum)