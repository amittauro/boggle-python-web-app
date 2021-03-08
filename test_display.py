from display import Display
from dictionary import Dictionary

def test_board():
    board = [
      ['h', 'a', 'a', 'a'],
      ['e', 'l', 'a', 'a'],
      ['a', 'p', 'l', 'a'],
      ['a', 'f', 'u', 'a']
    ]
    output = 'h|a|a|a\ne|l|a|a\na|p|l|a\na|f|u|a\n'
    display = Display()
    assert display.print_board(board) == output

def test_first_dict():
    dictionary = Dictionary()
    dictionary.read_dict_text_file()
    assert dictionary.dictionary[0] == 'AA'

def test_last_dict():
    dictionary = Dictionary()
    dictionary.read_dict_text_file()
    assert dictionary.dictionary[-1] == 'ZYZZYVAS'
