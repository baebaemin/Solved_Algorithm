def dfs(k, lst):
    if k == M:
        if len(lst) == M:
            print(*lst)
        return

    for i in range(N):
        if used[i]:
            continue
        used[i] = 1
        dfs(k+1, lst + [n_lst[i]])
        used[i] = 0


N, M = map(int, input().split())
n_lst = sorted(list(map(int, input().split())))
used = [0] * 10000
dfs(0, [])