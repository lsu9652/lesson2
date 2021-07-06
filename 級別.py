s=input("輸入成績:")
s=int(s)
if 90<=s:
    print("A")
elif 80<=s and s<=89:
    print("B")
elif 70<=s and s<=79:
    print("C")
elif 60<=s and s<=69:
    print("D")
else:
     print("E")