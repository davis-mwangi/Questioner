from werkzeug.security import generate_password_hash
from datetime import datetime

users = []
meetups = []
questions = []


class User(object):
    def __init__(self, data):
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.othername = data['othername']
        self.email = data['email']
        self.phoneNumber = data['phoneNumber']
        self.username = data['username']
        self.registered = datetime.now()
        self.isAdmin = data['isAdmin']

    def save_user(self):
        id = len(users) + 1
        user = {
            'id': id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'othername': self.othername,
            'email': self.email,
            'phoneNumber': self.phoneNumber,
            'username': self.username,
            'registered': self.registered,
            'isAdmin': self.isAdmin,
        }
        users.append(user)


class Meetup(object):
    def __init__(self, data):
        self.createdOn = datetime.now()
        self.location = data['location']
        self.topic = data['topic']
        self.happeningOn = data['happeningOn']
        self.tags = data['Tags']

    def save_meetup(self):
        id = len(meetups) + 1
        meetup = {
            'id': id,
            'createdOn': self.createdOn,
            'location': self.location,
            'topic': self.topic,
            'happeningOn': self.happeningOn,
            'Tags': self.tags,
        }
        meetups.append(meetup)


class Question(object):
    def __init__(self, data):
        self.createdOn = datetime.now()
        self.createdBy = data['createdBy']
        self.meetup = data['meetup']
        self.title = data['title']
        self.body = data['body']
        self.votes = data['votes']

    def save_question(self):
        id = len(questions) + 1
        question = {
            'id': id,
            'createdOn': self.createdOn,
            'createdBy': self.createdBy,
            'meetup': self.meetup,
            'title': self.title,
            'body': self.body,
            'votes': self.votes
        }
        questions.append(question)


def destroy():
    users.clear()
    meetups.clear()
    questions.clear()
