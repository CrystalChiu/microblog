from flask import Flask

app = Flask("crystal")
#from app import views
from app import app

from app import app

app.route('/')
@app.route('/index')
def index() :
	user = {'nickname' : 'Jonathan'} #fake user
	return '''
<html>
	<head>
		<titl>Home Page</ title>
	</head>
	<body>
		<h1?Hello, ''' + user['nickname'] + '''</h1>
	</body>
</html>
'''