print('''
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')


print("Welcome to the treasure island.\nYour mission is to find the treasure.")
print("You're at a cross road. Where do you want to go? " + 'Type "left" or "right"')
D1 = str(input().lower())
if D1 == 'right':
    print("You got eaten by a bear. Game Over!")
    print(f"\n\nYour choices : you went {D1} and Died.")
    exit()

if D1 == "left":
    print('You came to a lake. there is an island in the middle of in lake.' + 'Type "wait" to wait for a boat. Type '
                                                                               '"swim" to swim across')

D2 = str(input().lower())
if D2 == 'swim':
    print("You got F*cked by a angry crocodile. Game Over!")
    print(f"\n\nYour choices : you went {D1},  you {D2}ed ")
    exit()

if D2 == 'wait':
    print("You arrive at the island unharmed (i know right?). There is a  weird looking house with 3 doors. One red, "
          "one yellow and one blue. \nWhich colour do you choose?")

D3 = str(input().lower())

if D3 == 'red' or 'blue':
    print("Game Over!")
if D3 == 'yellow':
    print("You found a vibranium sword and a treasure chest!")
    print("The End")
    print(f"\n\nYour choices : you went {D1},  you {D2}ed , you chose the {D3} door")
