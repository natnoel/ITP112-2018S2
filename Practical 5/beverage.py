class Beverage:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.a = 'a'

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price