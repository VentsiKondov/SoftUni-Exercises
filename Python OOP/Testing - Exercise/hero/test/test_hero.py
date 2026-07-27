
import unittest

from project.hero import \
    Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Gosho" , 1, 10, 10)
        self.enemy = Hero("Mitko" , 1, 10, 10)

    def test_init(self):
        self.assertEqual(self.hero.username, "Gosho")
        self.assertEqual(self.hero.health, 10)
        self.assertEqual(self.hero.level ,1)
        self.assertEqual(self.hero.damage ,10)

    def test_battle_method_with_equal_names(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_method_with_lower_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_method_with_lower_enemy_health(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(str(ex.exception), "You cannot fight Mitko. He needs to rest")

    def test_battle_method_with_0_both_health(self):
        self.assertEqual(self.hero.battle(self.enemy), "Draw")

    def test_battle_method_with_0_enemy_health_and_updated_stats(self):
        self.hero.health = 20
        self.assertEqual(self.hero.battle(self.enemy), "You win")
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.damage, 15)
        self.assertEqual(self.hero.health, 15)

    def test_battle_method_lose(self):
        self.hero.health = 20
        self.enemy.health = 20
        self.assertEqual(self.hero.battle(self.enemy), "You lose")
        self.assertEqual(self.enemy.level, 2)
        self.assertEqual(self.enemy.health, 15)
        self.assertEqual(self.enemy.damage, 15)

    def test_str_method(self):
        self.assertEqual(str(self.hero), f"Hero Gosho: 1 lvl\n"+
                                               f"Health: 10\n" +
                                               f"Damage: 10\n")

if __name__ == '__main__':
    unittest.main()