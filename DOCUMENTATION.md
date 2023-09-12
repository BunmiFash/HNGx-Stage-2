# Overview
This API handles requests and reponses to a Person resource. The methods allowed include:
- GET: To retrieve all person objects from the database or a particular object by id or name.
- POST: To add a person object to the database.
- PUT: To completely update all fields requested by id or name.
- PATCH: To partially update an object by requested by id or name.
- DELETE: To remove a person object requested by id or name.

# HOST
The API is hosted on http://bunmifash.pythonanywhere.com
## Endpoints
### GET /api
- Returns a list of person objects present in the database.
- Example:
Request
```
$ curl http://bunmifash.pythonanywhere.com/api

```
Response
```
[
	{
		"id":7,
		"name":"Elon Musk"
	},
	{
		"id":10,
		"name":"Shubby10"
	},
	{
		"id":11,
		"name":"Shobowale"
	},
	{
		"id":12,
		"name":"Jola Yemi"
	},
	{
		"id":13,
		"name":"Arinze olu"
	}
]
```
### GET /api/id
- Returns the person object whose id was passed to the request.
- Example:
Request
```
$ curl http://bunmifash.pythonanywhere.com/api/10
```
Response
```
{
	"id":10,
        "name":"Shubby10"
}

```
### GET /api/name
- Returns the person object whose name was passed to the request.
- Example:
Request
```
$ curl http://bunmifash.pythonanywhere.com/api/Shubby10
```
Response
```
{
        "id":10,
        "name":"Shubby10"
}
```
### POST /api
- Creates a new person object and adds it to the database and returns it.
- Example:
Request
```
$ curl -X POST -d '{"name": "Austin Manuel"}' -H 'Content-Type: application/json' http://127.0.0.1:5000/api
```
Response
```
{
	"id":14,
	"name":"Austin Manuel"
}
```
### PUT /api/id
- Updates all the attributes of the person object whose id was passed to the request and returns the updated object.
- Sample request
```
$ curl -X PUT -d '{"name": "Maxwell Zion"}' -H 'Content-Type: application/json' http://127.0.0.1:5000/api/14
```
Response
```
{
	"id":14,
	"name":"Maxwell Zion"
}
```
### PUT /api/name
- Updates all the attributes of the person object whose name was passed to the request and returns the updated object.
- Sample request
```
$ curl -X PUT -d '{"name": "Abiola Samuel"}' -H 'Content-Type: application/json ' http://127.0.0.1:5000/api/Arinze%20olu
```
Response
```
{
        "id":13,
        "name":"Abiola Samuel"
}
```
### PATCH /api/id
- Updates the selected attributes of the person object whose id was passed to the request and returns the updated object.
- Sample request
```
$ curl -X PATCH -d '{"name": "Maxwell Zion"}' -H 'Content-Type: application/json' http://127.0.0.1:5000/api/14
```
Response
```
{
        "id":14,
        "name":"Maxwell Zion"
}
```
### PATCH /api/name
- Updates the selected attributes of the person object whose name was passed to the request and returns the updated object.
- Sample request
```
$ curl -X PATCH -d '{"name": "Abiola Samuel"}' -H 'Content-Type: application/json ' http://127.0.0.1:5000/api/Arinze%20olu
```
Response
```
{
        "id":13,
        "name":"Abiola Samuel"
}
```
### DELETE /api/id
- Removes the person object whose id was passed to the request from the database  and returns the deleted object.
- Sample request
```
$ curl -X DELETE http://127.0.0.1:5000/api/14
```
Response
```
{
        "id":14,
        "name":"Maxwell Zion"
}
```
A get request shows the object no longer exists in the database.

```
curl http://127.0.0.1:5000/api
```
```
[
	{
		"id":7,
		"name":"Elon Graft"
	},
	{
		"id":10,
		"name":"Shubby10"
	},
	{
		"id":11,
		"name":"Shobowale"
	},
	{
		"id":12,
		"name":"Jola Yemi"
	},
	{
		"id":13,
		"name":"Abiola Samuel"
	}
]
```

### DELETE /api/name
- Removes the person object whose name was passed to the request from the database  and returns the deleted object.
- Sample request
```
$ curl -X DELETE http://127.0.0.1:5000/api/Shubby10
```
Response
```
{
        "id":10,
        "name":"Shubby10"
}
```
A get request shows the object no longer exists in the database.

```
curl http://127.0.0.1:5000/api
```
```
[
        {
                "id":7,
                "name":"Elon Graft"
        },
        {
                "id":11,
                "name":"Shobowale"
        },
        {
                "id":12,
                "name":"Jola Yemi"
        },
        {
                "id":13,
                "name":"Abiola Samuel"
        }
]
```
# cases of absent id or name
