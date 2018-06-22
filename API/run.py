""" Initializes the whole app"""
from flask import Flask
from flask_restful import Resource, Api
from app.views import Rides, Ride

app = Flask(__name__)
api = Api(app)

api.add_resource(Ride, '/api/v1/rides/<int:ride_id>')
api.add_resource(Rides, '/api/v1/rides')

if __name__ == '__main__':
    app.run(debug=True)
