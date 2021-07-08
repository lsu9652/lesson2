import random
n=random.randint(1,10)
a=input("1~10猜一個數:")
a=int(a)
x=1
while a!=n:
    a=input("猜錯了:1~10猜一個數:") 
    a=int(a)
    x=x+1
    if x==5 and a!=n:
        print("猜錯5次達上限答案是:",n)
        break
if a==n:
    print("猜對了答案是:",n)
    print("答題次數:",x)

