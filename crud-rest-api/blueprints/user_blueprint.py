"""User blueprint module"""
from flask import Blueprint, request, jsonify
from flask.views import MethodView
from models.User import User
from app import db

# Define the blueprint
user_bp = Blueprint('user_bp', __name__)


class UserAPI(MethodView):
    """User class API to interact"""

    def get(self, user_id=None):
        """get method to fetch user details"""
        if user_id:
            user = User.query.get(user_id)
            return jsonify({'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }}), 200
        users = User.query.all()
        user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
        return jsonify(user_list), 200

    # POST request to create a new user
    def post(self):
        """
        post method to save new data
        """
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')

        if not username or not email:
            return jsonify({'error': 'Username and email are required'}), 400

        # Create a new user
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully',
                        'user': {'id': new_user.id, 'username': new_user.username, 'email': new_user.email}}), 201

    def put(self, user_id):
        """
        put method to update records
        """
        user = User.query.get(user_id)
        if user:
            data = request.get_json()
            user.username = data.get('username')
            user.email = data.get('email')
            db.session.commit()
            return jsonify({'message': "Data updated successfully",
                            'user': {
                                'id': user.id,
                                'username': user.username,
                                'email': user.email
                            }}), 202
        return jsonify({'message': "User not found"}), 404


# Register the class-based view with the Blueprint
user_view = UserAPI.as_view('user_api')
user_bp.add_url_rule('/users', view_func=user_view, methods=['GET', 'POST'])
user_bp.add_url_rule('/users/<string:user_id>', view_func=user_view, methods=['GET', 'PUT'])
