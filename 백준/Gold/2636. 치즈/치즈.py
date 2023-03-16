from collections import deque
from copy import deepcopy

def melting_cheese(nQ, cnt):
    Q = deepcopy(nQ)
    nQ = deque()
    last_cheese = len(Q)
    found_once = 0
    while Q:
        r, c = Q.popleft()
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if arr[nr][nc] == 1:
                    nQ.append((nr, nc))
                    arr[nr][nc] = 2
                    found_once = 1
                elif arr[nr][nc] == 0:
                    Q.append((nr, nc))
                    arr[nr][nc] = 2

    if not found_once:  # 남은 치즈가 없다면
        print(cnt)
        print(last_cheese)
        return
    else:
        melting_cheese(nQ, cnt+1)


R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
Q = deque()
nQ = deque()
Q.append((0, 0))
nQ.append((0, 0))
arr[0][0] = 2
while Q:
    r, c = Q.popleft()
    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nr, nc = r+dr, c+dc
        if 0 <= nr < R and 0 <= nc < C and not arr[nr][nc]:
            Q.append((nr, nc))
            nQ.append((nr, nc))
            arr[nr][nc] = 2

melting_cheese(nQ, 0)