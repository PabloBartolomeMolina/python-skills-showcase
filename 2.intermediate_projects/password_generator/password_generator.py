'''
    File Name: password_generator.py
    Version: 1.1.1
    Date: 19/08/2025
    Author: Pablo Bartolomé Molina
'''

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
    print("\nTPassword Generator")
    print("1. New Password")
    print("2. Information")
    print("3. Exit")

def show_information():
    print(info)

def check_length():
    while True:
        user_input = input("Enter wanted length for the password: ")
        try:
            number = int(user_input)
            if number > 0:
                return number  # valid input, exit function
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("That's not a valid length (number). Please try again.")

def get_user_pswd():
    user_text = ""
    print("Find here the constraints for your password")
    print(constraints_info)
    while user_text == "":
        user_text = input("Enter your password: ")
        if user_text == "":
            print("Your password is empty, enter a valid password.")
        else:
            break
    return user_text
    
def password_constraints(pswd = "", lenght = 1):
    pass

def new_password():
    check_length()
    pswd = get_user_pswd()
    password_constraints(pswd)

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
