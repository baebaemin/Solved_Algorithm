from collections import deque

def solution(cards):
    N = len(cards)
    visited = [True] + [False for _ in range(N)]
    cnt_lst = []
    
    for i in cards:
        group_cnt = 0
        if not visited[i]:
            group_cnt += 1
            visited[i] = True
            q = deque()
            q.append(i)
            while q:
                n = q.popleft()
                next_idx = cards[n-1]
                if not visited[next_idx]:
                    q.append(next_idx)
                    visited[next_idx] = True
                    group_cnt += 1
            cnt_lst.append(group_cnt)
    cnt_lst.sort(reverse=True)
    
    if len(cnt_lst) >= 2:
        ans = cnt_lst[0] * cnt_lst[1]
    else: 
        ans = 0
        
    return ans