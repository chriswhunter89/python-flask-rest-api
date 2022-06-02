from flask import Flask
from flask_restful  import Api, Resource

app = Flask(__name__) #always added when creating flask app
api = Api(app) # this statment says we will wrap the app in an API and initialises the restful API

names = {"chris": {"age": 32, "gender": "male"}, "presto": {"age": 72, "gender": "male"}}

class HelloWorld(Resource):
    def get(self, name):
        return names[name] #objects returned from an api must be json serialisable (dictionaries)

    def post(self):
        return {"data": "Posted"}

api.add_resource(HelloWorld, "/helloworld/<string:name>")

# starts the server and flask application
if __name__ == "__main__":
    app.run(debug=True)
