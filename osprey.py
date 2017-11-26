'''
Osprey is a "package" used to make a basic homepage
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
from functools import wraps
from utilites import dotdict
from os import listdir
from time import sleep
from sqlalchemy import *

app = Flask(__name__)

#Generate path for database in this folder
import sys, os
wd = os.getcwd()+'/'
dbstr = 'sqlite:///'+wd+'ospdb.db'

#Load development config and override config from an environment variable
#if needed.  The silent=true ignores it if there is no file
app.config.update(dict(
    DATABASE=dbstr,
    SECRET_KEY='developmentkey',
    VERSION='dev'))
app.config.from_envvar('OSPCONFIG', silent=True)

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

@app.route('/admin', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        #wait 5 sec on all login requests for security
        sleep(5000)
        admin = request.form('username')
        pw = reuqest.form('password')
        if admin == uname and pw == admin_pw:
           session['username'] = uname
           redirect(url_for('administration'))
        else:
            flash('Invalid Credentials')
    return render_template('login.html')

@login_required
@app.route('/admin')
#Notes:  This is the upper level of admin
#   Here you display sections and can make new secions
def administration():
    print "start of admin"
    if request.method == 'POST':
        sec_type = request.form('type')
        title = request.title('title')
        if stitle in sections:
            flash('Section already exists')
            return url_for('administration')
        else:
            create_section(title=title, sec_type=sec_type)
    return render_template('admin.html', sections=sections)

@login_required
@app.route('/admin/<section>')
#Notes: This is where you view, create, and delete articles for this section
def section_admin(section):
    print "admin of section %s" % section
    if request.method == 'POST':
        request.title('title')
        if title in articles:
            flash('Title already in use')
            return url_for('section_admin', section=section)
        else:
            create_article(title=title, section=section)
    return render_template('section_admin.html', articles=articles, section=section)

@login_required
@app.route('/admin/<article>')
#Notes: This is where you edit articles
def section_admin(article):
    print "editing article: %s" % article
    if request.method == 'POST':
        article_dict = request.form()
        save_article(article_dict)
        return url_for('section_admin', section=section)
    return render_template('section_admin.html', articles=articles, section=section)

@app.route('/')
def home():
    recent_articles = get_recent_articles()
    sections = get_sections()
    return render_template('top_page.html', recent_articles=recent_articles)

@app.route('/<section>')
def section(section, start=0):
    articles = get_section_articles(start)
    return render_template('section.html', articles=articles)

@app.route('/<section>/<article>')
def article(section, article):
    article_content = get_article_content(article)
    return render_template('article.html', article_content=article_content)

def save_article(article_dict):
    return 0

def get_section_articles(section):
    return 0

def get_sections():
    return 0

def create_article(title, section):
    return 0

def save_article():
    return 0

if __name__ == '__main__':
	app.run(debug = True, host='localhost')
