import sys; from heapq import heappush, heappop

HQ = []
for _ in range(int(input())):
    x = int(sys.stdin.readline())
    if not x:       # x는 0
        try:
            a, b = heappop(HQ)
            print(a*b)
        except: print(0)
    elif x > 0:     # x는 양수
        heappush(HQ, (x, 1))
    else:           # x는 음수
        heappush(HQ, (abs(x), -1))