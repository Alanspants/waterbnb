import os

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
# from models import generate_password_hash, User
from forms import RegisterForm

# from extension import db



prefix = 'sqlite:///'

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret string')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import models

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.body
        password = form.password.body
        user = models.User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
