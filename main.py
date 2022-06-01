from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__) #always added when creating flask app
api = Api(app) # this statment says we will wrap the app in an API and initialises the restful API
