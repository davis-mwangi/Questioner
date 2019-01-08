import re
from flask import make_response, jsonify, abort

from ..models.models import users

EMAIL_REGEX = re.compile(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$')


class UserValidation(object):
    def __init__(self, data):
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.othername = data['othername']
        self.email = data['email']
        self.phoneNumber = data['phoneNumber']
        self.username = data['username']
        self.isAdmin = data['isAdmin']

    def check_blank(self):
        if self.firstname.strip() == "":
            msg = "Firstname is missing"
            abort(400, msg)

        if self.lastname.strip() == "":
            msg = "Lastname is missing"
            abort(400, msg)

        if self.othername.strip() == '':
            msg = "Othername is missing"
            abort(400, msg)

        if self.email.strip() == '':
            msg = "Email is missing"
            abort(400, msg)

        if self.phoneNumber.strip() == '':
            msg = "Phone number is missing"
            abort(400, msg)

        if self.username.strip() == '':
            msg = "Username is missing"
            abort(400, msg)

    def validate_email(self):
        if not EMAIL_REGEX.match(self.email):
            msg = "Invalid email format"
            abort(400, msg)

    def check_type(self):
        if type(self.firstname) != str:
            msg = "Firstname must be a string"
            abort(400, msg)
        if type(self.lastname) != str:
            msg = "Lastnamename must be a string"
            abort(400, msg)  
        if type(self.othername) != str:
            msg = "Othername must be a string"
            abort(400, msg) 
        if type(self.phoneNumber) != str:
            msg = "Phone number must be a string"
            abort(400, msg)  
        if type(self.isAdmin) != bool:
            msg = "Role type  must be a boolean"
            abort(400, msg)           

    def validate_user(self):
        self.check_blank()
        self.check_type()
        self.validate_email()
