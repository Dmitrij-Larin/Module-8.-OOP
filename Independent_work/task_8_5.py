from task_8_4 import Employer


class President(Employer):

    def __str__(self):
        return f"Президент: {self.get_name()} {self.get_last_name()}"

    def __int__(self):
        return f"Возраст: {self.get_age()}"


class Manager(Employer):

    def __str__(self):
        return f"Менеджер: {self.get_name()} {self.get_last_name()}"

    def __int__(self):
        return f"Возраст: {self.get_age()}"


class Worker(Employer):

    def __str__(self):
        return f"Рабочий: {self.get_name()} {self.get_last_name()}"

    def __int__(self):
        return f"Возраст: {self.get_age()}"


president = President("Анатолий", "Сергеев", 54)
manager = Manager("Оксана", "Орхипова", 29)
worker = Worker("Пётр", "Суслов", 31)

print()
print(president)
print(president.__int__())
print()

print(manager)
print(manager.__int__())
print()

print(worker)
print(worker.__int__())
