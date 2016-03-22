from flask import render_template, flash, redirect, url_for, request
from app import app
from .forms import LoginForm
from collections import Counter
import random
import time

c = Counter({'health': 100, 'hunger': 0})
stash = []
backpack = range(len(stash))

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
                            stash=stash
                           )
@app.route('/intro')
def intro():
    c.update({'health': random.randint(-20, -1)})
    return render_template('intro.html',
                            title='Intro',
                            health=c['health'],
                            hunger=c['hunger'],
                            stash=stash
                          )

@app.route('/hatchet')
def hatchet():
    c.clear()
    c.update({'health': (100 - random.randint(1,10)), 'hunger':random.randint(1,20)})
    stash.append('hatchet')
    return render_template('hatchet.html',
                            title='Hatchet',
                            health=c['health'],
                            hunger=c['hunger'],
                            stash=stash
                          )

@app.route('/apples')
def apples():
    name = 'Caitlin'
    c.update({'health':(100 - random.randint(1,100)), 'hunger':0})
    stash.append('Applesauce')
    return render_template('apples.html',
                            title = 'Apples',
                            name=name,
                            health=c['health'],
                            hunger=c['hunger'],
                            stash=stash
                          )

@app.route('/river')
def river():
    c.update({'health':(100 - random.randint(1,100))})
    return render_template('river.html',
                            title='River',
                            health=c['health'],
                            hunger=c['hunger'],
                            stash=stash
                          )

@app.route('/blinded')
def blinded():
    c.update({'health':(100 - random.randint(1,100)), 'hunger':-25})
    return render_template('blinded.html',
                            title='Mushrooms',
                            health=c['health'],
                            hunger=c['hunger'],
                            stash=stash
                          )

@app.route('/gem')
def gem():
    c.update({'health':(100 - random.randint(1,100)),'hunger': 0})
    stash.append('gems')
    return render_template('gem.html',
                            title='Gems',
                            health=c['health'],
                            hunger=c['hunger'],
                            stash=stash
                          )


@app.route('/choir')
def Choir():
    c.update({'hunger':-25})
    return render_template('choir.html',
                            title='The Choir',
                            health=c['health'],
                            hunger=c['hunger'],
                            stash=stash
                          )

@app.route('/bear_trap')
def bear_trap():
    c.update({'health':(100 - random.randint(1,100)), 'hunger':0})
    return render_template('bear_trap.html',
                            title='Bear Trap',
                            health=c['health'],
                            hunger=c['hunger'],
                            stash=stash
                          )

@app.route('/turn')
def turn():
    c.update({'hunger':-25})
    return render_template('turn.html',
                            title='The Sound',
                            health=c['health'],
                            hunger=c['hunger'],
                            stash=stash
                          )
                    
