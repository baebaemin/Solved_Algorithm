def dfs(k, s, lst):
    if k == M:
        if len(lst) == M:
            print(*lst)
        return

    for i in range(s, N+1):
        dfs(k+1, i, lst+[i])  

N, M = map(int, input().split())
dfs(0, 1, [])