'''
    File Name: number_guessing_game.py
    Version: 1.1.1
    Date: 13/07/2025
    Author: Pablo Bartolomé Molina
'''

import random

def make_a_guess(user_number = 100, computer_number = 100, max_range = 100):
    while user_number not in range (0,max_range+1):
        try:
            user_number = int(input(f"Choose a number between 0 and {max_range}: "))
        except ValueError:
            print("It's not a number.")
    if user_number == computer_number:
        print("It's a correct guess!")
        return True
    else:
        print("You lose!")
        return False

def main():
    game_options = ["yes", "y", "no", "n"]
    new_game = "None"
    
    while(1):
        num_guess = int(input("How many guesses?: "))
        max_range = int(input("Higest number of the range?: "))
        computer_number = random.randint(0,max_range)
        user_number = max_range + 1 # For logic purposes.
        guess = 1
        
        while not make_a_guess(user_number, computer_number, max_range) :
            print("Try #", guess)
            guess = guess + 1
            if guess >= num_guess + 1:
                break
        
        print(f"Computer chose: {computer_number}")
        new_game = input("Do you want a new game (yes/no)?: ").lower()
        while new_game not in game_options:
            print("Please choose yes, or no.")
            new_game = input("Do you want a new game (yes/no)?: ").lower()
        if (new_game == "yes") or (new_game == "y"):
            print("Let's play again!")
        elif (new_game == "no") or (new_game == "n"):
            print("Bye!")
            break
    
if __name__ == "__main__":
    main()
   
