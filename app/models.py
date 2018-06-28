import psycopg2
db = "dbname='test' user='postgres' host='localhost' password='smokes'"
#ridemyway

class UserModel():
    """
    User object for defining all the methods to be taken on the users
    CREATE TABLE users(id INT PRIMARY KEY,username VARCHAR(100),
            password VARCHAR(100)); >
    """
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def new_user(self, username, password):
        conn = psycopg2(db)
        cur = conn.cursor

    @classmethod
    def find_user_by_id(cls, username):
        """Method to find user by id"""
        
        query = "SELECT * FROM users WHERE username=%s"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row is not None:
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        conn.close
        return user

    @classmethod
    def find_user_by_id(cls, _id):
        """Method to find user by id"""
        
        query = "SELECT * FROM users WHERE id=%s"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row is not None:
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        conn.close
        return user

class RideModel():
    """
    Ride object for defining all the methods to be taken on the users
    CREATE TABLE rides(id INT PRIMARY KEY, VARCHAR(100),
            password VARCHAR(100));
    """
    def __init__(self, _id, destination, location, date, time ):
        self.id = _id
        self.destination = destination
        self.date = date
        self.time = time

    @classmethod
    def find_ride_by_id(cls, _id):
        """Method to find user by id"""
        
        query = "SELECT * FROM rides WHERE id=%s"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row is not None:
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        conn.close
        return user
