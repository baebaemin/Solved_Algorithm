from collections import deque

def bfs(n, computers, com, v):
    q = deque()
    q.append(com)
    
    while q:
        com = q.pop()
        v[com] = True
        for i in range(n): # 대수만큼
            # 만약 0~2번 컴퓨터중에 아직 연결 안된 컴퓨터이고
            # computers 연결 맵엔 연결되어있다고 하고
            # 자기 자신이 아닌 컴퓨터면
            if v[i] == False and computers[i][com] == 1 and i != com:
                q.append(i)

def solution(n, computers):
    answer = 0
    
    v = [False for _ in range(n)]     # 컴퓨터 대수만
    
    for com in range(n): #  com = 컴퓨터 번호
        if not v[com]:  # 연결되지 않았다면
            bfs(n, computers, com, v)
            answer += 1 # 연결 싹 훑고 온거라 +1
            
    return answer