def get_word_list():
    word_list = []
    with open("/home/bloodwolf/project/python/pyExperaments/hangman/word_list.txt", "r") as word_string:
        line = word_string.read()
        for i in line.split("\n"):
            word_list.append(i)
        return word_list
