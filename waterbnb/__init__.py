from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from waterbnb.config import Config

db = SQLAlchemy()
migrate = Migrate()

# from waterbnb.route import index, register
from waterbnb.route import index, register


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
    return app

