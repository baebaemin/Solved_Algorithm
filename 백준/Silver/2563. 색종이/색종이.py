N = int(input())
arr = [[0] * 100 for _ in range(100)]
cnt = 0
for _ in range(N):
    N, M = map(int, input().split())
    for n in range(N, N+10):
        for m in range(M, M+10):
            if not arr[n][m]:
                arr[n][m] = 1
                cnt += 1
print(cnt)