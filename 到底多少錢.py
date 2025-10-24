ReserveRate = int(input("預備金幾趴?"))
ReserveRate = ReserveRate / 100
TotalRate = ReserveRate + 1
# 上面在作基礎計算
TheTotal = int(input("這樣多少錢"))
# 開始輸入
TheReserve = TheTotal*ReserveRate #預備金
TheFinal = TheTotal*TotalRate #總價
print("預備金為：",TheReserve)
print("總價為：",TheFinal)
# 輸出