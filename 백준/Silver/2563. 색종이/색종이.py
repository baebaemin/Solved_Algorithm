def mapping(lst, min, idx):
    for j in range(N):
        new[j][idx] = lst[j] - min

N = int(input())
left = [0] * N
up = [0] * N
new = [[0, 0] for _ in range(N)]

for i in range(N):
    l, u = map(int, input().split())
    left[i], up[i] = l, u

L, U = min(left), min(up)
ML, MU = max(left) + 10, max(up) + 10
arr = [[0] * ML for _ in range(MU)]

mapping(left, L, 1)
mapping(up, U, 0)

ans = 0
for k in range(N):
    R, C = new[k][0], new[k][1]
    for r in range(R, R+10):
        for c in range(C, C+10):
            if not arr[r][c]:
                arr[r][c] = 1
                ans += 1
print(ans)