from flask import Flask

app = Flask("crystal")
#from app import views
from app import app
@app.route('/') 
@app.route('/index')
def index():
	return "Hello, World!"

