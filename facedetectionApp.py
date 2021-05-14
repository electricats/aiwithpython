# encoding:utf-8
import urllib.request
#import cv2
import json
import ast
import base64
import urllib.parse
from urllib.parse import urlencode

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        data = base64.b64encode(fp.read())
        return data

img = get_file_content('tom.jpeg')

# request address
request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
# parameters , you can change the face_field to obtain more informations
# please check: https://cloud.baidu.com/doc/FACE/s/yk37c1u4t for detail
params = {'image': '' + str(img, 'utf-8') + '', 'image_type': 'BASE64',
          'face_field': 'age,beauty,gender,glasses,mask,emotion'}
params = urlencode(params)
# put in your access_token (already done by Will XD)
access_token = '24.50ba118178f6e38fa652c2378934a840.2592000.1623580748.282335-10439231'
request_url = request_url + "?access_token=" + access_token
request = urllib.request.Request(url=request_url, data=params.encode("utf-8"))
request.add_header('Content-Type', 'application/json')
response = urllib.request.urlopen(request)
content = response.read()
content = json.loads(content)
print(content['result']['face_list'][0]['beauty'])
