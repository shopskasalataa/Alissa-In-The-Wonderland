from item import *
from utils import verify_positive

class Alissa:
    @verify_positive
    def __init__(self, position):
        self.name = 'Alissa'
        self.health = 100
        self.base_weapon = BaseWeapon()
        self.weapon = None
        self.inventory = []
        self.position = position

    def __str__(self):
        return f'Alissa\'s health: {self.health}|Base damage: {self.base_weapon.damage}'

    def __repr__(self):
        return self.__str__()

    def add_weapon(self, item):
        self.inventory.append(item)

    @verify_positive
    def move(self, new_position):
        self.position = new_position

    @verify_positive
    def move_up(self):
        x, y = self.position
        self.move((x - 1, y))

    @verify_positive
    def move_down(self):
        x, y = self.position
        self.move((x + 1, y))

    @verify_positive
    def move_left(self):
        x, y = self.position
        self.move((x, y - 1))

    @verify_positive
    def move_right(self):
        x, y = self.position
        self.move((x, y + 1))

    def show_inventory(self):
        for (i, x) in enumerate(self.inventory):
            print(f'{i}. {x}')

    def weaponise(self, weapon):
        self.weapon = weapon

    def disarm(self):
        self.weapon = None

    def attack(self):
        weapon = self.weapon if self.weapon else self.base_weapon
        return weapon.damage

    def is_dead(self):
        return self.health <= 0

    @verify_positive
    def get_damage(self, damage):
        self.health -= damage


if __name__ == '__main__':
    alissa = Alissa((0, 0))
    alissa.move_up()
    alissa.add_weapon(DrinkMePotion())
    print(alissa.inventory)
