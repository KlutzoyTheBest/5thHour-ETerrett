#Name: Ethan Terrett
#Class: 5th Hour
#Assignment: Scenario 1

import random
from sys import hash_info

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.


mobs = {
    "Slime" : {
        "Property" : "Squishy",
        "Damage" : 2,
        "Defense" : 2 + 2,
        "Speed" : 1
    },
    "Goblin": {
        "Property": "Quick",
        "Damage": 3,
        "Defense": 1,
        "Speed": 2 + 2
    },
    "Wolf": {
        "Property": "Deep cut",
        "Damage": 3 + 1,
        "Defense": 3,
        "Speed": 3
    },
    "Ogre": {
        "Property": "Strength",
        "Damage": 3 + 2,
        "Defense": 4,
        "Speed": 2
    },
    "Titan": {
        "Property": "AoE",
        "Damage": 6 + 3,
        "Defense": 7,
        "Speed": 3
    },
}

player = {
    "Name" : "",
    "Property" : "Nothing",
    "Damage" : 0,
    "Defense" : 0,
    "Speed" : 0
}




damage_change = int(input("Enter Slime damage:"))
mobs["Slime"].update({"Damage" : damage_change})
print(mobs["Slime"]["Damage"])

damage_change2 = int(input("Enter Goblin damage:"))
mobs["Goblin"].update({"Damage" : damage_change2})
print(mobs["Goblin"]["Damage"])

damage_change = int(input("Enter Wolf damage:"))
mobs["Wolf"].update({"Damage" : damage_change + 1})
print(mobs["Wolf"]["Damage"])

damage_change = int(input("Enter Ogre damage:"))
mobs["Ogre"].update({"Damage" : damage_change + 2})
print(mobs["Ogre"]["Damage"])

damage_change = int(input("Enter Titan damage:"))
mobs["Titan"].update({"Damage" : damage_change + 3})
print(mobs["Titan"]["Damage"])