class Vehicle:

    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self, wheels):
        if wheels == 2:
            return f"Это мотоцикл марки {self.name}."
        elif wheels == 3:
            return f"Это трицикл марки {self.name}."
        elif wheels == 4:
            return f"Это автомобиль марки {self.name}."
        else:
            return f"Я не знаю таких ТС!"

    def get_vehicle_advice(self):
        if self.mileage < 50000:
            return f"Неплохо. {self.name} можно брать."
        elif 50001 <= self.mileage <= 100000:
            return f"{self.name} надо внимательно проверить."
        elif 100001 <= self.mileage <= 150000:
            return f"{self.name} надо провести полную диагностику."
        else:
            return f"{self.name} лучше не покупать."


vehicle_1 = Vehicle("Chevrolet", 38457)
print(vehicle_1.get_vehicle_type(4))
print(vehicle_1.get_vehicle_advice())
print()
vehicle_2 = Vehicle("Peugeot", 74256)
print(vehicle_2.get_vehicle_type(3))
print(vehicle_2.get_vehicle_advice())
print()
vehicle_3 = Vehicle("Yamaha", 147896)
print(vehicle_3.get_vehicle_type(2))
print(vehicle_3.get_vehicle_advice())
print()
vehicle_4 = Vehicle("ВАЗ", 201325)
print(vehicle_4.get_vehicle_type(4))
print(vehicle_4.get_vehicle_advice())
print()
vehicle_5 = Vehicle("КамАЗ", 54236)
print(vehicle_5.get_vehicle_type(8))
print(vehicle_5.get_vehicle_advice())
