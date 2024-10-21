from flask import Blueprint, request, jsonify
from flask.views import MethodView
from models.User import User

# Define the blueprint
user_bp = Blueprint('user_bp', __name__)


class UserAPI(MethodView):
    """User class API to interact"""

    def get(self):
        """get method to fetch user details"""
        users = User.query.all()
        user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
        return jsonify(user_list), 200


# Register the class-based view with the Blueprint
user_view = UserAPI.as_view('user_api')
user_bp.add_url_rule('/users', view_func=user_view, methods=['GET'])
