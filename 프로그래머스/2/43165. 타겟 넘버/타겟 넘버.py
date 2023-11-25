answer = 0

def dfs(n, sm, target, N, numbers):
    global answer
    if n == N:
        if sm == target:
            answer += 1
            # print(answer)
        return
    dfs(n+1, sm + numbers[n], target, N, numbers)
    dfs(n+1, sm - numbers[n], target, N, numbers)

def solution(numbers, target):
    N = len(numbers)
    dfs(0, 0, target, N, numbers)
    return answer