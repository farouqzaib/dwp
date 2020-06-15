from flask import Flask
from flask import jsonify, make_response
app = Flask(__name__)

import requests
import geopy.distance

LONDON_COORDS = (51.509865, -0.118092)

@app.route('/')
def fetch_people():
    london = []
    r = requests.get('https://bpdts-test-app.herokuapp.com/users')
    if r.status_code == 200:
        for person in r.json():
            query_coords = (float(person['latitude']), float(person['longitude']))
            if geopy.distance.distance(LONDON_COORDS, query_coords).miles <= 30:
                london.append(person)
        return make_response(jsonify({'status': 'success', 'data': london}), 200)
    else:
        return make_response(jsonify({'status': 'error', 'message': 'Upstream API did not respond with HTTP 200.'}), 502)