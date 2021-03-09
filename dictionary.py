class Dictionary:
    def __init__(self):
        self.dictionary = []

    def read_dict_text_file(self):
        f = open("dictionary-yawl.txt", "r")
        for x in f:
            self.dictionary.append(x[0:-1])
        return self.dictionary

dictionary = Dictionary().read_dict_text_file()
