import psycopg2
db = "dbname='test' user='postgres' host='localhost' password='smokes'"
# db = "dbname='db_tests' user='postgres' host='localhost' password='smokes'"
#ridemyway

class Database():
    
    def create_tables():
        conn = psycopg2.connect(db)
        cur = conn.cursor()

        query = """CREATE TABLE IF NOT EXISTS rides (
        ride_id serial, location VARCHAR(100),
        destination VARCHAR(100),
        departure VARCHAR(15)); CREATE TABLE IF NOT EXISTS users(
        id serial, username VARCHAR(100), password VARCHAR(100))"""

        cur.execute(query)
        conn.commit()
        conn.close()
    def drop_tables():
        conn = psycopg2.connect(db)
        cur = conn.cursor
        
        query = "DROP TABLE rides; DROP TABLE users;"

        cur.execute(query)
        conn.commit()
        conn.close()

class UserModel():
    """
    CREATE SEQUENCE 
    User object for defining all the methods to be taken on the users
    CREATE TABLE users(id INT PRIMARY KEY,username VARCHAR(100),
            password VARCHAR(100)); >
    """
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def new_user(self, _id, username, password):
        conn = psycopg2.connect(db)
        cur = conn.cursor()

        query ="INSERT INTO users VALUES(DEFAULT, %s, %s)"
        cur.execute(query, (self.username, self.password))

        conn.commit()
        conn.close()

    def delete_user(self, _id):
        conn = psycopg2.connect(db)
        cur = conn.cursor

        query = "DELETE FROM users WHERE id=%s"
        cur.execute(query, (self._id,))

        conn.commit()
        conn.close()

    @classmethod
    def find_by_username(cls, username):
        """Method to find user by username"""
        conn = psycopg2.connect(db)
        cur = conn.cursor()

        query = "SELECT * FROM users WHERE username=%s"
        result = cur.execute(query, (username,))
        row = cur.fetchone()
        if row is not None:
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        conn.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        """Method to find user by id"""
        conn = psycopg2.connect(db)
        cur = conn.cursor()

        query = "SELECT * FROM users WHERE id=%s"
        result = cur.execute(query, (_id,))
        row = cur.fetchone()
        if row is not None:
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        conn.close()
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
        self.location = location
        self.date = date
        self.time = time

    def new_ride(self, _id, destination, location, time, date):
        conn = psycopg2(db)
        cur = conn.cursor

        query ="INSERT INTO users VALUES(DEFAULT, %s, %s)"
        cur.execute(query, (self.destination, self.location, self.time, 
            self.date))

        conn.commit()
        conn.close()

    def delete_ride(self, _id):
        conn = psycopg2.connect(db)
        cur = conn.cursor

        query = "DELETE FROM rides WHERE id=%s"
        cur.execute(query, (self._id,))

        conn.commit()
        conn.close()

    @classmethod
    def find_ride_by_id(cls, _id):
        """Method to find ride by id"""
        conn = psycopg2.connect(db)
        cur = conn.cursor()

        query = "SELECT * FROM rides WHERE id=%s"
        result = cur.execute(query, (_id,))
        row = cur.fetchone()
        if row is not None:
            ride = cls(row[0], row[1], row[2],row[3], row[4])
        else:
            ride = None

        conn.close()
        return ride

    #def delete_ride(self, id):


