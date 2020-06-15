from flask import Flask
from flask import jsonify, make_response
app = Flask(__name__)

import requests

@app.route('/')
def fetch_people():
    r = requests.get('https://bpdts-test-app.herokuapp.com/city/London/users')
    if r.status_code == 200:
        return make_response(jsonify({'status': 'success', 'data': r.json()}), 200)
    else:
        return make_response(jsonify({'status': 'error', 'message': 'Upstream API did not respond with HTTP 200.'}), 502)