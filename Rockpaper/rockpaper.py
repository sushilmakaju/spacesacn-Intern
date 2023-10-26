import random

choices = ['rock', 'paper', 'scissor']  # list for choice

def user_choice():
    while True: #Infinity loop 
        user = input("Enter your choice (rock, paper, or scissor): ")
        if user in choices:
            return user
        else:
            print("Invalid entry")

def computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissor" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_again():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ["yes", "no"]:
            return play_again == "yes"
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def play_game():
    print("Let's play Rock-Paper-Scissors!")
    while True:
        user = user_choice()
        computer = computer_choice()
        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")
        print(determine_winner(user, computer))
        if not play_again():
            break
if __name__ == "__main__":
    play_game()