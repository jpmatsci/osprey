'''
Osprey is a package used to make a basic homepage
it has a tree based model with only a handfull of generic pages
The pages are: A top level page(index), a Subsection page,
    An article page, and an admin/login page for making pages.
The article pages are written in the admin page using a markup
language.  I know there are a number of these packages out there
but I wanted to write one from scratch for the learning experience.
This is going to be a open source package but is really just for my
own benifit as a learning experience.
'''

from flask import Flask, request, session, g, redirect, url_for, send_from_directory, \
     abort, render_template, flash, escape
from functools import wraps
from utilites import dotdict
from utilites import ospdb
import os

app = Flask(__name__)
app.secret_key = 'b=5TsfYH(2g{J:#'

#login required wrapper
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logintime' in session:
            logintime = session['logintime']
            if logintime != str(date.today()):
                flash('You must login')
                return redirect(url_for('login'))
        if 'username' in session:
            return f(*args, **kwargs)
        else:
            flash('You must login')
            return redirect(url_for('login'))
    return wrap

@app.route('/', methods = ['GET', 'POST'])
def index():
    page_data = dotdict({})
    page_data['subs'] = get_subsections()
    page_data['articles'] = get_articles()
    if request.method == "POST":
        page_data['text'] = request.form['text']
    #return render_template('text.html', page_data=page_data)
    return render_template('csstest.html')

def get_subsections():
    return []

def get_articles():
    return []

def get_toppage():
    return []

if __name__ == '__main__':
	app.run(debug = True, host='localhost')

