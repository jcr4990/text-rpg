import os
import random
# from random import randint
# import time
from enemies import Enemy
from player import Player


class Die:
    """Represents a single die."""

    def __init__(self, sides=6):
        """Set the number of sides (defaults to six)."""
        self.sides = sides

    def roll(self):
        """Roll the die."""
        return random.randint(1, self.sides)
    # for i in range(10):
        # d20 = Die(20)
        # print(f"{d20.roll()} / {d20.sides}")


def battle(player, enemy):
    while True:
        os.system("cls")
        dmg_dealt = random.randint(0, player.damage)
        enemy.hp = enemy.hp - dmg_dealt
        print(f"{player.name} attacks {enemy.name} dealing {round(dmg_dealt)} points of damage! {round(enemy.hp)} health remaining.")

        premitigated_damage = random.randint(0, enemy.damage)
        mitigated_damage = player.ac * 0.20
        dmg_received = premitigated_damage - mitigated_damage
        if dmg_received <= 0:
            dmg_received = 0
        player.hp = player.hp - dmg_received
        print(f"{enemy.name} attacks {player.name} dealing {round(dmg_received)} points of damage! {round(mitigated_damage)} mitigated! {round(player.hp)} health remaining.")

        if enemy.hp <= 0:
            return True

        if player.hp <= 0:
            return False

        input()


# testing combat loop
# for i in range(20):
#     player = Player("Macc", 15, 1, [])
#     enemy = Enemy.random(15)
#     battle(player, enemy)
#     input()

input("Welcome to blablabla! Press 'Enter' to advance the game dialogue.")
print("""\nYou awake in a cold dark cave. As you try to get your bearings and figure out how you got here you notice a robed man approaching you carrying a torch.
The man stands directly in front of you looking down at you suspiciously.

Robed man: Who are you? What are you doing here?\n""")

# Initialize Player
charname = input("Enter your character name:")
player = Player(charname.capitalize(), 15, 1, [])

input(f"\n{player.name}: My name is {player.name}. I'm afraid I don't know how I got here. May I ask who you are? Where are we?\n")

print("""Draigen: Very interesting... My name is Draigen and I haven't seen another human around these lands in many years.
We are in blablabla the home of the Blackscar Orcs. Unfortunately I have no time to chat, I have some unfinished business to tend to.
You should head south and seek shelter with the blablabla elves before the orcs find you. Here take this and hurry along! I will speak with you later.\n""")

input("Draigen hands you [A Rusty Short Sword] and disappears deeper into the cave. You equip [A Rusty Short Sword].\n")
player.weapon = "A Rusty Short Sword"

input("""You are still very confused. Not sure exactly where you are or how you got here but you decide to heed Draigen's warning about the orcs.
You stand up and walk toward the cave's entrance""")


enemy = Enemy.random(15)
print(f"""\nAs you exit the cave you are immediately spotted by {enemy.name} heading right for you!""")

encounter_decision = input("""
1: Raise your sword and prepare to fight
2: Attempt to Flee
""")

if encounter_decision == "1":
    encounter = battle(player, enemy)

    if encounter:
        print("VICTORY!")
    elif not encounter:
        print("GAME OVER!")
