class Parent:
    def __init__(self, id):
        self.__id = id

class Child(Parent):
    def __init__(self):
        Parent.__init__(self, 1)
        self.__own_attr = attr


c = Child()