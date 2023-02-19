def dfs(k, lst):
    if k == M:
        print(*lst)
        return
    for i in range(N):
        dfs(k+1, lst+[n_lst[i]])

N, M = map(int, input().split())
n_lst = sorted(list(map(int, input().split())))
dfs(0, [])