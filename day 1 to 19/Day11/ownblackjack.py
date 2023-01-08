import random

print("Welcome to blackjack.")
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def random_card():
    return random.choice(cards)


def replace_over(given_list):
    if 11 in given_list:
        if sum(given_list) > 21:
            index = given_list.index(11)
            given_list = given_list[:index] + [1] + given_list[index + 1:]
            return sum(given_list)


# game  on

player_cards = []
computer_cards = []
# giving two random cards out.
for num in range(0, 2):
    player_cards.append(random_card())
    computer_cards.append(random_card())

print(f"Your cards are : {player_cards}")
print(f"Computer's first card is : {computer_cards[0]}")

print("\n\n")  # Spacer

# check for blackjack
if sum(player_cards) == 21 and sum(computer_cards) != 21:
    print("BlackJack! , You won.")
    print(f"Computer's score was {sum(computer_cards)}. Cards : {computer_cards}")
    exit()

if sum(computer_cards) == 21 and sum(player_cards) != 21:
    print("Computer has BlackJack! , You lost.")
    print(f"Your Score was : {sum(player_cards)} points. Cards : {player_cards}")
    exit()

if sum(player_cards) == 21 and sum(computer_cards) == 21:
    print("Draw. Both of you have a blackjack.")
    exit()

# check if score is over 21 and if 11 number card can be replaced.

# check if player/computer score is over 21. if yes then replace 11 with 1 (if 11 is in the list.)
total = sum(player_cards)

# ask the player if they want another card while their sum is >= 21
halt = True
should_continue = 0
while halt:
    another_card = input(f"Do you want another card? Your Score is : {sum(player_cards)} Enter 'Y' or 'N'").lower()
    if another_card == 'y':
        player_cards.append(random_card())
        if sum(player_cards) > 21:
            replace_over(player_cards)
            if sum(player_cards) > 21:
                print(f"You went over 21. You lose. Cards : {player_cards}")
                print(f"Computer's score was {sum(computer_cards)}. Cards : {computer_cards}")
                exit()
        if sum(player_cards) == 21:
            print("BlackJack! , You won.")
            print(f"Computer's score was {sum(computer_cards)}. Cards : {computer_cards}")
            exit()
    elif another_card == 'solution':
        print("Alright. Skipping ahead!")
        should_continue = 1
        halt = False
        # game_on = False # delete this line in final program.
    else:
        print("Invalid input. skipping ahead.")
        should_continue = 1
        halt = False

while should_continue == 1:
    computer_score = sum(computer_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random_card())
        computer_score = sum(computer_cards)
    if computer_score == 21:
        print(f"Computer has BlackJack! , You lost.\nComputer Cards : {computer_cards}")
        exit()
        should_continue = 0
    if computer_score > 21:
        print(f"The Computer went over 21. Scoring {sum(computer_cards)}. Cards : {computer_cards}")
        print(f"You win. your score : {sum(player_cards)}. Cards : {player_cards}")
        exit()

        # do final comparison.
    if sum(computer_cards) < sum(player_cards) <= 21:
        print(f"\n\n\nYour Score is : {sum(player_cards)} points. . Cards : {player_cards}")
        print(f"Computer Scored : {sum(computer_cards)} points. Cards : {computer_cards}")
        print("You win")
        exit()

    if sum(player_cards) < sum(computer_cards) <= 21:
        print(f"\n\n\nComputer Scored : {sum(computer_cards)} points. Cards : {computer_cards}")
        print(f"Your Score is : {sum(player_cards)} points. Cards : {player_cards}")
        print("You lose")
        exit()
