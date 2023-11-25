def solution(num_list):
    dp = [0] * 31
    answer = 0
    for i in range(2, 31):
        if not i % 2:
            dp[i] = dp[i//2] + 1
        else:
            dp[i] = dp[(i-1) // 2] + 1
    # print(dp)
    for num in num_list:
        answer += dp[num]
    return answer