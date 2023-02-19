def dfs(k, lst):
    if k == M:
        try:
            ans_dict[tuple(lst)] += 1
        except:
            print(*lst)
            ans_dict[tuple(lst)] = 1
        return
    for i in range(N):
        if used[i]:
            continue
        used[i] = 1
        dfs(k+1, lst+[n_lst[i]])
        used[i] = 0

N, M = map(int, input().split())
n_lst = [str(i) for i in sorted(list(map(int, input().split())))]
used = [0] * N
ans_dict = {}
dfs(0, [])