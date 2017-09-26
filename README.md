# DigiTrader
A secure trading platform where people can exchange virtual currency with each other
## Installation instructions for Ubuntu

### Install the following for Ubuntu
`
sudo apt-get update
sudo apt-get install python3-dev postgresql postgresql-contrib django python-django-registration
`

### Use the following if you're going to use pip instead of apt-get

`pip install -r requirements`

### Database settings
Use Postgresql and make sure to configure settings.py for your database

### Notes
You might have to do the following before using runserver:

Run the following in a python shell   
`from django.contrib.sites.models import Site   
 Site.objects.create(name='127.0.0.1:8000', domain='localhost')`
 
 Create an admin account
 `python manage.py createsuperuser`
 
 make migrations
 `python manage.py makemigration` `python manage.py migrate` `python manage.py makemigrations credits_platform` `python manage.py migrate credits_plaform`   
 `
