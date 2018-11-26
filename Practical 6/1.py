class Monster:
    def __init__(self, name, health, attack, defence):
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__defence = defence

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_attack(self):
        return self.__attack

    def get_defence(self):
        return self.__defence

    def set_health(self, health):
        self.__health = health


class FireMonster(Monster):
    def __init__(self):
        super().__init__('firebug', 10, 9, 4)


class WaterMonster(Monster):
    def __init__(self):
        super().__init__('waterbug', 15, 6, 3)


class GrassMonster(Monster):
    def __init__(self):
        super().__init__('grasshopper', 20, 5, 3)


def display_info(monster):
    s = f'{monster.get_name()} is a '
    if isinstance(monster, FireMonster):
        s += 'Fire'
    elif isinstance(monster, WaterMonster):
        s += 'Water'
    elif isinstance(monster, GrassMonster):
        s += 'Grass'

    s += ' Type monster'
    print(s)


#m1 = FireMonster()
#m2 = GrassMonster()
#display_info(m1)
#display_info(m2)

from random import randint

class MonsterGame:
    def __init__(self):
        self.computer_monster = self.generate_monster()
        self.player_monster = self.choose_monster()

    def choose_monster(self):
        while True:
            type = input('Choose your monster (F, W or G): ')

            if type.upper() == 'F':
                return FireMonster()
            elif type.upper() == 'W':
                return WaterMonster()
            elif type.upper() == 'G':
                return GrassMonster()
            else:
                print('invalid type')

    def generate_monster(self):
        type = randint(0, 2)

        if type == 0:
            return FireMonster()
        elif type == 1:
            return WaterMonster()
        else:
            return GrassMonster()

    def play(self):
        while self.player_monster.get_health() > 0 and self.computer_monster.get_health() > 0:
            # player attacks computer
            dmg = self.player_monster.get_attack() - self.computer_monster.get_defence()
            self.computer_monster.set_health(self.computer_monster.get_health() - dmg)

            print(f'{self.computer_monster.get_name()} suffers {dmg} damage, the health is '
                  f'{self.computer_monster.get_health()} now')

            if self.computer_monster.get_health() <= 0:
                break

            # computer attacks player
            dmg = self.computer_monster.get_attack() - self.player_monster.get_defence()
            self.player_monster.set_health(self.player_monster.get_health() - dmg)

            print(f'{self.player_monster.get_name()} suffers {dmg} damage, the health is '
                  f'{self.player_monster.get_health()} now')


game = MonsterGame()
display_info(game.player_monster)
display_info(game.computer_monster)
game.play()
