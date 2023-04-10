def pipe(r, c, type):
    global cnt
    if (r, c) == (N-1, N-1):
        cnt += 1
        return

    # 대각 - 오른이어도, 아래여도 다 간다
    if r+1 < N and c+1 < N and not arr[r+1][c] and not arr[r][c+1] and not arr[r+1][c+1]:
        pipe(r+1, c+1, 0)

    # 오른 - 아래일때는 안 간다
    if type != 2 and c+1 < N and not arr[r][c+1]:
        pipe(r, c+1, 1)

    # 아래 - 오른일때는 안 간다
    if type != 1 and r+1 < N and not arr[r+1][c]:
        pipe(r+1, c, 2)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
pipe(0, 1, 1)  # 파이프의 끝점r, c, 유형
print(cnt)