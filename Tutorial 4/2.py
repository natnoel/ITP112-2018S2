class Mammal:
    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print('I am a', self.__species)

    def make_sound(self):
        print('Grrr')

class Dog(Mammal):
    def make_sound(self):
        print('woof')

class Cat(Mammal):
    def __init__(self):
        super().__init__('Cat')


pb = Mammal('Polar Bear')
pb.show_species()
pb.make_sound()

dog = Dog('Dog')
dog.show_species()
dog.make_sound()

cat = Cat()
cat.show_species()
cat.make_sound()