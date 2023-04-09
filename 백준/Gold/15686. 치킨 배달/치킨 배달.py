from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append([i, j])
        elif arr[i][j] == 2:
            chickens.append([i, j])

H = len(houses)
C = len(chickens)
table = [[0] * H for _ in range(C)]
for i in range(C):
    for j in range(H):
        c, h = chickens[i], houses[j]
        dist = abs(c[0]-h[0])+abs(c[1]-h[1])
        table[i][j] = dist

t_table = list(zip(*table))
minV = 0
for l in range(H):
    minV += min(t_table[l])
survived = list(combinations(range(C), M))

rlt = 0xffffff
for s_lst in survived:
    new_table = []
    for s in s_lst:  # s는 row인덱스
        new_table.append(table[s])

    sm = 0
    t_new_table = list(zip(*new_table))
    for t in range(H):
        sm += min(t_new_table[t])
    rlt = min(sm, rlt)
    if rlt == minV:
        break
print(rlt)