from collections import deque

def find_start_position(maps, start_char):
    for i, row in enumerate(maps):
        for j, char in enumerate(row):
            if char == start_char:
                return i, j
    return None

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
    si, sj = find_start_position(maps, "S")
    
    lever_rlt = finding("L", maps, si, sj)
    if not lever_rlt:
        return -1
    
    cnt, si, sj = lever_rlt
    
    end_rlt = finding("E", maps, si, sj)
    if not end_rlt:
        return -1
    
    return cnt + end_rlt[0]