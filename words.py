class Words:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word.upper())

    def show_words(self):
        return self.words
