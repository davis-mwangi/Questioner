from flask import Blueprint
from flask_restful import Api 

from .views.views import (
 UserResource, 
 MeetupResource, 
 QuestionResource,
 SingleMeetup,
 UpcomingMeetupsResource
) 

v1 = Blueprint('api', __name__ , url_prefix='/api/v1')

api = Api(v1)

api.add_resource(UserResource, '/auth/signup')
api.add_resource(MeetupResource, '/meetups')
api.add_resource(QuestionResource, '/questions')
api.add_resource(SingleMeetup, '/meetups/<int:meetup_id>')
api.add_resource(UpcomingMeetupsResource, '/meetups/upcoming')