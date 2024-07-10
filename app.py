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
            pass
        elif user_input == "2":
            pass
            pass
        elif user_input == "4":
            pass
        else:
            print("Invalid input. Please try again!")
menu()