import random
n=random.randint(1,20)
a=input("1~20猜一個數:")
a=int(a)
if a==n:
    print("猜對了答案是:",a)
else:
    print("猜錯了答案是:",n)