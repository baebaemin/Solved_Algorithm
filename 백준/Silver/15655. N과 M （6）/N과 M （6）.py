def dfs(k, s, lst):
    if k == M:
        print(*lst)
        return
    for j in range(s, N):
        dfs(k+1, j+1, lst+[n_lst[j]])  # 다음 시작지점을 하나 올림 (앞에서 쓰였으니)


N, M = map(int, input().split())
n_lst = sorted(list(map(int, input().split())))
dfs(0, 0, [])