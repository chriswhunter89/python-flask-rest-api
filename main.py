from flask import Flask
from flask_restful  import Api, Resource, reqparse
from flask import abort

app = Flask(__name__) #always added when creating flask app
api = Api(app) # this statment says we will wrap the app in an API and initialises the restful API

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)

videos = {}

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, "Video id is not valid . . . ")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id] # objects returned from an api must be json serialisable (dictionaries)

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201 #returns created video and status code
api.add_resource(Video, "/video/<int:video_id>")

# starts the server and flask application
if __name__ == "__main__":
    app.run(debug=True)
