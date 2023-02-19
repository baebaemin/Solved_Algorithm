lst = input()
laser = stack = rlt = 0

for i in lst:
    if not laser:
        if i == '(':
            laser = 1
        else:
            laser = 0
            stack -= 1
            rlt += 1
    else:
        if i == '(':
            stack += 1
        else:  # 레이저 가동
            rlt += stack
            laser = 0
print(rlt)