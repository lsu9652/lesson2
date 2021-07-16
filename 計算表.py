a=0
t=0
os=0
i=0
d=0
while i!=6:
    print("工能表")
    print("(1)設定")
    print("(2)進貨")
    print("(3)出貨")
    print("(4)營業額統計")
    print("(5)庫存")
    print("(6)離開")
    i=int(input("輸入選項:"))
    if i==1:
        a=int(input("最初有幾顆蘋果:"))
        d=int(input("一顆賣多少錢"))
        print("")
    elif i==2:
        t=int(input("進貨多少"))
    elif i==3:
        os=int(input("賣多少"))
    elif i==4:
        print("營業額:",os*d)
        print("")
    elif i==5:
        print("剩幾顆蘋果:",a+t-os)
        print("")
    