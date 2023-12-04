from collections import deque

def bfs(i, j, H, W, land, visited, cnt_dict, idx):
    q = deque()
    q.append((i, j))
    visited[i][j] = idx
    cnt = 1
    
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = di+ci, dj+cj
            if 0 <= ni < H and 0 <= nj < W and land[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = idx
                cnt += 1
                q.append((ni, nj))
    cnt_dict[idx] = cnt
    idx += 1
            
def solution(land):
    idx = 1
    H = len(land)    # 세로
    W = len(land[0]) # 가로
    visited = [[0] * W for _ in range(H)]
    cnt_dict = {}
    
    for i in range(H):
        for j in range(W): 
            if land[i][j] and not visited[i][j]:
                bfs(i, j, H, W, land, visited, cnt_dict, idx)
                idx += 1
                
    visited = list(map(list, zip(*visited)))  # 전치행렬
    lst = [[] for _ in range(W)]
    for i, l in enumerate(visited):
        lst[i] = set(l)
    unique_lst = list(map(set, set(map(frozenset, lst))))
    
    maxV = 0
    for unique_set in unique_lst:
        cnt = 0
        for u in unique_set:
            if u:
                cnt += cnt_dict[u]
        maxV = max(cnt, maxV)
    return maxV