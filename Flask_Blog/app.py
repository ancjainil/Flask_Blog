from crypt import methods
from flask import Flask, redirect, render_template, url_for, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd626cb46ccf413e61c6d8293412e7e65'


posts = [{
    'author': 'Jainil Rana',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'July 11, 2022'
},
    {
    'author': 'Jainil Rana',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'July 11, 2022'

}]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def hello_world():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
