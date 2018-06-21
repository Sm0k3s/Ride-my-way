from flask_restful import Resource
from data import users, rides

class Rides(Resource):   
    def get(self):
        return {'rides':rides}

