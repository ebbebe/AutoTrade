from pykiwoom.kiwoom import *
import time

# 로그인
kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
print("로그인 완료")


# 조건식을 PC로 다운로드
kiwoom.GetConditionLoad()

print("test1")
# 전체 조건식 리스트 얻기
conditions = kiwoom.GetConditionNameList()
print("test2")
# 0번 조건식에 해당하는 종목 리스트 출력
myindex = 69
# condition_index = conditions[myindex][0]
# condition_name = conditions[myindex][1]
print("test3")
condition_index = conditions[1][0]
condition_name = conditions[1][1]
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)
Count = 0
print("test4")
#주식계좌
accounts = kiwoom.GetLoginInfo("ACCNO")
stock_account = accounts[0]

print("test5")

if codes is not None:
    print(codes)
    for code in codes:
        print(code)
        info = kiwoom.SendOrder("시장가매수", "0101", stock_account, 1, code, 1, 0, "03", "")
        print(info)
else:
    print("검색된 종목이 없습니다.")


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