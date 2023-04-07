import sys;
from heapq import heappush, heappop

N = int(input())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x: heappush(heap, -x)
    else:
        try: print(-heappop(heap))
        except: print(0)