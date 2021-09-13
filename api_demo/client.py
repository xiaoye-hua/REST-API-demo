# -*- coding: utf-8 -*-
# @File    : client.py
# @Author  : Hua Guo
# @Time    : 2021/9/14 上午5:19
# @Disc    :
import requests
import json

from minimal_api_demo.config import host, port

# basic config
base_request_url = 'http://' + host + ":" + str(port) + '/'
norm_inference_url = base_request_url+'normal_inference/inference'
request_header = {'Content-Type': 'application/json'}

# get method
result_get = requests.get(norm_inference_url)
res = result_get.json()
print(f'Result: {res}')

# post
request_data = {'name': 'Tom'}
# convert request_data to json data
json_data = json.dumps(request_data)
# send requests
res = requests.post(headers=request_header, data=json_data, url=norm_inference_url)
# convert from json to normal data
result = json.loads(res.content)
print(f"Normal inference result: {result}")
