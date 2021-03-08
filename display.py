class Display:
    def print_board(self, board):
        for row in board:
            print('|'.join(row))
