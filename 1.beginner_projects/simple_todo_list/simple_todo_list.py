def display_menu():
    print("\nTodo List Application")
    print("1. Show todo list")
    print("2. Add todo item")
    print("3. Remove todo item")
    print("4. Exit")

def show_todo_list(todo_list):
    if not todo_list:
        print("\nYour todo list is empty.")
    else:
        print("\nTodo List:")
        for idx, item in enumerate(todo_list, 1):
            print(f"{idx}. {item}")

def add_todo_item(todo_list):
    item = input("Enter a new todo item: ").strip()
    if item:
        todo_list.append(item)
        print(f'"{item}" added to the list.')
    else:
        print("No item entered. Nothing added.")

def remove_todo_item(todo_list):
    show_todo_list(todo_list)
    if todo_list:
        try:
            index = int(input("Enter the number of the item to remove: "))
            if 1 <= index <= len(todo_list):
                removed = todo_list.pop(index - 1)
                print(f'"{removed}" removed from the list.')
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            show_todo_list(todo_list)
        elif choice == '2':
            add_todo_item(todo_list)
        elif choice == '3':
            remove_todo_item(todo_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
