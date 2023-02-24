from collections import deque

def BFS():
    cnt = -1
    while Q:
        r, c = Q.popleft()
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                Q.append((nr, nc))
                if arr[r][c] > cnt:
                    cnt = arr[r][c]
    return cnt

M, N = map(int, input().split())  # N이 r, M이 c
arr = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
UQ = deque()  # Unripe

rotten = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            Q.append((i, j))
        elif arr[i][j] == -1:  # 토마토가 없는 칸이 있다면
            UQ.append((i, j))
        elif arr[i][j] == 0:  # 안 익은 토마토가 하나라도 있다면 ( 그럼 답은 0은 아님 )
            rotten = 1

ans = BFS()
if rotten:
    if UQ:  # 빈 칸이 있었다면
        for i, j in UQ:
            for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):  # 주변에 안 익은 토마토가 있는지 확인
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                    ans = -1  # 안 익은 토마토가 있으면 결과는 -1
                    break
    print(ans)
else:
    print(0)