# # function logic
# from hangman import chosen_word, display, length
# from hangman_art import stages
#
# #
# # lives = 6
# end_of_game = False
#
#
# def ingamelogic(lives=int):
#     global end_of_game
#     while not end_of_game:
#         guess = str(input("Enter a Letter : ")).lower()
#
#         if guess in display:
#             print("You have already guessed this letter.")
#             print(f"Remaining lives : {lives}")
#             print(stages[lives])
#             print(display)
#
#         if guess not in chosen_word:
#             print(" \nNope. wrong letter.")
#             lives -= 1
#             print(stages[lives])
#             print(f"\nRemaining lives : {lives}")
#             print(display)
#
#         for letter in range(0, length):
#             if guess == chosen_word[letter]:
#                 display[letter] = guess
#                 print("Correct choice.")
#                 print(display)
#         if "_" not in display:
#             end_of_game = True
#             print('You Win!')
#
#         if lives == 0:
#             end_of_game = True
#             print(f"You progress: {display}")
#             print("\nNo more lives left. You lost amigo.")
