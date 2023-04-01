def BFS(v, cnt):
    global a
    if visited[v]: return
    a = cnt
    visited[v] = a

    for w in G[v]:
        BFS(w, a + 1)
    return

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    visited = [0] * (N+1)
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        t, u = map(int, input().split())
        G[t].append(u)
        G[u].append(t)

    cnt = 0
    BFS(1, 1)
    print(a-1)