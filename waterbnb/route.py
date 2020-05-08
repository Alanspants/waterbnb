from flask import render_template, url_for, app, flash
from werkzeug.utils import redirect
from waterbnb.forms import RegisterForm, LoginForm
from waterbnb import db
from waterbnb import models
from flask_login import login_user, current_user, logout_user, login_required



def index():
    return render_template('index.html')


def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = models.User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        thisUser = models.User.query.filter_by(username=form.username.data).first()
        if thisUser is None or (not thisUser.validate_password(form.password.data)):
            flash('Invalid username or password.')
        else:
            login_user(thisUser)
            return redirect(url_for('index'))
    return render_template('login.html', form=form)

def logout():
    logout_user()
    return redirect(url_for('index'))

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)
