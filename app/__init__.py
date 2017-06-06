from flask import Flask

# Initialize a new flask instance
app = Flask(__name__)

# When you declare app.route("/something"), this means that when the user
# visits localhost:5000/something on google chrome, he will see whatever
# you are returning in the function you defined (index)
# Note that eventually you will handle much more than 2 routes, so you will
# want to move this into a different file.
@app.route('/')
@app.route('/index')
def index():
	"""
	This function is responsible for all requests that come into
	http://127.0.0.1:5000/ or http://127.0.0.1:5000/index.
	"""
	user = {'nickname' : 'Jonathan'} #fake user
	return '''
<html>
	<head>
		<title>Home Page</title>
	</head>
	<body>
		<h1>Hello, ''' + user['nickname'] + '''</h1>
	</body>
</html>
'''
