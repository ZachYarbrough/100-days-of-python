print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("You\'re mission is to find the treasure.\n")
crossroads = input("You are at a cross road. Where do you want to go?  Type 'left' or 'right' ").lower()

if crossroads == 'left':
    lake = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if lake == 'wait':
        door = input("You arrive at the island unharmed. There is a houst with 3 doors. One 'red', one 'yellow', and one 'blue'. Which colour do you choose? ").lower()
        if door == 'red':
            print("You enter a room on fire! Game Over.")
        elif door == 'blue':
            print("You enter a room full of beasts! Game Over.")
        elif door == 'yellow':
            print("You found the treasure! You win!")
    else:
        print("You attempt to swim across the lake and get eaten by piranha! Game Over.")
else:
    print("You come to a cliff and as you look over... You are pushed! You fall to your death. Game Over.")
