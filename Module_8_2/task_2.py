from task_1 import Teacher


class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title

    def get_discipline(self):
        return self.__discipline

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, new_job_title):
        self.__job_title = new_job_title

    def get_teacher_data(self):
        teacher_data = super().get_teacher_data()
        return f"{teacher_data}\nПредмет {self.__discipline}, должность {self.__job_title}"

    def add_mark(self, name_student, mark):
        add_mark_data = super().add_mark(name_student, mark)
        return f"{add_mark_data}\nПредмет: {self.__discipline}"

    def remove_mark(self, name_student, mark):
        remove_mark_data = super().remove_mark(name_student, mark)
        return f"{remove_mark_data}\nПредмет: {self.__discipline}"

    def give_a_consultation(self, grade):
        give_a_consultation_data = super().give_a_consultation(grade)
        return f"{give_a_consultation_data}\nПо предмету {self.__discipline} как {self.__job_title}"


discipline_teacher = DisciplineTeacher("Марья Ивановна", "РГУ", 22, "Литература", "Учитель литературы")
discipline_teacher.set_job_title("завуч")
print(discipline_teacher.get_teacher_data())
print()
print(discipline_teacher.add_mark("Максим Афанасьев", 4))
print()
print(discipline_teacher.remove_mark("Марина Ветрова", 3))
print()
print(discipline_teacher.give_a_consultation("10А"))
