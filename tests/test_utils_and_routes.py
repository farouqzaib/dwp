import requests
import json
import unittest
from unittest import mock

from utils import filter_people_30_miles_around_london

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

    if args[0] == 'https://bpdts-test-app.herokuapp.com/users':
        return MockResponse(FIXTURES, 200)

    return MockResponse(None, 404)

# Our test case class
class FetchPeopleTestCase(unittest.TestCase):

    def test_filter_people_30_miles_around_london(self):
        filter_results = filter_people_30_miles_around_london(FIXTURES)
        self.assertEqual(2, len(filter_results))

if __name__ == '__main__':
    unittest.main()