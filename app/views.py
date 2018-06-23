""""""
from flask_restful import Resource,request
from data import users, rides

class Rides(Resource):   
    """Resource for /api/v1/rides"""
    def get(self):
        """Method to get all rides"""
        return {'All rides':rides}
    
    def post(self):
        """Method to create a ride offer"""
        request_data = request.get_json()
        ride = {
            'location': request_data['location'],
            'destination': request_data['destination']
        }
        rides.append(ride)
        return {'ride': ride}, 201

class Ride(Resource):
    """Resource for /api/v1/rides/<int:ride_id>"""
    def get(self, ride_id):
        """Method to a single ride by id"""
        for ride in rides:
            if ride['ride_id'] == ride_id:
                return ride
        return {'ride': 'not found'}, 404

class Users(Resource):   
    """Resource for /api/v1/users"""
    def get(self):
        """Method to get all users"""
        return {'All users':users}

    def post(self):
        """Method to add a user"""
        request_data = request.get_json()
        user = {
            'name': request_data['name'],
            'email': request_data['email'],
            'password': request_data['password']
        }
        users.append(user)
        return {'user': user}, 201
