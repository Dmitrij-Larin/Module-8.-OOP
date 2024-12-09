class Pet:

    def __init__(self, name, animal_type, sound, pet_type):
        self.__name = name
        self.__animal_type = animal_type
        self.__sound = sound
        self.__pet_type = pet_type

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_sound(self):
        return self.__sound

    def get_pet_type(self):
        return self.__pet_type


class Dog(Pet):

    def __init__(self, name, animal_type, sound, pet_type):
        super().__init__(name, animal_type, sound, pet_type)


class Cat(Pet):

    def __init__(self, name, animal_type, sound, pet_type):
        super().__init__(name, animal_type, sound, pet_type)


class Parrot(Pet):

    def __init__(self, name, animal_type, sound, pet_type):
        super().__init__(name, animal_type, sound, pet_type)


class Hamster(Pet):

    def __init__(self, name, animal_type, sound, pet_type):
        super().__init__(name, animal_type, sound, pet_type)


animals = [Dog("Рекс", "Немецкая овчарка", "гав-гав", "Пёс"),
           Cat("Мурзик", "Сфинкс", "мяу-мяу", "Кот"),
           Parrot("Кеша", "Какаду", "чивик", "Попугай"),
           Hamster("Вася", "Джунгарик", "пи-пи-пи", "Хомяк")]

for animal in animals:
    print(
        f"{Pet.get_pet_type(animal)}.\nКличка - {Pet.get_name(animal)}.\nПорода - {Pet.get_animal_type(animal)}.\nИздаёт звук - {Pet.get_sound(animal)}.\n")
