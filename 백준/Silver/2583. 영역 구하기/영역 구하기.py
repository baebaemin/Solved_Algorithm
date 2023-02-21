def BFS(r, c):
    arr[r][c] = 1
    Q = [(r, c)]
    visited[r][c] = 1
    cnt = 0

    while Q:
        r, c = Q.pop(0)
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and not arr[nr][nc] and not visited[nr][nc]:  # arr[r][c] == 0 할 필요 X?
                Q.append((nr, nc))
                arr[nr][nc] = 1
                visited[nr][nc] = 1
                cnt += 1
    return cnt


M, N, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for _ in range(K):
    sr, sc, er, ec = map(int, input().split())
    for i in range(sr, er):
        for j in range(sc, ec):
            arr[i][j] = 1

area = 0
lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            area += 1
            lst.append(BFS(i, j)+1)

print(area)
print(*sorted(lst))
