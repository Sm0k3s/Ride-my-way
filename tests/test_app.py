import unittest
import json
from run import app

class ApiTests(unittest.TestCase):
    """Testing for rides"""
    def setUp(self):
        """Creates a test client"""
        self.app = app
        self.client = self.app.test_client()
        self.ride = {
                      'ride_id':4,
                      'location':'mtaani',
                      'destination':'mayolo',
                      'Departure': '1900hrs'
                      }
        self.user = {
           'user_id':3,
           'name':'micko',
           'email':'mickoo@micko.com',
           'password':'deal123'
    }

    def tearDown(self):
        """Destroys the test client when done"""
        self.app.testing = False
        self.app = None

    def test_get_all_rides(self):
        """Test api can get all rides"""
        resp = self.client.get('/api/v1/rides')
        self.assertEqual(resp.status_code, 200)
    

    def test_can_create_a_ride(self):
        """Test api can create a ride"""
        newride = self.ride
        resp = self.client.post('/api/v1/rides', data=json.dumps(newride), content_type='application/json')
        self.assertEqual(resp.status_code, 201)

    def test_api_modify_a_ride(self):
        """Test api can modify a ride"""
        self.newride = {'ride_id':4,
                 'location':'hood',
                 'destination':'mombasa',
                 'Departure': '1400hrs'
                      }
        self.client.post('/api/v1/rides', data=json.dumps(self.ride), content_type='application/json')
        resp = self.client.get('/api/v1/rides/4')
        resp1 = self.client.put('/api/v1/rides/4', data=json.dumps(self.newride), content_type='application/json')
        self.assertNotEqual(resp, resp1)

    def test_api_can_make_a_ride_request(self):
        """Test api can make a ride request"""
        resp = self.client.post('/api/v1/<int:ride_id>/requests')
        self.assertEqual(resp.status_code, 201)

    def test_get_all_users(self):
        """Test api can get all users"""
        resp = self.client.get('/api/v1/users')
        self.assertEqual(resp.status_code, 200)

    def test_get_a_user_by_id(self):
        """Test api can get a user by id /api/v1/users/<int:user_id>"""
        resp = self.client.get('/api/v1/users/2')
        self.assertEqual(resp.status_code, 200)

    def test_cant_get_a_nonexistant_user_by_id(self):
        """Test api can get a user by id /api/v1/users/<int:user_id>"""
        resp = self.client.get('/api/v1/users/609')
        self.assertEqual(resp.status_code, 404)    

    def test_can_create_a_user(self):
        """Test api can create a user"""
        resp = self.client.post('api/v1/users', data=json.dumps(self.user), content_type='application/json')
        self.assertEqual(resp.status_code, 201)

    def test_drivers_can_get_requests(self):
        resp = self.client.get('/api/v1/drivers/requests')
        self.assertEqual(resp.status_code, 200)

if __name__=='__main__':
    unittest.main()
