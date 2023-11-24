def bfs(adj, n):
    q = []  # 넣을 곳
    v = [0] * (n+1)
    
    q.append(1) # 시작점부터 넣기
    v[1] = 1
    
    while q:
        c = q.pop(0)    # q에서 꺼낸 것. 맨 처음엔 1
        for a in adj[c]:
            if not v[a]: # 방문 안 했을 때
                q.append(a)     # 다음 방문 시작지점에 넣음
                v[a] = v[c] + 1 # 이동한 거리만큼 플러스
            # 방문 했을 땐 패스
            
    rlt = v.count(max(v))
    return rlt

def solution(n, edge):
    # 시작할 노드는 1 -> 0이라고 할까?
    s = 0
    # 간선 개수만큼 주기
    adj = [[] for _ in range(n+1)]
    for e in edge:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    return bfs(adj, n)