T = int(input())

for _ in range(T):
    y = k = 0
    for _ in range(9):
        Y, K = map(int, input().split())
        y += Y
        k += K
    else:
        if y > k:
            print('Yonsei')
        elif k > y:
            print('Korea')
        else:
            print('Draw')