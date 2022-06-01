from flask import Flask
from flask_restful  import Api, Resource

app = Flask(__name__) #always added when creating flask app
api = Api(app) # this statment says we will wrap the app in an API and initialises the restful API

class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"} #objects returned from an api must be json serialisable (dictionaries)

api.add_resource(HelloWorld, "/helloworld")

# starts the server and flask application
if __name__ == "__main__":
    app.run(debug=True)
