from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
houses, chickens = [], []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append([i, j])
        elif arr[i][j] == 2:
            chickens.append([i, j])

H, C = len(houses), len(chickens)

table = [[0] * H for _ in range(C)]
for i in range(C):
    for j in range(H):
        c, h = chickens[i], houses[j]
        table[i][j] = abs(c[0]-h[0]) + abs(c[1]-h[1])

minV = sum(min(dist_lst)for dist_lst in zip(*table))
survived = list(combinations(range(C), M))

rlt = 0xffffff
for s_lst in survived:
    new_table = [table[s] for s in s_lst]   # s는 row 인덱스
    sm = sum(min(t_lst) for t_lst in zip(*new_table))
    rlt = min(sm, rlt)
    if rlt == minV:
        break
print(rlt)