import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    min_heap = []
    max_heap = []
    heapDict = {}

    for _ in range(int(input())):
        cmd, val = input().split()
        val = int(val)

        if cmd == "I":
            heapq.heappush(min_heap, val)
            heapq.heappush(max_heap, -val)
            heapDict[val] = heapDict.get(val, 0) + 1
            
        elif cmd == "D":  # 삭제
            if val == 1:  # 최댓값 삭제
                while max_heap and heapDict[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    heapDict[-max_heap[0]] -= 1
                    heapq.heappop(max_heap)
            else:         # 최솟값 삭제
                while min_heap and heapDict[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    heapDict[min_heap[0]] -= 1
                    heapq.heappop(min_heap)

    while min_heap and heapDict[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and heapDict[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0], min_heap[0])