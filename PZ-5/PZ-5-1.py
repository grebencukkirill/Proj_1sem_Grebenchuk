#Составить функцию, которая выполнит сложение числового ряда

def count(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum
nums = (list(map(int, (input('Введите ряд чисел: ')).split())))

print('сумма: ', count(nums))
