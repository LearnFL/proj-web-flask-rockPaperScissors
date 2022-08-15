from app import app
from flask import render_template, url_for, request, session, redirect
from app.helper import alist, adict, winner, loser, Game, count_computer, count_human

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():

    title = "Rock Paper Scissors"
    session['human_score'] = 0
    session['computer_score'] = 0

    return render_template('index.html', title=title)

@app.route('/game', methods=['GET', 'POST'])
def game():
    title = "Let the game begin"
    return render_template('game.html', title=title)

@app.route('/logic', methods=['GET', 'POST'])
def logic():
    title = "Let the game begin"
    human_choice = None
    if request.method == 'POST':
        if request.form['choice'] == 'rock':
            human_choice = 0
        elif request.form['choice'] == 'paper':
            human_choice = 1
        elif request.form['choice'] == 'scissors':
            human_choice = 2
        
        elif request.form['choice'] == 'clear':
            redirect('game.html')
            session.pop('human_score', default=None)
            session.pop('computer_score', default=None)
    try:  

        game = Game(human_choice, alist, adict, winner, loser, game=None)
        game()
        computer_choice = game.computer_choice
        message = game.message
        if game.who_won == 'human':
            session['human_score'] += 1
        elif game.who_won == 'computer':
            session['computer_score'] += 1

    except:
        session['human_score'] = 0
        session['computer_score'] = 0
        message = None
        computer_choice = None
    
    finally:
        redirect('game.html')

    return render_template('game.html', human_score=session['human_score'], computer_score = session['computer_score'] , title=title, message=message, computer_choice=computer_choice)

@app.route('/about', methods=['GET', 'POST'])
def about():
    title = "ABOUT"
    return render_template('about.html', title=title)
