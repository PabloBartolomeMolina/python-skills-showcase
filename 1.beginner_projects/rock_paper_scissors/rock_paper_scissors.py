'''
    File Name: rock_paper_scissors.py
    Version: 1.0.0
    Date: 12/07/2025
    Author: Pablo Bartolomé Molina
'''

import random

def main():
    compt_options = ["rock", "paper", "scissors"]
    game_options = ["yes", "y", "no", "n"]
    
    while(1):
        computer_choice = random.choice(compt_options)
        user_choice = "None"
        new_game = "None"
        
        while user_choice not in compt_options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            user_choice = input("Choose rock, paper, or scissors: ").lower()
        
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
        
        while new_game not in game_options:
            print("Invalid choice. Please choose yes, or no.")
            new_game = input("Do you want a new game (yes/no)?: ").lower()
        if (new_game == "yes") or (new_game == "y"):
            print("Let's play again!")
        elif (new_game == "no") or (new_game == "n"):
            print("Bye!")
            break
    
if __name__ == "__main__":
    main()
   
