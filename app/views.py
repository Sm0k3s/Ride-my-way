from flask_jwt import JWT
from flask_restful import Resource,request, reqparse
from flask_jwt import JWT, jwt_required
from werkzeug.security import safe_str_cmp
import psycopg2
from models import UserModel, RideModel

#Saves the database in a db variable
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

        if UserModel.find_by_username(data['username']):
            return {'Message': 'Username already taken try another one'}, 400

        conn = psycopg2.connect(db)
        cur = conn.cursor()

        query = "INSERT INTO users VALUES (DEFAULT, %s, %s)"
        cur.execute(query, (data['username'], data['password']))

        conn.commit()
        conn.close()
        return {'Message': 'Account created Successfully'}, 201


class Rides(Resource):   
    """Resource for /api/v1/rides"""
    parser = reqparse.RequestParser()
    parser.add_argument('id',
        type=str,
        required=False,
        help="Identity"
    )
    parser.add_argument('destination',
        type=str,
        required=True,
        help="You must provide a destination."
    )
    parser.add_argument('location',
        type=str,
        required=True,
        help="You must provide a location."
    )
    parser.add_argument('time',
        type=str,
        required=True,
        help="You must provide departure time."
    )
    parser.add_argument('date',
        type=str,
        required=True,
        help="You must provide a date."
    )

    @jwt_required()
    def get(self):
        """Method to get all rides"""
        conn = psycopg2.connect(db)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM rides")
        result = cur.fetchall()
        all_rides = []
        for row in result:
            all_rides.append(
                {'id': row[0], 
                'destination': row[1], 
                'location': row[2], 
                'time': row[3], 
                'date': row[4]}
                )
        conn.close()
        return {'rides': all_rides}, 200

    def post(self):
        data = Rides.parser.parse_args()

        conn = psycopg2.connect(db)
        cur = conn.cursor()

        query = "INSERT INTO ride_offers VALUES (DEFAULT, %s, %s, %s, %s)"
        cur.execute(query, (data['destination'], data['location'],data['time'], data['date']))

        conn.commit()
        conn.close()

        return {'Message': 'Your ride offer has been successfully created'}


class Ride(Resource):
    """
    Resource for fetching the details of a single ride
    endpoint = /api/v1/rides/<int:ride_id>
    """
    def get(self, ride_id):
        """Method to get a single ride by id"""
        conn = psycopg2.connect(db)
        cur = conn.cursor()

        query = "SELECT * FROM rides WHERE id=%s"
        result = cur.execute(query, (ride_id,))

        row = cur.fetchone()
        if row is not None:
            ride ={
                'id': row[0],
                'destination': row[1],
                'location': row[2],
                'date': row[3],
                'time': row[4]
                }

        conn.close()
        return ride, 200

class Users(Resource):   
    """Resource for /api/v1/users"""
    @jwt_required()
    def get(self):
        """Method to get all rides"""
        conn = psycopg2.connect(db)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM users")
        result = cur.fetchall()
        all_users = []
        for row in result:
            all_users.append(
                {'id': row[0], 
                'username': row[1], 
                'password': row[2],}
                )
        conn.close()
        return {'users': all_users}


class RequestRide(Resource):
    """
    Resource for endpoint /api/v1/<int:ride_id>/requests
    """
    def post(self, ride_id):
        conn = psycopg2.connect(db)
        cur = conn.cursor()

        query = "SELECT * FROM rides WHERE id=%s"
        cur.execute(query, (ride_id,))
        row = cur.fetchone()
        if row:
            request_ = {
                'id': row[0],
                'destination': row[1],
                'location': row[2],
                'date': row[3],
                'time': row[4]
                }
            return {'A request has sent for':request_}

        return {'Request':'not found'}, 404

