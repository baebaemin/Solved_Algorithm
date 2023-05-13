from collections import deque
N, K = map(int, input().split())
Q = [i for i in range(1, N+1)]
Q = deque(Q)
K -= 1
idx = 0
print('<', end='')
while len(Q) != 1:
    idx += K
    if idx >= len(Q):
        idx = idx % len(Q)
    print(Q[idx], end=', ')
    del Q[idx]
print(f'{Q[0]}>')