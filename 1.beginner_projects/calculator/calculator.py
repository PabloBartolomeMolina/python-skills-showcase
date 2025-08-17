'''
    File Name: calculator.py
    Version: 1.0.0
    Date: 12/08/2025
    Author: Pablo Bartolomé Molina
'''

def display_menu():
    print("\nCalculator Application")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def addition(a = 0, b = 0):
    print(f"Addition result of {a}+{b} is {a+b}")
    return a+b

def substraction(a = 0, b = 0):
    print(f"Substraction result of {a}-{b} is {a-b}")
    return a-b
    
def multiplication(a = 0, b = 1):
    print(f"Addition result of {a}*{b} is {a*b}")
    return a*b

def division(a = 0, b = 0):
    if b == 0:
        print("Cannot divide by 0")
    else:
        print(f"Addition result of {a}/{b} is {a/b}")
        return a/b

def user_menuChoice():
    while True:
        user_input = input("Enter your choice: ")
        try:
            number = int(user_input)
            return number
            break
        except ValueError:
            print("That's not a valid choice (number). Please try again.")

def user_number():
    while True:
        user_input = input("Enter a number: ")
        try:
            number = float(user_input)  # accepts integers, floats, and negatives
            return number
            break
        except ValueError:
            print("That's not a valid number. Please try again.")

def user_reuse():
    while True:
        user_input = input("Reuse the result (y/n)? ")
        if (user_input == 'y') or (user_input == 'n'):
            return user_input
            break
        else:
            print("That's not a valid answer. Please try again.")
            
def main():
    op_idx = 0
    c = 0.0
    reuse = 'n'
    while True:
        display_menu()
        choice = user_menuChoice()
        
        if (choice > 0) and (choice < 5):
            if op_idx > 0:
                reuse = user_reuse()
            else:
                reuse = 'n'
            if reuse == 'n':
                a = user_number()
            else:
                a = c
            b = user_number()
        
        if choice == 1:
            c = addition(a, b)
            op_idx = op_idx + 1
        elif choice == 2:
            c = substraction(a, b)
            op_idx = op_idx + 1
        elif choice == 3:
            c = multiplication(a, b)
            op_idx = op_idx + 1
        elif choice == 4:
            c = division(a, b)
            op_idx = op_idx + 1
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
