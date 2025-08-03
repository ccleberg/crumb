import unittest
from flask import Flask
from server import app

class TestServer(unittest.TestCase):

    def test_log_visit_post(self):
        # Create a test client
        client = app.test_client()

        # Sample JSON data
        data = {
            'title': 'Test Visit',
            'url': 'https://test.com',
            'hostname': 'test.com',
            'path': '/',
            'query': 'test',
            'tabId': 123,
            'windowId': 456,
            'favIconUrl': 'https://example.com/favicon.ico'
        }

        # Send a POST request
        response = client.post('/', data=data, content_type='application/json')

        # Assertions
        self.assertEqual(response.status_code, 204)
        # Optionally check the log file contents (for verification)
        # This part would require additional logging setup.
        # self.assertTrue('Test Visit' in self.get_log_content())

    def test_log_visit_options(self):
        # Send an OPTIONS request
        response = client.options( '/', content_type='application/json')
        self.assertEqual(response.status_code, 204) #Verify 204 No Content for OPTIONS
