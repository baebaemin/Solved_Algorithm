N = int(input())
lst = sorted([tuple(map(int, input().split())) for _ in range(N)])
lst.sort(key=lambda x: x[1])
last = cnt = i = 0
while i < N:
    if last <= lst[i][0]:
        last = lst[i][1]
        cnt += 1
    i += 1
print(cnt)