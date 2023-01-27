# Составить генератор (yield), который выводит из строки только цифры.

def get_digits(text):
    yield from [i for i in text if i in '1234567890']
text = input('Введите набор символов: ')
digits = get_digits(text)
for i in digits:
    print(i, end=' ')