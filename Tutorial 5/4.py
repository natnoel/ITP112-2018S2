class Beverage:
   def __init__(self, name, calories):
       self.__name = name
       self.__calories = calories
   def get_name(self):
       return self.__name
   def display_calories(self):
       print(self.__name, 'has calories', self.__calories)
   def __str__(self):
       return '{} has {} calories'.format(self.__name, self.__calories)

class Lemonade(Beverage):
   def __init__(self, price):
       super().__init__('Lemonade', 100)
       self.__price = price
       pass
   # add in the missing code here
   def __str__(self):
       return f"{super().__str__()} and cost {self.__price}"
       pass
   # add in the missing code here

drink = Lemonade(1.5)
drink.display_calories()
print(drink)
