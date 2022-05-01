from pykiwoom.kiwoom import *
print("실햄됨")
kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

종목상태 = kiwoom.GetMasterStockState("005930")
print(종목상태)