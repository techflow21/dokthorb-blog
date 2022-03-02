from flask import Flask

app = Flask(__name__)

from flask import Flask, render_template, flash, request, redirect, url_for
from flask_login import login_required, logout_user
from webforms import LoginForm, PostForm, UserForm, SearchForm

app = Flask(__name__)

# secret key
app.config['SECRET_KEY'] = "tutorial"


@app.route('/')
def index():
	return render_template('index.html')

# Passing search term to the Navbar
@app.context_processor
def base():
	form = SearchForm()
	return dict(form=form)

# Create Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', form=form)

# Create logout function
@app.route('/logout', methods=['GET', 'POST'])
def logout():
	logout_user()
	flash("You Have been Logged Out!")
	return redirect(url_for('login'))

# Create Dashboard Page
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
	form = UserForm()
	return render_template('dashboard.html')


# Create Add User Page
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
	name =None
	form = UserForm()
	return render_template('add_user.html',
	  form=form, 
	  name=name)


# Create Edit User Function
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
	form = UserForm()
	if request.method == 'POST':
		return render_template("update.html", 
			form = form, 
			id = id)


# Create a Delete User function
@app.route('/delete/<int:id>')
def delete(id):
	name = None
	form = UserForm()

# Create Add Post Page
@app.route('/add-post', methods=['GET', 'POST'])
def add_post():
	form = PostForm()
	return render_template("add_post.html", form = form)


# Show Posts
@app.route('/posts')
def posts():
	return render_template("posts.html", posts = posts)

# Show Single Post
@app.route('/posts/<int:id>')
def post(id):
	return render_template("post.html", post = post)

# To edit Posts
@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
	form = PostForm()

# Create a Delete Post Function
@app.route('/posts/delete/<int:id>')
@login_required
def delete_post(id):
	return render_template("posts.html")

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500

