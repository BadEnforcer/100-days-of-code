import random
from hangman_art import logo, stages
from hangman_words import word_list

#
#
#
#
print(logo)

# choosing the word and converting its length into a variable
chosen_word = random.choice(word_list)
length = len(chosen_word)

# turn the length into an underscore string:
display = []
for letter in range(0, length):
    display += "_"
# lives
lives = 6
# start game
print(chosen_word)  # for testing
end_of_game = False


while not end_of_game:
    guess = str(input("Enter a Letter : ")).lower()

    if guess in display:
        print("You have already guessed this letter.")
        print(f"Remaining lives : {lives}")
        print(stages[lives])
        print(display)

    if guess not in chosen_word:
        print(" \nNope. wrong letter.")
        lives -= 1
        print(stages[lives])
        print(f"\nRemaining lives : {lives}")
        print(display)

    for letter in range(0, length):
        if guess == chosen_word[letter]:
            display[letter] = guess
            print("Correct choice.")
            print(display)
    if "_" not in display:
        end_of_game = True
        print('You Win!')

    if lives == 0:
        end_of_game = True
        print(f"You progress: {display}")
        print("\nNo more lives left. You lost amigo.")
