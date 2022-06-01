from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd6ee049fbe11f6e895bb2624748c7b93'
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


@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
            if form.email.data == 'admin@blog.com' and form.password.data == 'password':
                    flash(f'Hello again,{form.email.data}!','success')
                    return redirect(url_for('home'))
            else:
                flash('login Unsuccessful. Please check email or password','danger')
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
