# Function to get the price of a selected item
def get_price(item_number):
    if item_number == 1:
        return 2.50  # Price for Taco
    elif item_number == 2:
        return 3.75  # Price for Burrito
    elif item_number == 3:
        return 5.00  # Price for Nachos
    elif item_number == 4:
        return 1.50  # Price for Soft Drink
    return 0.0


# Function to get the name of the item
def get_item_name(item_number):
    if item_number == 1:
        return "Taco"
    elif item_number == 2:
        return "Burrito"
    elif item_number == 3:
        return "Nachos"
    elif item_number == 4:
        return "Soft Drink"
    return ""


# Function to display the menu options exactly as requested
def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")


def main():
    # Welcome message at the very start of the program execution
    print("Welcome to Taco Palace! Please view the menu below and make a selection:")

    ordered_items = []
    totalPrice = 0.0

    while True:
        print_menu()
        try:
            user_input = input("User entered: ")
            choice = int(user_input)
        except ValueError:
            print("Please enter a valid integer number.")
            continue

        # Option 5 to Quit/Checkout
        if choice == 5:
            # Joins items with "and" if multiple items exist to match prompt example output format
            if not ordered_items:
                print("\nYou ordered nothing. Your total is $0.00")
            else:
                items_str = " and a ".join(ordered_items)
                print(f"\nYou ordered a {items_str}. Your total is ${totalPrice:.2f}")
            break  # Exits the loop cleanly

        # Selection block for items 1 through 4
        elif 1 <= choice <= 4:
            item_name = get_item_name(choice)
            item_price = get_price(choice)

            ordered_items.append(item_name)
            totalPrice += item_price

            print(f"You selected a {item_name}")

        else:
            print("Invalid selection. Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()