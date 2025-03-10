# Deapartment for Transport Contact Module Task

## Cloning the Task form the Repo
[Task Repo](https://github.com/etoo1960/dt)

`git clone https://github.com/etoo1960/dt`

## Creating a virtual environment
`python -m venv .venv`

## Activating The Virtual Environment
`source .venv/bin/activate`

## Installing Django
`pip install -r requirements.txt`

## Running the Migration
`python manage.py migrate`

## Starting the Application server
`python manage.py runserver`

## Running the unit tests
`python manage.py test`

## Django deployment
Django can be seamless deploy to any cloud provider services
- AWS (EC2, Elastic Beanstack)
- Azure
- Google cloud

Django can be deploy with WSGI (Web Server Gateway Interface) or ASGI (Asynchronous Server Gateway Interface).
The [link](https://docs.djangoproject.com/en/5.1/howto/deployment/) reference django official documentation on how to seamlessly deploy django application to different servers.

## Application User Interface
![alt text](https://github.com/etoo1960/dt/blob/main/crud/static/crud/Screenshot%20from%202025-02-23%2019-15-27.png)