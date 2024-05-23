import random

def play_game():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print("Computer wins!")
        else:
            print("You win!")
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")

# Main function to run the game
def main():
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
    
    while input("\nDo you want to play again? (yes/no): ").lower() == 'yes':
        play_game()

if __name__ == "__main__":
    main()