from flask import Flask
from flask_restplus import Api

from minimal_api_demo.config import port, host

app = Flask(__name__)
api = Api(app)
# api.namespace()

if __name__ == '__main__':
    app.run(debug=True,
            host=host,port=port
            )
