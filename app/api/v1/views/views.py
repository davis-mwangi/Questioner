import datetime
from flask import Flask, json, request, make_response, jsonify
from flask_restful import Resource


from ..models.models import *
from ..utils.validation import *


class UserResource(Resource):
    """Create new user"""

    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({
                'status': '400',
                'error': 'No signup data provided'
            }), 400)

        for user in users:
            if data['username'] == user['username']:
                return make_response(jsonify({
                    'status': '409',
                    'error': "User '" + user['username'] + "'already exists"
                }), 409)
        validate_user = UserValidation(data)
        validate_user.validate_user()

        user = User(data)
        user.save_user()

        return make_response(jsonify({
            'status': '201',
            'message': 'User created successfully',
            'users': users
        }), 201)


class MeetupResource(Resource):
    """Create meetup"""

    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({
                'status': '400',
                'error': 'No meetup details  provided'
            }), 400)
        for meetup in meetups:
            if data['topic'] == meetup['topic']:
                return make_response(jsonify({
                    'status': '409',
                    'error': "Meetup '" + meetup['topic'] + "'already exists"
                }), 409)

        meetup = Meetup(data)
        meetup.save_meetup()

        return make_response(jsonify({
            'status': '201',
            'message': 'meetup created successfully',
            'data': meetups
        }), 201)


class SingleMeetup(Resource):
    def get(self, meetup_id):
        for meetup in meetups:
            if meetup['id'] == int(meetup_id):
                return make_response(jsonify({
                    'status': 200,
                    'data': meetup
                }), 200)
        return make_response(jsonify({
            'status': '200',
            'error': 'No such meetup found'
        }), 404)


class UpcomingMeetupsResource(Resource):
    """Get all upcoming meetups"""

    def get(self):
        if len(meetups) == 0:
            return make_response(jsonify({
                'status': 404,
                'error': 'No meetup records found'
            }), 404)
        return make_response(jsonify({
            'status': 200,
            'data': meetups
        }), 200)


class QuestionResource(Resource):
    """Post a question"""

    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({
                'status': '400',
                'error': 'No question  provided'
            }), 400)
        for question in questions:
            if data['title'] == question['title']:
                return make_response(jsonify({
                    'status': '409',
                    'error': "Question  with title '" + question['title'] + "'already exists"
                }), 409)

        question = Question(data)
        question.save_question()

        return make_response(jsonify({
            'status': '201',
            'message': 'Question created successfully',
            'data': questions
        }), 201)
