# Создайте класс "Автомобиль", который содержит информацию о марке, модели и годе выпуска.
# Создайте класс "Грузовик", который наследуется от класса "Автомобиль" и содержит информацию о грузоподъемности.
# Создайте класс "Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит информацию о количестве пассажиров.


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class Truck(Car):
    def __init__(self, brand, model, year, cargo_capacity):
        super().__init__(brand, model, year)
        self.cargo_capacity = cargo_capacity

class PassengerCar(Car):
    def __init__(self, brand, model, year, passenger_capacity):
        super().__init__(brand, model, year)
        self.passenger_capacity = passenger_capacity

