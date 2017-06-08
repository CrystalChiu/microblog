from flask import render_template 
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Jonathan'}  # fake user
	return render_template('index.html',
							title='Home',
							user=user)
def index():
	user = {'nickname': 'Jonathan'} # fake user
	posts = [ # fake array of posts 
		{
			'author': {'nickname': 'Crastal'},
			'body': 'I love boba'
		},
		{
			'author': {'nickname': 'Bruce'},
			'body': 'Batman'
		}
	]
	return render_template("index.html",
							title='Home',
							user=user
							posts=postss)