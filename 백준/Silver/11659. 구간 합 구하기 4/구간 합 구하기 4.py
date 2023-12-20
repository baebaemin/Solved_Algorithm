import sys
N, M = map(int, input().split())
lst = list(map(int, sys.stdin.readline().split())) + [0]

for i in range(N):
    lst[i] += lst[i-1]

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(lst[e-1] - lst[s-2])