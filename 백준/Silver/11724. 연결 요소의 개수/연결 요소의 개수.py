import sys
from collections import deque

def BFS(n, cnt):
    if v[n]:
        return
    Q = deque([n])
    v[n] = cnt
    while Q:
        n = Q.popleft()
        for m in adjL[n]:
            if not v[m]:
                v[m] = cnt
                Q.append(m)

    for i in range(1, N+1):
        if not v[i]:
            BFS(i, cnt+1)
            break
    else:
        print(cnt)

input = sys.stdin.readline
N, M = map(int, input().split())     # 정점의 개수 간선의 개수
adjL = [[] for _ in range(N+1)]
v = [0] * (N + 1)

for _ in range(M):
    t, u = map(int, input().split())
    adjL[t].append(u)
    adjL[u].append(t)

if M == 0:
    print(N)
    exit()

BFS(t, 1)