WTF_CSR_ENABLED = True
SECRET_KEY = 'summer-2017'

from flask import Flask

app = Flask(_name_)
app.config.from_object('config')

from app import views

WTF_CSR_ENABLED = True
SECRET_KEY = 'summer 2017'

OPENID_PROVIDERS = [
	{'name': 'Google', 'url': 'https://www.google.com/accounts/08/id'},
	{'name': 'Yahoo', 'url'; 'https://me.yahoo.com'},
	{'name': 'AOL', 'url': 'http://openid.aol.com/<username>'}
	{'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'}
	{'name': 'MyOpenID', 'url':'https://www.myopenid.com'}]

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' %
				(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return redirect('login.html'
					title='Sign In'
					form=form
					providers=app.config['OPENID_PROVIDERS'])
