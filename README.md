# DigiTrader
A secure trading platform where people can exchange virtual currency with each other
## Installation instructions for Ubuntu

### Install the following for Ubuntu
`sudo apt-get update` `sudo apt-get install python3-dev postgresql postgresql-contrib django python-django-registration`

### Use the following if you're going to use pip instead of apt-get

`pip install -r requirements.txt`

### Virtual environment instructions
`pip install virtualenv`   
`virtualenv mysiteenv`   
`source mysiteenv/bin/activate`   

### Database settings
You can use the database of your choice but this program defaults to using postgresql   
Don't forget to configure settings.py to input your database settings.   
Default database name: creditsdb 
Default database user: credits  
Default database password: password    


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

change permissions on manage.py
`chmod +x manage.py`
