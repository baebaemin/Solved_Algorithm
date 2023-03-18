from collections import deque
import sys

R, C = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

v = [[0] * C for _ in range(R)]
Q = deque([(0, 0)])
v[0][0] = 1

while Q:                                        # 공기랑 통하는 바깥영역
    r, c = Q.popleft()
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and not v[nr][nc] and not arr[nr][nc]:
            v[nr][nc] = 1
            Q.append((nr, nc))

melted = [[0] * C for _ in range(R)]
cnt = 0
while 1:
    cnt += 1
    melt = []                                   # 다 녹았는지 체크
    for r in range(R):
        for c in range(C):
            if arr[r][c]:                       # 녹을 수 있는 곳 체크
                meltable = sum(v[nr][nc] for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)])
                if meltable >= 2:
                    melt.append((r, c))
    if not melt:
        print(cnt-1)
        break
    for r, c in melt:
        arr[r][c] = 0
        melted[r][c] = 1

    v = [[0] * C for _ in range(R)]             # 바깥영역 갱신
    q = deque([(0, 0)])
    v[0][0] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not v[nr][nc] and not arr[nr][nc]:
                v[nr][nc] = 1
                q.append((nr, nc))