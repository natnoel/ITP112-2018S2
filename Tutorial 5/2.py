class Pet:
    def __init__(self, type, name):
        self.name = name
        self.type = type

    def make_sound(self):
        pass

    def move(self):
        print(self.name, 'moves')

    def sleep(self):
        print(self.name, 'sleeps')


class Dog(Pet):  # Specify Pet to inherit from
    def __init__(self, name):
        super().__init__('dog', name)  # No need to include self parameter

    def make_sound(self):
        print('woof')

    def move(self):
        print(self.name, 'runs')


dog = Dog('Spot')
dog.sleep()
dog.move()
