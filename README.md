#  User management
Application for managing users:
- displaying the list of users,
- displaying the list of groups,
- adding new users,
- adding new groups,
- adding user/users to group,
- editing users and changing data,
- removing existing users<,

### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
##### Prerequisites
What things you need to install the software and how to install them.
User management requires to run:
- Django (ver. 1.11+)
- Python (ver. 3.0+)
- MySQL/PostgreSQL
#### Installation
##### 1. virtualenv / virtualenvwrapper
You should already know what is [virtualenv](https://virtualenv.pypa.io/en/stable/), preferably [virtualenvwrapper](https://bitbucket.org/dhellmann/virtualenvwrapper) at this stage. So, simply create it for your own project, where projectname is the name of your project:
```
$ mkvirtualenv --clear projectname
```
##### 2. Download
Now, you need the django-sample-app project files in your workspace:
```
$ cd /path/to/your/workspace
$ git clone https://github.com/hubert-hernoga/user_management.git
```
##### 3. Requirements
Right there, you will find the requirements.txt file that has all the great debugging tools, django helpers and some other cool stuff. To install them, simply type:
```
$ pip install -r requirements.txt
```

###### To start the project you must:
- create database in MySQL/PostgreSQL named 'user_management'
- integrate your database with our project
Open user_management/settings.py and find 'DATABASE', replace settings for yours db:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', (or 'ENGINE': 'django.db.backends.postgresql_psycopg2',)
        'NAME': 'user_management',
        'USER': <your user_name to db>,
        'PASSWORD': <your password to db>,
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
- make project migration to the database
```
/<project folder> $ ./manage.py makemigrations
/<project folder> $ ./manage.py migrate
```
- start local server
```
/<project folder> $ python manage.py runserver 0.0.0.0:8000
```
- open http://127.0.0.1:8000/ to the browser


## Deployment
You can deploy project on
```heroku``` server (then you can use only ```PostgreSQL```).
More information about deployment you can find here:
https://devcenter.heroku.com/articles/getting-started-with-python#introduction

### Technologies used

* Python (Django),
* JavaScript + JQuery,
* HTML + CSS,
* MySQL/PostgreSQL,
