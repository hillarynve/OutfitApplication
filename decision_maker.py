import random

def get_random_option(options):
    return random.choice(options)

def main():
    options = {'top': ["red top", "blue top", "orange shirt", "beige cardigan", "collared shirt"],
               'bottom': ["yellow pants", "purple skirt", "jeans", "pleated skirt", "tiered skit", "gym shorts"],
               'shoes': ["white shoes", "black boots"],
               'fullbody': ["orange dress", "red dress", "jumpsuit"]
               }

    # Initial prompt
    print("Are you trying to pick an outfit today? (y/n)")
    pick_outfit_today = input().strip().lower()
    
    if pick_outfit_today != 'y':
        print("Have a nice day!")
        return
    
    while True:
        outfit_choice = input("Do you want a two-piece or one-piece outfit?(one/two): ").strip().lower()
    
        if outfit_choice == 'one':
            # randomly choose a top, bottom, and shoes
            top_choice = get_random_option(options['top'])
            bottom_choice = get_random_option(options['bottom'])
            shoes_choice = get_random_option(options['shoes'])
            print(f"Today's outfit is: the {top_choice} and {bottom_choice} paired with the {shoes_choice}")
            break
        elif outfit_choice == 'two':
            # randomly choose a fullbody outfit
            fullbody_choice = get_random_option(options['fullbody'])
            shoes_choice = get_random_option(options['shoes'])
            print(f"Today's outfit is: the {fullbody_choice} paired with the {shoes_choice}")
            break
        else:
            print("Please enter 'one' or 'two.")

    print("Enjoy today's outfit!")

if __name__ == "__main__":
    main()