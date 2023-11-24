from collections import deque

def solution(queue1, queue2):
    max_operations = 2 * (len(queue1) + len(queue2))
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    cnt = 0
    
    while sum1 != sum2:
        if cnt > max_operations:
            return -1
        if sum1 > sum2:
            out = q1.popleft()
            q2.append(out)
            sum1 -= out
            sum2 += out
        else:
            out = q2.popleft()
            q1.append(out)
            sum1 += out
            sum2 -= out
        cnt += 1
    
    return cnt