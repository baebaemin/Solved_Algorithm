def BFS(r, c, COLOR):
    Q = [(r, c)]
    arr[r][c] = color_num[COLOR]
    while Q:
        r, c = Q.pop(0)
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == COLOR:
                Q.append((nr, nc))
                arr[nr][nc] = color_num[COLOR]

N = int(input())
arr = [[st for st in input()] for _ in range(N)]
color_num = {'B': 1, 'R': 0, 'G': 0, 0: 1}
lst = []

for color in ('B', 'R', 'G', 0):
    area = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == color:
                BFS(i, j, color)
                area += 1
    lst.append(area)

print(lst[0] + lst[1] + lst[2], lst[0] + lst[3])