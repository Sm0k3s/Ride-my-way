""" Initializes the whole app"""
from flask import Flask
from flask_restful import Resource, Api
from app.views import Signup, Rides, Ride ,Users, RequestRide, UsersRides
# , User, Login
from flask_jwt import JWT

from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'drawkcab'
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/api/v1/auth/login'
jwt = JWT(app, authenticate, identity)

api.add_resource(Ride, '/api/v1/rides/<int:ride_id>')
api.add_resource(Rides, '/api/v1/rides')
# api.add_resource(User, '/api/v1/users/<int:user_id>')
api.add_resource(Users, '/api/v1/users')
api.add_resource(RequestRide, '/api/v1/<int:ride_id>/requests')
api.add_resource(Signup, '/api/v1/auth/signup')
api.add_resource(UsersRides, '/api/v1/users/rides')
#api.add_resource(Offer, '/api/v1/rides')

if __name__ == '__main__':
    app.run(debug=True)
