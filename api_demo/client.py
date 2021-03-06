# -*- coding: utf-8 -*-
# @File    : client.py
# @Author  : Hua Guo
# @Time    : 2021/9/14 上午5:19
# @Disc    :
import requests
import json
import cv2

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
request_data = {
          "name": "Xiaoye",
          "age": 13,
          "from": [
            "Friend1",
            "FriendB",
            "Friend C"
          ]
        }
# convert request_data to json data
json_data = json.dumps(request_data)
# send requests
res = requests.post(headers=request_header, data=json_data, url=norm_inference_url)
# convert from json to normal data
result = json.loads(res.content)
print(f"Normal inference result: {result}")


# # image post
#
# frame = cv2.imread(image_path)
# image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# img_resized = cv2.resize(frame, (IMAGE_W, IMAGE_H))
#
# # 得到request反馈
# boxes, scores, labels = get_inference(img_resized)
# # 得到结果都是相对于 img_resized
# # boxes: 框位置：[top_left_x, top_left_y, bottom_right_x, bottom_right_y]
# # score: probability
# # labels: card name
#
#
# # 画框，保存图片
# draw_save_image(image, (boxes, scores, labels), "output.png")
# _, img_encoded = cv2.imencode('.jpg', img_resized)
# content_type = 'image/jpeg'
# headers = {'content-type': content_type}
# r = requests.post(
#     'http://' + client_host + ':' + str(client_port) + '/inference',
#     data=img_encoded.tostring(), headers=headers
# )
