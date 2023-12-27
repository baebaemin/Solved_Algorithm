from collections import deque
N, M = map(int, input().split())
campus = [input() for _ in range(N)]
v = [[0] * M for _ in range(N)]

def finding_friends(sr, sc):
    v[sr][sc] = 1
    q=deque()
    q.append((sr, sc))
    cnt = 0
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = dr+r, dc+c
            if 0 <= nr < N and 0 <= nc < M and not v[nr][nc] and campus[nr][nc] != 'X':
                if campus[nr][nc] == 'P':
                    cnt += 1
                v[nr][nc] = 1
                q.append((nr, nc))
    if cnt:
        return cnt
    return 'TT'

# 도연이 위치 찾기
r, c = 0, 0
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            r, c = i, j
            break
    else: continue
    break
print(finding_friends(r, c))