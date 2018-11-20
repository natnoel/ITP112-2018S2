import mocktail as m

class Cocktail(m.Mocktail):
    def __init__(self, name, price, alcohol):
        super().__init__(name, price)
        self.__alcohol = alcohol

    def get_alcohol(self):
        return self.__alcohol

    def __str__(self):
        return f"{super().__str__()} with alcohol of {self.get_alcohol()}"
