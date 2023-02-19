def dfs(k, s, lst):
    if k == M:
        print(*lst)
        return
    for j in range(s, N+1):
        dfs(k+1, j+1, lst+[j])


N, M = map(int, input().split())
dfs(0, 1, [])