def burger(i, sumK, taste):
    global maxT
    if sumK >= target:
        maxT = max(maxT, taste)
        return

    if i == N:
        if sumK >= target:
            maxT = max(maxT, taste)
        return

    burger(i + 1, sumK + lstK[i][1], taste - lstK[i][0])
    burger(i + 1, sumK, taste)

for tc in range(1, int(input())+1):
    N, maxK = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    target = sum(list(k for _, k in lst)) - maxK
    totalT = sum(list(t for t, _ in lst))
    lstK = sorted(lst, key=lambda x: (x[1], x[0]), reverse=True)
    maxT = 0
    burger(0, 0, totalT)
    print(f'#{tc} {maxT}')