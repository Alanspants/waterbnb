from flask import render_template, url_for, app
from werkzeug.utils import redirect
from waterbnb.forms import RegisterForm
from waterbnb import db
from waterbnb import models


def index():
    return render_template('index.html')


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
    return render_template('register.html', form=form)

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)
