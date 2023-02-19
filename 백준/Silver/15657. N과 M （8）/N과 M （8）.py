def dfs(k, s, lst):
    if k == M:
        if len(lst) == M:
            print(*lst)
        return
    for i in range(s, N):
        dfs(k+1, i, lst+[n_lst[i]])
        # k번째 수가 k-1과 같은 부분에서 시작하려면 s를 i로 설정
        # i에 +1해서 s로 넘긴다면, k번째 수는 k-1보다 클 수밖에 없음

N, M = map(int, input().split())
n_lst = sorted(list(map(int, input().split())))
dfs(0, 0, [])