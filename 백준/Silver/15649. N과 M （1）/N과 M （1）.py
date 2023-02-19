N, M = map(int, input().split())
used = [0] * N
order = [0] * M

def perm(k, n):
    if k == n:
        print(*order)
    else:
        for i in range(N):
            if used[i]:
                continue
            else:
                used[i] = 1
                order[k] = i+1
                perm(k+1, M)
                used[i] = 0

perm(0, M)