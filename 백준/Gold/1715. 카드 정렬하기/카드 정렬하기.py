from heapq import heapify, heappush, heappop
import sys

N = int(sys.stdin.readline())
lst = ([int(sys.stdin.readline()) for _ in range(N)])
heapify(lst)

ans = 0
while len(lst) > 1:
    c1 = heappop(lst)
    c2 = heappop(lst)
    sm = c1 + c2
    ans += sm
    heappush(lst, sm)

print(ans)