class Boggle:
    def __init__(self, board, dictionary):
        self.board = board
        self.dictionary = dictionary
        self.found_words = []

    def play(self):
        self.words()
        user_input = ''
        user_words = []
        print('Boggle!')
        self.print_board()
        print("enter words and click enter after each word. When finished and type: 'get results' to view all possible words")
        while user_input != 'get results':
            user_input = input()
            if user_input == 'get results':
                break
            elif user_input not in self.found_words:
                print('incorrect word try again')
            else:
                user_words.append(user_input)

        print('your words:')
        print(user_words)
        print('your score:')
        self.score(user_words)
        print('computer words:')
        print(self.found_words)
        print('computer score')
        self.score(self.found_words)

    def score(self, words):
        word_scores = list(map(self.word_to_score, words))
        print(sum(word_scores))

    def word_to_score(self, word):
        if len(word) > 7:
            return 11
        scores = { 4: 1, 5: 2, 6: 3, 7: 4 }
        return scores[len(word)]

    def words(self):
        words = 0
        for word in self.dictionary:
            if len(word) < 4:
                continue
            first_letter = word[0]
            for boggle_row in range(4):
                for boggle_col in range(4):
                    if self.board[boggle_row][boggle_col]  == first_letter:
                        positions = [[boggle_row, boggle_col]]
                        if self.solve(word, first_letter, 1, boggle_row, boggle_col, positions):
                            words += 1

        return words

    def solve(self, string, soFar, index, x, y, positions):
        if soFar == string:
            self.found_words.append(string)
            return True

        for row in range(x - 1, x + 2):
            for col in range(y - 1, y + 2):
                if self.is_safe(row, col, string[index], positions):
                    positions.append([row, col])
                    if self.solve(string, soFar + string[index], index + 1, row, col, positions):
                        return True

        positions.pop()
        return False

    def is_safe(self, row, col, letter, positions):
        if row < 0 or col < 0:
            return False
        elif row > 3 or col > 3:
            return False
        elif [row, col] in positions:
            return False
        elif self.board[row][col] == letter:
            return True
        return False

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
