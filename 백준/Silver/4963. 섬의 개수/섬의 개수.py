while True:
    W, H = map(int, input().split())  # 가로, 세로
    if (W, H) == (0, 0):
        break
    arr = [list(map(int, input().split())) for _ in range(H)]
    v = [[0] * W for _ in range(H)]
    Q = []
    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] and not v[i][j]:
                Q.append((i, j))
                cnt += 1
                v[i][j] = cnt
                while Q:
                    r, c = Q.pop(0)
                    for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
                        nr, nc = dr+r, dc+c
                        if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] and not v[nr][nc]:
                            v[nr][nc] = cnt
                            Q.append((nr, nc))
    print(cnt)