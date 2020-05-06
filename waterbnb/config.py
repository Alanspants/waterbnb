import os

from flask import app

config_path = os.path.abspath(os.path.dirname(__file__))


class Config:
    prefix = 'sqlite:///'
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(config_path, 'data.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
