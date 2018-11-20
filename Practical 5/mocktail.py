import beverage

class Mocktail(beverage.Beverage):
    def __str__(self):
        return f"{self.get_name()} at {beverage.Beverage.get_price(self)}"