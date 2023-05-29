import random
import os
import Day11_art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Return a random card"""
    return random.choice(cards)


def calculate_score(cards):
    """Take a list of cards and returns the calaculated the score for the blackjack game"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and (11 in cards):
        cards[cards.index(11)] = 1
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score > 21:
        return "you went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(
            f"{user_cards}, current score: {user_score}\nComputer's first Card: {computer_cards[0]}"
        )
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Enter 'd' to draw a card or 's' to stand:")
            if choice == "d":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, Computer final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play Blackjack. 'y' or 'n' ")=='y':
    os.system('cls')
    print(Day11_art.logo)
    play_game()