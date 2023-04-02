def perm(n, sm):
    global ans
    if n == N:
        if B <= sm < ans:
            ans = sm
        return
    if sm >= B:      # 도달했을 때
        if sm < ans:
            ans = sm
        return

    perm(n + 1, sm + lst[n])
    perm(n + 1, sm)

for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0xfffffff
    perm(0, 0)
    print(f'#{tc} {ans-B}')
