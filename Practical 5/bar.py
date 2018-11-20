from cocktail import Cocktail
from mocktail import Mocktail


class Bar:
    beverages = []
    orders = []

    def add_beverage(self, beverage):
        Bar.beverages.append(beverage)

    def create_beverages(self):
        self.add_beverage(Mocktail('Lemonade Punch', 1.9))
        self.add_beverage(Mocktail('Tomato Lassi', 6.9))
        self.add_beverage(Cocktail('Singapore Sling', 2.9, '20%'))
        self.add_beverage(Cocktail('Mary\'s Blood', 11.9, '30%'))

    def __init__(self):
        self.create_beverages()

    def display_orders(self):
        total_bill = 0
        for bev in Bar.orders:
            print(bev)
            total_bill += bev.get_price()

        print(f"Total bill is {total_bill}")

    def show_menu(self):
        opt = -1
        while opt != 0:
            self.display_options()
            opt = int(input('Enter your option: '))
            print()
            if opt - 1 in range(len(Bar.beverages)):
                Bar.orders.append(Bar.beverages[opt - 1])

    def display_options(self):
        for idx in range(len(Bar.beverages)):
            print(f"{idx + 1} {Bar.beverages[idx]}")
            idx += 1
        print(f"0 Quit")


bar = Bar()
bar.show_menu()
bar.display_orders()