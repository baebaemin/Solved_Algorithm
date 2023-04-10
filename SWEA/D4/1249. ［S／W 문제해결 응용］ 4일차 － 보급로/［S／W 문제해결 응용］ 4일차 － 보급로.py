from collections import deque
from heapq import heappop, heappush

def BFS(r, c, sm):
    heapq = []
    heappush(heapq, (sm, r, c))
    # Q = deque([(r, c)])
    while heapq:
        sm, r, c = heappop(heapq)
        for dr, dc in ((1 ,0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N:
                if t_arr[r][c] + arr[nr][nc] < t_arr[nr][nc]:
                    t_arr[nr][nc] = arr[nr][nc] + t_arr[r][c]
                    heappush(heapq, (t_arr[nr][nc], nr, nc))

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    t_arr = [[0xffffff] * N for _ in range(N)]
    t_arr[0][0] = arr[0][0]  # 출발은 같게
    sm = 0
    BFS(0, 0, 0)
    print(f'#{tc} {t_arr[N - 1][N - 1]}')