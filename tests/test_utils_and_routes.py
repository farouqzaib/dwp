import requests
import json
import unittest
from unittest import mock

from utils import filter_people_50_miles_around_london
from config import UPSTREAM_API
from server import app

#FIXTURES contains 4 records with 2 of them within 50 miles of London
with open('./tests/fixtures.json') as json_file:
    FIXTURES = json.load(json_file)

# This method will be used by the mock to replace requests.get
def mocked_requests_get_200(*args, **kwargs):
    #This is a mock for the upstream API where it returns HTTP 200 and valid JSON
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse(FIXTURES, 200)

def mocked_requests_get_500(*args, **kwargs):
    #This is a mock for the upstream API where it returns HTTP 500 and no JSON
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({}, 500)

# Our test case class
class FetchPeopleTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()        

    def test_filter_people_50_miles_around_london_returns_2(self):
        filter_results = filter_people_50_miles_around_london(FIXTURES)
        self.assertEqual(2, len(filter_results))

    def test_filter_people_50_miles_around_london_returns_empty_list(self):
        filter_results = filter_people_50_miles_around_london([])
        self.assertEqual(0, len(filter_results))

    @mock.patch('requests.get', side_effect=mocked_requests_get_200)
    def test_fetch_people_route_returns_http_200(self, mock_get):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    @mock.patch('requests.get', side_effect=mocked_requests_get_200)
    def test_fetch_people_route_returns_list_of_length_2(self, mock_get):
        response = self.app.get('/')
        self.assertEqual(2, len(response.json['data']))

    @mock.patch('requests.get', side_effect=mocked_requests_get_500)
    def test_fetch_people_route_returns_http_502(self, mock_get):
        #for this test, we expect our API to return a HTTP 502 if the upstream API returns a 500
        response = self.app.get('/')
        self.assertEqual(response.status_code, 502)

if __name__ == '__main__':
    unittest.main()