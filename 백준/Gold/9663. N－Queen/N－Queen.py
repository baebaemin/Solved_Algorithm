def nQueen(k):
    global cnt
    if k == N:
        cnt += 1; return

    for col in range(N):
        d1, d2 = k+col, k-col+N  # dir2의 음수를 양수
        if used[col] or diag1[d1] or diag2[d2]: continue
        used[col] = diag1[d1] = diag2[d2] = 1
        nQueen(k+1)
        used[col] = diag1[d1] = diag2[d2] = 0

N = int(input())
# 대강 N*2보다 작은 수의 대각선
diag1 = [0] * (N << 1)  # (r + c)
diag2 = [0] * (N << 1)  # (r - c)
used = [0] * N      # 열은 중복되지 않으므로

cnt = 0; nQueen(0)
print(cnt)