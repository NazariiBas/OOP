class Car:
    def __init__(self, brand="Unknown", model="Unknown", year=0, mileage=0.0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    # Копіювальний конструктор
    @classmethod
    def copy(cls, other_car):
        return cls(other_car.brand, other_car.model, other_car.year, other_car.mileage)

    
    def get_info(self):
        return f"Марка: [{self.brand}], Модель: [{self.model}], Рік: [{self.year}], Пробіг: [{self.mileage} км]"

    # Деструктор
    def __del__(self):
        print(f"Автомобіль [{self.brand} {self.model}] видалено з пам’яті.")



# 1. Стандартний конструктор
car1 = Car()

# 2. Параметризований конструктор
car2 = Car("Toyota", "Corolla", 2015, 73500.5)

# 3. Копіювальний конструктор
car3 = Car.copy(car2)


print(car1.get_info())
print(car2.get_info())
print(car3.get_info())

# Видалення об'єктів (для виклику деструктора вручну)
del car1
del car2
del car3
