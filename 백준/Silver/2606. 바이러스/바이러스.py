def virus(n):
    global cnt
    if visited[n]:
        return
    visited[n] = 1
    cnt += 1
    for w in G[n]:
        virus(w)

N = int(input())
C = int(input())  # Connected
G = [[] for _ in range(N+1)]  # Graph
visited = [0] * (N+1)
cnt = 0

for i in range(C):
    t, u = map(int, input().split())
    G[t].append(u)
    G[u].append(t)

virus(1)
print(cnt-1)