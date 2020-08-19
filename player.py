import random

class Player:
    """Represents the player in the game."""
    def __init__(self, name, level, exp, inventory):
        self.name = name
        self.level = level
        self.exp = exp
        self.inventory = inventory
        self.hp = (level * 0.1 * 100) + random.randint(0, level * 0.1 * 10)
        self.ac = (level * 0.1 * 10) + random.randint(0, level * 0.1 * 4)
        self.damage = (level * 0.1 * 10) + random.randint(0, level * 0.1 * 6)


    def is_alive(self):
        return self.hp > 0
