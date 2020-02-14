from flask import Flask, render_template, redirect, url_for
from wtform import *
from models import *
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)

app.secret_key = 'replace later'

#configure the db
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:rajneesh@localhost:5432/auth1'

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()
    #Updates the database is validation successful

    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        hashed_pwd = pbkdf2_sha256.hash(password)

    #added the username validator in wtform.py file
        # #check username data
        # user_object = User.query.filter_by(username=username).first()
        # if user_object:
        #     return "Someone else has taken this username"

        # user = User(username=username, password=password)
        user = User(username=username, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("index.html", form = reg_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    #Allow login if validation success
    if login_form.validate_on_submit():
        return "Logged In, Finally!"
    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
