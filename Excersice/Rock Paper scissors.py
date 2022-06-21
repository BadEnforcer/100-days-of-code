rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
Dlist = ['rock', 'paper', 'scissors']

player_choice = str(input("Rock , Paper or Scissors? \n")).lower()
import random

computer_choice = random.choice(Dlist)

# game logic

##you win
if computer_choice == 'rock' and player_choice == 'paper':
    print(f"You Chose Paper\n{paper}")
    print(f"The Computer Chose Rock\n{rock}")
    print("You win")
elif computer_choice == 'paper' and player_choice == 'scissors':
    print(f"You Chose Paper\n{scissors}")
    print(f"The Computer Chose Rock\n{paper}")
    print("You win")
elif computer_choice == 'scissors' and player_choice == 'rock':
    print(f"You Chose Paper\n{rock}")
    print(f"The Computer Chose Rock\n{scissors}")
    print("You win")
##Tie
#rock
elif computer_choice == 'rock' == player_choice:
    print(f"You Chose Paper\n{rock}")
    print(f"The Computer Chose Rock\n{rock}")
    print("Tie")

#paper
elif computer_choice == 'paper' == player_choice:
    print(f"You Chose Paper\n{paper}")
    print(f"The Computer Chose Rock\n{paper}")
    print("Tie")

#scissors
elif computer_choice == 'scissors' == player_choice:
    print(f"You Chose Paper\n{scissors}")
    print(f"The Computer Chose Rock\n{scissors}")
    print("Tie")
##you lose
if computer_choice == 'paper' and player_choice != 'rock':
    print(f"You Chose Paper\n{rock}")
    print(f"The Computer Chose Rock\n{paper}")
    print("You Lost")
elif computer_choice == 'scissors' and player_choice == 'paper':
    print(f"You Chose Paper\n{paper}")
    print(f"The Computer Chose Rock\n{scissors}")
    print("You Lost")
elif computer_choice == 'rock' and player_choice == 'scissors':
    print(f"You Chose Paper\n{scissors}")
    print(f"The Computer Chose Rock\n{rock}")
    print("You Lost")
