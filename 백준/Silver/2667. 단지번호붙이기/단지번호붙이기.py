def BFS(r, c):
    Q = [(r, c)]
    arr[r][c] = 0
    cnt = 1

    while Q:
        r, c = Q.pop(0)
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
                arr[nr][nc] = 0
                cnt += 1
                Q.append((nr, nc))
    return cnt


N = int(input())
arr = [[int(i) for i in input()] for _ in range(N)]

rlt = 0
lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            lst.append(BFS(i, j))
            rlt += 1
print(rlt)
for i in range(len(lst)):
    print(sorted(lst)[i])