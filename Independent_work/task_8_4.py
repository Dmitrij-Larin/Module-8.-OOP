class Employer:

    def __init__(self, name, last_name, age):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        
    def get_name(self):
        return self.__name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_age(self):
        return self.__age

    def print_info(self):
        print('This is Employer class')


class President(Employer):
    
    def __init__(self, name, last_name, age):
        super().__init__(name, last_name, age)

    def print_info(self):
        return f"Президент {self.get_name()} {self.get_last_name()}. Возраст: {self.get_age()} год(-а)(лет)"


class Manager(Employer):

    def __init__(self, name, last_name, age):
        super().__init__(name, last_name, age)

    def print_info(self):
        return f"Менеджер {self.get_name()} {self.get_last_name()}. Возраст: {self.get_age()} год(-а)(лет)"


class Worker(Employer):

    def __init__(self, name, last_name, age):
        super().__init__(name, last_name, age)

    def print_info(self):
        return f"Рабочий {self.get_name()} {self.get_last_name()}. Возраст: {self.get_age()} год(-а)(лет)"


president = President("Михаил", "Шишкин", 65)
manager = Manager("Василий", "Коробов", 34)
worker = Worker("Андрей", "Вишневский", 28)

print(president.print_info())
print(manager.print_info())
print(worker.print_info())
