from web_flask import app
from flask import render_template
from web_flask.models import List

@app.route('/list')
def market_page():
    lists = List.query.all()
    return render_template('market.html', lists=lists)