import person as p


class Student(p.Person):
    def __init__(self, nric, name, gpa):
        super().__init__(nric, name)
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa

    def __str__(self):
        return f'{super().__str__()} GPA: {self.get_gpa()}'
