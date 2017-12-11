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
engine = create_engine(dbstr, echo=True)
articles = Table('articles', metadata, autoload=True)

#Load development config and override config from an environment variable
#if needed.  The silent=true ignores it if there is no file
app.config.update(dict(
    DATABASE=dbstr,
    SECRET_KEY='developmentkey',
    VERSION='dev'
    ADMIN_USER = 'admin',
    ADMIN_PASS = 'admin1234'))
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
        if admin == app.ADMIN_USER and pw == app.ADMIN_PASS:
           session['username'] = admin
           redirect(url_for('admin'))
        else:
            flash('Invalid Credentials')
    return render_template('login.html')

@login_required
@app.route('/admin')
#Notes: This the the admin for the home page 
def admin():
    print "start of admin"
    if request.method == 'POST':
        sec_type = request.form('type')
        title = request.title('title')
        if stitle in sections:
            flash('Section already exists')
            return url_for('admin')
        else:
            create_section(title=title, sec_type=sec_type)
    return render_template('admin.html', sections=sections)

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
    sub_articles = get_sub_articles()
    return render_template('top_page.html', recent_articles=recent_articles, sub_articles=sub_articles)

@app.route('/<article>')
def article(article):
    article_content = get_article_content(article)
    sub_articles = get_sub_articles()
    return render_template('article.html', article_content=article_content)

#TODO!
def save_article(article_dict):
    return 0

def get_sub_articles(parentid):
    subs = []
    temp = articles.select(articles.c.parentid == parentid).execute()
    for row in temp:
        subs.append(row)
    return subs

def create_article(title, section):
    return 0

def save_article():
    return 0

def get_article_content(article):
    return 0

if __name__ == '__main__':
	app.run(debug = True, host='localhost')
