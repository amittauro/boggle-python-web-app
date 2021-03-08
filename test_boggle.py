from boggle import Boggle

def test_word():
    board = [
      ['h', 'a', 'a', 'a'],
      ['e', 'l', 'a', 'a'],
      ['a', 'p', 'l', 'a'],
      ['a', 'f', 'u', 'a']
    ]
    dictionary = ['helpful']
    boggle = Boggle(board, dictionary)
    assert boggle.words() == 1

def test_another_word():
    board = [
      ['a', 'a', 'a', 'a'],
      ['e', 'a', 'a', 'a'],
      ['h', 'e', 'p', 'a'],
      ['a', 'l', 'l', 'o']
    ]
    dictionary = ['hello']
    boggle = Boggle(board, dictionary)
    assert boggle.words() == 1

def test_route_word():
    board = [
    ['h', 'a', 'a', 'a'],
    ['a', 'p', 'l', 'l'],
    ['h', 'e', 'a', 'a'],
    ['a', 'l', 'l', 'o']
  ]
    dictionary = ['hello']
    boggle = Boggle(board, dictionary)
    assert boggle.words() == 1

def test_different_letters():
    board = [
    ['b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b'],
    ['m', 'a', 'd', 'b'],
    ['b', 'b', 'b', 'b']
  ]
    dictionary = ['madam']
    boggle = Boggle(board, dictionary)
    assert boggle.words() == 0

def test_multiple_words():
    board = [
    ['h', 'b', 'b', 'b'],
    ['e', 'l', 'l', 'o'],
    ['m', 'a', 'g', 'c'],
    ['b', 'b', 'i', 'b']
  ]
    dictionary = ['hello', 'magic']
    boggle = Boggle(board, dictionary)
    assert boggle.words() == 2

def test_false_word():
    board = [
     ['x', 'q', 'a', 'e'],
     ['z', 'o', 't', 's'],
     ['i', 'n', 'd', 'l'],
     ['y', 'r', 'u', 'k']
    ]
    def word_lower(word):
        return word.lower()
    dictionary = map(word_lower, ['SETS'])
    boggle = Boggle(board, dictionary)
    assert boggle.words() == 0

def test_boggle():
    board = [
     ['x', 'q', 'a', 'e'],
     ['z', 'o', 't', 's'],
     ['i', 'n', 'd', 'l'],
     ['y', 'r', 'u', 'k']
    ]
    def word_lower(word):
        return word.lower()
    dictionary = map(word_lower, ['XQAESLKURYIZ', 'DNOT', 'NIZOTS', 'KUDL', 'STONI', 'SEAT', 'ONIYR', 'ZONIY', 'MY', 'SEAN', 'SETS', 'TOO', 'DOT'])
    boggle = Boggle(board, dictionary)
    assert boggle.words() == 8

def test_boggle_2():
    board = [
     ['f', 'y', 'c', 'l'],
     ['i', 'o', 'm', 'g'],
     ['o', 'r', 'i', 'l'],
     ['h', 'j', 'h', 'u']
    ]
    dictionary = ['coif', 'coil', 'coir', 'corm', 'firm', 'giro', 'glim', 'hoof', 'iglu', 'limo', 'limy', 'miri', 'moil', 'moor', 'rimy', 'roil', 'hello', 'goodbye']
    boggle = Boggle(board, dictionary)
    assert boggle.words() == 16
