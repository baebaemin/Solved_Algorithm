def BFS(h, w):
    v = [[0] * W for _ in range(H)]
    v[h][w] = 1
    maxV = 0
    Q = [(h, w)]
    while Q:
        y, x = Q.pop(0)
        for dy, dx in ((0, -1), (1, 0), (0, 1), (-1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W and arr[ny][nx] == 'L' and not v[ny][nx]:
                v[ny][nx] = v[y][x] + 1
                if maxV < v[ny][nx]:
                    maxV = v[ny][nx]
                Q.append((ny, nx))
    return maxV

H, W = map(int, input().split())
arr = [[ch for ch in input()] for _ in range(H)]

rlt = 0
for r in range(H):
    for c in range(W):
        if arr[r][c] == 'L':
            rlt = max(rlt, BFS(r, c))
if not rlt:
    print(0)
else:
    print(rlt-1)