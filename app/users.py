import psycopg2


class User():
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def find_by_username(self, username):
        connection = psycopg2.connect('ridemyway.db')
        cursor = connection.cursor()
