from flask import Flask
from flask import jsonify, make_response
app = Flask(__name__)

import requests

from utils import filter_people_30_miles_around_london
from config import UPSTREAM_API

@app.route('/')
def fetch_people():
    people_around_london = []
    try:
        r = requests.get(UPSTREAM_API)
    except:
        return make_response(jsonify({'status': 'error', 'message': 'Upstream API could not be reached.'}), 500)

    if r.status_code == 200:
        try:
            response = r.json()
        except:
            return make_response(jsonify({'status': 'error', 'message': 'Error parsing JSON object returned by upstream API.'}), 500)

        try:
            people_around_london = filter_people_30_miles_around_london(response)
        except Exception as e:
            return make_response(jsonify({'status': 'error', 'message': e.message}), 500)
        
        return make_response(jsonify({'status': 'success', 'data': people_around_london}), 200)
    else:
        return make_response(jsonify({'status': 'error', 'message': 'Upstream API did not respond with HTTP 200.'}), 502)