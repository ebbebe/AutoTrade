from pykiwoom.kiwoom import *
from datetime import datetime
import requests
import time
import schedule
import datetime
import sys

def time_function():
    now = datetime.datetime.now()
    print("test code- 현재 시간 출력하기")
    print(now)

def noti_hour():
    now = datetime.datetime.now()
    mes = "1시간마다 실행 체크\n현재시간: " + str(now)
    post_message(myToken, "#noti", ("1시간마다 실행 체크\n현재시간: " + mes))

def exit():
    print("function exit")
    post_message(myToken, "#noti", ("장마감으로 실행 종료"))
    sys.exit()


def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

def alert():
    codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)
    code_name = ""
    for i in range(len(codes)):
        name = kiwoom.GetMasterCodeName(codes[i])
        print(name)
        code_name += (str(i+1) + '. ' + name + '(' + codes[i] + ')\n')

    print("검색값 확인:\n", code_name)
    noti = "검색식 조건에 맞는 종목이 검색었습니다\n" + code_name
    post_message(myToken,"#noti",noti)

    buylist = ""
    for i in range(len(codes)):
        buy = kiwoom.SendOrder("시장가매수 테스트", "0101", stock_account, 1, codes[i], 1, 0, "03", "")
        buylist += (str(buy) + "\n")
    noti_buy = "매수 확인:\n" + buylist
    post_message(myToken, "#noti", noti_buy)
        




    
myToken = "xoxb-3476862373345-3466584837492-bAP0hea2RlXhM8lRcfLptPlM"


# 로그인
kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
print("로그인 완료")


# 조건식을 PC로 다운로드
kiwoom.GetConditionLoad()

# 전체 조건식 리스트 얻기
conditions = kiwoom.GetConditionNameList()

############################################
# 배열 문자열 배열로 변환
# for i in range(len(conditions)):
#     conditions[i] = str(conditions[i])

# str = ',\n'.join(conditions)
# print(str)
############################################

# 문자열 slack에 메시지 보내기
# post_message(myToken,"#noti",str)

# 검색할 조건식 설정
myindex = 69
condition_index = conditions[myindex][0]
condition_name = conditions[myindex][1]
# condition_index = conditions[1][0]
# condition_name = conditions[1][1]



Count = 0
#주식계좌
accounts = kiwoom.GetLoginInfo("ACCNO")
stock_account = accounts[0]

# buy = kiwoom.SendOrder("시장가매수 테스트", "0331", stock_account, 1, "005930", 1, 0, "03", "")
# print("매수시도:" , buy)

# sell = kiwoom.SendOrder("시장가매도 테스트", "0101", stock_account, 2, "005930", 10, 0, "03", "")
# print("매도시도:" , sell)


#일정 시간마다 test_fuction을 동작시키기
#schedule.every(1).seconds.do(noti_hour)
schedule.every(1).hour.do(noti_hour)
schedule.every().day.at("17:55").do(alert)
schedule.every().day.at("19:54").do(alert)
schedule.every().day.at("18:00").do(exit)

while True:
    schedule.run_pending()
    time.sleep(1)
    








# if codes is not None:
#     print(codes)
#     for code in codes:
#         print(code)
#         info = kiwoom.SendOrder("시장가매수", "0101", stock_account, 1, code, 1, 0, "03", "")
#         print(info)
# else:
#     print("검색된 종목이 없습니다.")


# 삼성전자, 10주, 시장가주문 매수
      #kiwoom.SendOrder("요청명, 화면번호, 계좌번호, 주문유형, 주식종목코드, 주문수량, 주문단가, 거래구분, 원주문번호")
# info = kiwoom.SendOrder("시장가매수", "0101", stock_account, 1, "005930", 10, 0, "03", "")
# print(info)

# while Count < 10:
#     if codes is not None:
#         print("검색된 종목이 없습니다")
#         print(Count)
#     else:
#         print(codes)
#     Count = Count + 1
#     time.sleep(5)

