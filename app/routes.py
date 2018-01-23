from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
import pprint
pp = pprint.PrettyPrinter(indent=4)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jay'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # validate_on_submit runs when POST with form data and checks validations
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    # pp.pprint(form.username.errors)
    return render_template('login.html', title='Sign In', form=form)
