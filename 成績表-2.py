f=input("全班多少人:")
f=int(f)
na=[]
w=[]
y=0
x=101
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
    if g>y:
        y=g
        maxi=i
    if g<y:
        x=g
        mini=i
    i=i+1
maxw=max(w)
minw=min(w)
sumw=sum(w)
print(na)
print(w)
print("平均分數:",sumw/f)
print("最高分數:",na[maxi],maxw)
print("最低分數:",na[mini],minw)
