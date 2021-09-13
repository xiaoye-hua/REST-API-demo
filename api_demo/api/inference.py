# -*- coding: utf-8 -*-
# @File    : inference.py
# @Author  : Hua Guo
# @Time    : 2021/9/14 上午5:41
# @Disc    :
from flask_restplus import Resource

from api_demo.app import api


@api.route('/inference')
class Inference(Resource):
    def get(self):
        return 'Hello world'
    # def post(self):
    #     return