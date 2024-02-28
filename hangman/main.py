from util.game_util import get_word, check_word


def main():
    get_word()
    running = True
    while running:
        guess = input("Guess a letter: ")
        check_word(guess)


if __name__ == "__main__":
    main()
