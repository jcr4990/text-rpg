class Player:
    """Represents the player in the game."""
    def __init__(self, name, hp, ac, damage, inventory, exp):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.damage = damage
        self.inventory = inventory
        self.exp = exp
 
    def is_alive(self):
        return self.hp > 0



class Player:
    """Represents the player in the game."""
    def __init__(self, name, level, exp, inventory):
        self.name = name
        self.level = level
        self.exp = exp
        self.inventory = inventory
        
 
    def is_alive(self):
        return self.hp > 0