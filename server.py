from flask import Flask
app = Flask(__name__)

import requests

@app.route('/')
def hello_world():
    return 'Hello, World!'