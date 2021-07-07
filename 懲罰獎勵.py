math=input("輸入數學成績:")
en=input("輸入英文成績:")
math=int(math)
en=int(en)
if math>=90 and en>=90:
    print("有獎品")
elif math<=60 and en<=60:
    print("要處罰")