'''
    File Name: number_guessing_game.py
    Version: 1.1.0
    Date: 13/07/2025
    Author: Pablo Bartolomé Molina
'''

import random

def make_a_guess(user_number = 100, computer_number = 100):
    while user_number not in range (0,51):
        user_number = int(input("Choose a number between 0 and 50: "))
    
    if user_number == computer_number:
        print("It's a correct guess!")
        return True
    else:
        print("You lose!")
        return False

def main():
    game_options = ["yes," "y", "no", "n"]
    new_game = "None"
    
    while(1):
        computer_number = random.randint(0,50)
        user_number = 100
        guess = 1
        
        while not make_a_guess(user_number, computer_number) :
            print("Try #", guess)  
            guess = guess + 1
            if guess == 4:
                break
        
        print(f"Computer chose: {computer_number}")
        
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
   
