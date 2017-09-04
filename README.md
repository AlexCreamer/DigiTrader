# Digital Credit Ledger
## Installation instructions for Ubuntu

### Install the following for Ubuntu
`
sudo apt-get update
sudo apt-get install python3-dev postgresql postgresql-contrib django python-django-registration
`

### Only use the following if you're going to use pip instead of apt-get

`pip install -r requirements`

### Notes
You might have to do the following before using runserver:

#### Site creation
`from django.contrib.sites.models import Site   
 Site.objects.create(name='127.0.0.1:8000', domain='localhost')`

#### Database
The default settings.py has `creditsdb` has the database name, `credits` as the user, and `password` as the password

