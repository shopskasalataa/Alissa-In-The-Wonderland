from Alissa import Alissa
from item import *
from monster import *
from random import randrange


ITEM_CLASSES = [TeleportationPotion,
                DrinkMePotion,
                EatMeCookie,
                MagicalHandFan,
                InvisibleHat,
                Rose]

MONSTER_CLASSES = [CheshireCat,
                   QueenOfHearts,
                   WhiteRabbit,
                   MadHatter]


def read_matrix(filename):
    file = open(filename)
    file_lines = file.readlines()
    file.close()

    # режем последния символ от всяка колона,
    # защото очакваме да е символ за нов ред
    return [line[:-1].split(' ') for line in file_lines]


def find_symbol(matrix, symbol):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == symbol:
                return (row, column)
    return None


def generate_random_array(size, source):
    # избираме случаен клас и му извикваме конструктора
    return [source[randrange(0, len(source))]() for _ in range(size)]


class LevelMap:
    empty_square = '-'
    blocked_square = '*'
    in_portal = 'i'
    out_portal = 'o'
    enemy_symbol = 'E'
    hero_symbol = 'A'
    weapon_symbol = 'x'

    direction_up = 'u'
    direction_down = 'd'
    direction_left = 'l'
    direction_right = 'r'

    def __init__(self, filename, range_of_weapons, range_of_monsters):
        from random import randint
        number_of_weapons = randint(range_of_weapons[0], range_of_weapons[1])
        number_of_monsters = randint(range_of_monsters[0], range_of_monsters[1])

        weapons = generate_random_array(number_of_weapons, ITEM_CLASSES)
        monsters = generate_random_array(number_of_monsters, MONSTER_CLASSES)

        self.level_map = read_matrix(filename)
        self.rows = len(self.level_map)
        self.columns = len(self.level_map[0])

        self.set_hero()
        self.set_weapons(weapons)
        self.set_monsters(monsters)

        self.is_finished = False

    def __str__(self):
        return '\n'.join([' '.join(line) for line in self.level_map])

    def set_hero(self):
        hero_position = find_symbol(self.level_map, LevelMap.in_portal)
        self.hero = Alissa(hero_position)
        self.set_hero_position(hero_position)

    def set_weapons(self, weapons):
        self.weapons = weapons
        self.spawn_items(self.weapons, LevelMap.weapon_symbol)

    def set_monsters(self, monsters):
        self.monsters = monsters
        self.spawn_items(self.monsters, LevelMap.enemy_symbol)

    def spawn_items(self, source, symbol):
        for _ in source:
            position = self.find_spawn()
            self.set_position_symbol(position, symbol)

    def check_position_value(self, position, value):
        n, m = position
        return self.level_map[n][m] == value

    def is_empty(self, position):
        return self.check_position_value(position, LevelMap.empty_square)

    def is_blocked(self, position):
        return self.check_position_value(position, LevelMap.blocked_square)

    def is_weapon(self, position):
        return self.check_position_value(position, LevelMap.weapon_symbol)

    def is_monster(self, position):
        return self.check_position_value(position, LevelMap.enemy_symbol)

    def check_final(self, position):
        self.is_finished = self.check_position_value(position, LevelMap.out_portal)

    def find_spawn(self):
        n = randrange(0, self.rows)
        m = randrange(0, self.columns)

        return (n, m) if self.is_empty((n, m)) else self.find_spawn()

    def set_position_symbol(self, position, symbol):
        self.level_map[position[0]][position[1]] = symbol

    def set_empty(self, position):
        self.set_position_symbol(position, LevelMap.empty_square)

    def set_hero_position(self, hero_position):
        self.set_position_symbol(hero_position, LevelMap.hero_symbol)

    def remove_weapon(self, index):
        self.weapons = self.weapons[:index] + self.weapons[index + 1:]

    def remove_monster(self, index):
        self.monsters = self.monsters[:index] + self.monsters[index + 1:]

    def get_random_weapon(self):
        index = randrange(0, len(self.weapons))
        weapon = self.weapons[index]
        self.remove_weapon(index)
        return weapon

    def get_random_monster(self):
        index = randrange(0, len(self.monsters))
        monster = self.monsters[index]
        self.remove_monster(index)
        return monster

    # Функциите надолу не са чисти и поддържат интерфейса на играта
    def move_hero(self, direction):
        old_position = self.hero.position
        if direction == LevelMap.direction_up:
            self.hero.move_up()
        elif direction == LevelMap.direction_down:
            self.hero.move_down()
        elif direction == LevelMap.direction_left:
            self.hero.move_left()
        elif direction == LevelMap.direction_right:
            self.hero.move_right()
        else:
            raise ValueError('Invalid direction alias!')

        new_position = self.hero.position
        if self.is_blocked(new_position):
            print('Invalid move - blocked square')
            self.hero.move(old_position)
        else:
            if self.is_weapon(new_position):
                weapon = self.get_random_weapon()
                print('You found a weapon\n', weapon)
                self.hero.add_weapon(weapon)

            if self.is_monster(new_position):
                self.fight(self.get_random_monster())

            self.check_final(new_position)

            self.set_empty(old_position)
            self.set_hero_position(new_position)

    def fight(self, monster):
        while not self.hero.is_dead() and not monster.is_dead():
            damage = self.hero.attack()
            monster.get_damage(damage)
            damage = monster.attack()
            self.hero.get_damage(damage)

        if not self.hero.is_dead():
            self.hero.disarm()
            print(f'{self.hero.name} wins!')
        # else

    def play(self):
        while not self.is_finished:
            print(self)
            direction = input()
            self.move_hero(direction)


# Wrapping класове за различните труднусти на нивата
class EasyLevel(LevelMap):
    def __init__(self, filename):
        range_of_weapons = (0, 3)
        range_of_monsters = (0, 3)
        LevelMap.__init__(self, filename, range_of_weapons, range_of_monsters)


class MediumLevel(LevelMap):
    def __init__(self, filename):
        range_of_weapons = (3, 5)
        range_of_monsters = (4, 7)
        LevelMap.__init__(self, filename, range_of_weapons, range_of_monsters)


class HardLevel(LevelMap):
    def __init__(self, filename):
        range_of_weapons = (5, 9)
        range_of_monsters = (7, 11)
        LevelMap.__init__(self, filename, range_of_weapons, range_of_monsters)


if __name__ == '__main__':
    filename = 'level1.txt'
    elevel = MediumLevel(filename)
    elevel.play()
