import sys

def DFS(n):
    if v[n]:
        return
    v[n] = 1
    for m in adjL[n]:
        DFS(m)

input = sys.stdin.readline
N, M = map(int, input().split())  # 정점의 개수 / 간선의 개수
adjL = [[] for _ in range(N+1)]
v = [0] * (N + 1)

for _ in range(M):
    t, u = map(int, input().split())
    adjL[t].append(u)
    adjL[u].append(t)

cnt = 0
for i in range(1, N+1):
    if not v[i]:
        DFS(i)
        cnt += 1

print(cnt)