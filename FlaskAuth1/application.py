from flask import Flask, render_template
from wtform import *
from models import *

app = Flask(__name__)

app.secret_key = 'replace later'

#configure the db
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:rajneesh@localhost:5432/auth1'

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

    #added the username validator in wtform.py file
        # #check username data
        # user_object = User.query.filter_by(username=username).first()
        # if user_object:
        #     return "Someone else has taken this username"

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Inserted into DB"
    return render_template("index.html",form = reg_form)


if __name__ == "__main__":
    app.run(debug=True)
