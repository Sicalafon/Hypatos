import unittest
from hello_world import app
from hello_world.formater import SUPPORTED
from flask import url_for


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()



    def test_outputs(self):
        for output in SUPPORTED:
            rv = self.app.get('/?output={}'.format(output))
            self.assertEqual(str(rv),"<Response streamed [200 OK]>","{} output invalid".format(output))


    def test_msg_with_output(self):
       rv= self.app.get('/?output=json')
       self.assertEqual(rv.data,b'{ "imie":"Natalia \\"Nat", "mgs":"Hello World!"}')
       rv= self.app.get('/?output=plain_uppercase')
       self.assertEqual(rv.data,b'NATALIA "NAT HELLO WORLD!')
       rv= self.app.get('/?output=plain_lowercase')
       self.assertEqual(rv.data,b'natalia "nat hello world!')
       rv= self.app.get('/?output=plain')
       self.assertEqual(rv.data, b'Natalia "Nat Hello World!')


    def test_redirection(self):
       #Testing if starts redirecting
       rv= self.app.get('/ui')
       self.assertEqual(str(rv.status_code),"302")

       #Testing if redirect
       rv= self.app.get('/ui', follow_redirects=True)
       self.assertEqual(str(rv.status_code),"200")

       rv= self.app.get('/ui', follow_redirects=True)
       print(rv.data)








