class Pet:
    __name = ''
    __animal_type = ''
    __age = 0

    def __init__(self, name, type, age):
        self.__name = name
        self.__animal_type = type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_type(self, type):
        self.__animal_type = type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def __str__(self):
        return f"Pet {self.get_name()} is a {self.get_type()}, and it is {self.get_age()} years old"


name = input("Enter name: ")
type = input("Enter type: ")
age = int(input("Enter age: "))

pet = Pet(name, type, age)
print(pet)