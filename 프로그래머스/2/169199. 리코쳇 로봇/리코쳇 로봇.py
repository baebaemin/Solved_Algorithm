from collections import deque
dir_lst = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(r, c, board, H, W):
    v = [[0 for _ in range(W)] for _ in range(H)]
    v[r][c] = 1
    q = deque()
    q.append((r, c, 0))
    
    while q:
        r, c, cnt = q.popleft()
        
        for dr, dc in dir_lst: # 4방향 탐색
            nr, nc = r, c
            
            while True:
                nr += dr
                nc += dc
                if not (0 <= nr < H and 0 <= nc < W) or board[nr][nc] == 'D':
                    nr -= dr
                    nc -= dc
                    if not v[nr][nc]:
                        v[nr][nc] = 1
                        q.append((nr, nc, cnt+1))
                    break
                    
                if board[r][c] == 'G':
                    return cnt
    return -1
        

def solution(board):
    H = len(board)
    W = len(board[0])
    
    # 시작지점 찾기
    r, c = 0, 0
    for i in range(H):
        for j in range(W):
            if board[i][j] == 'R':
                r, c = i, j
                break
        else: continue
        break
    
    return bfs(r, c, board, H, W)