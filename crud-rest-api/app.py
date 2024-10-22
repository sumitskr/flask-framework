"""Flask App initialization file"""
from flask import Flask
from config import db
from blueprints.user_blueprint import user_bp


def create_app():
    """
    function to create flask app
    """
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # Initialize the database
    db.init_app(app)
    app.register_blueprint(user_bp)

    return app
