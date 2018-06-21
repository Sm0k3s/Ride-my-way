from flask import Flask
from flask_restful import Resource, Api
from app.views import Rides

app = Flask(__name__)
api = Api(app)


api.add_resource(Rides, '/api/v1/rides')

if __name__=='__main__':
	app.run(debug=True)
