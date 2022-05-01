## 일정 시간 실행 예시


import schedule
import time
import datetime
import sys

def test_function():
    now = datetime.datetime.now()
    print("test code-  현재 시간 출력하기")
    print(now)

def exit():
    print("function exit")
    sys.exit()

schedule.every(1).seconds.do(test_function)
schedule.every().day.at("18:00").do(exit)


while True:
    schedule.run_pending()
    time.sleep(1)