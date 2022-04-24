class Item:
    def __init__(self, name, damage, action=None, description=''):
        self.name = name
        self.damage = damage
        self.action = action
        self.description = description

    def __str__(self):
        return f'Item: {self.name}|Damage: {self.damage}|Action: {self.action}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name == other.name and self.damage == other.damage


# 3 променливи, които се подават на родителския клас и не се пазят никъде
class BaseWeapon(Item):
    def __init__(self):
        name = 'Base weapon'
        damage = 15
        description = 'Base damage which Alissa makes\
 without having a special weapon.'
        Item.__init__(self, name, damage, description=description)


class TeleportationPotion(Item):
    def __init__(self):
        name = 'Teleportation potion'
        damage = 0

        # Ако до края на лабиринта остават по-малко от три полета,
        # то Алиса остава на мястото си.
        description = 'Moves Alissa 3 fields forward. If the field is\
 occupied, Alissa is moved to the first free field.\n If there are less \
 than 3 fields until the end of the labyrinth, Alissa doesn\'t move.'
        Item.__init__(self, name, damage, description=description)


class DrinkMePotion(Item):
    def __init__(self):
        name = '"Drink me" potion'
        damage = 10
        description = 'Reduces Alissa\'s abilities.'
        Item.__init__(self, name, damage, description=description)


class EatMeCookie(Item):
    def __init__(self):
        name = '"Eat me" cookie'
        damage = 40
        description = 'Increases Alissa\'s abilities.'
        Item.__init__(self, name, damage, description=description)


class MagicalHandFan(Item):
    def __init__(self):
        name = 'Magical Hand Fan'
        damage = 35
        description = "Reduces the enemy's size and gives Alissa an advantage."
        Item.__init__(self, name, damage, description=description)


# тук не трябва ли да се отбелязва кой път е използвана шапката?
class InvisibleHat(Item):
    def __init__(self):
        name = 'Invisible Hat'
        damage = 0
        description = 'Makes Alissa invisible and she can move without\
 being noticed 2 times.'
        Item.__init__(self, name, damage, description=description)


class Rose(Item):
    def __init__(self):
        name = 'Red rose'
        damage = 40
        description = 'Alissa doesn\'t know which rose is going to get.\
 There\'s 50% chance of getting the red rose.'
        from random import random
        if(random() < 0.5):
            name = 'White rose'
            damage = 10
        Item.__init__(self, name, damage, description=description)


if __name__ == '__main__':
    rose = Rose()
    print(rose)
    bs1 = BaseWeapon()
    bs2 = BaseWeapon()
    print(bs1 == bs2)
