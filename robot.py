import requests
import json


def getReply(msg):
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": msg
            }
        },
        # 图灵机器人api接口
        "userInfo": {
            "apiKey": "YOUR_APIKEY",
            "userId": "YOUR_USERID"
        }
    }
    rep = requests.post(url='http://openapi.tuling123.com/openapi/api/v2', json=data)
    res = json.loads(rep.text)
    result = res['results']
    return result[0]['values']['text']
