"""
Module - contains all the end point for
a person object
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os

# Initializing app
app = Flask(__name__)

# Database connection
load_dotenv()

# Database credentials
db_user = os.environ['DB_USER']
db_pwd = os.environ['DB_PWD']
db_name = os.environ['DB_NAME']

hng_db = "mysql://{}:{}@localhost/{}".format(db_user, db_pwd, db_name)
app.config['SQLALCHEMY_DATABASE_URI'] = hng_db

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Person(db.Model):
    """
    A class linked to the database as table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """
        Returns string representaion
        of person object
        """
        return "{}".format(self.name)


class PersonSchema(ma.Schema):
    """
    Serializes objects
    """
    class Meta:
        fields = ('id', 'name')


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)


# ENDPOINTS


@app.route('/api', methods=['GET'])
def get_persons():
    """
    Returns all Person objects
    """
    objs = Person.query.all()
    objs = persons_schema.dump(objs)

    return jsonify(objs)


@app.route('/api/<int:id>', methods=['GET'])
def get_person(id):
    """
    Returns a person object by id
    """
    obj = Person.query.get(id)

    return person_schema.jsonify(obj)


@app.route('/api/<name>', methods=['GET'])
def get_person_body(name):
    """
    Returns a person object by name
    """
    if type(name) == str:
        obj = Person.query.filter(Person.name == name).one_or_none()

        return person_schema.jsonify(obj)


@app.route('/api', methods=['POST'])
def create_person():
    """
    Creates a new person object
    """
    name = request.json['name']

    new = Person()
    new.name = name

    db.session.add(new)
    db.session.commit()

    return person_schema.jsonify(new)


@app.route('/api/<int:id>', methods=['PATCH'])
def partial_person_update(id):
    """
    Partially updates a person object
    """
    obj = Person.query.get(id)

    name = request.json['name']

    obj.name = name
    db.session.commit()

    return person_schema.jsonify(obj)


@app.route('/api/<name>', methods=['PATCH'])
def partial_person_update_name(name):
    """
    Partially updates a person object by name
    """
    if type(name) == str:
        obj = Person.query.filter(Person.name == name).one_or_none()
        name = request.json['name']
        obj.name = name

        db.session.commit()

        return person_schema.jsonify(obj)


@app.route('/api/<int:id>', methods=['PUT'])
def update_person(id):
    """
    Updates an object by id
    if object doesn't exist, it returns all objects
    """
    try:
        obj = Person.query.get(id)

        name = request.json['name']

        obj.name = name

        db.session.commit()
        return person_schema.jsonify(obj)

    except Exception as e:
        objs = Person.query.all()
        objs = persons_schema.dump(objs)

        return jsonify(objs)


@app.route('/api/<name>', methods=['PUT'])
def update_person_name(name):
    """
    Updates a person object by name attribute.
    If object doesn't exist, It returns all objects.
    """
    if type(name) == str:
        try:
            obj = Person.query.filter(Person.name == name).one_or_none()
            name = request.json['name']

            obj.name = name

            db.session.commit()
            return person_schema.jsonify(obj)
        except Exception as e:
            print(e)
            objs = Person.query.all()
            objs = persons_schema.dump(objs)
            return jsonify(objs)


@app.route('/api/<int:id>', methods=['DELETE'])
def delete_person(id):
    """
    Deletes a person object by id
    """
    obj = Person.query.get(id)
    db.session.delete(obj)
    db.session.commit()

    return person_schema.jsonify(obj)


@app.route('/api/<name>', methods=['DELETE'])
def delete_person_name(name):
    """
    Deletes a person object by name
    """
    if type(name) == str:
        obj = Person.query.filter(Person.name == name).one_or_none()
        db.session.delete(obj)
        db.session.commit()

        return person_schema.jsonify(obj)


if __name__ == "__main__":
    app.run()
