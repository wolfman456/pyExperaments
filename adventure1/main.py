import random

running = True


def start():
    return input("You enter a cave there are two branching paths before you, one to the left and one to the right. \n"
                 "do you want to go in to the left or to the right cave? (right or left) \n")


def left_cave(ran):
    if ran == 1:
        print("You Enter the left branching path of the cave."
              "\n There is a creaking sound from the sealing and it smell damp and moldy,\n"
              "but otherwise everything seem to be okay. \n"
              "you can make out a light at the end of the tunnel a you proceed.")
    else:
        print("You Enter the left branching path of the cave."
              "\n There is a creaking sound from the sealing and it smell damp and moldy.\n"
              "All of a sudden the sealing collapses and crushes you!")
        game_over("dead")


def right_cave(ran):
    play_again()


def central_cave(ran):
    print("here")
    play_again()


def left_door(ran):
    play_again()


def right_door(ran):
    play_again()


def game_over(alive_or_dead):
    if alive_or_dead.lower() == "alive":
        print("You won!")
        play_again()
    else:
        print("You lost!")
        play_again()


def play_again():
    global running
    answer = input("Do you want to play again? (yes or no)")
    if "y" == answer.lower() == "yes":
        main()
    else:
        running = False


def main():
    global running
    while running:
        name = input("What is your name? \n")
        answer = input(F"Would you like to play a game {name}? (y/n) \n")
        if answer.lower() == "y":
            print(f"Great lets get going {name}")
            answer = start()
            ran = random.randint(1, 2)
            if answer.lower() == "r" or 'right' == answer.lower():
                right_cave(ran)
                answer = central_cave(ran)
                if "right" == answer.lower == "r":
                    right_door(ran)
                else:
                    left_door(ran)
            elif answer.lower() == "l" or 'left' == answer.lower():
                left_cave(ran)
                answer = central_cave(ran)
                if answer.lower == "r" or "right" == answer.lower():
                    right_door(ran)
                else:
                    left_door(ran)

        elif answer.lower() == "n":
            print("Sorry to hear that, goodbye.")
            running = False


if __name__ == '__main__':
    main()
