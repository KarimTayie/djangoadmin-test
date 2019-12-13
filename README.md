# The Wall App

The Wall App is a website that allows users to register, login, and write on a wall.

## Features

- Registration / Login: Anonymous users can create a new user and this new user receives a welcome email. New users can then log in. 

- Wall (authed): After logging in, a user can post messages on the site-wide wall, similar to a Facebook wall except there is only one wall for the entire site.

- Wall (guest): Guests as well as authed users can see all of the messages on the wall.

## 	Prerequisites

Install virtualenv

On macOS and Linux:
```json
$ python3 -m pip install --user virtualenv
```

On Windows:
```json
$ py -m pip install --user virtualenv
```


Create virtualenv

On macOS and Linux:
```json
$ python3 -m venv env
```

On Windows:
```json
$ py -m venv env
```


Activate virtualenv

```json
$ source env/bin/activate
```


Install all project dependencies

```json
$ pip install -r /requirements.txt
```

## How to run

### Default

You can run the application from the command line with manage.py. Go to the root folder of the application.

First run:

```json
$ cd app/
```

Run migrations:

```json
$ python manage.py migrate
```

Run server on port 8000:

```json
$ python manage.py runserver 8000
```

## Docker

It is recommended to run the app using docker:

here you can read more about docker
* Docker Documentation (https://docs.docker.com/)

Build the Docker image:

```json
$ docker-compose up --build
```

## Unit Tests

To run the unit tests, run this command inside app folder:

```json
$ python manage.py test && flake8
```

If you are using docker, run this command inside app folder:

```json
$ docker-compose run app sh -c "python manage.py test && flake8"
```

## API Doc

Postman API collection link:
[wall-api Postman collection](https://www.getpostman.com/collections/d0f532a9d1631756bb45)

## Travis CI

Travis CI:
[wall-api Travis CI link](https://travis-ci.org/KarimTayie/wall-app)


## Django Admin Credentials

Email: admintest@themail3.net
Password: 123456
