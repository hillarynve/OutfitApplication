import database

MENU_PROMPT = """-- Outfit Styling App --

Please choose one of these options:

1) Add a new clothing item.
2) See all clothing items.
3) Find a clothing item by name.
4) See what color a clothing item is.
5) Exit

Your Selection: """

def menu():
    connection = database.connect()
    database.create_tables(connection)

    while(user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            name = ("Enter the clothing item's name: ")
            body_location = ("Enter the clothing item's body location: ")
            clothing_type = ("Enter the clothing item's type: ")
            color_pattern = ("Enter the clothing item's color: ")
            fashion_type = ("Enter the clothing item's fashion style: ")

            database.add_clothes(connection, name, body_location, clothing_type, color_pattern, fashion_type)
        elif user_input == "2":
            clothing = database.get_all_clothes(connection)

            for item in clothing:
                print(item)
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("Invalid input. Please try again!")
menu()

