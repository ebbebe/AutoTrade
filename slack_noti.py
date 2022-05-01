# 슬랙 채팅 보내기 예시

import requests

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "토큰 입력"
 
post_message(myToken,"#noti","채팅 테스트22")
