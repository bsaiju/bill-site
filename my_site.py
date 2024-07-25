from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '271b1f5887fa7ecd25ccc86bd0a0e338'
data = [["name", "phone"], ["bob","234"], ["james","2313"], ["hope", "232"], ["uliop", "6758"], ["phoebe", "234534"]]
@app.route("/home")
def home():
    return render_template('home.html', data=data)

@app.route("/")
@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.user.data}", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form = form)


if __name__ == '__main__':
    app.run(debug=True)