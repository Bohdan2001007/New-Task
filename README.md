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

# Usage
Start the server by running python manage.py runserver.

The following endpoints are available:

- GET /places/: Get a list of all places.
- POST /places/create/: Create a new place.
- PUT /places/<id>/: Update an existing place with given id.
- DELETE /places/<id>/: Delete an existing place with given id.
- GET /places/nearest/?latitude=<latitude>&longitude=<longitude>: Get the nearest place from the specified latitude and longitude.

# Data Format
