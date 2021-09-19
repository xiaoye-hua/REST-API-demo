# -*- coding: utf-8 -*-
# @File    : img_inference.py
# @Author  : Hua Guo
# @Time    : 2021/9/14 上午11:30
# @Disc    :
import numpy as np
import json
import cv2
import io
import zlib
from PIL import Image

from flask_restplus import Resource, Namespace, fields

ns = Namespace(name='img_inference', description="API for image inference")


def serialize(img_arr):
    f = io.BytesIO()
    np.save(f, img_arr)
    encoded = zlib.compress(f.getvalue())
    return encoded


def deserialize(img_str):
    decoded = np.load(io.BytesIO(zlib.decompress(img_str)))
    return decoded


@ns.route('/')
class ImgInference(Resource):
    def get(self):
        """
        boxes: 框位置：[top_left_x, top_left_y, bottom_right_x, bottom_right_y]
        score: problity
        labels: card labels
        :return:
        """
        # whether_log = False
        # serialize_timer = TimeLogger(whether_log)
        # # deserialize_timer = TimeLogger(whether_log)
        # inference_timer = TimeLogger(whether_log)
        # draw_timer = TimeLogger(whether_log)
        # respond_timer = TimeLogger(whether_log)
        # cvt_timer = TimeLogger(whether_log)
        #
        # # request json timer
        # request_json_timer = TimeLogger(whether_log)
        # request_json_timer.begin()
        # # serialized = request.json['img_resized'].encode(encodding)
        #
        # r = request
        # convert string of image data to uint8
        # nparr = np.fromstring(r.data, np.uint8)
        #
        # request_json_timer.end()
        #
        # # cvt timer
        # # decode image
        # cvt_timer.begin()
        # img_resized = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # img_resized = img_resized / 255.
        # img_resized = img_resized.astype(np.float32)
        # print('Server img_resized(cv2 version):')
        # print(img_resized)
        # img_resized = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
        # cvt_timer.end()

        # inference timer
        # inference_timer.begin()
        # boxes, scores = sess.run(output_tensors, feed_dict={input_tensor: np.expand_dims(img_resized, axis=0)})
        # inference_timer.end()
        #
        # # draw timer
        # draw_timer.begin()
        # boxes, scores, labels = utils.cpu_nms(boxes, scores, num_classes, score_thresh=confidence, iou_thresh=threshold)
        # draw_timer.end()

        # image = utils.draw_boxes(image, boxes, scores, labels, classes, (IMAGE_H, IMAGE_W), show=False)
        # print(boxes)
        # print(scores)
        # print(labels)
        # print(boxes.shape)
        # print(scores.shape)
        # print(labels.shape)

        # card_names = [classes[label] for label in labels]
        # # serialize timer
        # serialize_timer.begin()

        image_path = "api_demo/img/output_img.jpg"
        IMAGE_W = 416
        IMAGE_H = 416
        frame = cv2.imread(image_path)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # image = Image.fromarray(image)
        img_resized = cv2.resize(frame, (IMAGE_W, IMAGE_H))

        # image_uint8 = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        _, img_encoded = cv2.imencode('.jpg', img_resized)
        # content_type = 'image/jpeg'
        # headers = {'content-type': content_type}
        # r = requests.post(
        #     'http://' + client_host + ':' + str(client_port) + '/inference',
        #     data=img_encoded.tostring(), headers=headers
        # )
        result = {'img_encode': img_encoded.tostring()}
        # serialize_timer.end()

        # respond timer
        # respond_timer.begin()
        # res = Response(json.dumps(result), mimetype='application/json')
        # respond_timer.end()
        # print('Request json {}s'.format(request_json_timer.total_time))
        # print('Cvt timer {}s'.format(cvt_timer.total_time))
        # print('Serialize {}s'.format(serialize_timer.total_time))
        # print('Inference {}s'.format(inference_timer.total_time))
        # print('Draw {}s'.format(draw_timer.total_time))
        # print('Res {}s'.format(respond_timer.total_time))

        return result