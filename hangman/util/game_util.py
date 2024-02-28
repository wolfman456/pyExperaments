import random

chosen_word = ""
word_len = 0
word_arr = []


def get_word():
    global chosen_word, word_len
    word_list = ['dog', 'cat', 'elephant', 'sheep']
    chosen_word = random.choice(word_list)
    word_len = len(chosen_word)
    print(chosen_word)
    create_blank_word()
    return chosen_word


def check_word(guess):
    global chosen_word
    for letter in chosen_word:
        if letter == guess:
            print('correct')
        else:
            print('wrong')


def create_blank_word():
    global word_arr
    for i in range(word_len):
        word_arr.append('_')
    print(word_arr)
