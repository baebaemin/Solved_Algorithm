N = int(input())
dp = [0] * (N+1)

for i in range(2, N + 1):   # 1은 0번이니까 2부터 순회
    dp[i] = dp[i-1] + 1     # -1의 경우
    if not i % 2:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if not i % 3:
        dp[i] = min(dp[i], dp[i // 3] + 1)
        
print(dp[N])