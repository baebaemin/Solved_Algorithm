from collections import deque

import sys
input = sys.stdin.readline

def ripe():
    maxV = -1
    while Q:
        z, r, c = Q.popleft()
        for dz, dr, dc in ((-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (1, 0, 0)):
            nz, nr, nc = z+dz, r+dr, c+dc
            if 0 <= nz < H and 0 <= nr < R and 0 <= nc < C and arr[nz][nr][nc] == 0:
                arr[nz][nr][nc] = arr[z][r][c] + 1
                Q.append((nz, nr, nc))
                if maxV < arr[z][r][c]:
                    maxV = arr[z][r][c]
    return maxV

C, R, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(R)] for _ in range(H)]
Q = deque()
UQ = deque()

rotten = 0  # 0 발견 못했을시 1
for h in range(H):
    for i in range(R):
        for j in range(C):
            if arr[h][i][j] == 1:
                Q.append((h, i, j))
            elif arr[h][i][j] == -1:
                UQ.append((h, i, j))
            elif arr[h][i][j] == 0:  # 한 번이라도 안 익은 토마토가 있었다면
                rotten = 1
ans = ripe()
if rotten:  # 전부 이미 익은 상태가 아니었다면
    if UQ:  # 빈 상자가 있었고 안 익은게 있었다면
        for h, i, j in UQ:
            for dz, dr, dc in ((-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (1, 0, 0)):
                    nz, nr, nc = h + dz, i + dr, j + dc
                    if 0 <= nz < H and 0 <= nr < R and 0 <= nc < C and arr[nz][nr][nc] == 0:
                        ans = -1
                        break
    print(ans)
else:
    print(0)  # 전부 익었다면
