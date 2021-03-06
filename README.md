### FOLDER STRUCTURE
- server.py - main code for route
- utils.py - helper function
- config.py - contains configuration used. Mostly declaration of upstream API URL
- requirements.txt - contains packages required to be installed
- tests/test_utils_and_routes.py - tests for route and helper function
- tests/fixtures.json - fixtures used during tests

### INSTALLATION
This code has been tested on Python 3. 
In a terminal, navigate to root folder and run the following.

    pip install -r requirements.txt

### SET ENVIRONMENT VARIABLE
In a terminal set the following environment variable or do so in the appropriate profile file.

`export UPSTREAM_API='https://bpdts-test-app.herokuapp.com/users'`

### RUNNING THE TESTS
In a terminal, navigate to the root folder and run the following.

    python3 -m tests.test_utils_and_routes

### STARTING THE SERVER
In a terminal, navigate to the root folder and run the following commands.

1. `export FLASK_APP=server.py`
2. `flask run`

Server should be available at 127.0.0.1:5000

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

OR

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
5. Cache distance between coordinates in Redis or similar.