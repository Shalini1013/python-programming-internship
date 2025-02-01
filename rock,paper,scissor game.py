        
import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' to exit the game.\n")

    while True:
        print(f"Score: You {user_score} - {computer_score} Computer")
        user_choice = input("Your choice: ").lower()

        if user_choice == "quit":
            print("Thanks for playing!")
            print(f"Final Score: You {user_score} - {computer_score} Computer")
            break

        if user_choice not in options:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.\n")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round!")
            computer_score += 1

        print("\nWould you like to play again?")
        play_again = input("Type 'yes' to continue or 'no' to quit: ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            print(f"Final Score: You {user_score} - {computer_score} Computer")
            break
        print()

# Run the game
rock_paper_scissors()
