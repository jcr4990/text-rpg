import random

class Enemy:
    """Represents an enemy in the game."""
    def __init__(self, name, hp, ac, damage, inventory):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.damage = damage
        self.inventory = inventory


    def is_alive(self):
        return self.hp > 0

    @staticmethod
    def random(level):
        name = random.choice(enemy_names)
        hp = (level * 0.1 * 100) + random.randint(0, level * 0.1 * 10)
        ac = (level * 0.1 * 10) + random.randint(0, level * 0.1 * 4)
        damage = (level * 0.1 * 10) + random.randint(0, level * 0.1 * 6)
        enemy = Enemy(name, hp, ac, damage, [])
        return enemy


enemy_names = ["a mountain lion", "a grizzly bear", "a rattlesnake", "an elf bandit", "a wolf"]
