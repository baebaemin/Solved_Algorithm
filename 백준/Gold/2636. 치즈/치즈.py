from copy import deepcopy

def melting_cheese(nQ, cnt):
    Q = deepcopy(nQ)
    nQ = []
    last_cheese = len(Q)
    melted_yet = 0
    
    while Q:
        r, c = Q.pop(0)
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if arr[nr][nc] == 1:
                    nQ.append((nr, nc))
                    arr[nr][nc] = 2
                    melted_yet = 1
                elif arr[nr][nc] == 0:
                    Q.append((nr, nc))
                    arr[nr][nc] = 2
    if not melted_yet:
        print(f'{cnt}\n{last_cheese}')
        return
    else: melting_cheese(nQ, cnt+1)

R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
Q, nQ = [(0, 0)], [(0, 0)]
arr[0][0] = 2

while Q:
    r, c = Q.pop(0)
    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nr, nc = r+dr, c+dc
        if 0 <= nr < R and 0 <= nc < C and not arr[nr][nc]:
            Q.append((nr, nc))
            nQ.append((nr, nc))
            arr[nr][nc] = 2
            
melting_cheese(nQ, 0)