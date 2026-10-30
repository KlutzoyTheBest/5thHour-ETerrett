#Name: Ethan Terrett
#Class: 5th hour
#Assignment: Playground

import random
from turtledemo.round_dance import stop

print("YOU ARE ABOUT TO ENTER A GAME ABOUT HEAVY RNG, DO YOU WANT TO CONTINUE????")
yes_or_no = input("Y / N?: ")
#I was just about to add detection to typos here :(
if yes_or_no == "Y":
    print("-------------------------------------------")
    print("What difficulty would you like? Easy, Medium, or Hard?")
    difficulty = input("Select a difficulty: ")
    print("-------------------------------------------")
    if yes_or_no == "N":
        print("I DIDN'T LIKE YOU ANYWAYS!!!!")
        print("-------------------------------------------")

    if difficulty == "Easy":
        ene_health = random.randint(1, 10)
        ene_damage = random.randint(1, 4)
        print("Enemy health:", ene_health)
        print("Enemy damage:", ene_damage)
    else:
        print("Invalid Difficulty!")

    if difficulty == "Medium":
        ene_health = random.randint(10, 20)
        ene_damage = random.randint(4, 8)
        print("Enemy health:", ene_health)
        print("Enemy damage:", ene_damage)

    if difficulty == "Hard":
        ene_health = random.randint(20, 30)
        ene_damage = random.randint(8, 12)
        print("Enemy health:", ene_health)
        print("Enemy damage:", ene_damage)


    print("-------------------------------------------")

    if difficulty == "Easy":
        player_health = random.randint(10, 15)
        player_damage = random.randint(3, 6)
        print("Player health:", player_health)
        print("Player damage:", player_damage)

    if difficulty == "Medium":
        player_health = random.randint(10, 20)
        player_damage = random.randint(4, 8)
        print("Player health:", player_health)
        print("Player damage:", player_damage)

    if difficulty == "Medium":
        player_health = random.randint(10, 30)
        player_damage = random.randint(4, 12)
        print("Player health:", player_health)
        print("Player damage:", player_damage)

    print("-------------------------------------------")

    option = input("Do you want to run away, or attack?: ")
    if option == "Run" or option == "run":
        print("SCAREDY CAT!")
    elif option == "Attack" or "attack":
        ene_health = ene_health - player_damage
        if ene_health <= 0:
            print("Enemy health is dead!")
        elif ene_health > 0:
            print("Enemy health: ", ene_health)
        print("-------------------------------------------")
    print("-------------------------------------------")

    print("Enemy retaliated!")
    player_health = player_health - ene_damage
    if player_health <= 0:
        print("You died!")
    elif player_health > 0:
        print("Player health: ", player_health)
