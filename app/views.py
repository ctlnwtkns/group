from flask import render_template, flash, redirect, url_for, request
from app import app
from .forms import LoginForm
from collections import Counter
import random
import time

c = Counter({'health': 100, 'hunger': 0, 'stash': ''})

@app.route('/')
def home():
    return redirect('/index')
    
@app.route('/index', methods=['GET', 'POST'])           
def index():
    form = LoginForm()
    error = None
    if request.method == 'POST':
        if request.form['name'] == None:
            error = 'Please enter your name.'
        else:
            return redirect('/greet')
    return render_template('index.html', 
                            title='Index',
                            form=form
                           )

@app.route('/greet')
def greet():
    name = 'Caitlin'
    return render_template( 'greet.html', 
    						title='Greetings',
                            name=name,
                            health=c['health'],
                            hunger=c['hunger'],
                            stash=c['stash']
                          )

@app.route('/intro')
def intro():
    c.update({'health': random.randint(-20, -1), 'hunger': random.randint(1,10)})
    return render_template('intro.html',
                            title='Intro',
                            health=c['health'],
                            hunger=c['hunger'],
                            stash=c['stash']
                          )

@app.route('/hatchet')
def hatchet():
    c.clear()
    c.update({'health': (100 - random.randint(1,10)), 'hunger':random.randint(1,20), 'stash':'hatchet'})
    return render_template('hatchet.html',
                            title='Hatchet',
                            health=c['health'],
                            hunger=c['hunger'],
                            stash=c['stash']
                          )

@app.route('/apples')
def apples():
    name = 'Caitlin'
    c.update({'health': -100, 'hunger':0, 'stash':'Applesauce'})
    return render_template('apples.html',
                            title = 'Apples',
                            name=name,
                            health=c['health'],
                            hunger=c['hunger'],
                            stash=c['stash']
                          )

@app.route('/river')
def river():
    return render_template('river.html',
                            title='River')

@app.route('/mushrooms')
def mushrooms():
    return render_template('mushrooms.html',
                            title='Mushrooms')

