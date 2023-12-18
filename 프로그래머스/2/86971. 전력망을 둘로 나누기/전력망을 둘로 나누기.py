# 끊는다는건 주어진 wires 배열에서 원소(배열) 하나를 없앤다는 것

def bfs(adj, n, start, v):
    v[start] = 1
    q = []
    q.append(start)
    
    while q:
        current = q.pop(0)
        for next in adj[current]:
            if not v[next]:
                v[next] = 1
                q.append(next)

def solution(n, wires):
    ans = 999999
    # idx 0부터 n-1까지
    for d_idx in range(n):
        adj = [[] for _ in range(n+1)]  # 간선 정보 담을 배열 리셋
        
        for i, w in enumerate(wires):
            if i == d_idx: 
                continue
            else:
                adj[w[0]].append(w[1])
                adj[w[1]].append(w[0]) 
                
        # 무조건 1번 노드부터 들어갈 수 있다는 보장은 없으니까
        start = 0
        for i in range(len(adj)):
            if adj[i]:
                start = adj[i][0]
                break
                
        v = [0 for _ in range(n+1)]
        bfs(adj, n, start, v)
        sm = sum(v)
        # 만약 rlt가 half 0.5 이상 or 이하 범위 안에 있으면 더 이상 비슷하게 쪼갤 수 없음 
        if n//2 - 0.5 <= sm <= n//2 + 0.5:
            ans = abs(n-sm-sm)
            break
        else:
            ans = min(ans, abs(n-sm-sm))
        
    return ans