f=input("全班多少人:")
f=int(f)
na=[]
w=[]
max=0
min=101
n=0
i=0
i=int(i)
maxi=0
mini=0
while i<f:
    name=input("名字:")
    g=input("輸入數學分數:")
    g=int(g)
    w.append(g)
    na.append(name)
    print("號碼",i+1,"名字",name,"分數",g)
    n=n+g
    if g>max:
        max=g
        maxi=i
    if g<min:
        min=g
        mini=i
    i=i+1
print(na)
print(w)
print("平均分數:",n/f)
print("最高分數:",na[maxi],max)
print("最低分數:",na[mini],min)
