from Alissa import *
import unittest

class TestAlissa(unittest.TestCase):
    # запазен метод
    def setUp(self):
        self.alissa = Alissa((3, 3))

    def test_alissa_creation(self):
        self.assertEqual(self.alissa.health, 100)
        self.assertEqual(self.alissa.base_weapon, BaseWeapon())
        self.assertEqual(self.alissa.position, (3, 3))
        self.assertEqual(self.alissa.inventory, [])
#       self.assertEqual(len(alissa.inventory), 0)
    
    def test_add_inventory(self):
        item = DrinkMePotion()
        self.alissa.add_weapon(item)
        self.assertEqual(self.alissa.inventory, [item])

    def test_move(self):
        new_position = (3, 4)
        self.alissa.move(new_position)
        self.assertEqual(self.alissa.position, new_position)

    def test_move_up(self):
        self.alissa.move_up()
        self.assertEqual(self.alissa.position, (2, 3))

    def test_move_down(self):
        self.alissa.move_down()
        self.assertEqual(self.alissa.position, (4, 3))

    def test_move_left(self):
        self.alissa.move_left()
        self.assertEqual(self.alissa.position, (3, 2))

    def test_move_right(self):
        self.alissa.move_right()
        self.assertEqual(self.alissa.position, (3, 4))

    # как можем да проверим за невалидни позиции за down, left и right?
    def test_invalid_position(self):
        self.alissa.move((0, 0))
        with self.assertRaises(ValueError):
            self.alissa.move_up()

        

if __name__ == '__main__':
    unittest.main()