import sys
sys.setrecursionlimit(100000)

T = int(input())

def worm(r, c):
    if arr[r][c] == 2:
        return
    arr[r][c] = 2
    global cnt

    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nr, nc = r+dr, c+dc
        if -1 < nr < N and -1 < nc < M and arr[nr][nc] == 1:
            worm(nr, nc)
    else:
        return

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    lst = [(0, 0)] * K

    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
        lst[i] = (y, x)

    cnt = 0
    i = 0
    for x, y in lst:
        if arr[x][y] == 1:
            worm(x, y)
            cnt += 1
            
    print(cnt)