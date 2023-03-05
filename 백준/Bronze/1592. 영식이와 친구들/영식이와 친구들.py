N, M, L = map(int, input().split())
lst = [1] + [0] * (N-1)
i = cnt = 0

while lst[i] != M:
    if lst[i] % 2:
        i = (i+L) % N
    else:
        i = (i-L) % N
    lst[i] += 1
    cnt += 1
    
print(cnt)