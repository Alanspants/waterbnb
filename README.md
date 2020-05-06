#waterbnb

run server: python3 manager runserver -d

database initiate:
    python manager.py db init
    python manager.py db migrate -m "create user"
    python manager.py db upgrade

use shell to control database:
    you need to get into python shell firstly.

    >>> from waterbnb import db, create_app
    >>> app = create_app()
    >>> db
    <SQLAlchemy engine=None>
    >>> app.app_context().push()
    >>> db
    <SQLAlchemy engine=sqlite:////Users/Chz/JavaBackend/Python&Flask/waterbnb/waterbnb/data.db>
