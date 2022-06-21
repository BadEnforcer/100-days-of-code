from art import logo, vs
from game_data import data
import random


def random_account(database):
    return random.choice(database)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f" {name} , {description} , {country}"


def check_answer(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == "a"
    else:
        return guess == "b"


def run_game():
    keep_playing = True
    print(logo)
    score = 0
    while keep_playing:
        account_b = random_account(data)
        should_loop = True
        while should_loop:
            account_a = account_b
            account_b = random_account(data)
            while account_a == account_b:
                account_b = random_account(data)

            # format and print
            print(f"Compare A: {format_data(account_a)}")
            print(vs)
            print(f"Against B: {format_data(account_b)}")

            follow_a = account_a["follower_count"]
            follow_b = account_b["follower_count"]
            guess = input("Which one is higher? Type 'A' or 'B' : ").lower()
            is_correct = check_answer(guess, follow_a, follow_b)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
            if is_correct:
                score += 1
                print(f"That was right. Current score is : {score}")
            else:
                print(f"That was wrong. Your final score is : {score}")
                should_loop = False
                keep_playing = False


run_game()
