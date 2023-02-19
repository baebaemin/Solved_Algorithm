while 1:
    a, b, c = sorted(map(int, input().split()))
    if a == b == c == 0:
        break
    elif c ** 2 == a ** 2 + b ** 2:
        print('right')
    else:
        print('wrong')