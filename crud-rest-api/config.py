"""Module for configuration"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
SQLALCHEMY_DATABASE_URI = 'sqlite:///crud_rest_api.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
