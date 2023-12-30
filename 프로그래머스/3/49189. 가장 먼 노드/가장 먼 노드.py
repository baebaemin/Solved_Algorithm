from collections import deque

def bfs(n, adj):
    visited = [0] * (n+1)
    q = deque([1])
    visited[1] = 1
    
    while q:
        now = q.popleft()
        for next in adj[now]:
            if not visited[next]:
                visited[next] = visited[now] + 1
                q.append(next)
                
    return visited.count(max(visited))

def solution(n, edge):
    adj = [[] for _ in range(n+1)]
    
    # 양방향
    for s, e in edge:
        adj[s].append(e)
        adj[e].append(s)
        
    return bfs(n, adj)