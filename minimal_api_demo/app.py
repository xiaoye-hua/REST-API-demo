from flask import Flask
from flask_restplus import Resource, Api

from minimal_api_demo.config import port, host

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class Hello(Resource):
    def get(self):
        return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True,
            host=host, port=port
            )
