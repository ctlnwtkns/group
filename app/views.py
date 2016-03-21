from flask import render_template, flash, redirect, url_for, request
from app import app
from .forms import LoginForm

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
                            name=name
                          )

@app.route('/intro')
def intro():
    return render_template('intro.html',
                            title='Intro')

@app.route('/hatchet')
def hatchet():
    return render_template('hatchet.html',
                            title='Hatchet')

@app.route('/apples')
def apples():
    name = 'Caitlin'
    return render_template('apples.html',
                            title = 'Apples',
                            name=name
                          )

@app.route('/river')
def river():
    return render_template('river.html',
                            title='River')

@app.route('/mushrooms')
def mushrooms():
    return render_template('mushrooms.html',
                            title='Mushrooms')

