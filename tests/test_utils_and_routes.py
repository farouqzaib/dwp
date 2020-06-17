import requests
import json
import unittest
from unittest import mock

from utils import filter_people_30_miles_around_london
from config import UPSTREAM_API
from server import app

with open('./tests/fixtures.json') as json_file:
    FIXTURES = json.load(json_file)
    
# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == UPSTREAM_API:
        return MockResponse(FIXTURES, 200)

    return MockResponse(None, 404)

# Our test case class
class FetchPeopleTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()        

    def test_filter_people_30_miles_around_london(self):
        filter_results = filter_people_30_miles_around_london(FIXTURES)
        self.assertEqual(2, len(filter_results))

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch_people_route_returns_200(self, mock_get):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch_people_route_returns_list_of_length_2(self, mock_get):
        response = self.app.get('/')
        self.assertEqual(2, len(response.json['data']))

if __name__ == '__main__':
    unittest.main()