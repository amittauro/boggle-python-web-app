from dictionary import Dictionary
from boggle import Boggle
from board import Board
import display

board = Board().create()
dictionary = Dictionary().read_dict_text_file()
boggle = Boggle(board, dictionary)
boggle.play()
