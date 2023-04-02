def perm(n, sm):
    global cnt
    if sm >= K:
        if sm == K: cnt += 1
        return
    if n == N: return

    perm(n+1, sm + lst[n])
    perm(n+1, sm)

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    perm(0, 0)
    print(f'#{tc} {cnt}')