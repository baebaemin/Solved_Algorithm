def bfs(si, sj):
    q = []
    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] and not v[ni][nj]:
                v[ni][nj] = 1
                cnt += 1
                q.append((ni, nj))
    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0] * N for _ in range(N)]
ans = []

for i in range(N):
    for j in range(N):
        if arr[i][j] and not v[i][j]:
            ans.append(bfs(i, j))
            
ans.sort()
print(len(ans), *ans, sep='\n')