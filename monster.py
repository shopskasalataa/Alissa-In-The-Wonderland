from utils import verify_positive

class Monster:
    def __init__(self, name, damage, action=None, description=''):
        self.name = name
        self.health = 100
        self.damage = damage
        self.action = action
        self.description = description

    def __str__(self):
        return f'Monster: {self.name} | Damage: {self.damage} | Action: {self.action}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name == other.name and self.damage == other.damage

    def attack(self):
        return self.damage

    def is_dead(self):
        return self.health <= 0

    @verify_positive
    def get_damage(self, damage):
        self.health -= damage


class CheshireCat(Monster):
    def __init__(self):
        name = 'Cheshire cat'
        damage = 0
        description = ''
        Monster.__init__(self, name, damage, description=description)

class QueenOfHearts(Monster):
    def __init__(self):
        name = 'Queen of Hearts'
        damage = 20
        description = ''
        Monster.__init__(self, name, damage, description=description)

class WhiteRabbit(Monster):
    def __init__(self):
        name = 'White rabbit'
        damage = 25
        description = ''
        Monster.__init__(self, name, damage, description=description)

class MadHatter(Monster):
    def __init__(self):
        # импорт е винаги в началото
        from random import randint
        name = 'Mad hatter'
        damage = randint(10, 30)
        description = ''
        Monster.__init__(self, name, damage, description=description)

