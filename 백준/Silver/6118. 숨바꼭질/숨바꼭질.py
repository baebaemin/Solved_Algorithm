N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    v, u = map(int, input().split())
    G[v].append(u)
    G[u].append(v)

D = [0xffffff] * (N + 1)
D[1] = 0
Q = [1]

while Q:
    node = Q.pop(0)
    for nxt in G[node]:
        if D[nxt] > D[node] + 1:
            D[nxt] = D[node] + 1
            Q.append(nxt)
d = D[node]
print(D.index(d), d, D.count(d))