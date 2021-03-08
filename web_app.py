from flask import Flask, session, redirect, url_for, request, render_template, flash
from board import Board
from words import Words
from dictionary import Dictionary
from boggle import Boggle
words = Words()
board=Board().create()
dictionary = Dictionary().read_dict_text_file()
boggle = Boggle(board, dictionary)
boggle.words()
app = Flask(__name__)

app.secret_key = b"\xa3\nI\xe2N'\r\xe0\xf0$\xf4\xfc\x7f\xa5\xd9\x14"

@app.route('/')
@app.route('/<board>')
def index(board=board):
    return render_template('index.html', board=board)

@app.route('/scores', methods=['POST', 'GET'])
@app.route('/scores<board><comp_words><comp_score><user_words><user_score>')
def scores(board=board, comp_words=None, comp_score=None, user_words=None, user_score=None):
    if request.method == 'POST':
        user_word = request.form['word']
        if user_word.upper() not in boggle.found_words:
            flash('Word not valid try again')
        else:
            flash('Nice! Keep going')
            words.add_word(request.form['word'])
        return redirect(url_for('index'))
    else:
        comp_words = boggle.found_words
        comp_score = boggle.score(comp_words)
        user_words = words.show_words()
        user_score = boggle.score(user_words)
        return render_template('scores.html', board=board, comp_words=comp_words, comp_score=comp_score, user_words=user_words, user_score=user_score)
