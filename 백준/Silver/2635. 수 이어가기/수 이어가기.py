def BF(A, B, list):
    global maxV
    if B < 0:
        if len(list) > maxV:
            maxV = len(list)
        Q.append(list[:-1])
        return
    BF(B, A-B, list + [A-B])

N = int(input())
maxV = -1
Q = []
for num in range(1, N + 1):
    BF(N, num, [N, num])

for i in range(N):
    if len(Q[i])+1 == maxV:
        print(maxV-1)
        print(*Q[i])
        break