from collections import deque
  
def solution(land):
    H, W = len(land), len(land[0])  # 세로랑 가로
    visited = [[0] * W for _ in range(H)]
    oil_value = [0] * W
    
    for i in range(H):
        for j in range(W): 
            if land[i][j] and not visited[i][j]:
                land_width = set()
                q = deque()
                q.append([i, j])
                visited[i][j] = 1
                oil_cnt = 1
                land_width.add(j)
                while q:
                    ci, cj = q.popleft()
                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni, nj = di+ci, dj+cj
                        if 0 <= ni < H and 0 <= nj < W and land[ni][nj] == 1 and not visited[ni][nj]:
                            visited[ni][nj] = 1
                            q.append((ni, nj))
                            land_width.add(nj)
                            oil_cnt += 1
            
                for o in land_width:
                    oil_value[o] += oil_cnt
    return max(oil_value)