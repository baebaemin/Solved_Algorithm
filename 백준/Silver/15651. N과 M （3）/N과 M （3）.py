def dfs(k, lst):
    if k == M:
        if len(lst) == M:
            print(*lst)
        return
    for i in range(1, N+1):
        dfs(k+1, lst+[i])

N, M = map(int, input().split())
dfs(0, [])