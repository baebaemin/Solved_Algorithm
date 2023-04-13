N, L = map(int, input().split())

for l in range(L, 101):
    x = N - (l*l + l) // 2      # Lx = N - (L*L + L) // L
    if x % l == 0 and x//l >= -1:
        print(' '.join(str(x//l + n)for n in range(1, l+1)))
        break
else: print(-1)                 # 100까지 구했는데 없으면