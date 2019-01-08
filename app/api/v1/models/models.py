from werkzeug.security import generate_password_hash
from datetime import datetime

users =[]
meetups = []


class User(object):
    def __init__(self, data):
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.othername = data['othername']
        self.email = data['email']
        self.phoneNumber = data['phoneNumber']
        self.username =  data['username']
        self.registered = datetime.now()
        self.isAdmin = data['isAdmin']

    def save_user(self):
        id = len(users) + 1
        user = {
            'id' : id ,
            'firstname' : self.firstname ,
            'lastname' : self.lastname,
            'othername' : self.othername,
            'email' : self.email ,
            'phoneNumber' : self.phoneNumber,
            'username' : self.username,
            'registered': self.registered,
            'isAdmin' : self.isAdmin,
        }    
        users.append(user)

class Meetup(object):
    def __init__(self, data):
        self.createdOn = datetime.now()
        self.location = data['location']
        self.topic = data['topic']
        self.happeningOn = data['happeningOn']
        self.tags =  data['Tags']

    def save_meetup(self):
        id = len(users) + 1
        meetup = {
            'id': id,
            'createdOn' : self.createdOn ,
            'location' : self.location ,
            'topic' : self.topic ,
            'happeningOn' : self.happeningOn ,
            'Tags' :self.tags ,
        }    
        meetups.append(meetup)

     
def destroy():
    users.clear()





        