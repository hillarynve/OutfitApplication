import random

def get_random_option(options):
    return random.choice(options)

def main():
    options = ["red", "orange", "yellow", "green", "blue", "purple", "orange"]

    print("Available options:", ", ".join(options))

    user_input = input("Do you want to pick a random color? (yes/no): ").strip().lower()

    if user_input == 'yes':
        random_choice = get_random_option(options)
        print(f"Randomly chosen color: {random_choice}")
    else:
        print("No color was chosen. ")

if __name__ == "__main__":
    main()