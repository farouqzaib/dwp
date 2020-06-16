from flask import Flask
from flask import jsonify, make_response
app = Flask(__name__)

import requests
import geopy.distance

LONDON_COORDS = (51.509865, -0.118092)

@app.route('/')
def fetch_people():
    london = []
    try:
        r = requests.get('https://bpdts-test-app.herokuapp.com/users')
    except:
        return make_response(jsonify({'status': 'error', 'message': 'Upstream API could not be reached.'}), 500)

    if r.status_code == 200:
        try:
            response = r.json()
        except:
            return make_response(jsonify({'status': 'error', 'message': 'Error parsing JSON object returned by upstream API.'}), 500)

        for person in response:
            query_coords = (float(person['latitude']), float(person['longitude']))

            try:
                distance = geopy.distance.distance(LONDON_COORDS, query_coords).miles
            except:
                return make_response(jsonify({'status': 'error', 'message': 'We had a problem calculating the distance. Please try again later.'}), 500)
                
            if distance <= 30:
                london.append(person)
        return make_response(jsonify({'status': 'success', 'data': london}), 200)
    else:
        return make_response(jsonify({'status': 'error', 'message': 'Upstream API did not respond with HTTP 200.'}), 502)