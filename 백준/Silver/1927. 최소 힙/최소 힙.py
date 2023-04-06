import sys;
from heapq import heappush, heappop

N = int(input())
HQ = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x: heappush(HQ, x)
    else:
        try: print(heappop(HQ))
        except: print(0)
