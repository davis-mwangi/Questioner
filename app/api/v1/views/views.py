import datetime
from flask import Flask, json,request, make_response, jsonify
from flask_restful import Resource


from ..models.models import users,User
from ..utils.validation import *

class UserResource(Resource):
    """Create new user"""
    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify( {
                'status':'400',
                'error': 'No signup data provided'
            }), 400)

        for user in users:
            if data['username'] == user['username']:
               return make_response(jsonify({
                    'status':'409',
                    'error': "User '" + user['username'] + "'already exists"
                }), 409)
        validate_user = UserValidation(data)
        validate_user.validate_user()

        user = User(data)
        user.save_user()
        
        return make_response(jsonify({
            'status':'201',
            'message': 'User created successfully',
            'users': users
        }), 201)



