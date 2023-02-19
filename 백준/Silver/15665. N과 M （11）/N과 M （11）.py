def dfs(k, st):
    if k == M:
        try:
            check[st] += 1
        except:
            print(st)
            check[st] = 1
        return
    for i in range(N):
        dfs(k+1, st+n_lst[i]+' ')


N, M = map(int, input().split())
n_lst = [str(i) for i in sorted(list(map(int, input().split())))]
used = [0] * N
check = {}
dfs(0, '')