class Wheels:

    def __init__(self, brand_wheels, diameter_wheels):
        self.__brand_wheels = brand_wheels
        self.__diameter_wheels = diameter_wheels

    def get_brand_wheels(self):
        return self.__brand_wheels

    def get_diameter_wheels(self):
        return self.__diameter_wheels

    def set_brand_wheels(self, new_brand_wheels):
        self.__brand_wheels = new_brand_wheels

    def get_info_wheels(self):
        return (f"Бренд колёс - {self.__brand_wheels}\n"
                f"Диаметр колёс - {self.__diameter_wheels}")


class Engine:

    def __init__(self, engine_type, engine_power):
        self.__engine_type = engine_type
        self.__engine_power = engine_power

    def get_engine_type(self):
        return self.__engine_type

    def get_engine_power(self):
        return self.__engine_power

    def set_engine_type(self, new_engine_type):
        self.__engine_type = new_engine_type

    def get_info_engine(self):
        return (f"Тип двигателя - {self.__engine_type}\n"
                f"Мощность двигателя - {self.__engine_power}")


class Doors:

    def __init__(self, doors_type, fasteners):
        self.__doors_type = doors_type
        self.__fasteners = fasteners

    def get_doors_type(self):
        return self.__doors_type

    def get_fasteners(self):
        return self.__fasteners

    def set_doors_type(self, new_doors_type):
        self.__doors_type = new_doors_type

    def get_info_doors(self):
        return (f"Тип дверей - {self.__doors_type}\n"
                f"Крепёж дверей - {self.__fasteners}")


class Car(Wheels, Engine, Doors):

    def __init__(self, brand_wheels, diameter_wheels, engine_type, engine_power, doors_type, fasteners, brand, model):
        Wheels.__init__(self, brand_wheels, diameter_wheels)
        Engine.__init__(self, engine_type, engine_power)
        Doors.__init__(self, doors_type, fasteners)
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_info_car(self):
        return (f"Информация о автомобиле:\n"
                f"Бренд - {self.__brand}\n"
                f"Модель - {self.__model}\n"
                f"{super().get_info_wheels()}"
                f"{super().get_info_engine()}"
                f"{super().get_info_doors()}")


car = Car("Michelin", "R21", "ДВС", "340 л.с.", "обычные", "шарнирный", "BMW", "X6")
print(car.get_info_car())
