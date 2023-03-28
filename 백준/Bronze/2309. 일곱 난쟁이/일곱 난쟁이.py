def nCr(n, r, s):
    if r == 0:
        if sum(comb) == 100:
            for gnome in comb:
                print(gnome)
            exit()
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)

N = 9
A = [int(input()) for _ in range(N)]
A.sort(reverse=True)
comb = [0] * 7
nCr(9, 7, 0)