# 슬랙 채팅 보내기 예시

import requests

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-3476862373345-3466584837492-bAP0hea2RlXhM8lRcfLptPlM"
 
post_message(myToken,"#noti","채팅 테스트22")
