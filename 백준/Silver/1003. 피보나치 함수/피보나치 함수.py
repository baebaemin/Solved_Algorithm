T = int(input())

for _ in range(T):
    dp = [[1, 0], [0, 1]] + [[0, 0] for _ in range(39)]
    N = int(input())
    if N and N != 1:
        for i in range(2, N+1):
            dp[i][0] = dp[i-2][0] + dp[i-1][0]
            dp[i][1] = dp[i-2][1] + dp[i-1][1]
    print(*dp[N])