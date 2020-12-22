from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        return {'item': name}


api.add_resource(Item, '/item/<string:name>')

if __name__ == '__main__':
    app.run()
