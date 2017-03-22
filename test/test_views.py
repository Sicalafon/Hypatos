import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
    	rv = self.app.get('/?output=json')
    	self.fail()
        

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.fail()
