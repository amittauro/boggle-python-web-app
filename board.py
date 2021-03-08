import random

class Board:
    def create(self):
        board = [
         'AAEEGN', 'ABBJOO', 'ACHOPS', 'AFFKPS',
         'AOOTTW', 'CIMOTU', 'DEILRX', 'DELRVY',
         'DISTTY', 'EEGHNW', 'EEINSU', 'EHRTVW',
         'EIOSST', 'ELRTTY', 'HIMNQU', 'HLNNRZ'
        ]
        board_shufl_cubes = list(map(self.pick_random_letter, board))
        random.shuffle(board_shufl_cubes)
        return list(self.chunk(board_shufl_cubes, 4))

    def pick_random_letter(self, word):
        return word[random.randrange(6)]

    def chunk(self, l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]

board = [
     ['F', 'Y', 'C', 'L'],
     ['I', 'O', 'M', 'G'],
     ['O', 'R', 'I', 'L'],
     ['H', 'J', 'H', 'U']
    ]

board_instance = Board()
set_board = board_instance.create()
