N, L = map(int, input().split())
# Lx = N - (L*L + L) // 2
for l in range(L, 101):
    x = N - (l*l + l) // 2
    if x % l == 0:
        x //= l
        if x >= -1:
            rlt = ''
            for n in range(1, l+1):
                rlt += f'{x + n} '
            print(rlt)
            break
else: # 100까지 구했는데 없으면
    print(-1)