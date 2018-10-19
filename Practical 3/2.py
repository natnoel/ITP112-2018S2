class Pet:
    __name = ''
    __animal_type = ''
    __age = 0
    types = ['dog', 'cat']

    def __init__(self, name, type, age):
        self.__name = name
        self.__animal_type = type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_type(self, type):
        if type.lower() in self.types:
            self.__animal_type = type
            return True
        return False

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


pet = Pet('', '', 0)

name = input("Enter name: ")
pet.set_name(name)

type = input("Enter type: ")
if not pet.set_type(type):
    print("Invalid pet type", type)
    exit()

age = int(input("Enter age: "))
pet.set_age(age)

print(pet)