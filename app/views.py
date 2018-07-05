from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required, current_identity
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
        return {'rides': all_rides},200



class UsersRides(Resource):
    """Resource for /api/v1/users/rides"""
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

    def post(self):
        """Method to create a new ride offer"""
        data = UsersRides.parser.parse_args()

        conn = psycopg2.connect(db)
        cur = conn.cursor()

        query = "INSERT INTO ride_offers VALUES (DEFAULT, %s, %s, %s, %s)"
        cur.execute(query, (data['destination'], data['location'],
            data['time'], data['date']))

        conn.commit()
        conn.close()

        return {'Message': 'Your ride offer has been successfully created'}, 201



class Ride(Resource):
    """
    Resource for fetching the details of a single ride
    endpoint = /api/v1/rides/<int:ride_id>
    """
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

    def get(self, ride_id):
        """Method to get a single ride by id"""
        conn = psycopg2.connect(db)
        cur = conn.cursor()

        query = "SELECT * FROM rides WHERE id=%s"
        result = cur.execute(query, (ride_id,))

        row = cur.fetchone()

        conn.close()
        if row is not None:
            ride ={
                'id': row[0],
                'destination': row[1],
                'location': row[2],
                'date': row[3],
                'time': row[4]
                }
            return ride, 200    
        
        return {'Message':'ride not found'}

    def put(self, ride_id):
        """Method to update a ride by id"""
        data = Ride.parser.parse_args()

        conn = psycopg2.connect(db)
        cur = conn.cursor()

        query = "SELECT * FROM rides WHERE id=%s"
        cur.execute(query, (ride_id,))

        row = cur.fetchone()
        conn.close()
        if row:
            try:
                conn = psycopg2.connect(db)
                cur = conn.cursor()

                query1 = """UPDATE rides SET destination=%s,location=%s,
                    date=%s, time=%s WHERE id=%s"""
                cur.execute(query1, (data['destination'], data['location'], 
                    data['date'], data['time'], ride_id))

                conn.commit()
                conn.close()

                return {'Message': 'ride updated successfully'}
            except:
                return {'Message': 'An error occurred while updating your ride'}
        else:
            try:
                conn = psycopg2.connect(db)
                cur = conn.cursor()
                
                query2 = "INSERT INTO rides VALUES (DEFAULT, %s, %s, %s, %s)"
                cur.execute(query2, (data['destination'], data['location'],
                    data['time'], data['date']))

                conn.commit()
                conn.close()
            except:
                return {'Message': 'An error occurred while inserting your items'}
            


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
    Resource for endpoint /api/v1/rides/<int:ride_id>/requests
    """
    def post(self, ride_id):
        conn = psycopg2.connect(db)
        cur = conn.cursor()

        query = "SELECT * FROM rides WHERE id=%s"
        cur.execute(query, (ride_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            request_ = {
                'id': row[0],
                'destination': row[1],
                'location': row[2],
                'date': row[3],
                'time': row[4]
                }
            return {'A request was sent for':request_}
        else:
            return {'Message':'You just found a wormhole, next stop oblivion'}

class RequestAccept(Resource):
    """Resource for /api/v1/rides/<int:rideId>/requests/<requestId> """
    def put(self):
        pass

