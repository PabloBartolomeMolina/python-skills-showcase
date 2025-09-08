'''
    File Name: password_generator.py
    Version: 2.0.0
    Date: 19/08/2025
    Author: Pablo Bartolomé Molina
'''

import random
import string

info = """
==========================
    Password Generator
==========================

Description:
This application generates secure random passwords
with customizable length and character sets.

Features:
- Choose password length
- Include/exclude uppercase, lowercase, digits, symbols
- Exclude ambiguous characters
- Generate multiple passwords at once

Disclaimer:
This tool is intended for personal use and learning.
It does not guarantee compliance with enterprise-level
password security policies.
"""

constraints_info= """
Your password must contain:
- At least 8 characters
- At least one number
- At least 1 uppercase letter
- At least 1 lowercase one
- At least 1 special character from this list: &, @, *, #
"""

def display_menu():
    print("\nPassword Generator")
    print("1. New Password")
    print("2. Information")
    print("3. Exit")

def show_information():
    print(info)

def check_length():
    while True:
        user_input = input("Enter wanted length for the password (12 or more): ")
        try:
            number = int(user_input)
            if number >= 12:
                return number  # valid input, exit function
            else:
                print("Please enter a number greater than 12.")
        except ValueError:
            print("That's not a valid length (number). Please try again.")

def generate_pswd(length = 1, constrains = ["","","",""]):
    valid_answers = {"yes": True, "y": True, "no": False, "n": False}
    options_bool = [valid_answers.get(opt.lower(), False) for opt in constrains]
    
    char_pool = ""
    if options_bool[0]:  # uppercase
        char_pool += string.ascii_uppercase
    if options_bool[1]:  # lowercase
        char_pool += string.ascii_lowercase
    if options_bool[2]:  # digits
        char_pool += string.digits
    if options_bool[3]:  # special characters
        char_pool += string.punctuation
    
    if not char_pool:
        #raise ValueError("No character sets selected. At least one option must be 'yes'.")
        print("Password cannot be generated with no set of characters selected")
        return ""
    
    return ''.join(random.choice(char_pool) for _ in range(length))
    
def password_constraints():
    retVal = []
    valid_answers = {"yes": "yes", "y": "yes", "no": "no", "n": "no"}
    questions = ["Upercases: ", "Lowercases: ", "Numbers: ", "Special characters: "]
    
    print("Now, choose characters to be included in your password.")
    print('Answer with "yes"/"y" or "no"/"n".')
    
    for q in questions:
        while True:
            answer = input(f"{q}").strip().lower()
            if answer in valid_answers:
                retVal.append(valid_answers[answer])  # normalized
                break
            else:
                print("Invalid input. Please enter 'yes'/'y' or 'no'/'n'.")
    return retVal

def new_password():
    length = check_length()
    choice = password_constraints()
    pswd = generate_pswd(length, choice)
    if pswd == "":
        pass
    else:
        print(f"Your password is: {pswd}")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            new_password()
        elif choice == '2':
            show_information()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
