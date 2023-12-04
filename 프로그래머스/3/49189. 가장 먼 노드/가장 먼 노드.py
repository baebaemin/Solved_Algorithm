from collections import deque

def bfs(n, adj):
    v = [0] * (n+1)
    q = deque([1])
    v[1] = 1
    
    while q:
        now = q.popleft()
        for next in adj[now]:
            if not v[next]:
                v[next] = v[now] + 1
                q.append(next)
                
    return v.count(max(v))

def solution(n, edge):
    adj = [[] for _ in range(n+1)]
    
    # 양방향
    for s, e in edge:
        adj[s].append(e)
        adj[e].append(s)
        
    return bfs(n, adj)