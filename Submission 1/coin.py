from random import randint


class Coin:
    def __init__(self):
        self.__sideup = 'Heads'

    def toss(self):
        num = randint(0, 1)
        if num:
            self.__sideup = 'Tails'
        else:
            self.__sideup = 'Heads'

        #print(f"{num} {self.__sideup}")

    def get_sideup(self):
        return self.__sideup


def main():
    c = Coin()
    print(c.get_sideup())
    c.toss()
    print(c.get_sideup())


main()


def calculate():
    x = int(input('Enter the number of times to flip: '))

    coin = Coin()

    head_count = 0

    for i in range(x):
        print('I am tossing the coin ...')
        coin.toss()
        print(coin.get_sideup())
        if coin.get_sideup() == 'Heads':
            head_count += 1

    print(f"Result : {head_count} heads out of {x}")


calculate()
