dir_dict = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
dir_lst = [0, 3, 2, 1, 0, 3, 2, 1]

N, M = map(int, input().split())
row, col, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

def robot(r, c):
    global cnt, h
    while 1:
        if not arr[r][c]:
            arr[r][c] = 2   # 현재 칸 청소
            cnt += 1        # 청소 횟수

        x = dir_lst.index(h)
        ACW = dir_lst[x+1:x+5]

        for i in ACW:   # 반시계방향으로 찾기
            dr, dc = dir_dict[i]
            nr, nc = dr + r, dc + c
            if not arr[nr][nc]:
                h = i
                break
        else:
            dr, dc = dir_dict[h]
            nr, nc = r-dr, c-dc
            if arr[nr][nc] == 1:
                return
        r, c = nr, nc

robot(row, col)
print(cnt)