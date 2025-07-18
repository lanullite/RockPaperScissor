import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
print(f"Computer choice: {computer_choice}")

if user_choice not in choices:
    print("Your choice is invalid.")
elif user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == "rock" and computer_choice == "scissors") or
    (user_choice == "scissors" and computer_choice == "paper") or
    (user_choice == "paper" and computer_choice == "rock")
):
    print("You win!")
else:
    print("Computer wins!")
