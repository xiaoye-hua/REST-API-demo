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
            , 'age': fields.Integer(required=True, titile='Age', example=13, descriptions="Enter the age")
            ,

            'from': fields.List(fields.String(required=True,
                                              title='friends name',
                                              ),
                                example=["Friend1", 'FriendB', "Friend C"]
                                )
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
        age = payload.get('age')
        friends = payload.get('from')
        greeting = 'Happy Birthday for ' + str(age) + ', ' + name + ", from " + ", ".join(friends)
        res = {
            'greeting': greeting
        }
        return res