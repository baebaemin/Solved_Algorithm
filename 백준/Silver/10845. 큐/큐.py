import sys
from collections import deque
deq = deque()
N = int(input())

for i in range(N):
    line = sys.stdin.readline().rstrip().split()
    if(line[0] == "push"):
        deq.append(int(line[1]))
    elif (line[0] == "pop"):
        if(len(deq) <= 0):
            print(-1)
        else:
            print(deq.popleft())
    elif (line[0] == "size"):
        print(len(deq))
    elif (line[0] == "empty"):
        if (len(deq) <= 0):
            print(1)
        else:
            print(0)
    elif (line[0] == "front"):
        if (len(deq) <= 0):
            print(-1)
        else:
            print(deq[0])
    elif (line[0] == "back"):
        if (len(deq) <= 0):
            print(-1)
        else:
            print(deq[len(deq) - 1])