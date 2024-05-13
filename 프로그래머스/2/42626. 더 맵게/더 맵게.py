import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
    
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        newMixed = first + second * 2
        heapq.heappush(scoville, newMixed)

        cnt += 1
    return cnt