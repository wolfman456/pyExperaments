import random

from util.acii import HANGMANPICS

chosen_word = ""
word_len = 0
word_arr = []
live = 0


def get_word():
    global chosen_word, word_len
    word_list = ['dog', 'cat', 'elephant', 'sheep']
    chosen_word = random.choice(word_list)
    word_len = len(chosen_word)
    print(chosen_word)
    create_blank_word()
    return chosen_word


def check_word(guess):
    global chosen_word, live, word_arr
    if guess not in chosen_word:
        live = live + 1
    else:
        count = 0
        for letter in chosen_word:
            if letter == guess:
                word_arr[count] = guess
            count += 1
    print(word_arr)


def create_blank_word():
    global word_arr
    for i in range(word_len):
        word_arr.append('_')
    print(word_arr)


def game_over_check(running):
    global live, word_arr, chosen_word
    print(HANGMANPICS[live])
    if live == 6:
        print("You lost!")
        running = False
        return running
    if '_' not in word_arr:
        print("You won!")
        running = False
        return running
