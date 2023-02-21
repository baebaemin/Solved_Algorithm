def BFS(s, e):
    Q = [s]
    visited[s] = 1
    while Q:
        t = Q.pop(0)
        for w in G[t]:
            if w == e:
                return visited[t]
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[t] + 1
    return -1


N = int(input())  # 전체 사람의 수
P1, P2 = map(int, input().split())  # 촌수를 계산할 두 사람
M = int(input())  # 관계의 수
G = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    t, u = map(int, input().split())
    G[t].append(u)
    G[u].append(t)

print(BFS(P1, P2))