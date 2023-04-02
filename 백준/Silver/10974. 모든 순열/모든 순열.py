def perm(n):
    if n == N:
        print(*order)
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            order[n] = lst[i]
            perm(n+1)
            visited[i] = 0


N = int(input())
lst = [n for n in range(1, N+1)]
order = [0] * N
visited = [0] * N
perm(0)