import random

running = True


def start():
    cave_gen = random.randint(1, 2)


def main():
    global running
    while running:
        name = input("What is your name? \n")
        answer = input(F"Would you like to play a game {name}? (y/n) \n")
        if answer == "y":
            print(f"Great lets get going {name}")
            start()
        elif answer == "n":
            print("Sorry to hear that, goodbye.")
            running = False


if __name__ == '__main__':
    main()
