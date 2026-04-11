# Simple menu-driven program in Python

def show_menu():
    """Displays the menu options to the user."""
    print("\nMenu:")
    print("1. Yes / No Check")
    print("2. Compare Two Numbers")
    print("3. Work with Text")
    print("4. Exit")


# Boolean variable to control the menu loop
running: bool = True

while running:
    # Display the menu to user
    show_menu()

    # Get user's choice
    choice: str = input("Please enter your choice (1-4): ").strip()

    # Validate menu input
    if not choice.isdigit():
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    choice = int(choice)

    # Option 1: Yes / No Check
    if choice == 1:
        user_answer: str = input("Please enter yes or no: ").strip().lower()

        # Validate yes/no input
        if user_answer not in ["yes", "no"]:
            print("Invalid response. Please type 'yes' or 'no'.")
            continue

        # Boolean created from comparison
        is_yes: bool = (user_answer == "yes")

        if is_yes:
            print("You answered YES — the boolean value is True.")
        else:
            print("You answered NO — the boolean value is False.")

    # Option 2: Compare Two Numbers
    elif choice == 2:
        first_num_str: str = input("Enter the first number: ").strip()
        second_num_str: str = input("Enter the second number: ").strip()

        # Validate numeric input
        if not (first_num_str.replace('.', '', 1).isdigit() and
                second_num_str.replace('.', '', 1).isdigit()):
            print("Invalid input. Please enter valid numbers.")
            continue

        first_num: float = float(first_num_str)
        second_num: float = float(second_num_str)

        # Boolean comparisons
        is_greater: bool = first_num > second_num
        is_equal: bool = first_num == second_num

        if is_equal:
            print(f"{first_num} and {second_num} are equal.")
        elif is_greater:
            print(f"{first_num} is greater than {second_num}.")
        else:
            print(f"{first_num} is less than {second_num}.")

    # Option 3: Work with Text
    elif choice == 3:
        text: str = input("Enter some text: ").strip()

        # Use string methods
        upper_text: str = text.upper()
        lower_text: str = text.lower()
        text_length: int = len(text)

        print("\nText Results:")
        print(f"Original text: {text}")
        print(f"Uppercase: {upper_text}")
        print(f"Lowercase: {lower_text}")
        print(f"Number of characters: {text_length}")

        # Boolean example: check if text contains a space
        has_space: bool = (" " in text)

        if has_space:
            print("Your text contains at least one space.")
        else:
            print("Your text does not contain any spaces.")

    # Option 4: Exit Program
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        running = False

    # Invalid Menu Choice
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")