def BFS(r, c):
    Q = [(r, c)]
    t_arr[r][c] = 1

    while Q:
        r, c = Q.pop(0)
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and not t_arr[nr][nc]:
                Q.append((nr, nc))
                t_arr[nr][nc] = 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
height = 0
maxV = 0

while height <= 100:
    t_arr = [[0] * N for _ in range(N)]
    height += 1
    cnt = area = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= height:
                t_arr[i][j] = 1
                cnt += 1
    if cnt == N*N:
        if height == 1:
            maxV = 1
        break

    for i in range(N):
        for j in range(N):
            if t_arr[i][j] == 0:
                BFS(i, j)
                area += 1
    if maxV < area:
        maxV = area
print(maxV)