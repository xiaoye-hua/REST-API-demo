from flask import Flask
from flask_restplus import Api

from api_demo.config import port, host
from api_demo.api.inference import ns as inference_namespace
from api_demo.api.img_inference import ns as img_inference_namespace

app = Flask(__name__)
api = Api(app)
api.add_namespace(inference_namespace)
api.add_namespace(img_inference_namespace)

if __name__ == '__main__':
    app.run(debug=True,
            host=host, port=port
            )
