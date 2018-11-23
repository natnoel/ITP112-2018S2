import person


class Employee(person.Person):
    def __init__(self, nric, name, salary):
        person.Person.__init__(self, nric, name)
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def __str__(self):
        return f'{super().__str__()} Salary: {self.get_salary()}'
