import unittest
import json
from API.run import app

class RidesApiTests(unittest.TestCase):
    """Testing for rides"""
    def setUp(self):
        """Creates a test client"""
        self.app = app
        self.client = self.app.test_client()
    def tearDown(self):
        """Destroys the test client when done"""
        self.app.testing = False
        self.app = None
    def test_get_all_rides(self):
        rv = self.client.get('/api/v1/rides')
        self.assertEqual(rv.status_code, 200)

if __name__=='__main__':
    unittest.main()
