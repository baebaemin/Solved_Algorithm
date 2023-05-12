import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
Q = [i for i in range(1, N+1)]
Q = deque(Q)

while len(Q) > 1:
    Q.popleft()
    Q.append(Q.popleft())

print(Q[0])