def seat(r, c):
    cnt = 0
    while 1:
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            while 1:
                nr, nc = r+dr, c+dc
                if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == 0:
                    cnt += 1
                    if cnt == P:
                        print(nr+1, nc+1)
                        return
                    arr[nr][nc] = cnt
                    r, c = nr, nc
                else:
                    break

R, C = map(int, input().split())
P = int(input())
arr = [[0] * C for _ in range(R)]
if P > C*R: print(0)
else: seat(0, -1)