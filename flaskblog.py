from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

#app.cofig to secure the app from hack
#import secrets  ---from terminal
# secrets.token_hex(16)

app.config['SECRET_KEY'] = '35f89b9fe3d7d632eb156b7a67316ec6' 

posts=[
{'author':'modith hadya',
'title':'blog post1',
'content':'first post content',
'date':'nov 14, 2019'	
},
{
'author':'michael ross',
'title':'blog post2',
'content':'second post content',
'date':'nov 15, 2019'
	
}
]



@app.route('/')
@app.route('/home')

def home():
	return render_template('home.html', posts=posts)

@app.route('/about')

def about():
	return render_template('about.html', title='about')


@app.route('/register', methods=['GET','POST'])
def register():
	form= RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','success')
		return redirect (url_for('home'))
	return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
	form= LoginForm()
	return render_template('login.html', title='Login', form=form)





if __name__=='__main__':
	app.run(debug=True)