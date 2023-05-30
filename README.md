# New-Task
# Overview
This project is a REST API built using Django, Django REST Framework, and GeoDjango. The API allows users to create, retrieve, update, and delete geographical places stored in a PostGIS database. The API also supports retrieving the nearest place given a specific longitude and latitude.

# Installation and Setup
# Requirements
- Python 3.7+
- Django 3.0+
- Django REST Framework
- Django CORS Headers
- PostgreSQL with PostGIS extension

# Installation
- Clone the repository: git clone https://github.com/Bohdan2001007/New-Task.git
- Change into the project directory: cd New-Task
- Install the requirements: pip install -r requirements.txt
- Set up the database: Update the DATABASES configuration in settings.py with your PostgreSQL credentials and database name. Make - sure that the PostGIS extension is installed on your database.
- Run migrations: python manage.py migrate

# Setting environment variables
At the root of the project, create a `.env` file and add the following variables:
- SECRET_KEY=your-secret-key
- DB_NAME=your-database-name
- DB_USER=your-user
- DB_PASSWORD=your-password
- DB_HOST=your-localhost
- DB_PORT=your-port

Replace the values with your real credentials and secret key. Django will then automatically use those values.

# Usage
Start the server by running python manage.py runserver.

The following endpoints are available:

- GET /places/: Get a list of all places.
- POST /places/create/: Create a new place.
- PUT /places/<id>/: Update an existing place with given id.
- DELETE /places/<id>/: Delete an existing place with given id.
- GET /places/nearest/?latitude=<latitude>&longitude=<longitude>: Get the nearest place from the specified latitude and longitude.

# Data Format
The geographical data is formatted as GeoJSON. When creating or updating a place, you can send a JSON object in the following format: 
 {
  "name": "Place Name",
  "description": "Place Description",
  "geom": {
    "type": "Point",
    "coordinates": [longitude, latitude]
  }
}

