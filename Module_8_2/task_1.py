class Teacher:

    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, new_experience):
        self.__experience = new_experience

    def get_teacher_data(self):
        return f"{self.__name}, образование {self.__education}, опыт работы {self.__experience} год(-а)(лет)."

    def add_mark(self, name_student, mark):
        return f"{self.__name} поставила оценку {mark} ученику {name_student}"

    def remove_mark(self, name_student, mark):
        return f"{self.__name} удалила оценку {mark} ученику {name_student}"

    def give_a_consultation(self, grade):
        return f"{self.__name} провёла консультацию в классе {grade}"


teacher = Teacher("Марья Совельева", "РГУ", 21)
teacher.set_experience(22)
print(teacher.get_teacher_data())
print(teacher.add_mark("Илья Фролов", 5))
print(teacher.remove_mark("Ирина Цветкова", 3))
print(teacher.give_a_consultation("8В"))
print()


