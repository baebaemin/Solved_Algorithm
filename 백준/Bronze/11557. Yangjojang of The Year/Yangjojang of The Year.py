T = int(input())
for tc in range(T):
    N = int(input())
    maxV = -1
    for _ in range(N):
        school, num = input().split()
        if int(num) > maxV:
            maxV = int(num)
            rlt = school
    print(rlt)