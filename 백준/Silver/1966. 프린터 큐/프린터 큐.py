from collections import deque
for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    Q = [(arr[i], i) for i in range(N)]     # (중요도, idx)
    Q = deque(Q)
    cnt = 0

    while True:
        doc = Q.popleft()
        priorDoc = doc[0]
        if any(priorDoc < q[0] for q in Q): # Q elem 중 현재 문서보다 중요도가 높은 문서가 있는지
            Q.append(doc)
        else:
            cnt += 1
            if doc[1] == M:
                print(cnt)
                break