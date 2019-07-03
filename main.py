from flask import Flask
from flask_restful import Api

from controller.interad_object import InteradResource

app = Flask(__name__)
api = Api(app)

api.add_resource(InteradResource, '/stats/<string:source>')

if __name__ == "__main__":
    app.run(debug=True)