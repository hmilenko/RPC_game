from logging import raiseExceptions
import random
from time import sleep

def result_display():
    print("3...", end="")
    sleep(1)
    print("2...", end="")
    sleep(1)
    print("1...")
    sleep(1)

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    result_display()
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    bypass = False

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print("Choice not valid")
        bypass = True
        
    if not bypass:
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break