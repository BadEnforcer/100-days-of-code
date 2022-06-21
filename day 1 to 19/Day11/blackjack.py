# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

# give the computer and user random cards
user_card = []
dealer_cards = []


def deal_card(number_of_times):
    for i in range(0, number_of_times + 1):
        user_card.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))


deal_card(2)
player_sum = 0
dealer_sum = 0


# sum function
def calculate_score(plist, dlist):
    # checking for player
    if len(plist) == 2 and sum(plist) == 21:
        return "player0"
    elif sum(plist) > 21 and 11 not in plist:
        return f"Player score is {sum(plist)}. player loses.\n The computer scored {sum(dlist)}"
    elif sum(plist) > 21 and 11 in plist:
        index = plist.index[11]
        plist[index] = 1
        if sum(plist) > 21:
            return f"Player score is {sum(plist)}. player loses.\n The computer scored {sum(dlist)}"
        elif sum(plist) == 21:
            return "player0"
    else:
        return f"player score is {sum(plist)}"
        # checking for computer
    if len(dlist) == 2 and sum(dlist) == 21:
        return "com0"
    elif sum(plist) > 21 and 11 not in plist:
        return f"Player score is {sum(plist)}. player loses.\n The computer scored {sum(dlist)}"
    elif sum(plist) > 21 and 11 in plist:
        index = plist.index[11]
        plist[index] = 1
        if sum(plist) > 21:
            return f"Player score is {sum(plist)}. player loses.\n The computer scored {sum(dlist)}"
        elif sum(plist) == 21:
            return "com0"
    else:
        return f"player score is {sum(dlist)}"


calculate_score(user_card, dealer_cards)
# check sum of computer and user

# check score. if user won then end game. else,
# ask user if they want another card. if yes then add another card to both user and computer and calculate sum and
# check if user or computer has won.
# if the player said they don't want a card. and score is less than 17
# the computer will hand out cards until one of the players
# their sum reaches more than 17 and winner will be decided
