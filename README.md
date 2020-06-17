### FOLDER STRUCTURE
server.py - main code for route
utils.py - helper function
config.py - contains configuration used. Mostly declaration of upstream API url
requirements.txt - contains packages required to be installed
tests/test_utils_and_routes.py - tests for route and helper function
tests/fixtures.json - fixtures used during tests

### INSTALLATION
This code has been tested on Python 3. 
Navigate to root folder and run the following.

    pip install -r requirements.txt

### STARTING THE SERVER
Navigate to the root folder and run the following commands

1.  `export FLASK_APP=server.py`
2. `flask run`

### STOPPING THE SERVER
`Ctrl+C` in the respective terminal it was started from.

### API
GET /

#### Sample responses:
**HTTP 200**

    {
    "data": [{"email": "agarnsworthy7d@seattletimes.com", 
    "first_name": "Ancell", "id": 266, "ip_address": 
    "67.4.69.137", "last_name": 
    "Garnsworthy", "latitude": 51.6553959,"longitude": 0.0572553},
    "status": "success"    
    }

**HTTP 500**

    {
        "message": "Upstream API could not be reached.",
        "status": "error"    
    }

    {
        "message": "Error parsing JSON object returned by upstream API.",
        "status": "error"    
    }

**HTTP 502**

    {
        "message": "Upstream API did not respond with HTTP 200.",
        "status": "error"    
    }


### TODOS
1. Wrap code in a Docker container.
2. Use Swagger to publish API documentation.
3. Setup up production server using nginx reverse-proxy to a uswgi server.
4. Is there a better name for the route?