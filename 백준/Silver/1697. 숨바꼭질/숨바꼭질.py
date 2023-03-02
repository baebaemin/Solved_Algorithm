from collections import deque

N, K = map(int, input().split())
if N > K:
    print(N-K)
else:
    v = [0] * 100001
    Q = deque()
    Q.append((N, 1))
    while 1:
        n, c = Q.popleft()
        if n == K:
            break
        v[n] = 1
        if n*2 <= 100000 and not v[n*2]:
            Q.append((n*2, c+1))
        if n+1 <= 100000 and not v[n+1]:
            Q.append((n+1, c+1))
        if n-1 > 0 and not v[n-1]:
            Q.append((n-1, c+1))

    print(c-1)