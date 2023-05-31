import Day14_gamedata
import Day14_art
import random
import os


def format_data(option):
    name = option["name"]
    follower = option["follower_count"]
    description = option["description"]
    country = option["country"]
    return f"{option['name']}, {option['description']}, from {option['country']}."


def check_answer(a_follower, b_follower, guess):
    if a_follower > b_follower:
        return guess == "A"
    else:
        return guess == "B"


print(Day14_art.logo)
score = 0
game_continue = True
option_b = random.choice(Day14_gamedata.data)

while game_continue:
    option_a = option_b
    option_b = random.choice(Day14_gamedata.data)
    while option_a == option_b:
        option_b = random.choice(Day14_gamedata.data)

    print(f"Compare A: {format_data(option_a)}")
    print(Day14_art.vs)
    print(f"Against B: {format_data(option_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    os.system("cls")
    print(Day14_art.logo)
    a_follower = option_a["follower_count"]
    b_follower = option_b["follower_count"]

    is_correct = check_answer(a_follower, b_follower, guess)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_continue = False
        print(f"Sorry, that wrong. Final score {score}")
