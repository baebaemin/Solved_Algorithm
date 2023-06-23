K, N = map(int, input().split())
wires = [int(input()) for _ in range(K)]
sp = 1
ep = max(wires)

while sp <= ep:
    m = (sp + ep) // 2
    cnt = 0
    for wire in wires:
        cnt += wire // m
    if cnt >= N:
        ans = m
        sp = m + 1
    else:
        ep = m - 1
print(ans)