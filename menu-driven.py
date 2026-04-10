# Simple menu-driven program in Python

def show_menu():
    """Displays the menu options to the user."""
    print("Menu:")
    print("1. Yes / No Check")
    print("2. Compare Two Numbers")
    print("3. Work with Text")
    print("4. Exit")
    
    
# Boolean variable to control the menu loop
running: bool = True    

while running:
    # Display the menu to user
    show_menu()
    
    # Get users choice
    choice: str = input("Please enter your choice (1-4): ").strip()
    
    if not choice.isdigit():
        print("Invalid input. Please enter a number between 1 and 4.")
        continue
    
    choice: = int(choice)
    
    if choice == 1:
        #Handle Yes / No Check
        pass
    elif choice == 2:
        # Handle Compare Two Numbers
        pass
    elif choice == 3:
        # Handle Work with Text
        pass
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        running = False
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
