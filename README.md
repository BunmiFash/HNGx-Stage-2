# GETTING STARTED
### Dependencies
```
flask
flask-sqlalchemy
flask-marshmallow - To serialize our data
mysqlclient - To connect to the MySQL database used
```
### Installing dependencies
The dependencies are present in the requirements.txt file.
- Ensure a virtual environment is created and activated before installation.
```
$ pip install -r requirements.txt
```
- To run the API locally, the app.py file is executed as it contains all the endpoints.
```
$ python3 app.py
```
### Methods and enpoints
The methods allowed by this API are:
- GET - To retrieve all data or specific data from trhe database
- POST - To add data to the database.
- PUT - To update all fields of an object.
- PATCH - To partially update an object.
- DELETE - To remove an object from the database.
The formats for requests and response to each endpoint is explained in the [DOCUMENTATION.md](HNGx-Stage-2
/DOCUMENTATION.md) file.
