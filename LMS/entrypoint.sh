#!/bin/sh

#wait for db to initialize
echo "Wating for db to initialize"
sleep 5

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

#Loading the db state where we have few records and superuser already created
python manage.py loaddata db.json

# Start dev server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000