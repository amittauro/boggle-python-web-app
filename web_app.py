from flask import Flask, session, redirect, url_for, request, render_template, flash
from board import set_board
from dictionary import Dictionary
from boggle import Boggle

dictionary = Dictionary().read_dict_text_file()
boggle = Boggle(set_board, dictionary)
comp_words = boggle.find_words()
user_words = []
app = Flask(__name__)

app.secret_key = b"\xa3\nI\xe2N'\r\xe0\xf0$\xf4\xfc\x7f\xa5\xd9\x14"

@app.route('/')
def index(board=set_board):
    return render_template('index.html', board=set_board)

@app.route('/words', methods=['POST'])
def words():
    user_word = request.form['word']
    if user_word.upper() not in comp_words:
        flash('Word not valid try again')
    else:
        flash('Nice! Keep going')
        user_words.append(user_word.upper())
    return redirect(url_for('index'))

@app.route('/scores')
def scores(board=set_board, comp_words=comp_words,
comp_score=None, user_words=user_words, user_score=None):
    comp_score = boggle.score(comp_words)
    user_score = boggle.score(user_words)
    return render_template('scores.html', board=set_board, comp_words=comp_words,
    comp_score=comp_score, user_words=user_words, user_score=user_score)
