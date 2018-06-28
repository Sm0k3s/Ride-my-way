from flask_jwt import JWT
from flask_restful import Resource,request, reqparse
from flask_jwt import JWT, jwt_required
import psycopg2


#Saves the database in a variable
db = "dbname='test' user='postgres' host='localhost' password='smokes'"

class Signup(Resource):
    """ Resource for signing up /api/v1/auth/signup"""
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="You must provide a username."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="You must provide a password."
    )
   
    def post(self):
        data = Signup.parser.parse_args()

        conn = psycopg2.connect(db)
        cur = conn.cursor()

        query = "INSERT INTO users VALUES (NULL, %S, %S)"
        cur.execute(query, (data['username'], data['password']))

        conn.commit()
        conn.close()

class Rides(Resource):   
    """Resource for /api/v1/rides"""
     #@jwt_required()
    def get(self):
        """Method to get all rides"""
        conn = psycopg2.connect(db)
        cur = conn.cursor()
        
        result = cur.execute("SELECT * FROM rides")
        all_rides
        for row in result:
            all_rides.append({'id': row[0], 'destination': row[1], 'location': row[2], 'time': row[3], 'date': row[4]})
        conn.close()
        return {'rides': all_rides}
        
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
    """
    Resource for fetching the details of a single ride
    endpoint = /api/v1/rides/<int:ride_id>
    """
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
    """Resource to get single userfor /api/v1/users/<int:user_id>"""
    def get(self, user_id):
        """Method to a single user by id"""
        for user in users:
            if user['user_id'] == user_id:
                return user
        return {'user': 'not found'}, 404

class RequestRide(Resource):
    """
    Resource for endpoint /api/v1/<int:ride_id>/requests
    
    """
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

class DriverRequests(Resource):
    """REsource for all requests posted /api/v1/drivers/requests"""
    def get(self):
        return {'All requests': ride_requests}
