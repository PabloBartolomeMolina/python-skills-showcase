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

def substraction(a = 0, b = 0):
    print(f"Substraction result of {a}-{b} is {a-b}")
    
def multiplication(a = 0, b = 1):
    print(f"Addition result of {a}/{b} is {a/b}")

def division(a = 0, b = 0):
    print(f"Addition result of {a}*{b} is {a*b}")

def user_menuChoice():
    while True:
        user_input = input("Enter your choice: ")
        try:
            number = int(user_input)
            return number
            break
        except ValueError:
            print("That's not a valid choice (number). Please try again.")
    
def main():
    todo_list = []
    while True:
        display_menu()
        choice = user_menuChoice()
        
        if choice == 1:
            addition()
        elif choice == 2:
            substraction()
        elif choice == 3:
            multiplication()
        elif choice == 4:
            division()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
