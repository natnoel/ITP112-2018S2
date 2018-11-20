from cocktail import Cocktail
from mocktail import Mocktail


def main():
    bev_list = [
        Mocktail('Lemonade Punch', 1.9),
        Mocktail('Tomato Lassi', 6.9),
        Cocktail('Singapore Sling', 2.9, '20%'),
        Cocktail('Mary\'s Blood', 11.9, '30%')
    ]

    for bev in bev_list:
        print(bev)


main()
