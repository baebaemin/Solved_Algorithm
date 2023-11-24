from collections import deque

def finding(goal, maps, si, sj):
    H = len(maps)
    W = len(maps[0])
    v_map = [[0] * W for _ in range(H)]
    q = deque([[si, sj]])
    v_map[si][sj] = 1
    
    while q:
        ci, cj = q.popleft()
        if maps[ci][cj] == goal:
            q = deque([])
            return (v_map[ci][cj] - 1, ci, cj)
        
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<H and 0<=nj<W and maps[ni][nj] != 'X' and not v_map[ni][nj]:
                v_map[ni][nj] = v_map[ci][cj] + 1
                q.append([ni, nj])
    return None

def solution(maps):
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                si, sj = i, j
    cnt = 0
    lever_rlt = finding("L", maps, si, sj)
    if lever_rlt:
        cnt, si, sj = lever_rlt
    else:
        return -1
    
    end_rlt = finding("E", maps, si, sj)
    if end_rlt:
        ans = cnt + end_rlt[0]
        return ans
    else:
        return -1