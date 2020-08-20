class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return f"\n{self.name}\n------------\n{self.description}\nValue: {self.value}\n"


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold", description=f"You have {str(self.amt)} gold coins.", value=self.amt)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return f"\n{self.name}\n------------\n{self.description}\nValue: {self.value}\nDamage: {self.damage}"



rusty_short_sword = Weapon("Rusty Short Sword", "It's rusty and not very sharp but it's better than nothing.", "1", "4")
print(rusty_short_sword)

# gold = Gold(5)
# print(gold)
