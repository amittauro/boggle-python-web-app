class Boggle:
    def __init__(self, board, dictionary):
        self.board = board
        self.dictionary = dictionary

    def find_words(self):
        words = []
        for word in self.dictionary:
            if len(word) < 4:
                continue
            first_letter = word[0]
            for boggle_row in range(4):
                for boggle_col in range(4):
                    if self.board[boggle_row][boggle_col]  == first_letter:
                        positions = [[boggle_row, boggle_col]]
                        if self._solve(word, first_letter, 1, boggle_row, boggle_col, positions):
                            words.append(word)

        return words

    def _solve(self, string, soFar, index, x, y, positions):
        if soFar == string:
            return True

        for row in range(x - 1, x + 2):
            for col in range(y - 1, y + 2):
                if self._is_safe(row, col, string[index], positions):
                    positions.append([row, col])
                    if self._solve(string, soFar + string[index], index + 1, row, col, positions):
                        return True

        positions.pop()
        return False

    def _is_safe(self, row, col, letter, positions):
        if row < 0 or col < 0:
            return False
        elif row > 3 or col > 3:
            return False
        elif [row, col] in positions:
            return False
        elif self.board[row][col] == letter:
            return True
        return False
