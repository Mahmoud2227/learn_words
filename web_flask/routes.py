from web_flask import app
from flask import render_template
from web_flask.models import List

@app.route('/')
def landing_page():
    return render_template('landing.html',css_file = 'landing')

@app.route('/home')
def home_page():
    lists = List.query.all()
    return render_template('home.html', lists=lists)