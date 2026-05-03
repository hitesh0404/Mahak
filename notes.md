# Setup
## Virtual Environment
- Venv keep a copy of python into seperate folder for different project
- for multiple different python project we may require different version on packages
- the Venv help in keeping things seprate 
- command to create Venv
- 1. python -m venv env     -- for windows
- 1. python3 -m venv env    -- for mac or linux
- 2. env/Scripts/activate   -- for windows
- 2. . env/bin/activate     -- for mac or linux

## Install Django
- after activation of env 
- pip install django


## create new Django Project 
- django-admin startproject projectName

## run Django Project
- cd projectName
- python -m manage.py runserver

## create new app
- python manage.py startapp appName
- python manage.py startapp inventory

## transfer the models from class structure to db tables structure
- python manage.py makemigrations
- this command create migration file which help us to track the DB changes
- python manage.py migrate
- this command read the migration files and transfer the structure to DB

## collect static file 
- python manage.py collectstatic

## to create superUser
- python manage.py createsuperuser