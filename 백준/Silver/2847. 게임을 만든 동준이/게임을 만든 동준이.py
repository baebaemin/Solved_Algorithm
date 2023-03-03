N = int(input())
lst = [int(input()) for _ in range(N)]
cnt = 0
for i in range(N-1, 0, -1):
    if lst[i] <= lst[i-1]:
        adj = lst[i-1] - lst[i] + 1
        lst[i-1] -= adj
        cnt += adj

print(cnt)