# -*- coding: utf-8 -*-
# @File    : inference.py
# @Author  : Hua Guo
# @Time    : 2021/9/14 上午5:41
# @Disc    :
from flask_restplus import Resource, Namespace, fields

ns = Namespace(name='normal_inference', description='API for normal inference')


@ns.route('/inference')
class Inference(Resource):
    request_model = ns.model(
        name='request data format'
        , definition='Make sure to follow th format'
        , model={
            'name': fields.String(required=True, titile='Name', example='Xiaoye', descriptions="Enter the name")
        }
    )
    responds_model = ns.model(
        name='respond data format'
        , model={
            'greeting': fields.String(required=True, titile='Greeting', example='Happy Birthday, Xiaoye', descriptions="Greeting returned")
        }
    )
    def get(self):
        return 'Hello world'

    @ns.expect(request_model)
    @ns.marshal_with(responds_model)
    def post(self):
        payload = ns.payload
        name = payload.get('name')
        res = {
            'greeting': 'Happy Birthday, ' + name
        }
        return res