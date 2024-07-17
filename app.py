import database

MENU_PROMPT = """-- Outfit Styling App --

Please choose one of these options:

1) Add a new clothing item.
2) See all clothing items.
3) Find a clothing item by name.
4) See what color a clothing item is.
5) Delete a clothing item by name.
6) Exit

Your Selection: """

def menu():
    connection = database.connect()
    database.create_tables(connection)

    while(user_input := input(MENU_PROMPT)) != "6":
        if user_input == "1":
            name = input("Enter the clothing item's name: ")
            body_location = input("Enter the clothing item's body location: ")
            clothing_type = input("Enter the clothing item's type: ")
            color_pattern = input("Enter the clothing item's color: ")
            fashion_type = input("Enter the clothing item's fashion style: ")
            database.add_clothes(connection, name, body_location, clothing_type, color_pattern, fashion_type)
        elif user_input == "2":
            clothing = database.get_all_clothes(connection)

            print("The wardrobe contains: ")
            for item in clothing:
                print(f"{item[1]} in a {item[5]} style.")
        elif user_input == "3":
            name = input("Enter the clothing item's name to find: ")
            clothing = database.get_clothes_by_name(connection, name)

            for item in clothing:
                print(f"{name} in {fashion_type} style")
        elif user_input == "4":
            name = input("Enter the clothing item's name to find: ")
            color_option = database.get_color_pattern_for_clothes(connection, name)

            print(f"The color or pattern of the {name} is {color_option[0]}")
        elif user_input == "5":
            name = input("Enter the name of the clothing item to delete: ")
            database.delete_clothing_by_name(connection, name)
            print(f"Deleted clothing item '{name}' successfully.")
        else:
            print("Invalid input. Please try again!")
menu()