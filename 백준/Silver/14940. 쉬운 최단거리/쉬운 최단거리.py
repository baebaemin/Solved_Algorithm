from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[False for _ in range(M)] for _ in range(N)]   # 방문 배열
d = [[-1 for _ in range(M)] for _ in range(N)]      # 거리 배열

def bfs(r, c):
    q = deque([(r, c)])
    v[r][c] = True
    d[r][c] = 0

    while q:
        r, c = q.popleft()
        for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nr, nc = r+dr, c+dc
            # 범위 확인 및 방문하지 않은 갈 수 있는 곳인지 확인
            if 0 <= nr < N and 0 <= nc < M and not v[nr][nc] and arr[nr][nc] == 1:
                v[nr][nc] = True
                d[nr][nc] = d[r][c] + 1
                q.append((nr, nc))

r, c = 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            r, c = i, j
            break
    else: continue  # 끝까지 for문을 반복하지 않기 위함
    break

bfs(r, c)
# 원래 갈 수 없는 땅은 0으로 설정
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            d[i][j] = 0

for n in range(N):
    print(*d[n])