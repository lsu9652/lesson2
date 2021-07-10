f=input("全班多少人:")
f=int(f)
w=[]
t=0
y=100
n=0
i=1
while i<=f:
    g=input("輸入數學分數:")
    g=int(g)
    w.append(g)
    i=i+1
    if g>=t:
        t=g
    if g<=y:
        y=g
    n=n+g
print(w)
print("平均分數:",n/f)
print("最高分數:",t)
print("最低分數:",y)
