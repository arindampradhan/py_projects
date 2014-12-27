from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title="base apps!!")

@app.route('/calc')
def calc():
	return render_template('calc.html')	
