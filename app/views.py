""""""
from flask_restful import Resource,request
from data import users, rides, ride_requests

class Rides(Resource):   
    """Resource for /api/v1/rides"""
    def get(self):
        """Method to get all rides"""
        return {'All rides':rides}
    
    def post(self):
        """Method to create a ride offer"""
        _id =len(rides) + 1
        ride_id = {'ride_id':_id}
        request_data = request.get_json()
        ride = {
            'location': request_data['location'],
            'destination': request_data['destination']
        }
        ride.update(ride_id)
        rides.append(ride)
        return {'ride': ride}, 201

class Ride(Resource):
    """Resource for /api/v1/rides/<int:ride_id>"""
    def get(self, ride_id):
        """Method to get a single ride by id"""
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
        _id =len(users) + 1
        user_id = {'user_id':_id}
        request_data = request.get_json()
        user = {
            'name': request_data['name'],
            'email': request_data['email'],
            'password': request_data['password']
        }
        user.update(user_id)
        users.append(user)
        return {'user': user}, 201

class User(Resource):
    """Resource for /api/v1/user/<int:user_id>"""
    def get(self, user_id):
        """Method to a single user by id"""
        for user in users:
            if user['user_id'] == user_id:
                return user
        return {'user': 'not found'}, 404

class Request_ride(Resource):
    """Resource for /api/v1/<int:ride_id>/requests"""
    def get(self, ride_id):
        for ride in rides:
            if ride['ride_id'] == ride_id:
                requests.append(ride)

        return {'request':'not found'}, 404

class Login(Resource):
    """resouurce for /api/v1/auth/login"""
    def post(self,username,password):
        request_data = request.get_json()
        for user in users:
            if user['name'] == username and user['password'] == password:
                return {'login': 'successful'}

class Driver_requests(Resource):
    """REsource for all requests posted /api/v1/drivers/requests"""
    def get(self):
        return {'All requests': ride_requests}
