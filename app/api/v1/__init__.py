from flask import Blueprint
from flask_restful import Api

v1 = Blueprint('api', __name__ , url_prefix='/api/v1')

api = Api(v1)