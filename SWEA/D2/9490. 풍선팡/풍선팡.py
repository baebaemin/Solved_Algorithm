T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    rlt = -1
    for r in range(N):  # 0~2
        for c in range(M):  # 0~4
            cnt = 0
            for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                for k in range(1, arr[r][c] + 1): # 가운데 꽃가루가 1이면 범위 = 1, 2이면 범위 = 1~2
                    nr, nc = r + dr*k, c + dc*k
                    if 0 <= nr < N and 0 <= nc < M:
                        cnt += arr[nr][nc]
            rlt = max(cnt + arr[r][c], rlt)
    print(f'#{tc} {rlt}')