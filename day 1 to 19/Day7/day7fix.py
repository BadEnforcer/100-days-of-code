import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

chosen_word = random.choice(word_list)
length_of_chosen_word = len(chosen_word)

# empty list for blanks and underscores(display)
blanks = []
for char in range(0, length_of_chosen_word):
    blanks.append("_")

# user input and word checking.
# lives = 6
end_of_game = False
lives = 6
# before user input

print(logo)
print(blanks)
#

list_of_wrong_words = []
# game beings!
while not end_of_game:  # logic beings!
    guess = str(input("\nEnter a single letter : \n")).lower()
    if guess in blanks:
        print(f" you have already guess {guess}")
    if guess not in chosen_word:
        print(f"\nletter '{guess}' is not in the word.\n")
        lives -= 1
        print(f"lives left:{lives}")
        if lives == 0:
            end_of_game = True
            print("\nYou lost!")

    for letter in range(0, length_of_chosen_word):
        if guess == chosen_word[letter]:
            blanks[letter] = guess
    print(blanks)
    if "_" not in blanks:
        end_of_game = True
        print('You Win!')

    print(stages[lives])
