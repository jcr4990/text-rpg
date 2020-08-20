import os
import random
import time
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

def pause():
    input("\nPress Enter To Continue...\n")
    os.system("cls")

def battle(player, enemy):
    combat_round = 1
    print("Entering Combat...")
    time.sleep(2)

    while True:
        os.system("cls")
        print(f"Combat Round: {combat_round}")
        combat_round += 1

        # Player Dmg to Enemy
        dmg_dealt = random.randint(0, player.damage)
        enemy.hp = enemy.hp - dmg_dealt
        print(f"{player.name} attacks {enemy.name} dealing {round(dmg_dealt)} points of damage! {round(enemy.hp)} health remaining.")

        #Enemy Dmg to Player
        premitigated_damage = random.randint(0, enemy.damage)
        mitigated_damage = player.ac * 0.20
        dmg_received = premitigated_damage - mitigated_damage
        if dmg_received <= 0:
            dmg_received = 0
        player.hp = player.hp - dmg_received
        print(f"{enemy.name} attacks {player.name} dealing {round(dmg_received)} points of damage! {round(mitigated_damage)} mitigated! {round(player.hp)} health remaining.")

        if enemy.hp <= 0:
            return f"You have slain {enemy.name}!!!"

        if player.hp <= 0:
            return f"You have been slain by {enemy.name}."

        pause()

# testing combat loop
# for i in range(20):
#     player = Player("Macc", 15, 1, [])
#     enemy = Enemy.random(15)
#     print(battle(player, enemy))
#     pause()


print("Welcome to Gypsy Heroes!")
pause()

print("""You awake in a cold dark cave. As you try to get your bearings and figure out how you got here you notice a robed man approaching you carrying a torch.
The man stands directly in front of you looking down at you suspiciously.

Robed man: Who are you? What are you doing here?\n""")

# Initialize Player
charname = input("Enter your character name:")
player = Player(charname.capitalize(), 15, 1, [])

print(f"\n{player.name}: My name is {player.name}. I'm afraid I don't know how I got here. May I ask who you are? Where are we?")
pause()

print("""Draigen: Very interesting... My name is Draigen and I haven't seen another human around these lands in many years.
We are in blablabla the home of the Blackscar Orcs. Unfortunately I have no time to chat, I have some unfinished business to tend to.
You should head south and seek shelter with the blablabla elves before the orcs find you. Here take this and hurry along! I will speak with you later.

Draigen hands you [A Rusty Short Sword] and disappears deeper into the cave. You equip [A Rusty Short Sword].""")
pause()

print("""You are still very confused. Not sure exactly where you are or how you got here but you decide to heed Draigen's warning about the orcs.
You stand up and walk toward the cave's entrance""")
pause()

enemy = Enemy.random(15)
print(f"""As you exit the cave you are immediately spotted by {enemy.name} heading right for you!""")
encounter_decision = input("""
1: Raise your weapon and prepare to fight
2: Attempt to Flee

""")


if encounter_decision == "1":
    print(battle(player, enemy))
    pause()
elif encounter_decision == "2":
    flee_chance = random.randint(1, 10)

    if flee_chance >= 8:
        print("You fled successfully!")
    else:
        print("You failed to flee!")
        print(battle(player, enemy))
        pause()