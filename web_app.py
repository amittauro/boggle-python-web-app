from flask import Flask, session, redirect, url_for, request, render_template, flash
from board import Board
from dictionary import dictionary
from boggle import Boggle
from score import score, word_score

app = Flask(__name__)

app.secret_key = b"\xa3\nI\xe2N'\r\xe0\xf0$\xf4\xfc\x7f\xa5\xd9\x14"

@app.route('/')
def index(board=None):
    board = Board().create()
    session['board'] = board
    boggle = Boggle(board, dictionary)
    session['comp_words'] = boggle.find_words()
    session['user_words'] = []
    return render_template('index.html', board=session['board'])

@app.route('/play')
def play(board=None):
    board = session['board']
    return render_template('play.html', board=board)

@app.route('/words', methods=['POST'])
def words():
    user_word = request.form['word']
    if len(user_word) < 4:
        flash('Minimum word length: 4')
    elif user_word.upper() not in session['comp_words']:
        flash('Word not valid try again')
    else:
        flash('Nice! Keep going')
        session['user_words'].append(user_word.upper())
    return redirect(url_for('play'))

@app.route('/scores')
def scores(board=None, comp_words=None,
comp_score=None, user_words=None, user_score=None):
    board = session['board']
    comp_words = session['comp_words']
    user_words=session['user_words']
    comp_score = score(comp_words, word_score)
    user_score = score(user_words, word_score)
    return render_template('scores.html', board=board, comp_words=comp_words,
    comp_score=comp_score, user_words=user_words, user_score=user_score)
