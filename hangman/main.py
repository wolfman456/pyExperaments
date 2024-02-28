from util.game_util import get_word, check_word, game_over_check


def main():
    get_word()
    running = True
    while running:
        guess = input("Guess a letter: ")
        check_word(guess)
        game_over_check(running)



if __name__ == "__main__":
    main()
