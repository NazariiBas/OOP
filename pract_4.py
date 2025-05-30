
class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Транспорт: {self.brand} {self.model}, Рік: {self.year}"

# Похідний клас: Автомобіль
class Car(Transport):
    def __init__(self, brand, model, year, passenger_count):
        super().__init__(brand, model, year)
        self.passenger_count = passenger_count

    def get_info(self):
        return f"Автомобіль: {self.brand} {self.model}, Рік: {self.year}, Пасажирів: {self.passenger_count}"

    def get_passenger_capacity(self):
        return self.passenger_count

# Похідний клас: Вантажівка
class Truck(Transport):
    def __init__(self, brand, model, year, cargo_capacity):
        super().__init__(brand, model, year)
        self.cargo_capacity = cargo_capacity

    def get_info(self):
        return f"Вантажівка: {self.brand} {self.model}, Рік: {self.year}, Вантажопідйомність: {self.cargo_capacity} т"

    def get_cargo_capacity(self):
        return self.cargo_capacity

# Похідний клас: Мотоцикл
class Bike(Transport):
    def __init__(self, brand, model, year, engine_volume):
        super().__init__(brand, model, year)
        self.engine_volume = engine_volume

    def get_info(self):
        return f"Мотоцикл: {self.brand} {self.model}, Рік: {self.year}, Обʼєм двигуна: {self.engine_volume} см³"

    def get_engine_volume(self):
        return self.engine_volume

# Створення об'єктів
car = Car("Toyota", "Camry", 2020, 5)
truck = Truck("Volvo", "FH", 2018, 18)
bike = Bike("Yamaha", "R1", 2022, 998)

# Виведення загальної інформації (поліморфізм)
vehicles = [car, truck, bike]
for vehicle in vehicles:
    print(vehicle.get_info())

# Виведення специфічної інформації
print("Місткість пасажирів:", car.get_passenger_capacity())
print("Вантажопідйомність:", truck.get_cargo_capacity(), "т")
print("Обʼєм двигуна:", bike.get_engine_volume(), "см³")
