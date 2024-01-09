import random

def get_user_choice():
    print("Enter your choice: rock, paper, or scissors")
    user_choice = input().lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return "IT IS A TIE!!! NOT A NECKTIE!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "YOU WIN!"
    else:
        return "COMPUTER IS THE WINNER NA NA NA"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Play the game
play_game()
