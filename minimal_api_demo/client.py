# -*- coding: utf-8 -*-
# @File    : client.py
# @Author  : Hua Guo
# @Time    : 2021/9/14 上午5:19
# @Disc    :
import requests

from minimal_api_demo.config import host, port

base_request_url = 'http://' + host + ":" + str(port) + '/'

result_get = requests.get(base_request_url+'hello')
res = result_get.json()
print(f'Result: {res}')