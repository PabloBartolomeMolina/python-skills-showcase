'''
    File Name: number_guessing_game.py
    Version: 1.0.0
    Date: 13/07/2025
    Author: Pablo Bartolomé Molina
'''

import random

def main():
    
    while(1):
        game_options = ["yes," "y", "no", "n"]
        computer_number = random.randint(0,50)
        user_number = 100
        new_game = "None"
        
        while user_number not in range (0,51):
            user_number = int(input("Choose a number between 0 and 50: "))
        
        print(f"Computer chose: {computer_number}")
        
        if user_number == computer_number:
            print("It's a correct guess!")
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
   
