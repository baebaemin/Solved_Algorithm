import sys; sys.setrecursionlimit(100000)

def AirCleaner(t, arr):
    if t == T: return print(sum(map(sum, arr)) + 2)
    t_arr = [[0] * C for _ in range(R)]
    
    ar = 0
    for r in range(R):
        for c in range(C):
            if arr[r][c]:
                mid = arr[r][c]
                if mid == -1:
                    t_arr[r][c] = -1
                    ar = r
                else:   # 공기청정기가 아닌 곳
                    sm = 0
                    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                            t_arr[nr][nc] += mid // 5
                            sm += mid // 5
                    t_arr[r][c] += mid-sm

    # 먼지 청소..하드..코딩...
    for ur in range(ar-3, -1, -1):  t_arr[ur+1][0] = t_arr[ur][0]
    for uc in range(1, C):          t_arr[0][uc-1] = t_arr[0][uc]
    for ur in range(1, ar):         t_arr[ur-1][C-1] = t_arr[ur][C-1]
    for uc in range(C-2, -1, -1):   t_arr[ar-1][uc+1] = t_arr[ar-1][uc]
    for lr in range(ar+2, R):       t_arr[lr-1][0] = t_arr[lr][0]
    for lc in range(1, C):          t_arr[R-1][lc-1] = t_arr[R-1][lc]
    for lr in range(R-2, ar-1, -1): t_arr[lr+1][C-1] = t_arr[lr][C-1]
    for lc in range(C-2, 0, -1):    t_arr[ar][lc+1] = t_arr[ar][lc]

    t_arr[ar - 1][1] = t_arr[ar][1] = 0
    AirCleaner(t + 1, t_arr)

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
AirCleaner(0, arr)