from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # Initialize the database
    db.init_app(app)

    # Import and register blueprints here
    from blueprints.user_blueprint import user_bp
    app.register_blueprint(user_bp)

    return app
