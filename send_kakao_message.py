import requests
import json

with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

# kapi.kakao.com/v2/api/talk/memo/default/send 

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

data={
    "template_object": json.dumps({
        "object_type": "text",
        "text": "Sun 15:05",
        "link": {
            "web_url" : "헤헤. text와 link 객체는 필수로 넣어야 하는 거구나? button_title과 buttons는 안 넣어도 상관 없지만 말이야!",
            "mobile_web_url" : "헤헤. text와 link 객체는 필수로 넣어야 하는 거구나? button_title과 buttons는 안 넣어도 상관 없지만 말이야!",
        },
        "button_title" : "Saturday News"
    })
}

response = requests.post(url, headers=headers, data=data)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))