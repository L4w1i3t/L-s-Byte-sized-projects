import random

def russian_roulette():
    # Define the revolver's chamber size
    chamber_size = 6

    # Ask user how many bullets they want to load
    while True:
        try:
            bullets = int(input(f"How many bullets do you want to load? (1-{chamber_size}): "))
            if 1 <= bullets <= chamber_size:
                break
            else:
                print(f"Please enter a number between 1 and {chamber_size}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Create the revolver chamber and load the bullets
    chamber = [0] * chamber_size
    bullet_positions = random.sample(range(chamber_size), bullets)
    for pos in bullet_positions:
        chamber[pos] = 1

    # Spin the chamber
    random.shuffle(chamber)

    # Pull the trigger
    print("Spinning the chamber and pulling the trigger...")
    if chamber[0] == 1:
        print("Bang! You lost.")
        if bullets == 6:
            print("I don't know what you expected, given that you loaded 6 bullets...")
    else:
        print("Click! You win.")

russian_roulette()