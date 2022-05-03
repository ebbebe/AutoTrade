#참고용

# 로그인
# kiwoom = Kiwoom()
# kiwoom.CommConnect(block=True)
# print("로그인 완료")
# post_message(myToken, "#noti", "로그인 완료")

# # 조건식을 PC로 다운로드
# kiwoom.GetConditionLoad()

# # 전체 조건식 리스트 얻기
# conditions = kiwoom.GetConditionNameList()

# # 검색할 조건식 설정
# myindex = 69
# condition_index = conditions[myindex][0]
# condition_name = conditions[myindex][1]
    
# #주식계좌
# accounts = kiwoom.GetLoginInfo("ACCNO")
# stock_account = accounts[0]

############################################
# 배열 문자열 배열로 변환
# for i in range(len(conditions)):
#     conditions[i] = str(conditions[i])

# str = ',\n'.join(conditions)
# print(str)
############################################

# 문자열 slack에 메시지 보내기
# post_message(myToken,"#noti",str)





# buy = kiwoom.SendOrder("시장가매수 테스트", "0331", stock_account, 1, "005930", 1, 0, "03", "")
# print("매수시도:" , buy)

# sell = kiwoom.SendOrder("시장가매도 테스트", "0101", stock_account, 2, "005930", 10, 0, "03", "")
# print("매도시도:" , sell)
