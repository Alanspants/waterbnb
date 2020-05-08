from werkzeug.security import generate_password_hash, check_password_hash
from waterbnb import db, login_manager

from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'id={}, username = {}, password_hash={}'.format(
            self.id, self.username, self.password_hash
        )


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
