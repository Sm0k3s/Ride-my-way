from werkzeug.security import safe_str_cmp
from app.models import UserModel

db = "dbname='test' user='postgres' host='localhost' password='smokes'"

def authenticate(username, password):
	user = User.find_by_username(username, None)
	if user and safe_str_cmp(user.password == password):
		return user

def identity(payload):
	user_id = payload['identity']
	return User.find_by_id(user_id)
