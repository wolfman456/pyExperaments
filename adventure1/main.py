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
    if ran == 2:
        print("You Enter the right branching path of the cave and you are crushed by a trolls club")
        game_over("dead")
    else:
        print("You Enter the right branching path of the cave and you see a light coming from the other end.")


def central_cave(ran):
    print("here")
    if ran == 1:
        print("You Enter the a brightly light cavern with two doors guarded by a dragon. The dragon spots you and "
              "bathes you in fire. You are dead")
        game_over("dead")
    else:
        return input(
            "You Enter the a brightly light cavern with two doors, one on the left and one on the right. Which door \n"
            "do you want to go in to the left or to the right")


def left_door(ran):
    if ran == 1:
        print("You Enter the the left door and find a mountain of treasure.")
        game_over("alive")
    else:
        print(
            "You Enter the left door and find a mountain of of treasure guarded by a dragon. The dragon spots you and "
            "\n eats you in one bite.")
        game_over("dead")


def right_door(ran):
    if ran == 1:
        print("You Enter the the left door and find a mountain of treasure.")
        game_over("alive")
    else:
        print(
            "You Enter the left door and find a mountain of of treasure guarded by a dragon. The dragon spots you and "
            "\n eats you in one bite.")
        game_over("dead")


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
