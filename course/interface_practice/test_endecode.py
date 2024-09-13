'''
对接口的返回值进行解密
'''
import requests
import json
import base64


class ApiRequest:

    req_data = {
        "method": "get",
        "url": "",
        "headers": "",
        "encoding": "base64"
    }

    def send(self, data: dict):
        res = requests.request(data['methd'], data['url'])
        if data['encoding'] == 'base64':
            return json.loads(base64.b64decode(res.content))