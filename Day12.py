import random

"""Global variables"""
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def check_answer(number, guess, turn):
    """This function takes actual number, guessed number by the user and no of turns remaining and return the result of comparision"""
    if number > guess:
        print("Too low.")
        return turn - 1
    elif number < guess:
        print("Too high.")
        return turn - 1
    else:
        print(f"You got it! The answer was {number}.")
        return


def set_difficulty():
    """This function return the diffculty level based on user input."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURN
    elif level == "hard":
        return HARD_LEVEL_TURN


def game():
    print("Welcome to the Number Guessing Game! ")
    number = random.randint(1, 100)
    print(number)
    print("I'm thinking of a number between 1 and 100.")
    turns = set_difficulty()
    guess=-1
    while guess!=number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(number, guess, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
        elif guess != number:
            print("Guess again.")


game()
