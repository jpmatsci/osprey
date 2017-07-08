'''
Osprey is a package used to make a basic homepage
it has a tree based model with only a handfull of generic pages
The pages are: A top level page(index), a Subsection page,
    An article page, and an admin page for making/managing pages and subsections.
The article pages are written in the admin page using a markup
language.  I know there are a number of these packages out there
but I wanted to write one from scratch for the learning experience.
This is going to be a open source package but is really just for my
own benifit as a learning experience.
'''

from flask import Flask, request, session, g, redirect, url_for, send_from_directory, \
     abort, render_template, flash, escape
import json
from functools import wraps
from utilites import dotdict
from utilites import ospdb
import os
from os import listdir
import time

db = ospdb('OSP')

app = Flask(__name__)
#this will be changed before going live **********************
# add a parse section later for the secret key and the admin login
# app.secret_key = parse_settings
admin, pw = ('admin', '1234')
app.secret_key = 'b=5TsfYH(2g{J:#'

#login required wrapper
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logintime' in session:
            logintime = session['logintime']
            #if the logintime cookie is a not today then force logout
            if logintime != str(date.today()):
                logout()
        if 'username' in session:
            return f(*args, **kwargs)
        else:
            flash('You must login')
            return redirect(url_for('login'))
    return wrap

#clear cookies on logout
def logout():
    for key in session.keys():
        session.pop(key)
    return redirect(url_for('login'))


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        #wait 5 sec on all login requests
        time.sleep(5000)
        admin = request.form('username')
        pw = reuqest.form('password')
        if admin == uname and pw == admin_pw:
           session['username'] = uname
           redirect(url_for('administration'))
        else:
            flash('Invalid Credentials')
    return render_template('login.html')

@login_required
@app.route('/administration'):
def administration();
    articles = []
    article_iterator = iter_query('SELECT TITLE FROM ARTICLES')
    for article in article_iterator:
        articles.append(article)
    subsections = []
    subsection_iterator = iter_query('SELECT TITLE FROM SUBSECTIONS')
    for subsection in subsection_iterator:
        subsections.append(subsection)
    if request.method == 'POST':
        request.form('type')
        request.title('title')
        if ptype == 'subsection':
            if title in subsections
                flash('Title already in use')
                return url_for('administration')
        if ptype == 'article':
            if title in articles:
                flash('Title already in use')
                return url_for('administration')
    return render_template('admin.html', articles=articles, subsections=subsections)

@app.route('/', methods = ['GET', 'POST'])
def index():
    page_data = dotdict({})
#remove next line after testing
    image_dir = listdir('static/images/')
#next get subsections and most recent articles
    page_data['subs'] = get_subsections()
    page_data['recent'] = get_recent()
#next two lines for testing
    if request.method == "POST":
        page_data['text'] = request.form['text']
    return render_template('writepage.html', image_dir=fake_dir)

def get_subsections():
    subs = []
    sub_query = db.iter_query('SELECT TITLE FROM SUBSECTIONS')
    for sub in sub_query:
        subs.append(sub)
    return subs

def get_recent():
    articles = []
    article_query = db.iter_query('SELECT TITLE FROM ARTICLES ORDER BY DATE DESC LIMIT 5')
    for article in article_query:
        articles.append(article)
    return articles


if __name__ == '__main__':
	app.run(debug = True, host='localhost')

