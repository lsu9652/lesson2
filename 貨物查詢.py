i=0
d={"冰箱":"25000元","電視":"21000元","電池":"50元"}
while i!=2:
    i=int(input("輸入1進行貨物查詢,輸入2離開:"))
    if i==2:
        break
    else:
        n=input("輸入商品:")
        if n=="冰箱":
            t=d["冰箱"]
            print(t)
        elif n=="電視":
            t=d["電視"]
            print(t)
        elif n=="電池":
            t=d["電池"]
            print(t)
        else:
            import random
            s=random.randint(1000,100000)
            s=str(s)
            d[n]=s+"元"
            t=d[n]
            print(t)
