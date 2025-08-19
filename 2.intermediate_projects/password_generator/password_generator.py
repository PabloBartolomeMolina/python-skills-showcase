'''
    File Name: password_generator.py
    Version: 1.0.0
    Date: 19/08/2025
    Author: Pablo Bartolomé Molina
'''

def display_menu():
    print("\nTPassword Generator")
    print("1. New Password")
    print("2. Information")
    print("3. Exit")

def show_information():
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
    print(info)

def get_user_input():
    continue
    
def password_constraints():
    continue

def new_password():
    continue

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
