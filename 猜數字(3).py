import random
n=random.randint(1,20)
a=input("1~20猜一個數:")
a=int(a)
x=1
while a!=n:
    if a>n:
        a=input("太大了:1~20猜一個數:") 
        a=int(a)
    elif x==5 and a!=n:
        print("猜錯5次達上限答案是:",n)
        break
    else:
        a=input("太小了:1~20猜一個數:") 
        a=int(a)
    x=x+1
    
if a==n:
    print("猜對了答案是:",n)
    print("答題次數:",x)