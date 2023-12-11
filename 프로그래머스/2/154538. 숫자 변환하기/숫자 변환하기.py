from collections import deque
    
def bfs(x, y, n, v):
    q = deque()
    q.append(x)
    v[x] = 1 # 필요없...나
    # 가지치기 - 방문한 곳에 새로 넣을 값이 이전 값보다 크면 return
    
    while q: 
        c = q.popleft()
        if c == y:
            # print('here', v, c)
            break
        
        # 세 가지 연산
        for i in range(3):
            if i == 0:    temp_c = c*3
            elif i == 1: temp_c = c*2
            else:        temp_c = c+n
            
            if temp_c <= y and not v[temp_c]:
                v[temp_c] = v[c] + 1
                q.append(temp_c)
                
    return v[y]  -1
    
def solution(x, y, n): 
    v = [0 for i in range(y+1)]
    ans = bfs(x, y, n, v)
    # print(v, 'v', ans)
    
    return ans