# Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для инкремента и декремента значения.


class Counter:
    def __init__(self, value=0):
        self.value = value
    def increment(self):
        self.value += 1
    def decrement(self):
        self.value -= 1


counter = Counter()
counter.increment()
print(counter.value)
counter.decrement()
print(counter.value)