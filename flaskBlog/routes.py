from flask import  render_template, url_for, flash, redirect
from flaskBlog.forms import RegistrationForm, LoginForm
from flaskBlog.models import Post,User
from flaskBlog import app,bcrypt,db


posts = [
    {
        'author': 'Michaelo Matraczow',
        'title': 'First touch',
        'content': 'Blog',
        'date_posted': '22.12.1945'
    },
    {
        'author': 'Anna Mydło',
        'title': 'First touch',
        'content': 'Blog',
        'date_posted': '22.12.2024'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data ,email=form.email.data, password = hashed_password )
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in ', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'Hello again,{form.email.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('login Unsuccessful. Please check email or password', 'danger')
            return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)
