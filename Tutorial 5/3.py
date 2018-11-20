class Food:
   def __init__(self, type):
       self.__type = type

# meat class
class Meat(Food):
   def __init__(self, name):
       Food.__init__(self, 'Meat')
       self.__name = name

   def calculate_calories(self):
       pass

# beef class
class Beef(Meat):
   def __init__(self, weight):
       super().__init__('Beef')
       self.__weight = weight

   def calculate_calories(self):
       return self.__weight * 1.5

meal = Beef(300)
print(meal.calculate_calories())
