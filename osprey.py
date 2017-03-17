from flask import Flask, request, session, g, redirect, url_for, send_from_directory, \
     abort, render_template, flash, escape
from functools import wraps
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


@app.route('/', methods = ['GET'])
def index()
    subs = get_subsections()
    articles = get_articles()
	return render_template('osprey.html', page_data)


if __name__ == '__main__':
	app.run(debug = True, host='localhost')

