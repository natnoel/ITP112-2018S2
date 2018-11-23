class Person:
    def __init__(self, nric, name):
        self.__nric = nric
        self.__name = name

    def get_nric(self):
        return self.__nric

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Name: {Person.get_name(self)} NRIC: {self.get_nric()}"
