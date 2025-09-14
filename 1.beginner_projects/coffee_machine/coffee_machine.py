'''
    File Name: coffee-machine.py
    Version: 1.2.1
    Date: 14/09/2025
    Author: Pablo Bartolomé Molina
'''

# Menu of the coffee machine, with needed ingredients and their price.
menu = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 20,
        },
        "price": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 150,
            "milk": 200,
            "coffee": 25,
        },
        "price": 2.5,
    },
    "capuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 25,
        },
        "price": 3.0,
    }
}

resources = {
# Initial resources of the coffee machine
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,
    "money": 0
}

def payment(order):
    print(f"Pay ${menu[order]['price']}\n")

    print("Insert coins")
    total = int(input("Insert 1 euro pieces: "))
    if total < menu[order]['price']:
        total = total + int(input("Insert 2 euro pieces: "))
        if total < menu[order]['price']:
            total = total + int(input("Insert 50 cents pieces: "))
            if total < menu[order]['price']:
                total = total + int(input("Insert 20 cents pieces: "))
                if total < menu[order]['price']:
                    total = total + int(input("Insert 10 cents pieces: "))
                    if total < menu[order]['price']:
                        total = total + int(input("Insert 5 cents pieces: "))
    if total == menu[order]['price']:
        resources['water'] = resources['water'] - menu[order]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - menu[order]['ingredients']['coffee']
        resources['milk'] = resources['milk'] - menu[order]['ingredients']['milk']
        resources['money'] = resources['money'] + menu[order]['price']
        print("Transaction successful. Here is your coffee!")
    elif total > menu[order]['price']:
        change = total - menu[order]['price']
        print(f"You have inserted extra coins. Here is your change €{change}\n")
    else:
        print("Payment not complete. Cannot process order")

def main():
    end = False    
    while end != True:
        order = input("\nWhat would you like to order?\nCappuccino, Latte or Espresso?\n").lower()
        
        # Check if user's input is in the menu or not to continue with the program.
        if order not in menu:
            print("Sorry, that's not on the menu.")
        else:
            print(f"You chose {order}. Price: {menu[order]['price']}€")

        # Special inputs for maintenance.
        if order == 'off':
            end = True
        elif order == 'report':
            print(f"We have the following resources:\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g \nMoney: ${resources['money']}")
        elif resources['water'] >= menu[order]['ingredients']['water']:
            if resources['milk'] >= menu[order]['ingredients']['milk']:
                if resources['coffee'] >= menu[order]['ingredients']['coffee']:
                    payment(order)

                else:
                    print("\nResources insufficient! There is not enough coffee!\n")
            else:
                print("\nResources insufficient! There is not enough milk!\n")
        else:
            print("\nResources insufficient! There is not enough water!\n")

if __name__ == "__main__":
    main()
